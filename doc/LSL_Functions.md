# LSL Functions

Source: tmp/opensim-git/OpenSim/Region/ScriptEngine/Shared/Api/Interface/ILSL_Api.cs
Generated: 2026-04-18T20:33:12Z

### llAbs

- `integer llAbs(integer val)`

Returns absolute version as val (ie as positive value)

### llAcos

- `float llAcos(float val)`

Returns cosine of val (val in radians)

### llAddToLandBanList

- `void llAddToLandBanList(key avatarId, float hours)`

Sleep 0.1

### llAddToLandPassList

- `void llAddToLandPassList(key avatarId, float hours)`

Sleep 0.1

### llAdjustSoundVolume

- `void llAdjustSoundVolume(float volume)`

Sleep 0.1

### llAllowInventoryDrop

- `void llAllowInventoryDrop(integer add)`

### llAngleBetween

- `float llAngleBetween(rotation a, rotation b)`

### llApplyImpulse

- `void llApplyImpulse(vector force, integer local)`

### llApplyRotationalImpulse

- `void llApplyRotationalImpulse(vector force, integer local)`

### llAsin

- `float llAsin(float val)`

Returns sine of val (val in radians)

### llAtan2

- `float llAtan2(float y, float x)`

Returns the angle whose tangent is the y/x

### llAttachToAvatar

- `void llAttachToAvatar(integer attachment)`

### llAttachToAvatarTemp

- `void llAttachToAvatarTemp(integer attachmentPoint)`

### llAvatarOnLinkSitTarget

- `key llAvatarOnLinkSitTarget(integer linknum)`

### llAvatarOnSitTarget

- `key llAvatarOnSitTarget()`

### llAxes2Rot

- `rotation llAxes2Rot(vector fwd, vector left, vector up)`

### llAxisAngle2Rot

- `rotation llAxisAngle2Rot(vector axis, float angle)`

### llBase64ToInteger

- `integer llBase64ToInteger(string str)`

### llBase64ToString

- `string llBase64ToString(string str)`

### llBreakAllLinks

- `void llBreakAllLinks()`

### llBreakLink

- `void llBreakLink(integer linknum)`

### llCastRay

- `list llCastRay(vector start, vector end, list options)`

### llCastRayV3

- `list llCastRayV3(vector start, vector end, list options)`

### llCeil

- `integer llCeil(float f)`

### llChar

- `string llChar(integer unicode)`

### llClearCameraParams

- `void llClearCameraParams()`

### llClearLinkMedia

- `integer llClearLinkMedia(integer link, integer face)`

### llClearPrimMedia

- `integer llClearPrimMedia(integer face)`

Sleep 0.1

### llCloseRemoteDataChannel

- `void llCloseRemoteDataChannel(string channel)`

Sleep 1.0

### llCloud

- `float llCloud(vector offset)`

### llCollisionFilter

- `void llCollisionFilter(string name, key id, integer accept)`

### llCollisionSound

- `void llCollisionSound(string impact_sound, float impact_volume)`

### llCollisionSprite

- `void llCollisionSprite(string impact_sprite)`

Not Supported - does nothing

### llComputeHash

- `string llComputeHash(string message, string algo)`

### llCos

- `float llCos(float f)`

### llCreateLink

- `void llCreateLink(key targetId, integer parent)`

Sleep 1.0

### llCSV2List

- `list llCSV2List(string src)`

### llDeleteSubList

- `list llDeleteSubList(list src, integer start, integer end)`

### llDeleteSubString

- `string llDeleteSubString(string src, integer start, integer end)`

### llDerezObject

- `integer llDerezObject(key objectUUID, integer flag)`

### llDetachFromAvatar

- `void llDetachFromAvatar()`

### llDetectedGrab

- `vector llDetectedGrab(integer number)`

### llDetectedGroup

- `integer llDetectedGroup(integer number)`

### llDetectedKey

- `key llDetectedKey(integer number)`

### llDetectedLinkNumber

- `integer llDetectedLinkNumber(integer number)`

### llDetectedName

- `string llDetectedName(integer number)`

### llDetectedOwner

- `key llDetectedOwner(integer number)`

### llDetectedPos

- `vector llDetectedPos(integer number)`

### llDetectedRot

- `rotation llDetectedRot(integer number)`

### llDetectedTouchBinormal

- `vector llDetectedTouchBinormal(integer index)`

### llDetectedTouchFace

- `integer llDetectedTouchFace(integer index)`

### llDetectedTouchNormal

- `vector llDetectedTouchNormal(integer index)`

### llDetectedTouchPos

- `vector llDetectedTouchPos(integer index)`

### llDetectedTouchST

- `vector llDetectedTouchST(integer index)`

### llDetectedTouchUV

- `vector llDetectedTouchUV(integer index)`

### llDetectedType

- `integer llDetectedType(integer number)`

### llDetectedVel

- `vector llDetectedVel(integer number)`

### llDialog

- `void llDialog(key avatarId, string message, list buttons, integer chat_channel)`

### llDie

- `void llDie()`

### llDumpList2String

- `string llDumpList2String(list src, string seperator)`

### llEdgeOfWorld

- `integer llEdgeOfWorld(vector pos, vector dir)`

### llEjectFromLand

- `void llEjectFromLand(key avatarId)`

Sleep 1.0

### llEmail

- `void llEmail(string address, string subject, string message)`

### llEscapeURL

- `string llEscapeURL(string url)`

### llEuler2Rot

- `rotation llEuler2Rot(vector v)`

### llFabs

- `float llFabs(float f)`

### llFloor

- `integer llFloor(float f)`

### llForceMouselook

- `void llForceMouselook(integer mouselook)`

### llFrand

- `float llFrand(float mag)`

### llGenerateKey

- `key llGenerateKey()`

### llGetAccel

- `vector llGetAccel()`

### llGetAgentInfo

- `integer llGetAgentInfo(key id)`

### llGetAgentLanguage

- `string llGetAgentLanguage(key id)`

### llGetAgentList

- `list llGetAgentList(integer scope, list options)`

### llGetAgentSize

- `vector llGetAgentSize(key id)`

### llGetAlpha

- `float llGetAlpha(integer face)`

### llGetAndResetTime

- `float llGetAndResetTime()`

### llGetAnimation

- `string llGetAnimation(key id)`

### llGetAnimationList

- `list llGetAnimationList(key id)`

### llGetAnimationOverride

- `string llGetAnimationOverride(string anim_state)`

### llGetAttached

- `integer llGetAttached()`

### llGetAttachedList

- `list llGetAttachedList(key id)`

### llGetBoundingBox

- `list llGetBoundingBox(string obj)`

### llGetCameraAspect

- `float llGetCameraAspect()`

### llGetCameraFOV

- `float llGetCameraFOV()`

### llGetCameraPos

- `vector llGetCameraPos()`

### llGetCameraRot

- `rotation llGetCameraRot()`

### llGetCenterOfMass

- `vector llGetCenterOfMass()`

### llGetColor

- `vector llGetColor(integer face)`

### llGetCreator

- `key llGetCreator()`

### llGetDate

- `string llGetDate()`

### llGetDayLength

- `integer llGetDayLength()`

### llGetDayOffset

- `integer llGetDayOffset()`

### llGetDisplayName

- `string llGetDisplayName(key id)`

### llGetEnergy

- `float llGetEnergy()`

### llGetEnv

- `string llGetEnv(string name)`

### llGetForce

- `vector llGetForce()`

### llGetFreeMemory

- `integer llGetFreeMemory()`

### llGetFreeURLs

- `integer llGetFreeURLs()`

### llGetGeometricCenter

- `vector llGetGeometricCenter()`

### llGetGMTclock

- `float llGetGMTclock()`

### llGetHealth

- `float llGetHealth(string key)`

### llGetHTTPHeader

- `string llGetHTTPHeader(key request_id, string header)`

### llGetInventoryAcquireTime

- `string llGetInventoryAcquireTime(string item)`

### llGetInventoryCreator

- `key llGetInventoryCreator(string item)`

### llGetInventoryDesc

- `string llGetInventoryDesc(string name)`

### llGetInventoryKey

- `key llGetInventoryKey(string name)`

### llGetInventoryName

- `string llGetInventoryName(integer type, integer number)`

### llGetInventoryNumber

- `integer llGetInventoryNumber(integer type)`

### llGetInventoryPermMask

- `integer llGetInventoryPermMask(string item, integer mask)`

### llGetInventoryType

- `integer llGetInventoryType(string name)`

### llGetKey

- `key llGetKey()`

### llGetLandOwnerAt

- `key llGetLandOwnerAt(vector pos)`

### llGetLinkKey

- `key llGetLinkKey(integer linknum)`

### llGetLinkMedia

- `list llGetLinkMedia(integer link, integer face, list rules)`

### llGetLinkName

- `string llGetLinkName(integer linknum)`

### llGetLinkNumber

- `integer llGetLinkNumber()`

### llGetLinkNumberOfSides

- `integer llGetLinkNumberOfSides(integer link)`
- `integer llGetLinkNumberOfSides(integer link)`

### llGetLinkPrimitiveParams

- `list llGetLinkPrimitiveParams(integer linknum, list rules)`

### llGetLinkSitFlags

- `integer llGetLinkSitFlags(integer linknum)`

### llGetListEntryType

- `integer llGetListEntryType(list src, integer index)`

### llGetListLength

- `integer llGetListLength(list src)`

### llGetLocalPos

- `vector llGetLocalPos()`

### llGetLocalRot

- `rotation llGetLocalRot()`

### llGetMass

- `float llGetMass()`

### llGetMassMKS

- `float llGetMassMKS()`

### llGetMaxScaleFactor

- `float llGetMaxScaleFactor()`

### llGetMemoryLimit

- `integer llGetMemoryLimit()`

### llGetMinScaleFactor

- `float llGetMinScaleFactor()`

### llGetMoonDirection

- `vector llGetMoonDirection()`

### llGetMoonRotation

- `rotation llGetMoonRotation()`

### llGetNextEmail

- `void llGetNextEmail(string address, string subject)`

### llGetNotecardLine

- `key llGetNotecardLine(string name, integer line)`

### llGetNotecardLineSync

- `string llGetNotecardLineSync(string name, integer line)`

### llGetNumberOfNotecardLines

- `key llGetNumberOfNotecardLines(string name)`

### llGetNumberOfPrims

- `integer llGetNumberOfPrims()`

### llGetNumberOfSides

- `integer llGetNumberOfSides()`

### llGetObjectAnimationNames

- `list llGetObjectAnimationNames()`

### llGetObjectDesc

- `string llGetObjectDesc()`

### llGetObjectDetails

- `list llGetObjectDetails(key objectId, list args)`

### llGetObjectLinkKey

- `key llGetObjectLinkKey(key objectid, integer linknum)`

### llGetObjectMass

- `float llGetObjectMass(key objectId)`

### llGetObjectName

- `string llGetObjectName()`

### llGetObjectPermMask

- `integer llGetObjectPermMask(integer mask)`

### llGetObjectPrimCount

- `integer llGetObjectPrimCount(key objectId)`

### llGetOmega

- `vector llGetOmega()`

### llGetOwner

- `key llGetOwner()`

### llGetOwnerKey

- `key llGetOwnerKey(string id)`

### llGetParcelDetails

- `list llGetParcelDetails(vector pos, list param)`

### llGetParcelFlags

- `integer llGetParcelFlags(vector pos)`

### llGetParcelMaxPrims

- `integer llGetParcelMaxPrims(vector pos, integer sim_wide)`

### llGetParcelMusicURL

- `string llGetParcelMusicURL()`

### llGetParcelPrimCount

- `integer llGetParcelPrimCount(vector pos, integer category, integer sim_wide)`

### llGetParcelPrimOwners

- `list llGetParcelPrimOwners(vector pos)`

### llGetPermissions

- `integer llGetPermissions()`

### llGetPermissionsKey

- `key llGetPermissionsKey()`

### llGetPhysicsMaterial

- `list llGetPhysicsMaterial()`

### llGetPos

- `vector llGetPos()`

### llGetPrimitiveParams

- `list llGetPrimitiveParams(list rules)`

### llGetPrimMediaParams

- `list llGetPrimMediaParams(integer face, list rules)`

### llGetRegionAgentCount

- `integer llGetRegionAgentCount()`

### llGetRegionCorner

- `vector llGetRegionCorner()`

### llGetRegionDayLength

- `integer llGetRegionDayLength()`

### llGetRegionDayOffset

- `integer llGetRegionDayOffset()`

### llGetRegionFlags

- `integer llGetRegionFlags()`

### llGetRegionFPS

- `float llGetRegionFPS()`

### llGetRegionMoonDirection

- `vector llGetRegionMoonDirection()`

### llGetRegionMoonRotation

- `rotation llGetRegionMoonRotation()`

### llGetRegionName

- `string llGetRegionName()`

### llGetRegionSunDirection

- `vector llGetRegionSunDirection()`

### llGetRegionSunRotation

- `rotation llGetRegionSunRotation()`

### llGetRegionTimeDilation

- `float llGetRegionTimeDilation()`

### llGetRenderMaterial

- `string llGetRenderMaterial(integer face)`

### llGetRootPosition

- `vector llGetRootPosition()`

### llGetRootRotation

- `rotation llGetRootRotation()`

### llGetRot

- `rotation llGetRot()`

### llGetScale

- `vector llGetScale()`

### llGetScriptName

- `string llGetScriptName()`

### llGetScriptState

- `integer llGetScriptState(string name)`

### llGetSimStats

- `float llGetSimStats(integer stat_type)`

### llGetSimulatorHostname

- `string llGetSimulatorHostname()`

### llGetSPMaxMemory

- `integer llGetSPMaxMemory()`

### llGetStartParameter

- `integer llGetStartParameter()`

### llGetStartString

- `string llGetStartString()`

### llGetStatus

- `integer llGetStatus(integer status)`

### llGetSubString

- `string llGetSubString(string src, integer start, integer end)`

### llGetSunDirection

- `vector llGetSunDirection()`

### llGetSunRotation

- `rotation llGetSunRotation()`

### llGetTexture

- `string llGetTexture(integer face)`

### llGetTextureOffset

- `vector llGetTextureOffset(integer face)`

### llGetTextureRot

- `float llGetTextureRot(integer side)`

### llGetTextureScale

- `vector llGetTextureScale(integer side)`

### llGetTime

- `float llGetTime()`

### llGetTimeOfDay

- `float llGetTimeOfDay()`

### llGetTimestamp

- `string llGetTimestamp()`

### llGetTorque

- `vector llGetTorque()`

### llGetUnixTime

- `integer llGetUnixTime()`

### llGetUsedMemory

- `integer llGetUsedMemory()`

### llGetUsername

- `string llGetUsername(key id)`

### llGetVel

- `vector llGetVel()`

### llGetVisualParams

- `list llGetVisualParams(string id, list visualparams)`

### llGetWallclock

- `float llGetWallclock()`

### llGiveInventory

- `void llGiveInventory(key destination, string inventory)`

### llGiveInventoryList

- `void llGiveInventoryList(key destination, string folderName, list inventory)`

### llGiveMoney

- `integer llGiveMoney(key destination, integer amount)`

### llGodLikeRezObject

- `void llGodLikeRezObject(string inventory, vector pos)`

### llGround

- `float llGround(vector offset)`

### llGroundContour

- `vector llGroundContour(vector offset)`

### llGroundNormal

- `vector llGroundNormal(vector offset)`

### llGroundRepel

- `void llGroundRepel(float height, integer water, float tau)`

### llGroundSlope

- `vector llGroundSlope(vector offset)`

### llHash

- `integer llHash(string s)`

### llHMAC

- `string llHMAC(string private_key, string message, string algo)`

### llHTTPRequest

- `key llHTTPRequest(string url, list parameters, string body)`

### llHTTPResponse

- `void llHTTPResponse(key id, integer status, string body)`

### llInsertString

- `string llInsertString(string dst, integer position, string src)`

### llInstantMessage

- `void llInstantMessage(string user, string message)`

### llIntegerToBase64

- `string llIntegerToBase64(integer number)`

### llIsFriend

- `integer llIsFriend(key agent_id)`

### llIsLinkGLTFMaterial

- `integer llIsLinkGLTFMaterial(integer linknum, integer face)`

### llJson2List

- `list llJson2List(string json)`

### llJsonGetValue

- `string llJsonGetValue(string json, list specifiers)`

### llJsonSetValue

- `string llJsonSetValue(string json, list specifiers, string value)`

### llJsonValueType

- `string llJsonValueType(string json, list specifiers)`

### llKey2Name

- `string llKey2Name(key id)`

### llLinear2sRGB

- `vector llLinear2sRGB(vector src)`

### llLinkAdjustSoundVolume

- `void llLinkAdjustSoundVolume(integer linknumber, float volume)`

### llLinkParticleSystem

- `void llLinkParticleSystem(integer linknum, list rules)`

### llLinkPlaySound

- `void llLinkPlaySound(integer linknumber, string sound, float volume)`
- `void llLinkPlaySound(integer linknumber, string sound, float volume, integer flags)`

### llLinksetDataAvailable

- `integer llLinksetDataAvailable()`

### llLinksetDataCountFound

- `integer llLinksetDataCountFound(string pattern)`

### llLinksetDataCountKeys

- `integer llLinksetDataCountKeys()`

### llLinksetDataDelete

- `integer llLinksetDataDelete(string name)`

### llLinksetDataDeleteFound

- `list llLinksetDataDeleteFound(string pattern, string pass)`

### llLinksetDataDeleteProtected

- `integer llLinksetDataDeleteProtected(string name, string pass)`

### llLinksetDataFindKeys

- `list llLinksetDataFindKeys(string pattern, integer start, integer count)`

### llLinksetDataListKeys

- `list llLinksetDataListKeys(integer start, integer count)`

### llLinksetDataRead

- `string llLinksetDataRead(string name)`

### llLinksetDataReadProtected

- `string llLinksetDataReadProtected(string name, string pass)`

### llLinksetDataReset

- `void llLinksetDataReset()`

### llLinksetDataWrite

- `integer llLinksetDataWrite(string name, string value)`

### llLinksetDataWriteProtected

- `integer llLinksetDataWriteProtected(string name, string value, string pass)`

### llLinkSetSoundQueueing

- `void llLinkSetSoundQueueing(integer linknumber, integer queue)`

### llLinkSetSoundRadius

- `void llLinkSetSoundRadius(integer linknumber, float radius)`

### llLinkSitTarget

- `void llLinkSitTarget(integer link, vector offset, rotation rot)`

### llLinkStopSound

- `void llLinkStopSound(integer linknumber)`

### llList2CSV

- `string llList2CSV(list src)`

### llList2Float

- `float llList2Float(list src, integer index)`

### llList2Integer

- `integer llList2Integer(list src, integer index)`

### llList2Json

- `string llList2Json(string type, list values)`

### llList2Key

- `key llList2Key(list src, integer index)`

### llList2List

- `list llList2List(list src, integer start, integer end)`

### llList2ListSlice

- `list llList2ListSlice(list src, integer start, integer end, integer stride, integer stride_index)`

### llList2ListStrided

- `list llList2ListStrided(list src, integer start, integer end, integer stride)`

### llList2Rot

- `rotation llList2Rot(list src, integer index)`

### llList2String

- `string llList2String(list src, integer index)`

### llList2Vector

- `vector llList2Vector(list src, integer index)`

### llListen

- `integer llListen(integer channelID, string name, string ID, string msg)`

### llListenControl

- `void llListenControl(integer number, integer active)`

### llListenRemove

- `void llListenRemove(integer number)`

### llListFindList

- `integer llListFindList(list src, list test)`

### llListFindListNext

- `integer llListFindListNext(list src, list test, integer instance)`

### llListFindStrided

- `integer llListFindStrided(list src, list test, integer lstart, integer lend, integer lstride)`

### llListInsertList

- `list llListInsertList(list dest, list src, integer start)`

### llListRandomize

- `list llListRandomize(list src, integer stride)`

### llListReplaceList

- `list llListReplaceList(list dest, list src, integer start, integer end)`

### llListSort

- `list llListSort(list src, integer stride, integer ascending)`

### llListSortStrided

- `list llListSortStrided(list src, integer stride, integer stride_index, integer ascending)`

### llListStatistics

- `float llListStatistics(integer operation, list src)`

### llLoadURL

- `void llLoadURL(string avatar_id, string message, string url)`

### llLog

- `float llLog(float val)`

### llLog10

- `float llLog10(float val)`

### llLookAt

- `void llLookAt(vector target, float strength, float damping)`

### llLoopSound

- `void llLoopSound(string sound, float volume)`

### llLoopSoundMaster

- `void llLoopSoundMaster(string sound, float volume)`

### llLoopSoundSlave

- `void llLoopSoundSlave(string sound, float volume)`

### llMakeExplosion

- `void llMakeExplosion(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)`

### llMakeFire

- `void llMakeFire(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)`

### llMakeFountain

- `void llMakeFountain(integer particles, float scale, float vel, float lifetime, float arc, integer bounce, string texture, vector offset, float bounce_offset)`

### llMakeSmoke

- `void llMakeSmoke(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)`

### llManageEstateAccess

- `integer llManageEstateAccess(integer action, string avatar)`

### llMapBeacon

- `void llMapBeacon(string simname, vector pos, list loptions)`

### llMapDestination

- `void llMapDestination(string simname, vector pos, vector look_at)`

### llMD5String

- `string llMD5String(string src, integer nonce)`

### llMessageLinked

- `void llMessageLinked(integer linknum, integer num, string str, string id)`

### llMinEventDelay

- `void llMinEventDelay(float delay)`

### llModifyLand

- `void llModifyLand(integer action, integer brush)`

### llModPow

- `integer llModPow(integer a, integer b, integer c)`

### llMoveToTarget

- `void llMoveToTarget(vector target, float tau)`

### llName2Key

- `key llName2Key(string name)`

### llOffsetTexture

- `void llOffsetTexture(float u, float v, integer face)`

### llOpenRemoteDataChannel

- `void llOpenRemoteDataChannel()`

### llOrd

- `integer llOrd(string s, integer index)`

### llOverMyLand

- `integer llOverMyLand(string id)`

### llOwnerSay

- `void llOwnerSay(string msg)`

### llParcelMediaCommandList

- `void llParcelMediaCommandList(list commandList)`

### llParcelMediaQuery

- `list llParcelMediaQuery(list aList)`

### llParseString2List

- `list llParseString2List(string str, list separators, list spacers)`

### llParseStringKeepNulls

- `list llParseStringKeepNulls(string src, list seperators, list spacers)`

### llParticleSystem

- `void llParticleSystem(list rules)`

### llPassCollisions

- `void llPassCollisions(integer pass)`

### llPassTouches

- `void llPassTouches(integer pass)`

### llPlaySound

- `void llPlaySound(string sound, float volume)`

### llPlaySoundSlave

- `void llPlaySoundSlave(string sound, float volume)`

### llPointAt

- `void llPointAt(vector pos)`

### llPow

- `float llPow(float fbase, float fexponent)`

### llPreloadSound

- `void llPreloadSound(string sound)`

### llPushObject

- `void llPushObject(string target, vector impulse, vector ang_impulse, integer local)`

### llRefreshPrimURL

- `void llRefreshPrimURL()`

### llRegionSay

- `void llRegionSay(integer channelID, string text)`

### llRegionSayTo

- `void llRegionSayTo(string target, integer channelID, string text)`

### llReleaseCamera

- `void llReleaseCamera(string avatar)`

### llReleaseControls

- `void llReleaseControls()`

### llReleaseURL

- `void llReleaseURL(string url)`

### llRemoteDataReply

- `void llRemoteDataReply(string channel, string message_id, string sdata, integer idata)`

### llRemoteDataSetRegion

- `void llRemoteDataSetRegion()`

### llRemoteLoadScript

- `void llRemoteLoadScript(string target, string name, integer running, integer start_param)`

### llRemoteLoadScriptPin

- `void llRemoteLoadScriptPin(string target, string name, integer pin, integer running, integer start_param)`

### llRemoveFromLandBanList

- `void llRemoveFromLandBanList(string avatar)`

### llRemoveFromLandPassList

- `void llRemoveFromLandPassList(string avatar)`

### llRemoveInventory

- `void llRemoveInventory(string item)`

### llRemoveVehicleFlags

- `void llRemoveVehicleFlags(integer flags)`

### llReplaceSubString

- `string llReplaceSubString(string src, string pattern, string replacement, integer count)`

### llRequestAgentData

- `key llRequestAgentData(string id, integer data)`

### llRequestDisplayName

- `key llRequestDisplayName(key id)`

### llRequestInventoryData

- `key llRequestInventoryData(string name)`

### llRequestPermissions

- `void llRequestPermissions(string agent, integer perm)`

### llRequestSecureURL

- `key llRequestSecureURL()`

### llRequestSimulatorData

- `key llRequestSimulatorData(string simulator, integer data)`

### llRequestURL

- `key llRequestURL()`

### llRequestUserKey

- `key llRequestUserKey(string username)`

### llRequestUsername

- `key llRequestUsername(key id)`

### llResetAnimationOverride

- `void llResetAnimationOverride(string anim_state)`

### llResetLandBanList

- `void llResetLandBanList()`

### llResetLandPassList

- `void llResetLandPassList()`

### llResetOtherScript

- `void llResetOtherScript(string name)`

### llResetScript

- `void llResetScript()`

### llResetTime

- `void llResetTime()`

### llRezAtRoot

- `void llRezAtRoot(string inventory, vector position, vector velocity, rotation rot, integer param)`

### llRezObject

- `void llRezObject(string inventory, vector pos, vector vel, rotation rot, integer param)`

### llRezObjectWithParams

- `key llRezObjectWithParams(string inventory, list lparam)`

### llRot2Angle

- `float llRot2Angle(rotation rot)`

### llRot2Axis

- `vector llRot2Axis(rotation rot)`

### llRot2Euler

- `vector llRot2Euler(rotation r)`

### llRot2Fwd

- `vector llRot2Fwd(rotation r)`

### llRot2Left

- `vector llRot2Left(rotation r)`

### llRot2Up

- `vector llRot2Up(rotation r)`

### llRotateTexture

- `void llRotateTexture(float rotation, integer face)`

### llRotBetween

- `rotation llRotBetween(vector start, vector end)`

### llRotLookAt

- `void llRotLookAt(rotation target, float strength, float damping)`

### llRotTarget

- `integer llRotTarget(rotation rot, float error)`

### llRotTargetRemove

- `void llRotTargetRemove(integer number)`

### llRound

- `integer llRound(float f)`

### llSameGroup

- `integer llSameGroup(string agent)`

### llSay

- `void llSay(integer channelID, string text)`

### llScaleByFactor

- `integer llScaleByFactor(float scaling_factor)`

### llScaleTexture

- `void llScaleTexture(float u, float v, integer face)`

### llScriptDanger

- `integer llScriptDanger(vector pos)`

### llScriptProfiler

- `void llScriptProfiler(integer flag)`

### llSendRemoteData

- `key llSendRemoteData(string channel, string dest, integer idata, string sdata)`

### llSensor

- `void llSensor(string name, string id, integer type, float range, float arc)`

### llSensorRemove

- `void llSensorRemove()`

### llSensorRepeat

- `void llSensorRepeat(string name, string id, integer type, float range, float arc, float rate)`

### llSetAlpha

- `void llSetAlpha(float alpha, integer face)`

### llSetAngularVelocity

- `void llSetAngularVelocity(vector angularVelocity, integer local)`

### llSetAnimationOverride

- `void llSetAnimationOverride(string animState, string anim)`

### llSetBuoyancy

- `void llSetBuoyancy(float buoyancy)`

### llSetCameraAtOffset

- `void llSetCameraAtOffset(vector offset)`

### llSetCameraEyeOffset

- `void llSetCameraEyeOffset(vector offset)`

### llSetCameraParams

- `void llSetCameraParams(list rules)`

### llSetClickAction

- `void llSetClickAction(integer action)`

### llSetColor

- `void llSetColor(vector color, integer face)`

### llSetContentType

- `void llSetContentType(key id, integer type)`

### llSetDamage

- `void llSetDamage(float damage)`

### llSetForce

- `void llSetForce(vector force, integer local)`

### llSetForceAndTorque

- `void llSetForceAndTorque(vector force, vector torque, integer local)`

### llSetHoverHeight

- `void llSetHoverHeight(float height, integer water, float tau)`

### llSetInventoryPermMask

- `void llSetInventoryPermMask(string item, integer mask, integer value)`

### llSetKeyframedMotion

- `void llSetKeyframedMotion(list frames, list options)`

### llSetLinkAlpha

- `void llSetLinkAlpha(integer linknumber, float alpha, integer face)`

### llSetLinkCamera

- `void llSetLinkCamera(integer link, vector eye, vector at)`

### llSetLinkColor

- `void llSetLinkColor(integer linknumber, vector color, integer face)`

### llSetLinkMedia

- `integer llSetLinkMedia(integer link, integer face, list rules)`

### llSetLinkPrimitiveParams

- `void llSetLinkPrimitiveParams(integer linknumber, list rules)`

### llSetLinkPrimitiveParamsFast

- `void llSetLinkPrimitiveParamsFast(integer linknum, list rules)`

### llSetLinkSitFlags

- `void llSetLinkSitFlags(integer linknum, integer flags)`

### llSetLinkTexture

- `void llSetLinkTexture(integer linknumber, string texture, integer face)`

### llSetLinkTextureAnim

- `void llSetLinkTextureAnim(integer linknum, integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)`

### llSetLocalRot

- `void llSetLocalRot(rotation rot)`

### llSetMemoryLimit

- `integer llSetMemoryLimit(integer limit)`

### llSetObjectDesc

- `void llSetObjectDesc(string desc)`

### llSetObjectName

- `void llSetObjectName(string name)`

### llSetObjectPermMask

- `void llSetObjectPermMask(integer mask, integer value)`

### llSetParcelMusicURL

- `void llSetParcelMusicURL(string url)`

### llSetPayPrice

- `void llSetPayPrice(integer price, list quick_pay_buttons)`

### llSetPhysicsMaterial

- `void llSetPhysicsMaterial(integer material_bits, float material_gravity_modifier, float material_restitution, float material_friction, float material_density)`

### llSetPos

- `void llSetPos(vector pos)`

### llSetPrimitiveParams

- `void llSetPrimitiveParams(list rules)`

### llSetPrimMediaParams

- `integer llSetPrimMediaParams(integer face, list rules)`

### llSetPrimURL

- `void llSetPrimURL(string url)`

### llSetRegionPos

- `integer llSetRegionPos(vector pos)`

### llSetRemoteScriptAccessPin

- `void llSetRemoteScriptAccessPin(integer pin)`

### llSetRenderMaterial

- `void llSetRenderMaterial(string material, integer face)`

### llSetRot

- `void llSetRot(rotation rot)`

### llSetScale

- `void llSetScale(vector scale)`

### llSetScriptState

- `void llSetScriptState(string name, integer run)`

### llSetSitText

- `void llSetSitText(string text)`

### llSetSoundQueueing

- `void llSetSoundQueueing(integer queue)`

### llSetSoundRadius

- `void llSetSoundRadius(float radius)`

### llSetStatus

- `void llSetStatus(integer status, integer value)`

### llSetText

- `void llSetText(string text, vector color, float alpha)`

### llSetTexture

- `void llSetTexture(string texture, integer face)`

### llSetTextureAnim

- `void llSetTextureAnim(integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)`

### llSetTimerEvent

- `void llSetTimerEvent(float sec)`

### llSetTorque

- `void llSetTorque(vector torque, integer local)`

### llSetTouchText

- `void llSetTouchText(string text)`

### llSetVehicleFlags

- `void llSetVehicleFlags(integer flags)`

### llSetVehicleFloatParam

- `void llSetVehicleFloatParam(integer param, float value)`

### llSetVehicleRotationParam

- `void llSetVehicleRotationParam(integer param, rotation rot)`

### llSetVehicleType

- `void llSetVehicleType(integer type)`

### llSetVehicleVectorParam

- `void llSetVehicleVectorParam(integer param, vector vec)`

### llSetVelocity

- `void llSetVelocity(vector vel, integer local)`

### llSHA1String

- `string llSHA1String(string src)`

### llSHA256String

- `string llSHA256String(string src)`

### llShout

- `void llShout(integer channelID, string text)`

### llSin

- `float llSin(float f)`

### llSitTarget

- `void llSitTarget(vector offset, rotation rot)`

### llSleep

- `void llSleep(float sec)`

### llSound

- `void llSound(string sound, float volume, integer queue, integer loop)`

### llSoundPreload

- `void llSoundPreload(string sound)`

### llSqrt

- `float llSqrt(float f)`

### llsRGB2Linear

- `vector llsRGB2Linear(vector src)`

### llStartAnimation

- `void llStartAnimation(string anim)`

### llStartObjectAnimation

- `void llStartObjectAnimation(string anim)`

### llStopAnimation

- `void llStopAnimation(string anim)`

### llStopHover

- `void llStopHover()`

### llStopLookAt

- `void llStopLookAt()`

### llStopMoveToTarget

- `void llStopMoveToTarget()`

### llStopObjectAnimation

- `void llStopObjectAnimation(string anim)`

### llStopPointAt

- `void llStopPointAt()`

### llStopSound

- `void llStopSound()`

### llStringLength

- `integer llStringLength(string str)`

### llStringToBase64

- `string llStringToBase64(string str)`

### llStringTrim

- `string llStringTrim(string src, integer type)`

### llSubStringIndex

- `integer llSubStringIndex(string source, string pattern)`

### llTakeCamera

- `void llTakeCamera(string avatar)`

### llTakeControls

- `void llTakeControls(integer controls, integer accept, integer pass_on)`

### llTan

- `float llTan(float f)`

### llTarget

- `integer llTarget(vector position, float range)`

### llTargetedEmail

- `void llTargetedEmail(integer target, string subject, string message)`

### llTargetOmega

- `void llTargetOmega(vector axis, float spinrate, float gain)`

### llTargetRemove

- `void llTargetRemove(integer number)`

### llTeleportAgent

- `void llTeleportAgent(string agent, string simname, vector pos, vector lookAt)`

### llTeleportAgentGlobalCoords

- `void llTeleportAgentGlobalCoords(string agent, vector global, vector pos, vector lookAt)`

### llTeleportAgentHome

- `void llTeleportAgentHome(string agent)`

### llTextBox

- `void llTextBox(string avatar, string message, integer chat_channel)`

### llToLower

- `string llToLower(string source)`

### llToUpper

- `string llToUpper(string source)`

### llTransferLindenDollars

- `key llTransferLindenDollars(key destination, integer amount)`

### llTriggerSound

- `void llTriggerSound(string sound, float volume)`

### llTriggerSoundLimited

- `void llTriggerSoundLimited(string sound, float volume, vector top_north_east, vector bottom_south_west)`

### llUnescapeURL

- `string llUnescapeURL(string url)`

### llUnSit

- `void llUnSit(string id)`

### llVecDist

- `float llVecDist(vector a, vector b)`

### llVecMag

- `float llVecMag(vector v)`

### llVecNorm

- `vector llVecNorm(vector v)`

### llVolumeDetect

- `void llVolumeDetect(integer detect)`

### llWater

- `float llWater(vector offset)`

### llWhisper

- `void llWhisper(integer channelID, string text)`

### llWind

- `vector llWind(vector offset)`

### llWorldPosToHUD

- `vector llWorldPosToHUD(vector WorldPosition)`

### llXorBase64

- `string llXorBase64(string str1, string str2)`

### llXorBase64Strings

- `string llXorBase64Strings(string str1, string str2)`

### llXorBase64StringsCorrect

- `string llXorBase64StringsCorrect(string str1, string str2)`

