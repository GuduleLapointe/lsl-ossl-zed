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
        let ext = if matches!(os, Os::Windows) { ".exe" } else { "" };
        let binary = match os {
            // Universal fat binary covers both Intel and Apple Silicon
            Os::Mac => "lsp/prebuilt/lsl-lsp-macos".to_string(),
            Os::Linux => {
                let arch_str = match arch {
                    Architecture::Aarch64 => "aarch64",
                    Architecture::X8664 | Architecture::X86 => "x86_64",
                };
                format!("lsp/prebuilt/lsl-lsp-linux-{arch_str}")
            }
            Os::Windows => format!("lsp/prebuilt/lsl-lsp-windows-x86_64{ext}"),
        };

        Ok(zed::Command {
            command: binary,
            args: vec![],
            env: vec![],
        })
    }
}

zed::register_extension!(LslOsslExtension);
