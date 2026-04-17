use zed_extension_api::{
    self as zed, Architecture, GithubReleaseOptions, LanguageServerId,
    LanguageServerInstallationStatus, Os, Result,
};

const GITHUB_REPO: &str = "GuduleLapointe/lsl-ossl-zed";
const SERVER_ID: &str = "lsl-lsp";

struct LslOsslExtension {
    cached_binary_path: Option<String>,
}

impl LslOsslExtension {
    fn server_binary_path(&mut self, language_server_id: &LanguageServerId) -> Result<String> {
        if let Some(path) = &self.cached_binary_path {
            if std::fs::metadata(path).is_ok() {
                return Ok(path.clone());
            }
        }

        let (os, arch) = zed::current_platform();

        let os_str = match os {
            Os::Mac => "macos",
            Os::Linux => "linux",
            Os::Windows => "windows",
        };
        let arch_str = match arch {
            Architecture::Aarch64 => "aarch64",
            Architecture::X8664 => "x86_64",
            Architecture::X86 => "x86",
        };
        let ext = if matches!(os, Os::Windows) { ".exe" } else { "" };
        let asset_name = format!("{SERVER_ID}-{os_str}-{arch_str}{ext}");
        let binary_path = format!("{SERVER_ID}/{asset_name}");

        zed::set_language_server_installation_status(
            language_server_id,
            &LanguageServerInstallationStatus::CheckingForUpdate,
        );

        let release = zed::latest_github_release(
            GITHUB_REPO,
            GithubReleaseOptions {
                require_assets: true,
                pre_release: false,
            },
        )?;

        let asset = release
            .assets
            .iter()
            .find(|a| a.name == asset_name)
            .ok_or_else(|| {
                format!(
                    "No pre-built binary for {os_str}-{arch_str} in release {}. \
                     Build lsl-lsp manually: cd lsp && cargo build --release",
                    release.version
                )
            })?;

        zed::set_language_server_installation_status(
            language_server_id,
            &LanguageServerInstallationStatus::Downloading,
        );

        zed::download_file(
            &asset.download_url,
            &binary_path,
            zed::DownloadedFileType::Uncompressed,
        )
        .map_err(|e| format!("Failed to download {}: {}", asset.name, e))?;

        zed::make_file_executable(&binary_path)?;

        zed::set_language_server_installation_status(
            language_server_id,
            &LanguageServerInstallationStatus::None,
        );

        self.cached_binary_path = Some(binary_path.clone());
        Ok(binary_path)
    }
}

impl zed::Extension for LslOsslExtension {
    fn new() -> Self {
        Self {
            cached_binary_path: None,
        }
    }

    fn language_server_command(
        &mut self,
        language_server_id: &LanguageServerId,
        _worktree: &zed::Worktree,
    ) -> Result<zed::Command> {
        let command = self.server_binary_path(language_server_id)?;
        Ok(zed::Command {
            command,
            args: vec![],
            env: vec![],
        })
    }
}

zed::register_extension!(LslOsslExtension);
