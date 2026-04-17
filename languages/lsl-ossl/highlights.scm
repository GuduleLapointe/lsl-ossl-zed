; -------------------------
; TYPES
; -------------------------
(type) @type

; -------------------------
; KEYWORDS
; -------------------------
[
 "state" "default"
 "if" "else"
 "for" "while"
 "return" "jump"
] @keyword

; -------------------------
; CONSTANTS (grammar nodes)
; -------------------------
(constant) @constant

; -------------------------
; EVENTS
; event_name is a distinct grammar node, not an identifier
; -------------------------
(event_name) @function.special

; -------------------------
; BUILTIN OSSL FUNCTIONS
; Add functions here as they are documented and verified
; Reference: http://opensimulator.org/wiki/Category:OSSL_Functions
; -------------------------
(call_expression
  function: (identifier) @function.builtin
  (#any-of? @function.builtin
    "osTeleportAgent"
  ))

; -------------------------
; BUILTIN LSL FUNCTIONS
; Add functions here as they are documented and verified
; Reference: https://wiki.secondlife.com/wiki/Category:LSL_Functions
; -------------------------
(call_expression
  function: (identifier) @function.builtin
  (#any-of? @function.builtin
    "llDetectedKey"
    "llRegionSayTo"
    "llResetScript"
    "llWhisper"
  ))

; -------------------------
; FUNCTION CALLS (user-defined)
; -------------------------
(call_expression
  function: (identifier) @function.call)

; -------------------------
; VARIABLES
; -------------------------
(identifier) @variable

; -------------------------
; STRINGS / NUMBERS / COMMENTS
; -------------------------
(string) @string
(number) @number
(comment) @comment

; -------------------------
; OPERATORS
; -------------------------
[
 "+" "-" "*" "/" "%"
 "==" "!=" "<" ">" "<=" ">="
 "&&" "||"
 "="
] @operator
