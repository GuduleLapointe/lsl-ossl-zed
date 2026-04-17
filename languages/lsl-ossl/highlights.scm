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
; CONSTANTS (grammar nodes: TRUE, FALSE, PI, CHANGED_OWNER, etc.)
; -------------------------
(constant) @constant

; -------------------------
; EVENTS
; -------------------------
(event_name) @function.special

; -------------------------
; BUILTIN LSL FUNCTIONS (ll* prefix)
; Reference: https://wiki.secondlife.com/wiki/Category:LSL_Functions
; -------------------------
(lsl_function) @function.builtin

; -------------------------
; BUILTIN OSSL FUNCTIONS (os* prefix)
; Reference: http://opensimulator.org/wiki/Category:OSSL_Functions
; -------------------------
(ossl_function) @function.builtin

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
 "&" "|" "^" "~"
 "<<" ">>"
 "="
] @operator
