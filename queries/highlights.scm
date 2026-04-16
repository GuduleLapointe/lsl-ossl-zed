; Types
(type) @type

; Keywords
[
 "state" "default" "if" "else" "for" "while" "return" "jump"
] @keyword

; Constants
(constant) @constant

; Strings
(string) @string

; Numbers
(number) @number

; Comments
(comment) @comment

; Function calls
(call_expression
  function: (identifier) @function.call)

; Native LSL / OSSL functions (subset)
((identifier) @function.builtin
  (#match? @function.builtin "^(llSay|llSetText|llGetPos|llSetPos|llOwnerSay|osTeleportAgent|osSetDynamicTextureURL)$"))
