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
; CONSTANTS
; -------------------------
(constant) @constant

((identifier) @constant.builtin
  (#match? @constant.builtin "^(TRUE|FALSE|NULL_KEY|ZERO_VECTOR|ZERO_ROTATION|PI|TWO_PI|PI_BY_TWO)$"))

; -------------------------
; STRINGS / NUMBERS / COMMENTS
; -------------------------
(string) @string
(number) @number
(comment) @comment

; -------------------------
; EVENTS LSL
; -------------------------
((identifier) @function.special
  (#match? @function.special "^(state_entry|state_exit|touch_start|touch|touch_end|collision_start|collision|collision_end|listen|timer|changed|on_rez|attach|dataserver|run_time_permissions|sensor|no_sensor|control|money|email|http_response|path_update)$"))

; -------------------------
; BUILTIN LSL FUNCTIONS
; -------------------------
((identifier) @function.builtin
  (#match? @function.builtin "^ll[A-Z].*"))

; -------------------------
; BUILTIN OSSL FUNCTIONS
; -------------------------
((identifier) @function.builtin
  (#match? @function.builtin "^os[A-Z].*"))

; -------------------------
; FUNCTION CALLS (user)
; -------------------------
(call_expression
  function: (identifier) @function.call)

; -------------------------
; VARIABLES
; -------------------------
(identifier) @variable

; -------------------------
; OPERATORS
; -------------------------
[
 "+" "-" "*" "/" "%"
 "==" "!=" "<" ">" "<=" ">="
 "&&" "||"
 "="
] @operator
