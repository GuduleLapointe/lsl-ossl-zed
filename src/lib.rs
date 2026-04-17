use zed_extension_api as zed;

struct LslOsslExtension;

impl zed::Extension for LslOsslExtension {
    fn new() -> Self {
        Self
    }
}

zed::register_extension!(LslOsslExtension);
