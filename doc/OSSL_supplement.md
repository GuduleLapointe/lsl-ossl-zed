# OSSL Functions — Supplemental

Functions confirmed real but absent from the XML export (new, undocumented, or deprecated).
Manually curated. Do not regenerate; update by hand when new functions are confirmed.


### osAESDecrypt

- `string osAESDecrypt(string secret, string encryptedText)`

Decrypts text encrypted by osAESEncrypt. Not yet documented on the wiki.

### osLineTo

- `string osLineTo(string drawList, integer x, integer y)`

Draws a line from the current pen position to (x, y). Used in dynamic texture drawing scripts. Appears in wiki code examples on OsSetPenCap page.

### osRestartRegion

- `osRestartRegion()`
- `osRestartRegion(float seconds)`

Deprecated predecessor of osRegionRestart. Still functional in many OpenSim versions.

### osSetPenColour

- `string osSetPenColour(string drawList, string colour)`

Deprecated alias for osSetPenColor (British spelling). Still triggers deprecation warning but functions correctly.

### osSunSetParam

- `osSunSetParam(string param, float value)`

Deprecated predecessor of osSetSunParam.

### osWindParamGet

- `float osWindParamGet(string plugin, string param)`

Deprecated predecessor of osGetWindParam (added in 0.7.2-post-fixes).

### osWindParamSet

- `osWindParamSet(string plugin, string param, float value)`

Deprecated predecessor of osSetWindParam.

