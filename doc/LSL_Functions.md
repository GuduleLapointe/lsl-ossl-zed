# LSL Functions

Source: https://wiki.secondlife.com/wiki/Special:Export
Fetched:

### llAbs

- `integer llAbs(integer val)`

### llAcos

- `float llAcos(float val)`

The returned value is in the range {{Interval

### llAddToLandBanList

- `void llAddToLandBanList(key avatar, float hours
|func_footnote)`

Add avatar to the parcel ban list for the specified number of hours.
A value of 0 for hours will add the agent indefinitely. The smallest value that hours will accept is 0.01; anything smaller will be seen as 0.
Residents teleporting to a parcel where they are banned will be redirected to a neighboring parcel.
|return_text
|spec

### llAddToLandPassList

- `void llAddToLandPassList(key avatar, float hours)`

Add avatar to the land pass list for hours, or indefinitely if hours is zero.
|return_text
|spec

### llAdjustDamage

- `void llAdjustDamage(integer number, float new_damage)`

The llAdjustDamage modifies the amount of damage that will be applied by the current on_damage event after it has completed processing. 
|return_text

### llAgentInExperience

- `integer llAgentInExperience(key agent)`

Determines whether or not the specified agent is in the script's experience.
|func_footnote

### llAllowInventoryDrop

- `void llAllowInventoryDrop(integer add)`

Allows for all users without modify permissions to add inventory items to a prim.
|return_text
|spec

### llAngleBetween

- `float llAngleBetween(rotation a, rotation b)`

### llApplyImpulse

- `void llApplyImpulse(vector momentum, integer local)`

Applies impulse to object
|return_text|spec

### llApplyRotationalImpulse

- `void llApplyRotationalImpulse(vector force, integer local)`

Applies rotational impulse to object.
|func_footnote
|return_text
|spec

### llAsin

- `float llAsin(float val)`

The returned value is in the range {{Interval

### llAtan2

- `float llAtan2(float y|p1_desc, float x|p2_desc)`

Similar to the (y/x) except it utilizes the signs of x & y to determine the quadrant and avoids division by zero.

### llAttachToAvatar

- `void llAttachToAvatar(integer attach_point)`

Attaches the object to the avatar who has granted permission to the script. The object is taken into the users inventory and attached to attach_point.

### llAttachToAvatarTemp

- `void llAttachToAvatarTemp(integer attach_point)`

Follows the same convention as llAttachToAvatar, with the exception that the object will not create new inventory for the user, and will disappear on detach or disconnect. Also, this function can be used on avatars other than the owner (if granted permission) in which case the ownership is changed to the new wearer.

### llAvatarOnLinkSitTarget

- `key llAvatarOnLinkSitTarget(integer link|)`

If the prim lacks a sit target or there is no avatar sitting on the prim, then {{LSL Const|NULL_KEY|key|&quot;00000000-0000-0000-0000-000000000000&quot;

### llAvatarOnSitTarget

- `key llAvatarOnSitTarget()`

If the prim lacks a sit target or there is no avatar sitting on the prim, then NULL_KEY is returned.

### llAxes2Rot

- `rotation llAxes2Rot(vector fwd, vector left, vector up)`

All three vectors must be mutually orthogonal unit vectors.

### llAxisAngle2Rot

- `rotation llAxisAngle2Rot(vector axis|p1_desc, float angle)`

axis need not be normalized, only the direction is important. 
angle need to be between the value 0<angle<PI (higher values than PI lead to 2*PI-angle)
, because a rotation is not really a rotation (it is more of a rigid motion/mirroring) 
,the final destination is the rotation. 
(in other words: it doesn't matter wether you rotate left by 90 degrees or right by 270 degrees it will return the same rotation)
|spec
|caveats

### llBase64ToInteger

- `integer llBase64ToInteger(string str)`

### llBase64ToString

- `string llBase64ToString(string str)`

### llBreakAllLinks

- `void llBreakAllLinks()`

Delinks all prims in the link set.
|func_footnote
|return_text
|spec

### llBreakLink
|inject-2={{Issues/SVC-3510}}
{{LSL_Function/link|link

- `void llBreakLink
|inject-2={{Issues/SVC-3510}}
{{LSL_Function/link|link(integer link)`

Delinks the prim with the given link number in a linked object set
|func_footnote
|return_text
|spec

### llCastRay

- `list llCastRay(vector start, vector end, list options)`

Cast a line from start to end and report collision data for intersections with objects.

### llCeil

- `integer llCeil(float val)`

### llChar

- `string llChar(integer val)`

Construct a single character string from the supplied Unicode value.

### llClearCameraParams

- `void llClearCameraParams()`

Resets all camera parameters to default values and turns off scripted camera control.
|return_text
|spec
|caveats
|constants

### llClearLinkMedia

- `integer llClearLinkMedia(integer link|p1_desc, integer face|p2_desc)`

Clears (deletes) the media and all params from the given face on the linked prim(s).

### llClearPrimMedia

- `integer llClearPrimMedia(integer face|p1_desc)`

Clears (deletes) the media and all params from the given face.

### llCloseRemoteDataChannel

- `void llCloseRemoteDataChannel(key channel)`

Closes XML-RPC channel.

### llCloud

- `float llCloud(vector offset)`

Returned values are in the range {{Interval

### llCollisionFilter

- `void llCollisionFilter(string name, key id, integer accept)`

Sets the collision filter, exclusively or inclusively.
|return_text
|spec

### llCollisionSound

- `void llCollisionSound(string impact_sound, float impact_volume)`

Suppress default collision sounds, replace default impact sounds with impact_sound at the volume impact_volume
|return_text
|spec

### llCollisionSprite

- `void llCollisionSprite(string impact_sprite)`

Suppress default collision sprites, replace default impact sprite with impact_sprite

### llComputeHash

- `string llComputeHash(string message, string algorithm)`

Supported values of algorithm are md5, md5_sha1, sha1, sha224, sha256, sha384, sha512.
|func_desc

### llCos

- `float llCos(float theta)`

### llCreateCharacter

- `void llCreateCharacter(list options)`

Creates a pathfinding entity, known as a "character", from the object containing the script. Required to activate use of pathfinding functions.

### llCreateKeyValue

- `key llCreateKeyValue(string k, string v)`

Start an asynchronous transaction to create a key-value pair associated with the script's using the given key (k) and value (v).

### llCreateLink

- `void llCreateLink(key target, integer parent)`

Attempt to link the script's object with target.

### llCSV2List

- `list llCSV2List(string src)`

DESCRIPTION

### llDamage

- `void llDamage(key target, float damage, integer damage_type)`

This function delivers damage to tasks and agent in the same region.
|return_text

### llDataSizeKeyValue

- `key llDataSizeKeyValue()`

Start an asynchronous transaction to request the used and total amount of data allocated for the .

### llDeleteCharacter

- `void llDeleteCharacter()`

Convert the object back to a standard object, removing all pathfinding properties.

### llDeleteKeyValue

- `key llDeleteKeyValue(string k)`

Start an asynchronous transaction to delete a key-value pair associated with the script's with the given key (k).

### llDeleteSubList

- `list llDeleteSubList(list src, integer start, integer end)`

While the function result is different than src, src is not modified, remember to use or store the result of this function. 
The opposite function would be llListInsertList.

### llDeleteSubString

- `string llDeleteSubString(string src, integer start, integer end)`

Characters at positions start and end are removed.
|func_desc

### llDerezObject

- `integer llDerezObject(key id, integer flag)`

Derezzes an object previously rezzed from within the object containing the script.

### llDetachFromAvatar

- `void llDetachFromAvatar()`

Detach object from avatar.
|return_text
|spec

### llDetectedDamage

- `list llDetectedDamage(integer number)`

Returns an empty list if number does not relate to a valid damage source or if called from a handler other than on_damage
The list has the following format:
[float damage, integer damage_type, float original_damage]
|func_desc

### llDetectedGrab

- `vector llDetectedGrab(integer number
|func_desc)`

Returns if number is out of range or if called from an event other than the touch event.

### llDetectedGroup

- `integer llDetectedGroup(integer number)`

Returns FALSE if number is out of range.
|func_desc

### llDetectedKey

- `key llDetectedKey(integer number)`

Returns an empty key if number does not correspond to a valid sensed object or avatar.
|func_desc

### llDetectedLinkNumber

- `integer llDetectedLinkNumber(integer number)`

For touch and collision categories of events only.
|func_desc
|spec
|caveats
|constants

### llDetectedName

- `string llDetectedName(integer item)`

Returns NULL KEY if item is not valid. 
If the item detected is an avatar then the legacy name is returned.
|func_desc

### llDetectedOwner

- `key llDetectedOwner(integer number)`

Returns an empty key if number does not relate to a valid sensed object
|func_desc

### llDetectedPos

- `vector llDetectedPos(integer number)`

Returns if number is not valid sensed object.
|func_desc

### llDetectedRezzer

- `key llDetectedRezzer(integer number)`

Returns an empty key if number does not correspond to a valid sensed object or avatar.
|func_desc

### llDetectedRot

- `rotation llDetectedRot(integer number)`

Returns if number is not valid sensed object.
|func_desc

### llDetectedTouchBinormal

- `vector llDetectedTouchBinormal(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise you can use llDetectedTouchFace to determine which face was touched.To find the third tangent vector, cross this vector with the normal.
|func_desc
|spec

### llDetectedTouchFace

- `integer llDetectedTouchFace(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise you can use llDetectedTouchFace to determine which face was touched.
|func_desc
|spec

### llDetectedTouchNormal

- `vector llDetectedTouchNormal(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise you can use llDetectedTouchFace to determine which face was touched.To find the third tangent vector, cross the binormal with this vector.
|func_desc
|spec

### llDetectedTouchPos

- `vector llDetectedTouchPos(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise you can use llDetectedTouchFace to determine which face was touched.
|func_desc
|spec

### llDetectedTouchST

- `vector llDetectedTouchST(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise, you can use llDetectedTouchFace to determine which face was touched.
|func_desc
|spec

### llDetectedTouchUV

- `vector llDetectedTouchUV(integer index)`

For the touch category of events only. The prim that was touched may not be the prim receiving the event, use llDetectedLinkNumber to check for this; likewise you can use llDetectedTouchFace to determine which face was touched.
|func_desc

### llDetectedType

- `integer llDetectedType(integer number)`

Returns zero if number is not valid sensed object or avatar.
|func_desc

### llDetectedVel

- `vector llDetectedVel(integer number)`

Returns if number is not valid sensed object or avatar.
|func_desc

### llDialog

- `void llDialog(key avatar|p1_desc, string message|p2_desc, list buttons, integer channel|p4_desc)`

Shows a dialog box in the lower right corner of the avatar's screen (upper right in Viewer 1.x) with a message and choice buttons, as well as an ignore button. This has many uses ranging from simple message delivery to complex menu systems.

### llDie

- `void llDie()`

Deletes the object. The object does not go to the owner's Inventory 🗑 Trash.
|return_text
|spec

### llDumpList2String

- `string llDumpList2String(list src, string separator)`

Use llParseString2List or llParseStringKeepNulls to undo the process.
Unlike llList2CSV, which dumps a list to a comma-separated formatted string with no choice over the separator, llDumpList2String gives you more control. This can be useful if you don't trust commas as a separator because you might be working with data supplied to the script by a user who uses, say, commas as part of a street address.
|func_desc

### llEdgeOfWorld

- `integer llEdgeOfWorld(vector pos|p1_desc, vector dir)`

Checks to see whether the border hit by dir from pos is the edge of the world (has no neighboring simulator).

### llEjectFromLand

- `void llEjectFromLand(key avatar)`

Ejects avatar from the parcel.
|func_footnote
|caveats
|constants

### llEmail

- `void llEmail(string address, string subject, string message)`

Sends an email to address with subject and message.
|return_text

### llEscapeURL

- `string llEscapeURL(string url)`

To clarify, numbers and ASCII7 alphabetical characters are NOT escaped. If a character requires more then one byte in form then it returns multiple "%xx" sequences chained together.
|func_desc

### llEuler2Rot

- `rotation llEuler2Rot(vector v)`

### llEvade

- `void llEvade(key target, list options)`

Characters will (roughly) try to hide from their pursuers if there is a good hiding spot along their fleeing path. Hiding means no direct line of sight from the head of the character (center of the top of its physics bounding box) to the head of its pursuer and no direct path between the two on the navmesh.|

### llExecCharacterCmd

- `void llExecCharacterCmd(integer command, list options)`

Send a command to the pathing system.

### llFabs

- `float llFabs(float val)`

### llFindNotecardTextSync

- `list llFindNotecardTextSync(string name, string pattern, integer start, integer count, list options)`

Returns a list of lines and columns where the search pattern is found in the notecard.

### llFleeFrom

- `void llFleeFrom(vector position, float distance, list options)`

Directs a character to keep a specific distance from a specific position in the region or adjacent regions.

### llFloor

- `integer llFloor(float val)`

### llForceMouselook

- `void llForceMouselook(integer mouselook
|p1_desc)`

Sets if a sitting avatar should be forced into mouselook when they sit on this prim.
|return_text
|spec

### llFrand

- `float llFrand(float mag)`

### llGenerateKey

- `key llGenerateKey()`

Generates a key using [http://en.wikipedia.org/wiki/UUID#Version_5_.28SHA-1_hash.29 Version 5 (SHA-1 hash)] UUID generation to create a unique key.

### llGetAccel

- `vector
|func_footnote
|func_desc llGetAccel()`

### llGetAgentInfo

- `integer llGetAgentInfo(key id
|func_footnote
|func_desc)`

### llGetAgentLanguage

- `string llGetAgentLanguage(key avatar|p1_desc)`

### llGetAgentList

- `list llGetAgentList(integer scope, list options)`

Requests a list of agents currently in the region, limited by the scope parameter.

### llGetAgentSize

- `vector llGetAgentSize(key avatar)`

is returned if avatar is not in the region or if it is not an avatar.
|func_desc

### llGetAlpha

- `float llGetAlpha(integer face)`

Otherwise the return is in the range {{Interval

### llGetAndResetTime

- `float llGetAndResetTime()`

### llGetAnimation

- `string llGetAnimation(key id)`

llGetAgentInfo provides information on some animation states not covered by this function (typing, away, busy). llGetAnimationList provides more detailed information about the running animations, but may not reflect avatar state as accurately as llGetAnimation.
|func_desc

### llGetAnimationList

- `list llGetAnimationList(key avatar
|func_footnote
|func_desc)`

### llGetAnimationOverride

- `string llGetAnimationOverride(string anim_state)`

### llGetAttached

- `integer llGetAttached()`

### llGetAttachedList
|func_desc

- `list llGetAttachedList
|func_desc(key avatar|p1_desc)`

By design HUD attachment keys are not reported by this function. 
If avatar is a child agent, ["NOT ON REGION"] is returned. 
If avatar is not a main agent and not a child agent or not an agent at all, ["NOT FOUND"] is returned.
|spec

### llGetAttachedListFiltered
|func_desc

- `list llGetAttachedListFiltered
|func_desc(key avatar|p1_desc, list options|p2_desc)`

If avatar is a child agent, ["NOT ON REGION"] is returned. 
If avatar is not a main agent and not a child agent or not an agent at all, ["NOT FOUND"] is returned.
|spec

### llGetBoundingBox

- `list llGetBoundingBox(key object)`

The bounding box is for the entire link set, not just the requested prim. Returns an empty list ( [] ) if object is not found.
|func_desc

### llGetCameraAspect

- `float
|func_desc llGetCameraAspect()`

### llGetCameraFOV

- `float
|func_desc llGetCameraFOV()`

### llGetCameraPos

- `vector
|func_desc llGetCameraPos()`

### llGetCameraRot

- `rotation
|func_desc llGetCameraRot()`

### llGetCenterOfMass

- `vector
|func_desc llGetCenterOfMass()`

If called from a child prim, the child's center of mass is returned instead (but still in region coordinates).

### llGetClosestNavPoint

- `list llGetClosestNavPoint(vector point, list options)`

Used to get a point on the navmesh that is the closest point to point.

### llGetColor

- `vector llGetColor(integer face)`

### llGetCreator

- `key llGetCreator()`

### llGetDate

- `string llGetDate()`

If you wish to know the time as well use: llGetTimestamp which uses the format 
|func_desc

### llGetDayLength

- `integer llGetDayLength()`

Return the number of seconds in the day cycle applied to the current parcel. llGetDayLength returns the number of seconds for the current parcel, llGetRegionDayLength is the number of seconds in the day cycle applied to the entire region.

### llGetDayOffset

- `integer llGetDayOffset()`

Return the number of seconds added to the current time before calculating the current environmental time for the parcel. llGetDayOffset returns the value for the current parcel, llGetRegionDayOffset produces the same value for the entire region.

### llGetDisplayName

- `string llGetDisplayName(key id)`

id must specify a valid avatar key, present in or otherwise known to the sim in which the script is running, otherwise an empty string is returned. This function will still return a valid display name if the avatar is a child agent of the sim (i.e., in an adjacent sim, but presently able to see into the one the script is in), or for a short period after the avatar leaves the sim (specifically, when the client completely disconnects from the sim, either as a main or child agent).
|func_desc

### llGetEnergy

- `float
|func_footnote
|func_desc llGetEnergy()`

### llGetEnv

- `string llGetEnv(string name)`

Note that the value returned is a string, you may need to cast it to an integer for use in calculations.
|func_desc

### llGetEnvironment

- `list llGetEnvironment(vector pos, list params)`

If an unknown rule is encountered in the parameter list an error is sent to the debug channel.

### llGetExperienceDetails

- `list llGetExperienceDetails(key experience_id)`

If experience_id is NULL_KEY, then information about the script's experience is returned. In this situation, if the script isn't associated with an experience, an empty list is returned.

### llGetExperienceErrorMessage

- `string llGetExperienceErrorMessage(integer error)`

Returns a text description of a particular Experience LSL error constant.

### llGetForce

- `vector
|func_footnote
|func_desc llGetForce()`

### llGetFreeMemory

- `integer
|func_desc llGetFreeMemory()`

### llGetFreeURLs

- `integer
|func_footnote
|func_desc llGetFreeURLs()`

### llGetGeometricCenter

- `vector
|func_footnote
|func_desc llGetGeometricCenter()`

### llGetGMTclock

- `float llGetGMTclock()`

For SL time, which is the same as California time, use llGetWallclock
|func_desc

### llGetHealth

- `float llGetHealth(key id)`

Returns the current health of an avatar or object in the region.
|return_text

### llGetHTTPHeader

- `string llGetHTTPHeader(key request_id, string header)`

Returns an empty string if the header is not found, if the request_id is not a valid key received through the http_request event, or if the headers can no longer be accessed. Headers can only be accessed before llHTTPResponse is called and with-in the first 30&nbsp;seconds after the http_request event is queued.
|func_desc

### llGetInventoryAcquireTime

- `string llGetInventoryAcquireTime(string item)`

### llGetInventoryCreator

- `key llGetInventoryCreator(string item)`

### llGetInventoryDesc

- `string llGetInventoryDesc(string item)`

### llGetInventoryKey

- `key llGetInventoryKey(string name)`

If name is not copy, mod, trans then the return is {{LSL Const|NULL_KEY|key|&quot;00000000-0000-0000-0000-000000000000&quot;

### llGetInventoryName

- `string llGetInventoryName(integer type, integer number)`

Inventory items are sorted in alphabetical order (not chronological order).
|func_desc

### llGetInventoryNumber

- `integer llGetInventoryNumber(integer type)`

### llGetInventoryPermMask

- `integer llGetInventoryPermMask(string item, integer category)`

### llGetInventoryType

- `integer llGetInventoryType(string name)`

If name does not exist, INVENTORY_NONE is returned (no errors or messages are generated), making this function ideal for testing the existence of a certain item in inventory.

### llGetKey

- `key llGetKey()`

### llGetLandOwnerAt

- `key llGetLandOwnerAt(vector pos)`

### llGetLinkMedia

- `list llGetLinkMedia(integer link|p1_desc, integer face|p2_desc, list params)`

Get the media params for a particular face on a linked prim, given the desired list of named params.

### llGetLinkName

- `string llGetLinkName(integer link)`

|func_desc

### llGetLinkNumber

- `integer llGetLinkNumber()`

0 means the prim is not linked, 1 the prim is the root, 2 the prim is the first child, etc. Links are numbered in the reverse order in which they were linked -- if you select a box, a sphere and a cylinder in that order, then link them, the cylinder is 1, the sphere is 2 and the box is 3. The last selected prim has the lowest link number.
|func_desc

### llGetLinkNumberOfSides

- `integer llGetLinkNumberOfSides(integer link
|func_desc)`

See for more information about faces and the conditions that control the number of faces a prim will have. 
|spec
|caveats
|constants

### llGetLinkPrimitiveParams

- `list llGetLinkPrimitiveParams(integer link, list params)`

Identical to llGetPrimitiveParams except that it acts on the prim specified by the link number given.

### llGetLinkSitFlags

- `integer llGetLinkSitFlags(integer link)`

Returns the current flags on the link's sittarget.
|return_text

### llGetListEntryType

- `integer llGetListEntryType(list src, integer index)`

|func_desc

### llGetListLength

- `integer llGetListLength(list src
|func_footnote
|func_desc)`

### llGetLocalPos

- `vector llGetLocalPos()`

If called from the root prim it returns the position in the region unless it is attached to which it returns the position relative to the attach point.
|func_desc

### llGetLocalRot

- `rotation llGetLocalRot()`

If called from the root prim, it returns the objects rotation.
|func_desc

### llGetMass

- `float
|func_footnote
|func_desc llGetMass()`

|spec

### llGetMassMKS

- `float
|func_footnote
|func_desc llGetMassMKS()`

MKS as used in the name of this function is likely a reference to the [https://en.wikipedia.org/wiki/MKS_system_of_units MKS system of units] (Meter, Kilogram, Second), which form the base of SI units (with some minor differences).
|constants

### llGetMaxScaleFactor

- `float
|func_desc llGetMaxScaleFactor()`

### llGetMemoryLimit

- `integer llGetMemoryLimit()`

Get the maximum memory a script can use.

### llGetMinScaleFactor

- `float
|func_desc llGetMinScaleFactor()`

### llGetMoonDirection

- `vector llGetMoonDirection()`

Returns a normalized vector to the current moon position at the location of object containing the script. llGetMoonDirection is the vector to the parcel's moon, llGetRegionMoonDirection is the vector to region's moon. If there is no custom environment set for the current parcel llGetMoonDirection returns the direction to the region's moon. These functions are altitude aware.

### llGetMoonRotation

- `rotation llGetMoonRotation()`

Return the rotation applied to the moon for the parcel at the location of the object containing the script. These function are altitude aware and so will pick up the moon for their current track. llGetRegionMoonRotation returns the rotation applied at the region level, llGetMoonRotation does the same for the parcel. If there is no custom environment applied to parcel llGetMoonRotation returns the same value as llGetRegionMoonRotation.

### llGetNextEmail

- `void llGetNextEmail(string address, string subject)`

Get the next queued email that comes from address, with specified subject.
|return_text

### llGetNotecardLine

- `key llGetNotecardLine(string name, integer line)`

Requests the line line of the notecard name from the dataserver.

### llGetNotecardLineSync

- `string llGetNotecardLineSync(string name, integer line)`

Gets the line of the notecard name from the region's notecard cache immediately without raising a dataserver event.

### llGetNumberOfNotecardLines

- `key llGetNumberOfNotecardLines(string name
|func_footnote)`

Requests the number of lines in notecard name via the dataserver event (cast dataserver value to integer)

### llGetNumberOfPrims

- `integer
|func_footnote
|func_desc llGetNumberOfPrims()`

### llGetNumberOfSides

- `integer llGetNumberOfSides()`

See for more information about faces and the conditions that control the number of faces a prim will have. 
|func_desc

### llGetObjectAnimationNames

- `list
|func_desc llGetObjectAnimationNames()`

### llGetObjectDesc

- `string llGetObjectDesc()`

To get the ''object's'' description (not the current prim's), use PRIM_DESC or OBJECT_DESC.
|func_desc

### llGetObjectDetails

- `list llGetObjectDetails(key id, list params)`

An empty list if id is not found.
{{LSL Const|OBJECT_UNKNOWN_DETAIL|integer|-1

### llGetObjectLinkKey

- `key llGetObjectLinkKey(key object_id, integer link)`

### llGetObjectMass

- `float llGetObjectMass(key id
|func_footnote
|func_desc)`

### llGetObjectName

- `string llGetObjectName()`

|func_desc

### llGetObjectPermMask

- `integer llGetObjectPermMask(integer category)`

### llGetObjectPrimCount

- `integer llGetObjectPrimCount(key prim|p1_desc)`

Avatars sitting on the object are not counted. Zero is returned if prim: (A) is not found, (B) is part of an attachment{{Footnote|Whether the attachment exception is a bug or a feature is unclear.

### llGetOmega

- `vector
|func_footnote
|func_desc llGetOmega()`

### llGetOwner

- `key
|func_footnote
|func_desc llGetOwner()`

### llGetOwnerKey

- `key llGetOwnerKey(key id
|func_footnote
|func_desc)`

### llGetParcelDetails

- `list llGetParcelDetails(vector pos, list params)`

Both x and y components of pos are clamped to the range {{Interval

### llGetParcelFlags

- `integer llGetParcelFlags(vector pos)`

Both x and y components of pos are clamped to the range {{Interval

### llGetParcelMaxPrims

- `integer llGetParcelMaxPrims(vector pos, integer sim_wide
|func_footnote
|func_desc)`

### llGetParcelMusicURL

- `string llGetParcelMusicURL()`

The object owner must also be the land owner. If the land is deeded to a group the object will need to be deeded to the same group for this function to work.
|func_desc|spec|caveats

### llGetParcelPrimCount

- `integer llGetParcelPrimCount(vector pos|p1_desc, integer category, integer sim_wide|p3_desc
|func_footnote
|func_desc)`

### llGetParcelPrimOwners

- `list llGetParcelPrimOwners(vector pos
|func_desc)`

Requires owner-like permissions for the parcel.

### llGetPermissions

- `integer
|func_footnote
|func_desc llGetPermissions()`

### llGetPermissionsKey

- `key llGetPermissionsKey()`

Returns {{LSL Const|NULL_KEY|key|&quot;00000000-0000-0000-0000-000000000000&quot;

### llGetPhysicsMaterial

- `list llGetPhysicsMaterial()`

Used to get the physical characteristics of an object.

### llGetPos

- `vector
|func_footnote
|func_desc llGetPos()`

### llGetPrimMediaParams

- `list llGetPrimMediaParams(integer face|p1_desc, list params)`

Get the media params for a particular face on an object, given the desired list of names.

### llGetRegionAgentCount

- `integer llGetRegionAgentCount()`

### llGetRegionCorner
|func_desc

- `vector llGetRegionCorner
|func_desc()`

Divide the returned value by 256 to get the region offset.

### llGetRegionDayLength

- `integer llGetRegionDayLength()`

Return the number of seconds in the day cycle applied to the current region. llGetDayLength returns the number of seconds for the current parcel, llGetRegionDayLength is the number of seconds in the day cycle applied to the entire region.

### llGetRegionDayOffset

- `integer llGetRegionDayOffset()`

Return the number of seconds added to the current time before calculating the current environmental time for the region. llGetDayOffset returns the value for the current parcel, llGetRegionDayOffset produces the same value for the entire region.

### llGetRegionFlags

- `integer
|func_desc llGetRegionFlags()`

Only a small number of flags are actually used; the rest (shown below in strike-through) are always zero. In particular, it is not possible to detect the status of "Allow Land Resell", "Allow Land Join/Divide", or "Block Land Show in Search"; nor, obviously, it is possible for a script to detect that "Disable Scripts" has been set.
|spec
|caveats

### llGetRegionFPS

- `float llGetRegionFPS()`

### llGetRegionMoonDirection

- `vector llGetRegionMoonDirection()`

Returns a normalized vector to the current moon position at the location of object containing the script. llGetMoonDirection is the vector to the parcel's moon, llGetRegionMoonDirection is the vector to region's moon. If there is no custom environment set for the current parcel llGetMoonDirection returns the direction to the region's moon. These functions are altitude aware.

### llGetRegionMoonRotation

- `rotation llGetRegionMoonRotation()`

Return the rotation applied to the moon for the region at the location of the object containing the script. These function are altitude aware and so will pick up the moon for their current track. llGetRegionMoonRotation returns the rotation applied at the region level, llGetMoonRotation does the same for the parcel. If there is no custom environment applied to parcel llGetMoonRotation returns the same value as llGetRegionMoonRotation.

### llGetRegionName

- `string
|func_footnote
|func_desc llGetRegionName()`

### llGetRegionSunDirection

- `vector llGetRegionSunDirection()`

Returns a normalized vector to the current sun position at the location of object containing the script. llGetSunDirection is the vector to the parcel's sun, llGetRegionSunDirection is the vector to region's sun. If there is no custom environment set for the current parcel llGetSunDirection returns the direction to the region's sun. These functions are altitude aware.

### llGetRegionSunRotation

- `rotation llGetRegionSunRotation()`

Return the rotation applied to the sun for the region at the location of the object containing the script. These functions are altitude aware and so will pick up the sun for their current track. llGetRegionSunRotation returns the rotation applied at the region level, llGetSunRotation does the same for the parcel. If there is no custom environment applied to parcel llGetSunRotation returns the same value as llGetRegionSunRotation.

### llGetRegionTimeDilation

- `float
|func_desc llGetRegionTimeDilation()`

It is used as the ratio between the change of script time to that of real world time.

### llGetRegionTimeOfDay

- `float llGetRegionTimeOfDay()`

By default (without custom environment settings), Second Life day cycles are 4 hours long (3 hours of light, 1 hour of dark). The sunrise and sunset time varies slowly.
|func_desc

### llGetRenderMaterial

- `string llGetRenderMaterial(integer face)`

If the Material is in the prim's inventory, the return value is the inventory name, otherwise the returned value is the Material UUID.
|spec

### llGetRootPosition

- `vector
|func_footnote
|func_desc llGetRootPosition()`

### llGetRootRotation

- `rotation
|func_footnote
|func_desc llGetRootRotation()`

### llGetRot

- `rotation llGetRot()`

### llGetScale

- `vector
|func_footnote
|func_desc llGetScale()`

### llGetScriptName
|func_footnote
|func_desc

- `string llGetScriptName
|func_footnote
|func_desc()`

### llGetScriptState

- `integer llGetScriptState(string script
|func_footnote
|func_desc)`

### llGetSimStats

- `float llGetSimStats(integer stat_type)`

### llGetSimulatorHostname

- `string
|func_footnote
|func_desc llGetSimulatorHostname()`

### llGetSPMaxMemory

- `integer
|func_desc llGetSPMaxMemory()`

### llGetStartParameter

- `integer llGetStartParameter()`

*If the script was loaded with llRemoteLoadScriptPin then that start parameter is returned.
*If the containing object was rezzed by llRezObjectWithParams or llRezObject or llRezAtRoot then the return is the on_rez parameter.
*If the containing object was manually rezzed, by dragging from inventory, the start parameter is 0.
|func_desc

### llGetStartString

- `string llGetStartString()`

*If the containing object was manually rezzed, by dragging from inventory, the start string is blank.
*This function reads the start string of the object's root prim.
*Child prims of objects rezzed via llRezObjectWithParams() have an empty start string.
|func_desc

### llGetStaticPath
|func_desc

- `list llGetStaticPath
|func_desc(vector start, vector end, float radius, list params)`

The list also always contains an integer in the last element, which is a status code indicating the outcome of the path query:
* If llGetStaticPath() finds a path, it will return waypoint vectors and will return a status code of 0, for success
* If llGetStaticPath() cannot find a path for some reason, it only returns the status code, indicating the sort of error. The error codes correspond to the constants in path_update (e.g. PU_FAILURE_INVALID_START is returned if the start vector is not near the nav mesh)

### llGetStatus

- `integer llGetStatus(integer status)`

### llGetSubString

- `string llGetSubString(string src, integer start, integer end
|func_footnote
|func_desc)`

### llGetSunDirection

- `vector llGetSunDirection()`

Returns a normalized vector to the current sun position at the location of object containing the script. llGetSunDirection is the vector to the parcel's sun, llGetRegionSunDirection is the vector to region's sun. If there is no custom environment set for the current parcel llGetSunDirection returns the direction to the region's sun. These functions are altitude aware.

### llGetSunRotation

- `rotation llGetSunRotation()`

Return the rotation applied to the sun for the parcel at the location of the object containing the script. These function are altitude aware and so will pick up the sun for their current track. llGetRegionSunRotation returns the rotation applied at the region level, llGetSunRotation does the same for the parcel. If there is no custom environment applied to parcel llGetSunRotation returns the same value as llGetRegionSunRotation.

### llGetTexture

- `string llGetTexture(integer face)`

If the texture is in the prim's inventory, the return value is the inventory name, otherwise the returned value is the texture UUID.
|spec

### llGetTextureOffset

- `vector llGetTextureOffset(integer face
|func_footnote
|func_desc)`

### llGetTextureRot

- `float llGetTextureRot(integer face
|func_footnote
|func_desc)`

### llGetTextureScale

- `vector llGetTextureScale(integer face
|func_footnote
|func_desc)`

### llGetTime

- `float llGetTime()`

### llGetTimeOfDay

- `float llGetTimeOfDay()`

By default (without custom environment settings), Second Life day cycles are 4 hours long (3 hours of light, 1 hour of dark). The sunrise and sunset time varies slowly.
|func_desc

### llGetTimestamp

- `string llGetTimestamp()`

Appears to be accurate to milliseconds.
|func_desc

### llGetTorque

- `vector
|func_footnote
|func_desc llGetTorque()`

### llGetUnixTime

- `integer
|func_footnote
|func_desc llGetUnixTime()`

### llGetUsedMemory

- `integer
|func_desc llGetUsedMemory()`

### llGetUsername

- `string llGetUsername(key id)`

id must specify a valid avatar key, present in or otherwise known to the sim in which the script is running, otherwise an empty string is returned. This function will still return a valid username if the avatar is a child agent of the sim (i.e., in an adjacent sim, but presently able to see into the one the script is in), or for a short period after the avatar leaves the sim (specifically, when the client completely disconnects from the sim, either as a main or child agent).
|func_desc

### llGetVel

- `vector llGetVel()`

Speed is the magnitude of the velocity. Speed is measured in meter per second. 
Velocity reported is relative to the global coordinate frame (the object rotation has no affect on this functions output). 
For physic objects , velocity is the velocity of its center of mass llGetCenterOfMass . ( When the object has some torque and has not force , position of the object moves ( it turns ) , but its center of mass is unchanged , so the velocity is null )
|func_desc

### llGetVisualParams

- `list llGetVisualParams(key agentid, list params)`

An empty list if agentid is not found.
An empty string, "", is returned in the place of any invalid or unknown visual parameter.

### llGetWallclock

- `float llGetWallclock()`

For GMT use llGetGMTclock
|func_desc

### llGiveAgentInventory

- `integer llGiveAgentInventory(key agent, string folder, list inventory, list options)`

Gives inventory items to agent, creating a new folder to put them in.

### llGiveInventory

- `void llGiveInventory(key destination|p1_desc, string inventory)`

Give inventory to destination.
|return_text
|spec

### llGiveInventoryList

- `void llGiveInventoryList(key target|p1_desc, string folder, list inventory
|func_footnote
|return_text)`

Gives inventory items to target, creating a new folder to put them in.

### llGiveMoney

- `integer llGiveMoney(key destination, integer amount)`

Transfer amount of L$ money from script owner to destination avatar.
|func_footer
|spec

### llGodLikeRezObject

- `void llGodLikeRezObject(key inventory, vector pos)`

Rez directly off of UUID if owner has god-bit set.

### llGround

- `float llGround(vector offset
|func_desc)`

### llGroundContour

- `vector llGroundContour(vector offset
|func_desc
|func_footnote)`

### llGroundNormal

- `vector llGroundNormal(vector offset
|func_footnote
|func_desc)`

### llGroundRepel

- `void llGroundRepel(float height, integer water, float tau)`

Critically damps to height if within height * 0.5 of ground or water level (which ever is higher). 
|return_text

### llGroundSlope

- `vector llGroundSlope(vector offset
|func_footnote
|func_desc)`

### llHash

- `integer llHash(string val)`

Returns a 32bit hash for the provided string. Returns 0 if the input string is empty.

### llHMAC

- `string llHMAC(string private_key, string msg, string algorithm)`

This function supports md5, sha1, sha224, sha256, sha384, sha512 for algorithm.
|func_desc

### llHTTPRequest

- `key llHTTPRequest(string url, list parameters, string body)`

Sends an HTTP request to the specified URL with the body of the request and parameters. When the response is received, a http_response event is raised.

### llHTTPResponse

- `void llHTTPResponse(key request_id, integer status, string body)`

Responds to request_id with status and body.
|return_text
|spec

### llInsertString

- `string llInsertString(string dst, integer pos, string src)`

i.e. unlike other somewhat similar string functions such as llGetSubString and llDeleteSubString, you cannot use -1 for the counting with this function. You may use instead the function provided a bit further below.
|func_desc

### llInstantMessage

- `void llInstantMessage(key user|p1_desc, string message|p2_desc)`

Sends an Instant Message specified in the string message to the user specified by user.

### llIntegerToBase64

- `string llIntegerToBase64(integer number
|func_footnote
|func_desc)`

### llIsFriend

- `integer llIsFriend(key agent_id)`

### llIsLinkGLTFMaterial

- `integer llIsLinkGLTFMaterial(integer link, integer face)`

### llJson2List

- `list llJson2List(string src)`

This function takes a string representing [http://json.org JSON], and returns a list of the top level.

### llJsonSetValue

- `string llJsonSetValue(string json, list specifiers, string value)`

Returns, if successful, a new [http://json.org JSON] text string which is json with the value indicated by the specifiers list set to value.
If unsuccessful (usually because of specifying an out of bounds array index) it returns JSON_INVALID.
An "out of bounds array index" is defined to be any Integer specifiers greater than the length of an existing array at that level within the Json text or greater than 0 (zero) at a level an array doesn't exist.
A special specifiers, JSON_APPEND, is accepted which appends the value to the end of the array at the specifiers level. Care should be taken- if that level is not an array, the existing Value there will be overwritten and replaced with an array containing value at it's first (0) index.
Contrary to lists and strings, negative indexing of Json arrays is not supported.
If an existing "Key" is specifiers at that level, its Value will be overwritten by value unless value is the magic value JSON_DELETE. If a value does not exist at specifiers, a new Key:Value pair will be formed within the Json object. 
To delete an existing value at specifiers, use JSON_DELETE as the value. Note it will not prune empty objects or arrays at higher levels.
If value is JSON_TRUE, JSON_FALSE or JSON_NULL, the Value set will be the bare words 'true', 'false' or 'null', respectively, at the specifiers location within json.

### llKey2Name

- `string llKey2Name(key id)`

id must specify a valid rezzed prim or avatar key, present in or otherwise known to the sim in which the script is running, otherwise an empty string is returned. In the case of an avatar, this function will still return a valid name if the avatar is a child agent of the sim (i.e., in an adjacent sim, but presently able to see into the one the script is in), or for a short period after the avatar leaves the sim (specifically, when the client completely disconnects from the sim, either as a main or child agent). 
Keys of inventory items will not work; in the case of these, use llGetInventoryName instead.
|func_desc

### llKeyCountKeyValue

- `key llKeyCountKeyValue()`

Start an asynchronous transaction to request the number of keys with the script's .
|func_footnote

### llKeysKeyValue

- `key llKeysKeyValue(integer first, integer count)`

Start an asynchronous transaction to request a number of keys from the script's .

### llLinear2sRGB

- `vector llLinear2sRGB(vector color)`

### llLinkAdjustSoundVolume

- `void llLinkAdjustSoundVolume(integer link, float volume}}

|func_footnote
|func_desc
|return_text
|spec)`

### llLinkParticleSystem

- `void llLinkParticleSystem(integer link, list rules)`

A particle system defined by a list of rules is set for the prim(s) link.
|return_text

### llLinkPlaySound

- `void llLinkPlaySound(integer link, string sound, float volume, integer flags)`

Plays attached sound once at volume
|return_text
|spec

### llLinksetDataAvailable

- `integer llLinksetDataAvailable()`

The llLinksetDataAvailable returns the number of bytes available in the linkset's datastore.
|func_footnote
|spec
|caveats
|helpers

### llLinksetDataCountFound

- `integer llLinksetDataCountFound(string pattern)`

The llLinksetDataCountFound function returns the number of keys in the linkset datastore that match the pattern supplied in the pattern.
|func_footnote

### llLinksetDataCountKeys

- `integer llLinksetDataCountKeys()`

The llLinksetDataCountKeys returns the number of unique keys that have been stored in the linkset's datastore.
|func_footnote
|spec
|caveats
|helpers

### llLinksetDataDeleteFound

- `list llLinksetDataDeleteFound(string pattern, string pass)`

The llLinksetDataDeleteFound function finds and attempts to delete all keys in the data store that match pattern. This function will delete protected key-value pairs only if the matching pass phrase is passed in the pass parameter. The function returns a list, the first entry in the list is the number of keys deleted, the second entry in the list is the number of keys that could not be deleted due to a non-matching pass phrase. 
If this function successfully deletes any keys from the datastore it will trigger a linkset_data event with the type of LINKSET_DATA_MULTIDELETE, the key name will consist of a comma separated list of the key names removed from the datastore.
|func_footnote

### llLinksetDataDeleteProtected
|func_footnote

- `integer llLinksetDataDeleteProtected
|func_footnote(string name, string pass)`

The llLinksetDataDeleteProtected function erases a protected name:value pair from the linkset's datastore. 
|func_footnote

### llLinksetDataFindKeys

- `list llLinksetDataFindKeys(string pattern, integer start, integer count)`

The llLinksetDataFindKeys function returns a list of up to count keys from the datastore that match pattern, starting at the one indicated by start. If count is less than 1, then all keys between start and the end which match pattern are returned. If count minus start exceeds the number of matching keys, the returned list will be shorter than count, down to a zero-length list if start equals or exceeds the number of matching keys. The list is ordered alphabetically.
|func_footnote

### llLinksetDataListKeys

- `list llLinksetDataListKeys(integer start, integer count)`

The llLinksetDataListKeys function returns a list of up to count keys in the datastore, starting at the one indicated by start. If count is less than 1, then all keys between start and the end are returned. If count minus start exceeds the total number of keys, the returned list will be shorter than count, down to a zero-length list if start equals or exceeds the total number of keys.
|func_footnote
|spec

### llLinksetDataReadProtected

- `string llLinksetDataReadProtected(string name, string pass)`

Reads a protected name:value pair from the datastore.
|func_footnote

### llLinksetDataReset
|func_footnote

- `void llLinksetDataReset
|func_footnote()`

The llLinksetDataReset function erases all name:value pairs stored in the linkset's datastore. When this function is called the linkset_data event is triggered in all scripts running in the linkset with an action of LINKSETDATA_RESET.
|func_footnote
|spec

### llLinksetDataWriteProtected

- `integer llLinksetDataWriteProtected(string name, string value, string pass)`

Creates or updates a protected name:value pair from the linkset's datastore. Further attempts to read, write or update the name:value pair must use the protected versions of those functions and must supply the same string that was used in pass.
|func_footnote

### llLinkSetSoundQueueing

- `void llLinkSetSoundQueueing(integer link, integer queue)`

### llLinkSetSoundRadius

- `void llLinkSetSoundRadius(integer link, float radius
|func_footnote
|func_desc
|return_text)`

### llLinkSitTarget

- `void llLinkSitTarget(integer link|, vector offset, rotation rot)`

Set the sit location for the linked prim(s). The sit location is relative to the prim's position and rotation.
|return_text

### llLinkStopSound

- `void llLinkStopSound(integer link)`

### llList2CSV

- `string llList2CSV(list src)`

More precisely the values are separated with a comma and a space (", "). 
This function's functionality is equivalent to llDumpList2String(src, ", "); 
The result of this function is more or less the format, but it does not conform in all its details. 
To reverse the process use llCSV2List. But see the Caveat.
|func_desc

### llList2Float

- `float llList2Float(list src, integer index)`

|func_desc

### llList2Integer

- `integer llList2Integer(list src, integer index)`

|func_desc

### llList2Json

- `string llList2Json(string type, list values)`

This function takes a list and returns a [http://json.org JSON] string of that list as either a json object or json array.

### llList2Key

- `key llList2Key(list src, integer index)`

|func_desc

### llList2List

- `list llList2List(list src, integer start, integer end
|func_footnote
|func_desc)`

### llList2ListSlice

- `list llList2ListSlice(list src, integer start, integer end, integer stride, integer slice_index)`

The index of the first entry in the list is 0 
The index of the first entry in a slice is 0 
If start, end, or slice_index are negative they are indexed from end of list. -1 is last element in the list. -list_length is the 1st element of the list. 
If slice_index is negative it is counted from the end of its stride regardless of whether or not the stride exceeds the end of the list. e.g: -1 is the last element in a stride. 
If start > end the range from start to end is treated as an exclusion range. 
|func_desc

### llList2ListStrided

- `list llList2ListStrided(list src, integer start, integer end, integer stride
|func_footnote
|func_desc)`

### llList2Rot

- `rotation llList2Rot(list src, integer index)`

|func_desc

### llList2String

- `string llList2String(list src, integer index
|func_footnote
|func_desc)`

### llList2Vector

- `vector llList2Vector(list src, integer index
|func_footnote
|func_desc)`

### llListen

- `integer llListen(integer channel, string name, key id, string msg)`

Sets a [http://foldoc.org/index.cgi?query=handle handle] for msg on channel from name and id.

### llListenControl

- `void llListenControl(integer handle, integer active
|func_footnote)`

Makes listen event callback handle active or inactive
|return_text
|spec

### llListenRemove

- `void llListenRemove(integer handle
|func_footnote)`

Removes listen event callback handle
|return_text
|spec

### llListFindList

- `integer llListFindList(list src, list test)`

If test is not found in src, -1 (in LSL) or nil (in SLua) is returned. 
The index of the first entry in the list is 0 
If test is found at the last index in src the positive index is returned (5th entry of 5 returns 4).
|func_desc
|spec

### llListFindListNext

- `integer llListFindListNext(list src, list test, integer instance)`

If test is not found in src, -1 (in LSL) or nil (in SLua) is returned. 
The index of the first entry in the list is 0 
An expansion of llListFindList which adds an instance parameter to select the nth match to test parameter. 
llListFindListNext(src, test, 0); is functionally equivalent to llListFindList(src, test); 
Given a list like [ 'Resident', 'Alexia', 'Resident', 'Bob', 'Resident', 'Steve', 'Resident', 'Evil' ]
using a test of [ 'Resident' ] and an instance of 0, 1, 2, 3 would return indices of 0, 2, 4, and 6 respectively.
Selecting the 4th or greater instance will not be found and will return -1. 
Reverse indexing is also supported. Using an instance of -1, -2, -3, -4 would respectively return 6, 4, 2, 0
And -5 and lower would again return -1 
If test is found at the last index in src the positive index is returned (5th entry of 5 returns 4).
|func_desc
|spec

### llListFindStrided

- `integer llListFindStrided(list src, list test, integer start, integer end, integer stride)`

If test matching range and stride conditions is not found in src, -1 (in LSL) or nil (in SLua) is returned. 
The length of test may be equal to or less than stride in order to generate a match. 
The index of the first entry in the list is 0 
If test is found at the last index in src the positive index is returned (5th entry of 5 returns 4). 
If start or end is negative, it is counted from the end list. The last element in the list is -1, the first is -list_length 
|func_desc
|spec

### llListInsertList

- `list llListInsertList(list dest, list src, integer start
|func_footnote
|func_desc)`

### llListRandomize

- `list llListRandomize(list src, integer stride)`

### llListReplaceList

- `list llListReplaceList(list dest, list src, integer start, integer end
|func_footnote
|func_desc)`

### llListSort

- `list llListSort(list src, integer stride, integer ascending)`

### llListSortStrided

- `list llListSortStrided(list src, integer stride, integer stride_index, integer ascending)`

llListSortStrided is llListSort with the added parameter of stride_index, adding the flexibility to sort by any item in the stride. These routines use the same underlying code and have the same computational complexity.

### llListStatistics

- `float llListStatistics(integer operation, list src)`

If a list entry type is not a float or an integer it is silently ignored. 
|func_desc

### llLoadURL

- `void llLoadURL(key avatar, string message, string url)`

Shows dialog to avatar offering to load web page at url with message. If user clicks yes, launches the page in their web browser, starting the browser if required.
|return_text
|spec

### llLog

- `float llLog(float val)`

To get the base 10 logarithm use .
|func_desc

### llLog10

- `float llLog10(float val)`

To get the {{Wikipedia|natural logarithm

### llLookAt

- `void llLookAt(vector target, float strength, float damping)`

Cause object to point its up axis (positive z) towards target, while keeping its forward axis (positive x) below the horizon.
Continues to track target until llStopLookAt is called.
|return_text

### llLoopSound

- `void llLoopSound(string sound, float volume
|func_footnote)`

Plays attached sound looping indefinitely at volume
|return_text
|spec

### llLoopSoundMaster

- `void llLoopSoundMaster(string sound, float volume
|func_footnote)`

Plays attached sound looping at volume, declares it a sync master.
|return_text
|spec

### llLoopSoundSlave

- `void llLoopSoundSlave(string sound, float volume
|func_footnote)`

Plays attached sound looping at volume, synced to most audible sync master declared by llLoopSoundMaster.
|return_text
|spec

### llMakeExplosion

- `void llMakeExplosion(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset)`

Make a round explosion of particles
|func_footnote
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles

### llMakeFire

- `void llMakeFire(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset
|func_footnote)`

Make fire like particles
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles

### llMakeFountain

- `void llMakeFountain(integer particles, float scale, float vel, float lifetime, float arc, integer bounce, string texture, vector offset, float bounce_offset
|func_footnote)`

Make a fountain of particles
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles

### llMakeSmoke

- `void llMakeSmoke(integer particles, float scale, float vel, float lifetime, float arc, string texture, vector offset
|func_footnote)`

Make smoke like particles
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles

### llManageEstateAccess

- `integer llManageEstateAccess(integer action, key avatar)`

Use to add or remove agents from the estate's agent access or ban lists or groups from the estate's group access list.

### llMapBeacon

- `void llMapBeacon(string region_name, vector pos, list options)`

Asks the viewer to create a beacon for the user and optionally opens the world map centered on the location.
|return_text

### llMapDestination

- `void llMapDestination(string simname, vector pos, vector look_at)`

Opens world map centered on simname with pos highlighted. Only works for scripts attached to avatar, or during touch events.
|return_text
|spec

### llMatchGroup

- `integer llMatchGroup(key avatar|p1_desc|p1_hover, list group_keys)`

(Also suggested to be called as llIsGroupActive or llCheckGroupActive).
This function is a request from several scripters to reach what llDetectedGroup and llSameGroup is not able to provide. It would not cause any security and/or privacy issues due the fact it will return an integer as boolean instead of any information about the group.
Furthermore, this function will only check against an agent's current active group, something which can be readily discovered by most residents using the standard viewer even if the group is marked as hidden.

### llMD5String

- `string llMD5String(string src, integer nonce
|func_footnote
|func_desc)`

### llMessageLinked

- `void llMessageLinked(integer link|p1_desc, integer num, string str, key id)`

The purpose of this function is to allow scripts in the same object to communicate. It triggers a link_message event with the same parameters num, str, and id in all scripts in the prim(s) described by link.

### llMinEventDelay

- `void llMinEventDelay(float delay)`

Set the minimum time between events being handled.
Defaults and minimums vary by the event type, see LSL Delay.
|return_text
|spec

### llModifyLand

- `void llModifyLand(integer action, integer brush)`

Modify land with action on brush
|return_text
|spec

### llModPow

- `integer llModPow(integer a, integer b, integer c
|func_footnote
|func_desc)`

### llMoveToTarget

- `void llMoveToTarget(vector target, float tau)`

Critically damp to target in tau seconds (if the script is physical)
|return_text
|spec

### llName2Key

- `key llName2Key(string name)`

指定した名前のエージェントがリージョンにいない場合、この関数は NULL_KEY を返します。
名前は常に "First[ Last]" または "first[.last]" という形式で提供されます。（ファーストネームとオプションのラストネーム（姓））
ラストネームが省略されている場合、ラストネームとして "Resident" が使用されます。エージェント名では、大文字小文字は考慮されません。
|spec

### llNavigateTo

- `void llNavigateTo(vector pos, list options)`

Directs an object to travel to a defined position in the region or adjacent regions.

### llOffsetTexture

- `void llOffsetTexture(float u, float v, integer face)`

Sets the texture u & v offsets for the chosen face.
|return_text
|spec
|caveats
|constants

### llOpenFloater
|func_desc

- `integer llOpenFloater
|func_desc(string floater_name, string url, list params)`

This function may be called only from a Linden owned experience.

### llOpenRemoteDataChannel
|func_footnote

- `void llOpenRemoteDataChannel
|func_footnote()`

Creates a channel to listen for XML-RPC calls. Will trigger a event with channel id once it is available.
|return_text
|spec

### llOrd

- `integer llOrd(string val, integer index)`

Calculate the ordinal value for a character in a string.

### llOverMyLand

- `integer llOverMyLand(key id)`

On group deeded land the object containing the script must be deeded to the same group. (It is not enough to set the script to the group.)
|func_desc

### llOwnerSay

- `void llOwnerSay(string msg)`

Says msg to the object's owner only, if the owner is currently in the same region.
|return_text
|spec

### llParcelMediaCommandList

- `void llParcelMediaCommandList(list commandList)`

Controls the playback of movies and other multimedia resources on a parcel or for an agent.
|func_footnote
|return_type
|return_text

### llParcelMediaQuery

- `list llParcelMediaQuery(list query
|func_footnote
|func_desc)`

### llParseString2List

- `list llParseString2List(string src, list separators, list spacers)`

In most situations llParseStringKeepNulls should be used instead. Discarding null values is rarely desired.
When dealing with vector and rotation data, consider using llCSV2List instead, since it can correctly parse them.
|func_desc

### llParseStringKeepNulls

- `list llParseStringKeepNulls(string src, list separators, list spacers)`

### llPassCollisions

- `void llPassCollisions(integer pass
|func_footnote)`

Sets the pass-collisions prim attribute.
|return_text
|spec
|caveats
|constants
|examples
|helpers

### llPassTouches

- `void llPassTouches(integer pass
|func_footnote)`

Sets whether touches detected on this prim are passed to the root prim.
|return_text
|spec
|caveats
|constants
|helpers

### llPatrolPoints

- `void llPatrolPoints(list patrolPoints, list options)`

Sets the object patrolling between the points specified in patrolPoints.

### llPlaySound

- `void llPlaySound(string sound, float volume
|func_footnote)`

Plays attached sound once at volume
|return_text
|spec

### llPlaySoundSlave

- `void llPlaySoundSlave(string sound, float volume
|func_footnote)`

Plays attached sound once at volume, synced to next loop of most audible sync master declared by llLoopSoundMaster.
|return_text
|spec

### llPointAt

- `void llPointAt(vector pos
|func_footnote)`

Make agent that owns object point at pos
|return_text
|spec
|caveats
|constants
|examples
|helpers

### llPow

- `float llPow(float base|p1_desc, float exponent|p2_desc)`

Returns when base is negative and exponent is not an integer (an imaginary result, (exponent != (integer)exponent) && (base ).

### llPreloadSound

- `void llPreloadSound(string sound
|func_footnote)`

Preloads sound on viewers within range
|return_text
|spec
|caveats
|constants

### llPursue

- `void llPursue(key target, list options)`

Causes the object to pursue target.

### llPushObject

- `void llPushObject(key target|p1_desc, vector impulse, vector ang_impulse, integer local)`

Applies impulse and ang_impulse to object target
|return_text
|spec

### llReadKeyValue

- `key llReadKeyValue(string k)`

Start an asynchronous transaction to read the value associated with the specified key (k) and the script's .

### llRefreshPrimURL

- `void llRefreshPrimURL()`

Reloads the web page shown on the sides of the object.

### llRegionSay

- `void llRegionSay(integer channel|p1_desc, string msg|p2_desc)`

Says the string msg on channel number channel that can be heard anywhere in the region by a script listening on channel.

### llRegionSayTo

- `void llRegionSayTo(key target, integer channel, string msg)`

Says the text supplied in string msg on channel supplied in integer channel to the object or avatar specified by target
|return_text
|spec

### llReleaseCamera

- `void llReleaseCamera(key avatar
|func_footnote)`

This function is recognized by the compiler, but was never implemented in Second Life.
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles
|notes
|permission
|negative_index

### llReleaseControls
|func_footnote

- `void llReleaseControls
|func_footnote()`

Stop taking inputs (that were taken with llTakeControls), dequeues any remaining control events. If PERMISSION_TAKE_CONTROLS was previously granted, it will be revoked.
|return_text
|spec

### llReleaseURL|return_type

- `void llReleaseURL|return_type(string url)`

Releases the specified URL, it will no longer be usable.
|return_text
|spec

### llRemoteDataReply

- `void llRemoteDataReply(key channel, key message_id, string sdata, integer idata
|func_footnote)`

Send an XML-RPC reply on channel to message_id with payload of string sdata and integer idata
|return_text
|spec

### llRemoteDataSetRegion

- `void llRemoteDataSetRegion()`

Used with XML-RPC. If an object using remote data channels changes regions, you must call this function to reregister the remote data channels.

### llRemoteLoadScript

- `void llRemoteLoadScript(key target, string name, integer running, integer start_param
|func_footnote)`

Deprecated
|return_text
|spec

### llRemoteLoadScriptPin

- `void llRemoteLoadScriptPin(key target|p1_desc, string name|p2_desc, integer pin, integer running, integer start_param)`

Copy script name into target and set to running with a start_param only if target's pin matches pin

### llRemoveFromLandBanList

- `void llRemoveFromLandBanList(key avatar
|func_footnote)`

Remove avatar from the land ban list
|return_text
|spec
|caveats
|constants

### llRemoveFromLandPassList

- `void llRemoveFromLandPassList(key avatar
|constants
|spec
|caveats)`

Remove avatar from the land pass list.
|func_footnote

### llRemoveInventory

- `void llRemoveInventory(string item
|func_footnote)`

Remove the named inventory item
|return_text
|spec

### llRemoveVehicleFlags

- `void llRemoveVehicleFlags(integer flags)`

Disable the specified vehicle flags
|return_text
|spec
|caveats

### llReplaceAgentEnvironment

- `Integer llReplaceAgentEnvironment(key agent_id, float transition, string environment)`

The llReplaceAgentEnvironment function overrides the current region and parcel environment seen by an agent. The new environment persists until the agent crosses to a new region or this function is called with the NULL_KEY or empty string in the environment parameter for the particular agent, doing so will strip all environmental settings applied to this agent as part of the experience. This function must be executed as part of an experience.

### llReplaceEnvironment

- `Integer llReplaceEnvironment(vector position, string environment, integer track_no, integer day_length, integer day_offset)`

The llReplaceEnvironment function replaces the environment in a parcel or a region. Either for a single elevation track or the entire environment. The owner of the script must have permission to edit the environment on the destination parcel, or be an estate manage in the case of an entire region.
In most cases errors are reported as a return value from the function (see table below). However, issues with the environment assets may be reported in the debug chat.

### llReplaceSubString

- `string llReplaceSubString(string src, string pattern, string replacement_pattern, integer count)`

If count = 0, all matching substrings are replaced. If count > 0, substrings are replaced starting from the left/beginning of src. If count < 0, substrings are replaced starting from the right/end of src.
|func_desc

### llRequestAgentData

- `key llRequestAgentData(key id, integer data)`

Requests data about agent id. When data is available the dataserver event will be raised

### llRequestDisplayName

- `key llRequestDisplayName(key id
|func_footnote)`

Requests the Display Name of the agent identified by id. When the Display Name is available the dataserver event will be raised. The agent identified by id does not need to be in the same region or online at the time of the request.

### llRequestExperiencePermissions

- `void llRequestExperiencePermissions(key agent, string name)`

Asks the agent for permission to participate in the script's .

### llRequestInventoryData

- `key llRequestInventoryData(string name|p1_desc
|func_footnote)`

Requests data about the item name in the prim's inventory. When data is available the dataserver event will be raised.

### llRequestPermissions

- `void llRequestPermissions(key agent|p1_desc, integer permissions)`

Ask agent for permissions to run certain classes of functions.

### llRequestSecureURL

- `key llRequestSecureURL()`

Requests one () for use by this object. The http_request event is triggered with result of the request. HTTPS-in uses port .

### llRequestSimulatorData

- `key llRequestSimulatorData(string region, integer data)`

Requests data about region. When data is available the event will be raised.

### llRequestURL

- `key llRequestURL()`

Requests one HTTP:// for use by this script. The http_request event is triggered with the result of the request.

### llRequestUserKey

- `key llRequestUserKey(string username)`

名前に一致するエージェントのエージェント ID を dataserver に要求します。指定する名前は、現在の名前または過去に使用された名前のいずれも使用することが出来ます。指定された名前のエージェントが見つからない場合は、この関数は NULL_KEY 値を返します。 
dataserver イベントが発生した際にリクエストを識別するために使用出来るハンドル（キー）を返します。
この関数で検索するエージェントは、セカンドライフにログインしている必要はありません。
|spec

### llRequestUsername

- `key llRequestUsername(key id)`

Requests the Username of the agent identified by id. When the Username is available the dataserver event will be raised. The agent identified by id does not need to be in the same region or online at the time of the request.

### llResetAnimationOverride

- `void llResetAnimationOverride(string anim_state)`

Resets the animation override of the specified animation state (anim_state) to the corresponding default value.
|spec
|caveats

### llResetLandBanList

- `void llResetLandBanList()`

Removes all residents from the land ban list.
|func_footnote
|return_type
|return_text
|constants
|spec
|caveats

### llResetLandPassList

- `void llResetLandPassList()`

Removes all residents from the land access/pass list.
|func_footnote
|return_type
|return_text
|constants
|spec
|caveats

### llResetOtherScript

- `void llResetOtherScript(string name)`

Resets script name.

### llResetScript

- `void llResetScript()`

Resets the script.
|return_text
|spec
|caveats
|constants

### llResetTime

- `void llResetTime()`

Resets the script-time timer to zero.
|return_text
|spec

### llReturnObjectsByID

- `integer llReturnObjectsByID(list objects)`

If the script is owned by an agent, PERMISSION_RETURN_OBJECTS may be granted by the owner. If the script is owned by a group, this permission may be granted by an agent belonging to the group's "Owners" role.

### llReturnObjectsByOwner

- `integer llReturnObjectsByOwner(key owner, integer scope)`

If the script is owned by an agent, PERMISSION_RETURN_OBJECTS may be granted by the owner. If the script is owned by a group, this permission may be granted by an agent belonging to the group's "Owners" role.

### llRezAtRoot

- `void llRezAtRoot(string inventory, vector position, vector velocity, rotation rot, integer param)`

Instantiate inventory object rotated to rot with its root at position, moving at velocity, using param as the start parameter

### llRezObject

- `void llRezObject(string inventory, vector pos, vector vel, rotation rot, integer param)`

Instantiate inventory object at pos with velocity vel and rotation rot with start parameter param
|return_text
|spec

### llRezObjectWithParams

- `key llRezObjectWithParams(string inventory, list params)`

Instantiate inventory object at pos with an initial set of parameters specified in params.
pos will default to the position of the object containing the script, unless REZ_POS is specified. (see below)

### llRot2Angle

- `float llRot2Angle(rotation rot)`

Use in conjunction with llRot2Axis. To undo use llAxisAngle2Rot.
|func_desc

### llRot2Axis

- `vector llRot2Axis(rotation rot)`

Use in conjunction with . To undo use or .
|func_desc

### llRot2Euler

- `vector llRot2Euler(rotation quat)`

### llRot2Fwd

- `vector llRot2Fwd(rotation q)`

Computes the orientation of the local x-axis relative to the parent (i.e. the root prim or the world).

### llRot2Left

- `vector llRot2Left(rotation q)`

Computes the orientation of the local y-axis relative to the parent (i.e. relative to the root prim or the world).

### llRot2Up

- `vector llRot2Up(rotation q)`

Computes the orientation of the local z-axis relative to the parent (i.e. the root prim or the world).

### llRotateTexture

- `void llRotateTexture(float angle, integer face
|func_footnote)`

Sets the rotation of a texture on the chosen face to angle.
|return_text
|spec
|caveats
|constants

### llRotBetween

- `rotation llRotBetween(vector start, vector end
|func_footnote
|func_desc)`

### llRotLookAt

- `void llRotLookAt(rotation target_direction, float strength, float damping)`

Causes an object to smoothly rotate to target_direction with strength resistance at damping force.
Maintains rotation target_direction until stopped with llStopLookAt.
|return_text
|spec

### llRotTarget

- `integer llRotTarget(rotation rot, float error)`

This function is to have the script know when it has reached a rotation. It registers a rot with a error that triggers at_rot_target and not_at_rot_target events continuously until unregistered.

### llRotTargetRemove

- `void llRotTargetRemove(integer handle
|func_footnote)`

Removes rotational target handle registered with llRotTarget
|return_text
|spec
|caveats
|constants

### llRound

- `integer llRound(float val)`

If the absolute value of the tenths position is 4 or less, val is rounded off; otherwise, val is rounded towards positive infinity.

### llSameGroup

- `integer llSameGroup(key uuid
|func_desc)`

This function compares the of the prim containing the script to that of the of what uuid describes.
It answers these two questions:
*"Is the script's prim in the same group as uuid?"
*"Is the of the script's prim equal to uuid?"

### llSay

- `void llSay(integer channel, string msg)`

Says the text supplied in string msg on channel supplied in integer channel. The message can be heard 20m away, usually (see caveats)
|return_text
|spec
|constants

### llScaleByFactor

- `integer llScaleByFactor(float scaling_factor)`

Attempts to resize the entire object by scaling_factor, maintaining the size-position ratios of the prims.
Resizing is subject to prim scale limits and linkability limits. This function can not resize the object if the linkset is physical, a pathfinding character, in a keyframed motion, or if resizing would cause the parcel to overflow.

### llScaleTexture

- `void llScaleTexture(float u, float v, integer face
|func_footnote)`

Sets the texture u & v scales for the chosen face.
|return_text

### llScriptDanger

- `integer llScriptDanger(vector pos)`

The usefulness of this function is limited as it does not give the reason why the script would be in danger. llGetParcelFlags on the other hand can be used in much the same way and gives more detailed information.
|func_desc

### llScriptProfiler
|return_type

- `void llScriptProfiler
|return_type(integer flags)`

Enables or disables the scripts profiling state.
|Return_text
|func_footer

### llSendRemoteData

- `key llSendRemoteData(key channel, string dest, integer idata, string sdata
|func_footnote)`

Send an XML-RPC request to dest through channel with payload of channel (in a string), integer idata and string sdata.

### llSensor

- `void llSensor(string name, key id, integer type, float radius, float arc)`

Performs a single scan for name and id with type within radius meters and arc radians of forward vector.
Script execution continues immediately. When the scan is completed, a sensor or no_sensor event is put in the event queue.

### llSensorRemove

- `void llSensorRemove()`

Removes the sensor setup by llSensorRepeat.

### llSensorRepeat

- `void llSensorRepeat(string name, key id, integer type, float radius, float arc, float rate)`

Performs a scan for name and id with type within range meters and arc radians of forward vector and repeats every rate seconds. The first scan is not performed until rate seconds have passed.
Script execution continues immediately. Whenever a scan is completed, a sensor or no_sensor event is put in the event queue.
|return_text
|spec

### llSetAgentEnvironment

- `integer llSetAgentEnvironment(key agent_id, float transition, list params)`

This function sets environment values for an individual agent in an experience. The changes to the environment persist until the agent moves to a new region or llSetAgentEnvironment is called for an agent with an empty list. Passing an empty list in params will strip all environmental settings applied to this agent as part of the experience

### llSetAgentRot

- `void llSetAgentRot(rotation rot, integer flags)`

Sets the rotation the avatar to rot.
|return_text

### llSetAlpha

- `void llSetAlpha(float alpha, integer face
|func_footnote)`

Sets the Blinn-Phong alpha on face
|return_text
|spec

### llSetAngularVelocity

- `void llSetAngularVelocity(vector initial_omega, integer local)`

Applies rotational velocity to object. 
It does the same job as llApplyRotationalImpulse but doesn't depend of the mass of object .
|func_footnote
|return_text
|spec
|caveats
|constants

### llSetAnimationOverride

- `void llSetAnimationOverride(string anim_state, string anim)`

Set the animation (anim) that will play for the given animation state (anim_state). 
|spec

### llSetBuoyancy

- `void llSetBuoyancy(float buoyancy|p1_desc)`

Sets the buoyancy of the task or object. Requires physics to be enabled.

### llSetCameraAtOffset

- `void llSetCameraAtOffset(vector offset)`

Sets the point the camera is looking at to offset for avatars that sit on the object.

### llSetCameraEyeOffset

- `void llSetCameraEyeOffset(vector offset)`

Sets the camera eye offset for avatars that sit on the object.

### llSetCameraParams

- `void llSetCameraParams(list rules)`

Sets multiple camera parameters at once.
|return_text
|spec

### llSetClickAction

- `void llSetClickAction(integer action)`

Sets the action performed when a prim is clicked upon (aka click action).

### llSetColor

- `void llSetColor(vector color, integer face
|func_footnote)`

Sets the Blinn-Phong color on face of the prim.
|return_text
|spec

### llSetContentType

- `void llSetContentType(key request_id, integer content_type)`

Sets the header of any subsequent LSL HTTP server response via llHTTPResponse.
|sort
|func_footnote
|return_type
|return_text

### llSetDamage

- `void llSetDamage(float damage)`

Sets the amount of damage that will be done when this object hits an avatar.
|return_text

### llSetEnvironment

- `Integer llSetEnvironment(vector position, list params)`

This function overrides the environmental settings for a region or a parcel. The owner of the script must have permission to modify the environment on the parcel or be an estate manager to change the entire region.
An override for a given parameter can be set at the region scope or parcel scope. It can also be set for a single sky track, all sky tracks, or both. If an override of a given parameter is specified for both an individual track and all tracks, the individual track's override takes priority.
Note that the list of valid parameters differs from those available for llGetEnvironment.

### llSetForce

- `void llSetForce(vector force, integer local)`

Applies force to the object (if the object is physical)
|spec

### llSetForceAndTorque

- `void llSetForceAndTorque(vector force, vector torque, integer local)`

Sets the force and torque of object (if the script is physical)
|spec

### llSetGroundTexture

- `integer llSetGroundTexture(list changes)`

Changes the textures used to paint the terrain of a region. The owner of the script must be able to manage the estate.
|return_text
|spec

### llSetHoverHeight

- `void llSetHoverHeight(float height, integer water, float tau)`

Critically damps to a height above the ground (or water) in tau seconds.
|return_text
|spec

### llSetInventoryPermMask

- `void llSetInventoryPermMask(string item, integer category, integer value)`

Sets the given permission category to the new value on the inventory item.
|return_text
|spec
|caveats

### llSetKeyframedMotion

- `void llSetKeyframedMotion(list keyframes, list options)`

Specify a list of positions, orientations, and timings to be followed by an object. The object will be smoothly moved between those keyframes by the simulator.
Collisions with other nonphysical or keyframed objects will be ignored (no script events will fire and collision processing will not occur). Collisions with physical objects will be computed and reported, but the keyframed object will be unaffected by those collisions. (The physical object will be affected, however.) 
|func_sleep
|func_energy
|func_footnote

### llSetLinkAlpha

- `void llSetLinkAlpha(integer link, float alpha, integer face
|func_footnote)`

If a prim exists in the link set at link, set the Blinn-Phong alpha on face of that prim.
|return_text
|spec

### llSetLinkCamera

- `void llSetLinkCamera(integer link, vector eye|p2_desc, vector at|p3_desc)`

Sets the camera eye offset, and the offset that camera is looking at, for avatars that sit on the linked prim.
|func_footnote
|return_text
|spec

### llSetLinkColor

- `void llSetLinkColor(integer link, vector color, integer face
|func_footnote)`

If a prim exists in the link set at link, set the Blinn-Phong color on face of that prim.
|return_text
|spec

### llSetLinkGLTFOverrides

- `void llSetLinkGLTFOverrides(integer link, integer face, list params)`

Sets or removes individual overrides applied to a PBR texture on a face

### llSetLinkMedia

- `integer llSetLinkMedia(integer link|p1_desc, integer face|p2_desc, list params)`

Set the media params for a particular face on the linked prim(s) without a delay.

### llSetLinkPrimitiveParamsFast

- `void llSetLinkPrimitiveParamsFast(integer link, list rules)`

Sets the prims parameters according to rules.

### llSetLinkRenderMaterial

- `void llSetLinkRenderMaterial(integer link, string material, integer face
|func_footnote)`

If a prim exists in the link set at link, set material on face of that prim. This function will clear most PRIM_GLTF_* properties on the face, with the exceptions of repeats, offsets, and rotation_in_radians
|return_text
|spec

### llSetLinkSitFlags

- `void llSetLinkSitFlags(integer link, integer flags)`

Sets flags on the link's sittarget.
|return_text

### llSetLinkTexture

- `void llSetLinkTexture(integer link, string texture, integer face
|func_footnote)`

If a prim exists in the link set at link, set Blinn-Phong diffuse texture on face of that prim.
|return_text
|spec

### llSetLinkTextureAnim

- `void llSetLinkTextureAnim(integer link, integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)`

Animate the texture on the specified face/faces of the specified prim/prims by setting the texture scale and offset. Identical to llSetTextureAnim except able to modify any prim in the link set.
|return_text

### llSetLocalRot

- `void llSetLocalRot(rotation rot|p1_desc)`

Sets the rotation of a child prim relative to the root prim
|return_text
|spec
|caveats
|constants

### llSetMemoryLimit

- `integer llSetMemoryLimit(integer limit)`

Request limit bytes to be reserved for this script.

### llSetObjectDesc

- `void llSetObjectDesc(string description
|func_footnote)`

Sets the prims description
|return_text
|spec

### llSetObjectName

- `void llSetObjectName(string name)`

Sets the prim's name according to the name parameter.

### llSetObjectPermMask

- `void llSetObjectPermMask(integer mask, integer value)`

Sets the given permission mask to the new value on the root object the task is attached to.
|return_text
|spec
|caveats

### llSetParcelForSale

- `integer llSetParcelForSale(integer ForSale, list Options)`

Sets the parcel the object is on for sale.\nForSale is a boolean, if TRUE
the parcel is put up for sale. Options is a list of options to set for the sale,
such as price, authorized buyer, and whether to include objects on the parcel.\n
Setting ForSale to FALSE will remove the parcel from sale and clear any options
that were set.
This function requires that the script be owned by the parcel owner and that they have granted the PERMISSION_PRIVILEGED_LAND_ACCESS permission.

### llSetParcelMusicURL

- `void llSetParcelMusicURL(string url)`

Sets the streaming audio URL for the parcel object is on
|return_text
|spec
|caveats
|constants

### llSetPayPrice

- `void llSetPayPrice(integer price, list quick_pay_buttons)`

Suggest default amounts for the pay text field and pay buttons of the appearing dialog when someone chooses to pay this object.

### llSetPhysicsMaterial

- `void llSetPhysicsMaterial(integer {{#var:material_mask}}, float gravity_multiplier, float restitution, float friction, float density)`

Used to set the physical characteristics of an object.

### llSetPos

- `void llSetPos(vector pos)`

Moves the object or primitive towards pos without using physics.

### llSetPrimMediaParams

- `integer llSetPrimMediaParams(integer face|p1_desc, list params)`

Set the media params for a particular face.

### llSetPrimURL

- `void llSetPrimURL(string url
|func_footnote)`

Updates the URL for the web page shown on the sides of the object.
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_tests
|also_events
|also_articles

### llSetRegionPos

- `integer llSetRegionPos(vector position)`

Tries to move the entire object so that the root prim is within 0.1m of position.

### llSetRemoteScriptAccessPin

- `void llSetRemoteScriptAccessPin(integer pin)`

Allows a prim to have scripts remotely loaded via llRemoteLoadScriptPin when it is passed the correct pin and the prim is set mod.
|func_footnote
|spec

### llSetRenderMaterial

- `void llSetRenderMaterial(string material, integer face
|func_footnote)`

Sets the material of this prim's face. This function will clear most PRIM_GLTF_* properties on the face, with the exceptions of repeats, offsets, and rotation_in_radians.|return_text.
|spec
|constants

### llSetRot

- `void llSetRot(rotation rot)`

Sets the rotation of the prim to rot.
|return_text

### llSetScale

- `void llSetScale(vector size|p1_desc)`

Sets the size of the prim according to size

### llSetScriptState

- `void llSetScriptState(string name, integer running
|func_footnote)`

Set the running state of the script name.
|return_text
|spec

### llSetSculptAnim

- `void llSetSculptAnim(integer mode, integer sizex, integer sizey, integer start_frame, integer end_frame, float rate, boolean texture_sync)`

'Animate' a sculpted prim by way of segments of a larger sculpt map. (Rather than by using UUID-swapping via llSetPrimitiveParams)

### llSetSitText

- `void llSetSitText(string text
|func_footnote)`

Displays text rather than the default "Sit Here" in the right-click menu.
|return_text

### llSetStatus

- `void llSetStatus(integer status, integer value
|func_footnote)`

Sets the object status attributes indicated in the status} mask to value
|return_text
|spec

### llSetText

- `void llSetText(string text, vector color, float alpha)`

Displays text that hovers over the prim with specific color and translucency (specified with alpha).
|return_text

### llSetTexture

- `void llSetTexture(string texture, integer face
|func_footnote)`

Sets the Blinn-Phong diffuse texture of this prim's face.
|return_text
|spec

### llSetTextureAnim

- `void llSetTextureAnim(integer mode, integer face, integer sizex, integer sizey, float start, float length, float rate)`

Animate the texture on the specified face/faces by setting the texture scale and offset.
|return_text

### llSetTimerEvent

- `void llSetTimerEvent(float sec)`

Cause the timer event to be triggered a maximum of once every sec seconds. Passing in 0.0 stops further timer events.
|func_footnote
|return_text
|spec

### llSetTorque

- `void llSetTorque(vector torque, integer local)`

Sets the torque of object (if the script is physical)
|spec
|caveats
|constants

### llSetTouchText

- `void llSetTouchText(string text)`

Displays text rather than the default "Touch" in the right-click menu
|return_text
|spec

### llSetVehicleFlags

- `void llSetVehicleFlags(integer flags)`

Enabled the specified vehicle flags
|return_text
|spec

### llSetVehicleFloatParam

- `void llSetVehicleFloatParam(integer param, float value
|func_footnote)`

Sets the vehicle float parameter param to value.
|return_text
|spec
|caveats

### llSetVehicleRotationParam

- `void llSetVehicleRotationParam(integer param, rotation rot
|func_footnote)`

Sets the vehicle rotation parameter param to rot.
|return_text
|spec
|caveats

### llSetVehicleType

- `void llSetVehicleType(integer type
|func_footnote)`

Sets the vehicle type to one of the default types.
|return_text
|spec

### llSetVehicleVectorParam

- `void llSetVehicleVectorParam(integer param, vector vec)`

Sets the vehicle vector parameter param to vec.
|return_text
|spec
|caveats

### llSetVelocity

- `void llSetVelocity(vector velocity, integer local)`

Applies velocity to object
|return_text|spec

### llSHA1String

- `string llSHA1String(string src
|func_footnote
|func_desc)`

### llSHA256String

- `string llSHA256String(string src
|func_footnote
|func_desc)`

### llShout

- `void llShout(integer channel, string msg)`

Shouts the text supplied in string msg on channel supplied in integer channel.
|spec
|constants

### llSignRSA

- `string llSignRSA(string private_key, string msg, string algorithm)`

This function supports sha1, sha224, sha256, sha384, sha512 for algorithm.
|func_desc

### llSin

- `float llSin(float theta)`

### llSitOnLink

- `Integer llSitOnLink(key agent_id, integer link)`

The avatar specified by agent_id is forced to sit on the sit target of the prim indicated by the link parameter. If the specified link is already occupied, the simulator searches down the chain of prims in the link set looking for an available sit target.

### llSitTarget

- `void llSitTarget(vector offset, rotation rot)`

Set the sit location for the prim. The sit location is relative to the prim's position and rotation.
|return_text

### llSleep

- `void llSleep(float sec)`

Puts the script to sleep for sec seconds. The script will not do anything during this time.
The script will sleep at least until the next server-frame, which happen every (1/45 = ~0.02222) seconds under normal conditions.
If sec is zero or less, the script will not sleep at all.
|return_text
|spec
|caveats
|constants

### llSound

- `void llSound(string sound, float volume, integer queue, integer loop)`

Plays sound at volume and whether it should loop or not.
|return_text
|spec
|caveats
|constants

### llSoundPreload

- `void llSoundPreload(string sound
|func_footnote)`

Preloads sound on viewers within range.
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_events
|also_tests
|also_articles
|notes
|permission
|negative_index

### llSqrt

- `float llSqrt(float val)`

For imaginary results (val < 0.0), a Math Error is triggered under LSO , or 'NaN' (Not A Number) is returned under Mono

### llStartAnimation

- `void llStartAnimation(string anim)`

Start animation anim for agent that granted PERMISSION_TRIGGER_ANIMATION if the permission has not been revoked.
|return_text
|spec

### llStartObjectAnimation

- `void llStartObjectAnimation(string anim)`

Start animation for the current object.
|return_text
|spec

### llStopAnimation

- `void llStopAnimation(string anim)`

Stop animation anim for agent that granted PERMISSION_TRIGGER_ANIMATION if the permission has not been revoked.
|return_text
|spec

### llStopHover
|func_footnote

- `void llStopHover
|func_footnote()`

Stop hovering to a height
|return_text
|spec
|caveats
|constants

### llStopLookAt

- `void llStopLookAt()`

Stop causing object to point at a target
|return_text
|spec
|caveats
|constants

### llStopMoveToTarget

- `void llStopMoveToTarget()`

Stops critically damped motion
|return_text
|spec
|caveats
|constants
|examples
|helpers
|also_functions
|also_tests
|also_events
|also_articles
|notes

### llStopObjectAnimation

- `void llStopObjectAnimation(string anim)`

Stop an animation for the current object.
|return_text
|spec

### llStopPointAt
|func_footnote

- `void llStopPointAt
|func_footnote()`

Stop agent that owns object pointing
|return_text
|spec
|caveats
|constants
|examples
|helpers

### llStringLength

- `integer llStringLength(string str
|func_footnote
|func_desc)`

### llStringToBase64

- `string llStringToBase64(string str)`

If extra bits are needed to complete the last base64 symbol, those extra bits will be zero. To go in the other direction, use llBase64ToString.
|func_desc

### llStringTrim

- `string llStringTrim(string src|p1_desc, integer type)`

### llSubStringIndex

- `integer llSubStringIndex(string source, string pattern)`

If pattern is not found in source, -1 (in LSL) or nil (in SLua) is returned. 
The index of the first character in the string is 0
|func_desc

### llTakeCamera

- `void llTakeCamera(key avatar
|func_footnote)`

This function is recognized by the compiler, but was never implemented in Second Life.
|return_text

### llTakeControls

- `void llTakeControls(integer controls, integer accept, integer pass_on)`

Allows for intercepting of keyboard and mouse clicks, specifically those specified by controls, from the agent the script has permissions for.
|return_text
|spec

### llTan

- `float llTan(float theta)`

### llTarget

- `integer llTarget(vector position, float range)`

This function is to have the script know when it has reached a position. It registers a position with a range that triggers and events continuously until unregistered.

### llTargetedEmail

- `void llTargetedEmail(integer target, string subject, string message)`

Sends an email to the owner (selected by target) of an object with subject and message.
|return_text

### llTargetOmega

- `void llTargetOmega(vector axis, float spinrate, float gain)`

Rotates the object/prim around axis at a rate of spinrate * llVecMag(axis) in radians per second with strength gain.

### llTargetRemove

- `void llTargetRemove(integer handle
|func_footnote)`

Removes positional target handle registered with llTarget
|return_text
|spec
|caveats
|constants

### llTeleportAgent

- `void llTeleportAgent(key agent, string landmark|p2_desc, vector position, vector look_at)`

Teleports an agent to a landmark stored in the object's inventory.
If landmark is an empty string, the avatar is teleported to the location position in the current region.
If the destination is in the current region, the avatar will land facing look_at as a position within that region. Otherwise, look_at is treated as a unit direction.
|func_footnote

### llTeleportAgentGlobalCoords

- `void llTeleportAgentGlobalCoords(key agent, vector global_coordinates, vector region_coordinates, vector look_at)`

Teleports an agent to region_coordinates within a region specified by global_coordinates.
A region's global coordinates can be retrieved using llRequestSimulatorData("region name", DATA_SIM_POS) 
If the destination is in the current region, the avatar will land facing look_at as a position within that region. Otherwise, look_at is treated as a unit direction.

### llTeleportAgentHome

- `void llTeleportAgentHome(key avatar)`

Teleports avatar on owner's land to their home location without any warning, similar to a God Summons or dying.
|func_footnote
|spec
|caveats
|constants

### llTextBox

- `void llTextBox(key avatar, string message, integer channel
|return_type
|return_text)`

Shows a dialog box on avatar's screen with the text message. It contains a text box for input, any text that is entered is said by avatar on channel when the "Submit" button is clicked.
|func_footnote

### llToLower

- `string llToLower(string src)`

The opposite is llToUpper.
|func_desc

### llToUpper

- `string llToUpper(string src)`

The opposite is llToLower.
|func_desc

### llTransferLindenDollars

- `key llTransferLindenDollars(key destination, integer amount)`

Transfer amount of L$ money from script owner to destination avatar.

### llTransferOwnership

- `integer llTransferOwnership(key agent_id, integer flags, list options)`

Transfer ownership of the object containing this script to agent_id.

### llTriggerSound

- `void llTriggerSound(string sound, float volume)`

Plays sound at volume, centered at but not attached to object.
|return_text
|spec

### llTriggerSoundLimited

- `void llTriggerSoundLimited(string sound|p1_desc, float volume|p2_desc, vector top_north_east, vector bottom_south_west)`

Plays sound at volume, centered at but not attached to the object, limited to the box defined by vectors top_north_east and bottom_south_west
|return_text
|spec

### llUnescapeURL

- `string llUnescapeURL(string url)`

|func_desc

### llUnSit

- `void llUnSit(key id
|func_footnote)`

The agent identified by id is forced to stand up if any of the following apply:
# The agent is sitting on the scripted object
# The agent is over land owned by the scripted object's owner and/or a group the owner has land rights for.
|return_text
|spec
|caveats
|constants

### llUpdateCharacter

- `void llUpdateCharacter(list options)`

Updates settings for a character

### llUpdateKeyValue

- `key llUpdateKeyValue(string k, string v, integer checked, string original_value)`

Start an asynchronous transaction to update a key-value pair associated with the script's with the given key (k) and value (v).

### llVecDist

- `float llVecDist(vector vec_a, vector vec_b)`

### llVecMag

- `float llVecMag(vector vec|p1_desc)`

### llVecNorm

- `vector llVecNorm(vector vec)`

If vec is a ZERO_VECTOR, than the value returned is a ZERO_VECTOR.
|spec
|caveats

### llVerifyRSA

- `integer llVerifyRSA(string public_key, string msg, string signature, string algorithm)`

This function supports sha1, sha224, sha256, sha384, sha512 for algorithm.
|func_desc

### llVolumeDetect

- `void llVolumeDetect(integer detect)`

If detect is TRUE, VolumeDetect is enabled, physical object and avatars can pass through the object.
|return_text

### llWanderWithin

- `void llWanderWithin(vector origin, vector dist, list options)`

Sets a character to wander about a central spot within a specified radius.

### llWater

- `float llWater(vector offset)`

Water height is constant across each entire sim and is typically 20 meters but not always.
|func_desc

### llWhisper

- `void llWhisper(integer channel, string msg)`

Whispers the text supplied in string msg on channel supplied in integer channel.
|return_text
|spec
|constants

### llWind

- `vector llWind(vector offset
|func_footnote)`

### llWorldPosToHUD

- `vector llWorldPosToHUD(vector world_pos
|func_desc)`

### llXorBase64

- `string llXorBase64(string str1, string str2)`

Correctly performs an exclusive or on two strings.

### llXorBase64Strings

- `string llXorBase64Strings(string str1, string str2)`

s2 repeats if it is shorter than s1. Retained for backwards compatibility.

### llXorBase64StringsCorrect

- `string llXorBase64StringsCorrect(string str1, string str2)`

Correctly performs an exclusive or on two Base 64 strings.
