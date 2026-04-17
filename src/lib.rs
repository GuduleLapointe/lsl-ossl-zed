use zed_extension_api::{self as zed, Architecture, LanguageServerId, Os, Result};

struct LslOsslExtension;

impl zed::Extension for LslOsslExtension {
    fn new() -> Self {
        Self
    }

    fn language_server_command(
        &mut self,
        _language_server_id: &LanguageServerId,
        _worktree: &zed::Worktree,
    ) -> Result<zed::Command> {
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
        let binary = format!("lsp/prebuilt/lsl-lsp-{os_str}-{arch_str}{ext}");

        Ok(zed::Command {
            command: binary,
            args: vec![],
            env: vec![],
        })
    }
}

zed::register_extension!(LslOsslExtension);
