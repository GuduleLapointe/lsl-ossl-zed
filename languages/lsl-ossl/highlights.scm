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
; CONSTANTS (grammar nodes: TRUE, FALSE, PI, etc.)
; -------------------------
(constant) @constant

; -------------------------
; CONSTANTS (UPPER_CASE identifiers: CHANGED_OWNER, ATTACH_HEAD, etc.)
; -------------------------
((identifier) @constant
  (#match? @constant "^[A-Z][A-Z0-9_]+$"))

; -------------------------
; EVENTS
; -------------------------
(event_name) @function.special

; -------------------------
; BUILTIN LSL FUNCTIONS
; Reference: https://wiki.secondlife.com/wiki/Category:LSL_Functions
; -------------------------
(call_expression
  function: (identifier) @function.builtin
  (#match? @function.builtin "^ll(DetectedKey|RegionSayTo|ResetScript|Whisper)$"))

; -------------------------
; BUILTIN OSSL FUNCTIONS
; Reference: http://opensimulator.org/wiki/Category:OSSL_Functions
; -------------------------
(call_expression
  function: (identifier) @function.builtin
  (#match? @function.builtin "^os(TeleportAgent)$"))

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
