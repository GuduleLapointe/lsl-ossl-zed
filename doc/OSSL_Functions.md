# OSSL Functions

Source: tmp/opensim-git/OpenSim/Region/ScriptEngine/Shared/Api/Interface/IOSSL_Api.cs
Generated: 2026-04-18T20:33:12Z

### osAdjustSoundVolume

- `void osAdjustSoundVolume(integer linknum, float volume)`

Sets the sound volume of a given link.

### osAESDecrypt

- `string osAESDecrypt(string secret, string encryptedText)`

Decrypt an encrypted text using osAESEncrypt() and the same Key (secret) used in the encryption. Returns the decrypted text.

### osAESDecryptFrom

- `string osAESDecryptFrom(string secret, string encryptedText, string ivString)`

Decrypt an encrypted text using osAESEncryptTo() and the same Key (secret) and Initialization Vector (ivString) used in the encryption. Returns the decrypted text.

### osAESEncrypt

- `string osAESEncrypt(string secret, string plainText)`

Encrypt a plain text using AES-256-CBC Symmetric Algorithm Key (secret) and a random Initialization Vector (IV). Returns the Hex string of the IV bytes and the Hex string of the encrypted text bytes separated with (:).

### osAESEncryptTo

- `string osAESEncryptTo(string secret, string plainText, string ivString)`

Encrypt a plain text using AES-256-CBC Symmetric Algorithm Key (secret) and a custom Initialization Vector (ivString). Returns the Hex string of the IV bytes and the Hex string of the encrypted text bytes separated with (:).

### osAgentSaveAppearance

- `key osAgentSaveAppearance(key agentId, string notecard)`
- `key osAgentSaveAppearance(key agentId, string notecard, integer includeHuds)`

Save appearance of an avatar to a notecard in the primitive inventory.

### osAngleBetween

- `float osAngleBetween(vector a, vector b)`

Returns the angle between two vectors.

### osApproxEquals

- `integer osApproxEquals(float a, float b)`
- `integer osApproxEquals(float a, float b, float margin)`
- `integer osApproxEquals(vector va, vector vb)`
- `integer osApproxEquals(vector va, vector vb, float margin)`
- `integer osApproxEquals(rotation ra, rotation rb)`
- `integer osApproxEquals(rotation ra, rotation rb, float margin)`

Returns an integer whether two float values are within floating point precision equal.

### osAvatarName2Key

- `string osAvatarName2Key(string firstname, string lastname)`

Returns the avatar key, based on their first and last name.

### osAvatarPlayAnimation

- `void osAvatarPlayAnimation(key avatarId, string animation)`

Forcefully plays a given animation for a given avatar bypassing animation permissions.

### osAvatarStopAnimation

- `void osAvatarStopAnimation(key avatarId, string animation)`

Forcefully stops a given animation for a given avatar bypassing animation permissions.

### osAvatarType

- `integer osAvatarType(key avkey)`
- `integer osAvatarType(string sFirstName, string sLastName)`

Returns the type of a given avatar (key).

### osCauseDamage

- `void osCauseDamage(key avatar, float damage)`

Subtracts health from a given avatar by a given amount.

### osCauseHealing

- `void osCauseHealing(key agentId, float healing)`

Heals a given avatar by a given amount.

### osCheckODE

- `integer osCheckODE()`

### osClearInertia

- `void osClearInertia()`

Unsets the inertia data of the object containing the script.

### osClearObjectAnimations

- `integer osClearObjectAnimations()`

Removes the object animations and returns the count of removed animations.

### osCollisionSound

- `void osCollisionSound(string impact_sound, float impact_volume)`

Sets a given collision sound and volume to the object containing the script.

### osConsoleCommand

- `integer osConsoleCommand(string Command)`

Execute a console command.

### osDetectedCountry

- `string osDetectedCountry(integer number)`

Detected params return of triggered user event of their set country.

### osDie

- `void osDie(key objectUUID)`

Similar to llDie, but works on a given object UUID.

### osDrawEllipse

- `string osDrawEllipse(string drawList, integer width, integer height)`

Appends an ellipse drawing command to the string provided in drawList and returns the result.\nThe ellipse is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawFilledEllipse

- `string osDrawFilledEllipse(string drawList, integer width, integer height)`

Appends a filled ellipse drawing command to the string provided in drawList and returns the result.\nThe ellipse is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawFilledPolygon

- `string osDrawFilledPolygon(string drawList, list x, list y)`

Appends a filled polygon drawing command to the string provided in drawList and returns the result.\nThe polygon is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawFilledRectangle

- `string osDrawFilledRectangle(string drawList, integer width, integer height)`

Appends a filled rectangle drawing command to the string provided in drawList and returns the result.\nThe rectangle is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawImage

- `string osDrawImage(string drawList, integer width, integer height, string image)`

Draw a given image from URL or asset uuid with given width and height at the current draw position.

### osDrawLine

- `string osDrawLine(string drawList, integer startX, integer startY, integer endX, integer endY)`
- `string osDrawLine(string drawList, integer endX, integer endY)`

Draws a line from a starting coordinate (pixels x y) to a target position.

### osDrawPolygon

- `string osDrawPolygon(string drawList, list x, list y)`

Appends a polygon drawing command to the string provided in drawList and returns the result.\nThe polygon is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawRectangle

- `string osDrawRectangle(string drawList, integer width, integer height)`

Appends a rectangle drawing command to the string provided in drawList and returns the result.\nThe rectangle is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.

### osDrawResetTransform

- `string osDrawResetTransform(string drawList)`

Reset all transforms.

### osDrawRotationTransform

- `string osDrawRotationTransform(string drawList, float x)`

Appends a rotation transform drawing command to the string provided in drawList and returns the result.

### osDrawScaleTransform

- `string osDrawScaleTransform(string drawList, float x, float y)`

Appends a scale transform drawing command to the string provided in drawList and returns the result.

### osDrawText

- `string osDrawText(string drawList, string text)`

Draws a given string as text at the current drawing position. Text extends right and downwards.

### osDrawTranslationTransform

- `string osDrawTranslationTransform(string drawList, float x, float y)`

Appends a translation transform drawing command to the string provided in drawList and returns the result.

### osDropAttachment

- `void osDropAttachment()`

Attempts to drop the attachment the script is in to the ground.

### osDropAttachmentAt

- `void osDropAttachmentAt(vector pos, rotation rot)`

Attempts to drop the attachment the script is in to a given position on the ground.

### osEjectFromGroup

- `integer osEjectFromGroup(key agentId)`

Removes a given avatar from the group the object belongs to.

### osForceAttachToAvatar

- `void osForceAttachToAvatar(integer attachment)`

Forcefully attaches the object containing this script to the object owner bypassing attach permissions.

### osForceAttachToAvatarFromInventory

- `void osForceAttachToAvatarFromInventory(string itemName, integer attachment)`

Forcefully attaches an object from the inventory of the object containing this script to the object owner bypassing attach permissions.

### osForceAttachToOtherAvatarFromInventory

- `void osForceAttachToOtherAvatarFromInventory(string rawAvatarId, string itemName, integer attachmentPoint)`

Forcefully attaches an object from the inventory of the object containing this script to a given attachment point of a given avatar bypassing attach permissions.

### osForceBreakAllLinks

- `void osForceBreakAllLinks()`

Break all links of a linkset bypassing object owner permissions.

### osForceBreakLink

- `void osForceBreakLink(integer linknum)`

Break a link of a linkset bypassing object owner permissions.

### osForceCreateLink

- `void osForceCreateLink(string target, integer parent)`

Add a link to a linkset bypassing object owner permissions.

### osForceDetachFromAvatar

- `void osForceDetachFromAvatar()`

Forcefully detach the object containing this script from the avatar it is attached to bypassing attach permissions.

### osForceDropAttachment

- `void osForceDropAttachment()`

Attempts to drop the attachment the script is in to the ground bypassing script permissions.

### osForceDropAttachmentAt

- `void osForceDropAttachmentAt(vector pos, rotation rot)`

Attempts to drop the attachment the script is in to a given position on the ground bypassing script permissions.

### osForceOtherSit

- `void osForceOtherSit(string avatar)`
- `void osForceOtherSit(string avatar, string target)`

Forces a given avatar to sit bypassing permissions.

### osFormatString

- `string osFormatString(string str, list strings)`

Fills a given strings placeholders {%d} with the entries of the given list.

### osGetAgentCountry

- `string osGetAgentCountry(key agentId)`

Returns the country of a user.

### osGetAgentIP

- `string osGetAgentIP(string agent)`

Returns the IP address of a given avatar.

### osGetAgents

- `list osGetAgents()`

Returns a list of avatars in the current region.

### osGetApparentRegionTime

- `float osGetApparentRegionTime()`

Returns the virtual seconds since environment midnight.

### osGetApparentRegionTimeString

- `string osGetApparentRegionTimeString(integer format24)`

Returns the virtual second since environment midnight as timestamp.

### osGetApparentTime

- `float osGetApparentTime()`

Returns the virtual seconds since environment midnight.

### osGetApparentTimeString

- `string osGetApparentTimeString(integer format24)`

Returns the virtual second since environment midnight as timestamp.

### osGetAvatarHomeURI

- `string osGetAvatarHomeURI(string uuid)`

Tries to determine the home grid URI of an avatar.

### osGetAvatarList

- `list osGetAvatarList()`

Returns a strided list (key, position, name) of all the avatars in the region.

### osGetCurrentSunHour

- `float osGetCurrentSunHour()`

Returns the current region sun hour as float (24 hour clock).

### osGetDrawStringSize

- `vector osGetDrawStringSize(string contentType, string text, string fontName, integer fontSize)`

Returns a vector containing the horizontal and vertical dimensions in pixels of the specified text, if drawn in the specified font and at the specified point size. The horizontal extent is returned in the .x component of the vector, and the vertical extent is returned in .y. The .z component is not used.

### osGetGender

- `string osGetGender(key rawAvatarId)`

Returns the gender of a given avatar as string.

### osGetGridCustom

- `string osGetGridCustom(string key)`

Returns custom grid information based on input key.

### osGetGridGatekeeperURI

- `string osGetGridGatekeeperURI()`

Returns the gatekeeper URI of the current grid.

### osGetGridHomeURI

- `string osGetGridHomeURI()`

Returns the home URI of the current grid.

### osGetGridLoginURI

- `string osGetGridLoginURI()`

Returns the login URI of the current grid.

### osGetGridName

- `string osGetGridName()`

Returns the grid name of the current grid.

### osGetGridNick

- `string osGetGridNick()`

Returns the grid nick of the current grid.

### osGetHealRate

- `float osGetHealRate(key agentId)`

Returns the rate of healing for a given avatar.

### osGetHealth

- `float osGetHealth(key agentId)`

Returns the current health of a given avatar.

### osGetInertiaData

- `list osGetInertiaData()`

Returns a list of the inertia data of the object containing the script.

### osGetInventoryDesc

- `string osGetInventoryDesc(string itemNameOrId)`

Returns the description of a given inventory item key or name in the object containing the script.

### osGetInventoryItemKey

- `key osGetInventoryItemKey(string name)`

Returns the key of a given inventory item of the object containing the script. Not the asset UUID.

### osGetInventoryItemKeys

- `list osGetInventoryItemKeys(integer type)`

Returns a list of inventory item keys filtered by type in the object containing the script.

### osGetInventoryLastOwner

- `key osGetInventoryLastOwner(string itemNameOrId)`

Returns the last owner (key) of a given inventory item (name or key) of the object containing the script.

### osGetInventoryName

- `string osGetInventoryName(key itemId)`

Returns the name of a given inventory item key in the object containing the script.

### osGetInventoryNames

- `list osGetInventoryNames(integer type)`

Returns a list of inventory names filtered by type in the object containing the script.

### osGetLastChangedEventKey

- `key osGetLastChangedEventKey()`

Returns the key of the last event setting detected params.

### osGetLinkColor

- `vector osGetLinkColor(integer linknum, integer face)`

Returns the color vector of a given link and face.

### osGetLinkInventoryDesc

- `string osGetLinkInventoryDesc(integer linkNumber, string itemNameorid)`

Returns the description of a given inventory item key or name in a given link.

### osGetLinkInventoryItemKey

- `key osGetLinkInventoryItemKey(integer linkNumber, string name)`

Returns the asset UUID of a given inventory item of a given link.

### osGetLinkInventoryItemKeys

- `list osGetLinkInventoryItemKeys(integer linkNumber, integer type)`

Returns a list of inventory item keys filtered by type in a given link.

### osGetLinkInventoryKey

- `key osGetLinkInventoryKey(integer linkNumber, string name, integer type)`

Returns the asset UUID of a given inventory item filtered by type in a given link.

### osGetLinkInventoryKeys

- `list osGetLinkInventoryKeys(integer linkNumber, integer type)`

Returns a list of asset UUIDs of inventory items filtered by type in a given link.

### osGetLinkInventoryName

- `string osGetLinkInventoryName(integer linkNumber, key itemId)`

Returns the name of a given inventory item key in a given link.

### osGetLinkInventoryNames

- `list osGetLinkInventoryNames(integer linkNumber, integer type)`

Returns a list of inventory names filtered by type in a given link.

### osGetLinkNumber

- `integer osGetLinkNumber(string name)`

Return the link number of a given primitive in the linkset by name.

### osGetLinkPrimitiveParams

- `list osGetLinkPrimitiveParams(integer linknumber, list rules)`

Returns a list of the primitive parameters given its link number.

### osGetLinkSitActiveRange

- `float osGetLinkSitActiveRange(integer linkNumber)`

Returns the max distance for allowing avatars to sit on a given link.

### osGetLinkStandTarget

- `vector osGetLinkStandTarget(integer linkNumber)`

Returns the stand offset of a given link.

### osGetMapTexture

- `key osGetMapTexture()`

Returns the asset UUID of the texture representing the region map tile of the current region.

### osGetNotecard

- `string osGetNotecard(string name)`

Directly returns the entire contents of a given notecard as a string.

### osGetNotecardLine

- `string osGetNotecardLine(string name, integer line)`

Directly returns a given line of a notecard in the primitive inventory.

### osGetNPCList

- `list osGetNPCList()`

Returns a strided list (key, position, name) of all NPCs in the region.

### osGetNumberOfAttachments

- `list osGetNumberOfAttachments(key avatar, list attachmentPoints)`

Returns the number of attachments attached to a list of attachment points of a given avatar.

### osGetNumberOfNotecardLines

- `integer osGetNumberOfNotecardLines(string name)`

Returns the number of lines of a given notecard.

### osGetParcelDetails

- `list osGetParcelDetails(key id, list details)`

Returns a list with the requested parcel details.

### osGetParcelDwell

- `integer osGetParcelDwell(vector pos)`

Returns the number of visitors to the region since start.

### osGetParcelID

- `key osGetParcelID()`

Returns the parcel id of the current parcel.

### osGetParcelIDs

- `list osGetParcelIDs()`

Returns a list of parcel ids of the current region.

### osGetPhysicsEngineName

- `string osGetPhysicsEngineName()`

Returns the name of the currently enabled physics engine.

### osGetPhysicsEngineType

- `string osGetPhysicsEngineType()`

Returns the type of the currently enabled physics engine.

### osGetPrimCount

- `integer osGetPrimCount()`
- `integer osGetPrimCount(key object_id)`

Returns the number of links in the object containing the script.

### osGetPrimitiveParams

- `list osGetPrimitiveParams(key prim, list rules)`

Returns a list of primitive params of a given primitive (object UUID).

### osGetPSTWallclock

- `float osGetPSTWallclock()`

Returns the seconds since midnight of the PST time zone.

### osGetRegionMapTexture

- `key osGetRegionMapTexture(string regionNameOrID)`

Returns the asset UUID of the texture representing the region map tile of a given region name or UUID.

### osGetRegionSize

- `vector osGetRegionSize()`

Returns the x and y size of the region as vector. z is unused.

### osGetRegionStats

- `list osGetRegionStats()`

Returns a list of statistics regarding the region and simulator from the stats reporter module.

### osGetRezzingObject

- `key osGetRezzingObject()`

Returns the key of the object that rezzed the object the script is in.

### osGetScriptEngineName

- `string osGetScriptEngineName()`

Returns the name of the active script engine.

### osGetSimulatorMemory

- `integer osGetSimulatorMemory()`

Returns the current memory usage of the simulator in bytes.

### osGetSimulatorMemoryKB

- `integer osGetSimulatorMemoryKB()`

Returns the current memory usage of the simulator in kilobytes.

### osGetSimulatorVersion

- `string osGetSimulatorVersion()`

Returns the version information of the current simulator.

### osGetSitActiveRange

- `float osGetSitActiveRange()`

Returns the max distance for allowing avatars to sit on the object containing the script.

### osGetSitTargetPos

- `vector osGetSitTargetPos()`

Returns the position of the sit target of the object containing the script.

### osGetSitTargetRot

- `rotation osGetSitTargetRot()`

Returns the rotation of the sit target of the object containing the script.

### osGetSittingAvatarsCount

- `integer osGetSittingAvatarsCount()`
- `integer osGetSittingAvatarsCount(key object_id)`

Returns the number of avatars seated on the object containing the script.

### osGetStandTarget

- `vector osGetStandTarget()`

Returns the stand offset of the object containing the script.

### osGetSunParam

- `float osGetSunParam(string param)`

Returns parameters about the skybox.

### osGetTerrainHeight

- `float osGetTerrainHeight(integer x, integer y)`

Returns the height of terrain at a given x and y coordinate (meters).

### osGetWindParam

- `float osGetWindParam(string plugin, string param)`

Get a parameter from a given wind plugin.

### osGiveLinkInventory

- `void osGiveLinkInventory(integer linkNumber, key destination, string inventory)`

Send a given inventory item (name) from a given link to a destination object or avatar (key).

### osGiveLinkInventoryList

- `void osGiveLinkInventoryList(integer linkNumber, key destination, string folderName, list inventory)`

Send a list of inventory items (key) in a given link to a given destination avatar (key) creating a new named folder.

### osInviteToGroup

- `integer osInviteToGroup(key agentId)`

Sends a group invite to a given avatar for the group the object belongs to.

### osIsNotValidNumber

- `integer osIsNotValidNumber(float v)`

Returns an integer whether a given number is out of bounds or NaN.

### osIsNpc

- `integer osIsNpc(key npc)`

Returns an integer whether a given key is an NPC or avatar.

### osIsUUID

- `integer osIsUUID(string thing)`

Returns an integer whether a given string is a UUID or not.

### osKey2Name

- `string osKey2Name(string id)`

Returns the avatar name given their key.

### osKickAvatar

- `void osKickAvatar(string FirstName, string SurName, string alert)`
- `void osKickAvatar(key agentId, string alert)`

Disconnects an avatar from the simulator by first and last name or avatar key.

### osLinkParticleSystem

- `void osLinkParticleSystem(integer linknumber, list rules)`

Sets the particle system rules of a given link.

### osListAsFloat

- `float osListAsFloat(list src, integer index)`

Returns a float that is at index(>=0) in src or 0 if that is not a float

### osListAsInteger

- `integer osListAsInteger(list src, integer index)`

Returns a integer that is at index(>=0) in src or 0 if that is not a integer

### osListAsRotation

- `rotation osListAsRotation(list src, integer index)`

Returns a rotation that is at index(>=0) in src or zero rotation if that is not a vector

### osListAsString

- `string osListAsString(list src, integer index)`

Returns a string that is at index(>=0) in src or empty string if that is not a string

### osListAsVector

- `vector osListAsVector(list src, integer index)`

Returns a vector that is at index(>=0) in src or Zero vector if that is not a vector

### osListenRegex

- `integer osListenRegex(integer channelID, string name, string ID, string msg, integer regexBitfield)`

Creates a listener that parses matches for name and message through regex.

### osListFindListNext

- `integer osListFindListNext(list src, list test, integer start, integer end, integer instance)`

Returns the nth index of the sublist constrained with start and end count.

### osListSortInPlace

- `void osListSortInPlace(list src, integer stride, integer ascending)`

Sorts a given list in place.

### osListSortInPlaceStrided

- `void osListSortInPlaceStrided(list src, integer stride, integer stride_index, integer ascending)`

Sorts a given strided list in place.

### osLoadedCreationDate

- `string osLoadedCreationDate()`

Returns the creation date of the loaded region scene data.

### osLoadedCreationID

- `string osLoadedCreationID()`

Returns the original region UUID of the loaded region scene data.

### osLoadedCreationTime

- `string osLoadedCreationTime()`

Returns the creation time of the loaded region scene data.

### osLocalTeleportAgent

- `void osLocalTeleportAgent(key agent, vector position, vector velocity, vector lookat, integer flags)`

Teleport a given avatar (key) to a given position and rotation as look at vector with a velocity vector and teleport flags.

### osLoopSound

- `void osLoopSound(integer linknum, string sound, float volume)`

Sets a looping sound and volume of a given link.

### osLoopSoundMaster

- `void osLoopSoundMaster(integer linknum, string sound, float volume)`

Sets a looping sound and volume of a given link as master.

### osLoopSoundSlave

- `void osLoopSoundSlave(integer linknum, string sound, float volume)`

Sets a looping sound and volume of a given link as slave.

### osMakeNotecard

- `void osMakeNotecard(string notecardName, string contents)`
- `void osMakeNotecard(string notecardName, list contents)`

Creates a new notecard in the primitive inventory with given contents.

### osMatchString

- `list osMatchString(string src, string pattern, integer start)`

Returns a list of matches from a given string from a given start.

### osMax

- `float osMax(float a, float b)`

Returns the larger of two given numbers.

### osMessageAttachments

- `void osMessageAttachments(key avatar, string message, list attachmentPoints, integer flags)`

Sends a message as dataserver event to a given attachment based on the avatar key and attachment point. Can be constrained further with options.

### osMessageObject

- `void osMessageObject(key objectUUID, string message)`

Directly send a message as dataserver event to a given object by its key.

### osMin

- `float osMin(float a, float b)`

Returns the smaller of two given numbers.

### osMovePen

- `string osMovePen(string drawList, integer x, integer y)`

Move the drawing position to a given coordinate (pixels x y).

### osNpcCreate

- `key osNpcCreate(string user, string name, vector position, string notecard)`
- `key osNpcCreate(string user, string name, vector position, string notecard, integer options)`

Creates a new NPC with a given name at a given position using a supplied notecard for appearance.

### osNpcGetOwner

- `key osNpcGetOwner(key npc)`

Returns the owner key of a given NPC. NULL_KEY if the NPC is unowned.

### osNpcGetPos

- `vector osNpcGetPos(key npc)`

Returns the position of a given NPC (key).

### osNpcGetRot

- `rotation osNpcGetRot(key npc)`

Returns the current rotation of a given NPC (key).

### osNpcLoadAppearance

- `void osNpcLoadAppearance(key npc, string notecard)`

Loads a given appearance notecard to a given NPC (key).

### osNpcLookAt

- `integer osNpcLookAt(key npckey, integer type, key objkey, vector offset)`

Sets the look at direction of a NPC to a given object (key) and offset.

### osNpcMoveTo

- `void osNpcMoveTo(key npc, vector position)`

Moves a given NPC (key) to a position.

### osNpcMoveToTarget

- `void osNpcMoveToTarget(key npc, vector target, integer options)`

Sets a target for a given NPC (key) to move towards.

### osNpcPlayAnimation

- `void osNpcPlayAnimation(key npc, string animation)`

Instructs a given NPC (key) to play a given animation (name) from the inventory of the object containing the script.

### osNpcRemove

- `void osNpcRemove(key npc)`

Removes a given NPC (key).

### osNpcSaveAppearance

- `key osNpcSaveAppearance(key npc, string notecard)`
- `key osNpcSaveAppearance(key npc, string notecard, integer includeHuds)`

Creates a new notecard with a given name from a given NPC (key).

### osNpcSay

- `void osNpcSay(key npc, string message)`
- `void osNpcSay(key npc, integer channel, string message)`

Instructs a given NPC (key) to say a given message.

### osNpcSayTo

- `void osNpcSayTo(key npc, key target, integer channel, string msg)`

Instructs a given NPC (key) to say to a given avatar (key) a given message on a given channel.

### osNpcSetProfileAbout

- `void osNpcSetProfileAbout(key npc, string about)`

Sets a given NPC (key) profile about text to a given string.

### osNpcSetProfileImage

- `void osNpcSetProfileImage(key npc, string image)`

Sets a given NPC (key) profile image to a given image (asset UUID).

### osNpcSetRot

- `void osNpcSetRot(key npc, rotation rot)`

Sets the rotation of a given NPC (key).

### osNpcShout

- `void osNpcShout(key npc, integer channel, string message)`

Instructs a given NPC (key) to shout a given message on a given channel.

### osNpcSit

- `void osNpcSit(key npc, key target, integer options)`

Instructs a given NPC (key) to sit on a given object (UUID).

### osNpcStand

- `void osNpcStand(key npc)`

Instructs a given NPC (key) to stand up.

### osNpcStopAnimation

- `void osNpcStopAnimation(key npc, string animation)`

Instructs a given NPC (key) to stop playing a given animation (name).

### osNpcStopMoveToTarget

- `void osNpcStopMoveToTarget(key npc)`

Removes the target a given NPC (key) is moving towards.

### osNpcTouch

- `void osNpcTouch(key npcLSL_Key, key object_key, integer link_num)`

Instructs a given NPC (key) to touch a given object (UUID) and link.

### osNpcWhisper

- `void osNpcWhisper(key npc, integer channel, string message)`

Instructs a given NPC (key) to whisper a given message on a given channel.

### osOldList2ListStrided

- `list osOldList2ListStrided(list src, integer start, integer end, integer stride)`

Returns a strided list of a given list.

### osOwnerSaveAppearance

- `key osOwnerSaveAppearance(string notecard)`
- `key osOwnerSaveAppearance(string notecard, integer includeHuds)`

Save appearance of object owner to a notecard in the primitive inventory.

### osParcelJoin

- `void osParcelJoin(vector pos1, vector pos2)`

Joins a parcel with another based on positions within both parcels as vectors.

### osParcelSetDetails

- `void osParcelSetDetails(vector pos, list rules)`

DEPRECATED. Use osSetParcelDetails instead.

### osParcelSubdivide

- `void osParcelSubdivide(vector pos1, vector pos2)`

Subdivides a parcel as rectangle given a start and end position as vector.

### osParticleSystem

- `void osParticleSystem(list rules)`

Sets the particle system rules of the object containing the script.

### osPlaySound

- `void osPlaySound(integer linknum, string sound, float volume)`

Sets a sound and volume of a given link.

### osPlaySoundSlave

- `void osPlaySoundSlave(integer linknum, string sound, float volume)`

Sets a sound and volume of a given link as slave.

### osPreloadSound

- `void osPreloadSound(integer linknum, string sound)`

Sets a sound to preload for a given link.

### osRegexIsMatch

- `integer osRegexIsMatch(string input, string pattern)`

Returns an integer whether the input string matches a regex pattern.

### osRegionNotice

- `void osRegionNotice(string msg)`
- `void osRegionNotice(key agentID, string msg)`

Send a notice message to all avatars in the region.

### osRegionRestart

- `integer osRegionRestart(float seconds)`
- `integer osRegionRestart(float seconds, string msg)`

Schedule a region restart seconds in the future.

### osRemoveLinkInventory

- `void osRemoveLinkInventory(integer linkNumber, string name)`

Removes a inventory item by name in a given link.

### osReplaceAgentEnvironment

- `integer osReplaceAgentEnvironment(key agentkey, integer transition, string daycycle)`

Sets the environment of a given avatar (key) to a given settings item (asset UUID) with transition time.

### osReplaceParcelEnvironment

- `integer osReplaceParcelEnvironment(integer transition, string daycycle)`

Sets the environment of the current parcel to a given settings item (asset UUID) with transition time.

### osReplaceRegionEnvironment

- `integer osReplaceRegionEnvironment(integer transition, string daycycle, float daylen, float dayoffset, float altitude1, float altitude2, float altitude3)`

Alters the region environment base parameters of a given settings item (asset UUID) with transition time.

### osReplaceString

- `string osReplaceString(string src, string pattern, string replace, integer count, integer start)`

Returns a string with replaced substrings given a match pattern from a given start for a given number of matches.

### osRequestSecureURL

- `key osRequestSecureURL(list options)`

Request a new secure URL and directly return the assigned key.

### osRequestURL

- `key osRequestURL(list options)`

Request a new URL and directly return the assigned key.

### osResetAllScripts

- `void osResetAllScripts(integer AllLinkset)`

Resets all scripts in the inventory of a link, the entire linkset or itself.

### osResetEnvironment

- `integer osResetEnvironment(integer parcelOrRegion, integer transition)`

Resets either the parcel or region environment to their default values.

### osRound

- `float osRound(float value, integer digits)`

Rounds a given value to a specified amount of digits.

### osSetContentType

- `void osSetContentType(key id, string type)`

Sets the response type of a HTTP request or response

### osSetDynamicTextureData

- `string osSetDynamicTextureData(string dynamicID, string contentType, string data, string extraParams, integer timer)`

Generate a dynamic texture from a given draw string, returns the texture UUID, applies to all faces.

### osSetDynamicTextureDataBlend

- `string osSetDynamicTextureDataBlend(string dynamicID, string contentType, string data, string extraParams, integer timer, integer alpha)`

Generate a dynamic texture alpha blended from a given draw string, returns the texture UUID, applies to all faces.

### osSetDynamicTextureDataBlendFace

- `string osSetDynamicTextureDataBlendFace(string dynamicID, string contentType, string data, string extraParams, integer blend, integer disp, integer timer, integer alpha, integer face)`

Generate a dynamic texture alpha blended from a given draw string, returns the texture UUID, applies to a given face.

### osSetDynamicTextureDataFace

- `string osSetDynamicTextureDataFace(string dynamicID, string contentType, string data, string extraParams, integer timer, integer face)`

Generate a dynamic texture from a given draw string, returns the texture UUID, applies to a given face.

### osSetDynamicTextureURL

- `string osSetDynamicTextureURL(string dynamicID, string contentType, string url, string extraParams, integer timer)`

Generate a dynamic texture from a given URL, returns the texture UUID, applies to all faces.

### osSetDynamicTextureURLBlend

- `string osSetDynamicTextureURLBlend(string dynamicID, string contentType, string url, string extraParams, integer timer, integer alpha)`

Generate a dynamic texture alpha blended from a given URL, returns the texture UUID, applies to all faces.

### osSetDynamicTextureURLBlendFace

- `string osSetDynamicTextureURLBlendFace(string dynamicID, string contentType, string url, string extraParams, integer blend, integer disp, integer timer, integer alpha, integer face)`

Generate a dynamic texture alpha blended from a given URL, returns the texture UUID, applies to a given face.

### osSetEstateSunSettings

- `void osSetEstateSunSettings(integer sunFixed, float sunHour)`

Set sun type (fixed, daycycle) and time offset for the estate sun.

### osSetFontName

- `string osSetFontName(string drawList, string fontName)`

Set the name of the font that will be used by osDrawText.\n- Threat Level: Not Checked.

### osSetFontSize

- `string osSetFontSize(string drawList, integer fontSize)`

Sets the size of the font used by subsequent osDrawTextText() calls. The fontSize parameter represents the font height in points.

### osSetHealRate

- `void osSetHealRate(key agentId, float health)`

Sets the rate of healing for a given avatar to a given amount.

### osSetHealth

- `void osSetHealth(key agentId, float health)`

Sets the health of a given avatar to a given amount.

### osSetInertia

- `void osSetInertia(float mass, vector centerOfMass, vector principalInertiaScaled, rotation rot)`

Sets the inertia data for the object containing the script.

### osSetInertiaAsBox

- `void osSetInertiaAsBox(float mass, vector boxSize, vector centerOfMass, rotation rot)`

Sets the inertia data for the object containing the script based on a box shape bounding box calculation.

### osSetInertiaAsCylinder

- `void osSetInertiaAsCylinder(float mass, float radius, float length, vector centerOfMass, rotation lslrot)`

Sets the inertia data for the object containing the script based on a cylindrical bounding box calculation.

### osSetInertiaAsSphere

- `void osSetInertiaAsSphere(float mass, float radius, vector centerOfMass)`

Sets the inertia data for the object containing the script based on a spherical bounding box calculation.

### osSetLinkSitActiveRange

- `void osSetLinkSitActiveRange(integer linkNumber, float v)`

Sets the max distance for allowing avatars to sit on a given link..

### osSetLinkStandTarget

- `void osSetLinkStandTarget(integer linkNumber, vector v)`

Sets the stand offset from the position of a given link.

### osSetOwnerSpeed

- `void osSetOwnerSpeed(float SpeedModifier)`

Sets a modifier for the movement speed of the object owner.

### osSetParcelDetails

- `void osSetParcelDetails(vector pos, list rules)`

Sets PARCEl_FLAGS for a parcel given a vector inside the parcel.

### osSetParcelMediaURL

- `void osSetParcelMediaURL(string url)`

Sets the current parcel media URL.

### osSetParcelMusicURL

- `void osSetParcelMusicURL(string url)`

Sets the current parcel music URL.

### osSetParcelSIPAddress

- `void osSetParcelSIPAddress(string SIPAddress)`

Sets the voice module SIP address to a given address.

### osSetPenCap

- `string osSetPenCap(string drawList, string direction, string type)`

Sets the start, end or both caps to either "diamond", "arrow", "round", or default "flat" shape.

### osSetPenColor

- `string osSetPenColor(string drawList, string color)`
- `string osSetPenColor(string drawList, vector color)`
- `string osSetPenColor(string drawList, vector color, float alpha)`

This sets the drawing color to either a named .NET color, a 32-bit color value (formatted as eight hexadecimal digits in the format aarrggbb, representing the eight-bit alpha, red, green and blue channels) or a LSL vector color and alpha float value.

### osSetPenColour

- `string osSetPenColour(string drawList, string colour)`

DEPRECATED. Use osSetPenColor instead.

### osSetPenSize

- `string osSetPenSize(string drawList, integer penSize)`

Sets the pen size to a square of penSize pixels by penSize pixels. If penSize is an odd number, the pen will be exactly centered on the coordinates provided in the various drawing commands.

### osSetPrimFloatOnWater

- `void osSetPrimFloatOnWater(integer floatYN)`

Sets whether the object should float on water.

### osSetPrimitiveParams

- `void osSetPrimitiveParams(key prim, list rules)`

Sets primitive params of a given primitive (object UUID).

### osSetProjectionParams

- `void osSetProjectionParams(integer projection, key texture, float fov, float focus, float amb)`
- `void osSetProjectionParams(key prim, integer projection, key texture, float fov, float focus, float amb)`
- `void osSetProjectionParams(integer linknumber, integer projection, key texture, float fov, float focus, float amb)`

Sets the light projection parameters of the object containing the script.

### osSetRegionSunSettings

- `void osSetRegionSunSettings(integer useEstateSun, integer sunFixed, float sunHour)`

Set whether to use estate sun, sun type (fixed, daycycle) and time offset for the region.

### osSetRegionWaterHeight

- `void osSetRegionWaterHeight(float height)`

Set the water height of the region.

### osSetRot

- `void osSetRot(UUID target, Quaternion rotation)`

### osSetSitActiveRange

- `void osSetSitActiveRange(float v)`

Sets the max distance for allowing avatars to sit on the object containing the script.

### osSetSoundRadius

- `void osSetSoundRadius(integer linknum, float radius)`

Sets the sound radius for a given link.

### osSetSpeed

- `void osSetSpeed(string UUID, float SpeedModifier)`

Sets a modifier for the movement speed of a given avatar.

### osSetStandTarget

- `void osSetStandTarget(vector v)`

Sets the stand offset from the position of the object containing the script.

### osSetSunParam

- `void osSetSunParam(string param, float value)`

Not implemented.

### osSetTerrainHeight

- `integer osSetTerrainHeight(integer x, integer y, float val)`

Set the terrain height at a given x and y coordinate (meters).

### osSetTerrainTexture

- `void osSetTerrainTexture(integer level, key texture)`

Sets the terrain texture for a given level.

### osSetTerrainTextureHeight

- `void osSetTerrainTextureHeight(integer corner, float low, float high)`

Sets the texture low and high values for a given region corner.

### osSetTerrainTextures

- `void osSetTerrainTextures(list textures, integer types)`

Sets terrain textures for legacy viewers it types == 0 or 2, textures for new viewers it types == 1 or 2 or PBR materials if types == 1

### osSetWindParam

- `void osSetWindParam(string plugin, string param, float value)`

Set a parameter in a given wind plugin.

### osSHA256

- `string osSHA256(string input)`

Returns the SHA256 representation of the input string.

### osSlerp

- `rotation osSlerp(rotation a, rotation b, float amount)`
- `vector osSlerp(vector a, vector b, float amount)`

Returns a spherical interpolation of two rotations shifted by amount.

### osStopSound

- `void osStopSound(integer linknum)`

Stops the sound for a given link.

### osStringEndsWith

- `integer osStringEndsWith(string src, string value, integer ignorecase)`

Returns an integer whether a string ends with another string.

### osStringIndexOf

- `integer osStringIndexOf(string src, string value, integer ignorecase)`
- `integer osStringIndexOf(string src, string value, integer start, integer count, integer ignorecase)`

Returns the index of a substring of a given string.

### osStringLastIndexOf

- `integer osStringLastIndexOf(string src, string value, integer ignorecase)`
- `integer osStringLastIndexOf(string src, string value, integer start, integer count, integer ignorecase)`

Returns the index of the last substring of a given string.

### osStringRemove

- `string osStringRemove(string src, integer start, integer count)`

Returns the remainder of a given string with characters from start index and count removed.

### osStringReplace

- `string osStringReplace(string src, string oldvalue, string newvalue)`

Returns a string with a substring replaced with another string.

### osStringStartsWith

- `integer osStringStartsWith(string src, string value, integer ignorecase)`

Returns an integer whether a string starts with another string.

### osStringSubString

- `string osStringSubString(string src, integer start)`
- `string osStringSubString(string src, integer start, integer length)`

Returns the remainder of a string from start index.

### osSunGetParam

- `float osSunGetParam(string param)`

DEPRECATED. Use osGetSunParam instead.

### osSunSetParam

- `void osSunSetParam(string param, float value)`

DEPRECATED. Use osSetSunParam instead.

### osTeleportAgent

- `void osTeleportAgent(string agent, string regionName, vector position, vector lookat)`
- `void osTeleportAgent(string agent, integer regionX, integer regionY, vector position, vector lookat)`
- `void osTeleportAgent(string agent, vector position, vector lookat)`

Teleport a given avatar (key) to a given region by name and local position and rotatation as look at vector.

### osTeleportObject

- `integer osTeleportObject(key objectUUID, vector targetPos, rotation targetrotation, integer flags)`

Teleport a given primitive (object UUID) to a given position and rotation.

### osTeleportOwner

- `void osTeleportOwner(string regionName, vector position, vector lookat)`
- `void osTeleportOwner(integer regionX, integer regionY, vector position, vector lookat)`
- `void osTeleportOwner(vector position, vector lookat)`

Teleport the object owner to a given region by name and local position and rotation as look at vector.

### osTemperature2sRGB

- `vector osTemperature2sRGB(float dtemp)`

Returns the color vector of a given color temperature.

### osTerrainFlush

- `void osTerrainFlush()`

Send terrain to all agents

### osTerrainGetHeight

- `float osTerrainGetHeight(integer x, integer y)`

DEPRECATED. Use osGetTerrainHeight instead.

### osTerrainSetHeight

- `integer osTerrainSetHeight(integer x, integer y, float val)`

DEPRECATED. Use osSetTerrainHeight instead.

### osTriggerSound

- `void osTriggerSound(integer linknum, string sound, float volume)`

Trigger a given preloaded sound with volume for a given link.

### osTriggerSoundLimited

- `void osTriggerSoundLimited(integer linknum, string sound, float volume, vector top_north_east, vector bottom_south_west)`

Trigger a given preloaded sound with volume and axis-aligned bounding box for a given link.

### osUnixTimeToTimestamp

- `string osUnixTimeToTimestamp(integer time)`

Returns the timestamp string for a given unix epoch (seconds).

### osVecDistSquare

- `float osVecDistSquare(vector a, vector b)`

Returns the difference of two squared vectors.

### osVecMagSquare

- `float osVecMagSquare(vector a)`

Returns the squared values of a vector multiplied with each other.

### osVolumeDetect

- `void osVolumeDetect(integer detect)`

Sets or unsets volume detection for the object containing the script.

### osWindActiveModelPluginName

- `string osWindActiveModelPluginName()`

Returns the name of the currently enabled wind plugin.

