# OSSL Functions

Source: MediaWiki export

---

### osAddAgentToGroup

* `osAddAgentToGroup(key AgentID, string GroupName, string RequestedRole)`

### osAdjustSoundVolume

* `osAdjustSoundVolume(integer linknum, float volume)`

This function was added in 0.9.0.1

### osAvatarPlayAnimation

* `osAvatarPlayAnimation(key avatar, string animation)`

When using this function in an object that requires the user to sit on the object (like a chair,or a poseball), you will need to stop the sit animation by including the following snippet:
changed(integer change)
{
 // Check if there's a change in the link set
 if (change & CHANGED_LINK)
 {
 // Get the key of the user sitting on the object
 key user = llAvatarOnSitTarget();
 // Stop the sit animation
 osAvatarStopAnimation(user, "sit");
 // Play the desired animation on the user
 osAvatarPlayAnimation(user, anim);
 }
}
|

### osAvatarStopAnimation

* `osAvatarStopAnimation(key avatar, string animation)`

### osCauseDamage

* `osCauseDamage(key avatar, float damage)`

### osCauseHealing

* `osCauseHealing(key avatar, float healing)`

Implemented December 30,2009 by Revolution in GIT# 87959464c9db8948bed89909913400bc2eb7524d - Rev 11850

### osClearInertia

* `osClearInertia()`

### osCollisionSound

* `osCollisionSound(string impact_sound, float impact_volume)`

### osDie

* `osDie(key objectID)`

This function was added in the 0.9 version of Open Simulator.
Only objects rezzed by the script can be deleted. This function can not be used on attachments.

### osDropAttachment

* `osDropAttachment()`

This function was added in 0.7.5-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osDropAttachmentAt

* `osDropAttachmentAt(vector pos, rotation rot)`

This function was added in 0.7.5-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceAttachToAvatar

* `osForceAttachToAvatar(integer attachmentPoint)`

This function was added in 0.7.4-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceAttachToAvatarFromInventory

* `osForceAttachToAvatarFromInventory(string itemName, integer attachmentPoint)`

This function was added in 0.7.4-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceAttachToOtherAvatarFromInventory

* `osForceAttachToOtherAvatarFromInventory(string rawAvatarId, string itemName, integer attachmentPoint)`

This function was added in 0.7.4-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceBreakAllLinks

* `osForceBreakAllLinks()`

This function was added in 0.8-post-fixes

### osForceBreakLink

* `osForceBreakLink(integer linknumber)`

This function was added in 0.8-post-fixes

### osForceCreateLink

* `osForceCreateLink(key target, integer parent)`

This function was added in 0.8-post-fixes

### osForceDetachFromAvatar

* `osForceDetachFromAvatar()`

This function was added in 0.7.4-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceDropAttachment

* `osForceDropAttachment()`

This function was added in 0.7.5-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceDropAttachmentAt

* `osForceDropAttachmentAt(vector pos, rotation rot)`

This function was added in 0.7.5-post-fixes. 
See [http://wiki.secondlife.com/wiki/Template:LSL_Constants_Attachment Attachment Points] for the complete list of LSL Attachment Points Constants.

### osForceOtherSit

* `osForceOtherSit(key avatar)`
* `osForceOtherSit(key avatar, key target)`

This function was added in 0.8.1-post-fixes

### osGetParcelDetails

* `osGetParcelDetails(key parcelID, list rules)`

This function was added in 0.9.3.0

### osGetParcelID

* `osGetParcelID()`

This function was added in 0.9.3.0

### osGetParcelIDs

* `osGetParcelIDs()`

This function was added in 0.9.3.0

### osGiveLinkInventory

* `osGiveLinkInventory(integer linkNumber, key destination, string inventory)`

This function was added in 0.9.3.0

### osGiveLinkInventoryList

* `osGiveLinkInventoryList(integer linkNumber, key destination, string category, list inventory)`

This function was added in 0.9.3.0

### osGrantScriptPermissions

* `osGrantScriptPermissions(key allowed_key, string function)`

### osLinkParticleSystem

* `osLinkParticleSystem(LSL_Integer linknumber, LSL_List rules)`
* `|Test`
* `*`

### osListSortInPlace

* `osListSortInPlace(list src, integer stride, integer ascending)`

This function was added in 0.9.2

### osListSortInPlaceStrided

* `osListSortInPlaceStrided(list src, integer stride, integer stride_index, integer ascending)`

This function was added in 0.9.3

### osLocalTeleportAgent

* `osLocalTeleportAgent(key agentID, vector newPosition, vector newVelocity, vector newLookat, integer optionFlags)`

### osLoopSound

* `osLoopSound(integer linknum, string sound, float volume)`

This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked.

### osLoopSoundMaster

* `osLoopSoundMaster(integer linknum, string sound, float volume)`

This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osLoopSoundSlave

* `osLoopSoundSlave(integer linknum, string sound, float volume)`

A prim can only have one active sound. The osLoopSoundSlave() function should refer to a different prim than the one that was defined as a master or it will remove the master sound and there will be no master sound to which the slave can be synchronized.
This function was added in 0.9.0.1 
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osMakeNotecard

* `osMakeNotecard(string notecardName, list contents)`
* `osMakeNotecard(string notecardName, string contents)`

### osMessageAttachments

* `osMessageAttachments(key avatar, string message, list attachmentPoints, integer options);`

This function was added in 0.7.5-post-fixes

### osMessageObject

* `osMessageObject(key primID, string message)`

### osNpcLoadAppearance

* `osNpcLoadAppearance(key npc, string notecard)`

This function was added in 0.7.2-post-fixes
An important hint: This function works only for the npc owner. 
You must create the npc with OsNpcCreate and the option OS_NPC_NOT_OWNED to allow all others to change the appearance.

### osNpcMoveTo

* `osNpcMoveTo(key npc, vector position)`

### osNpcMoveToTarget

* `osNpcMoveToTarget(key npc, vector target, integer options)`

This function was added in 0.7.2-post-fixes

### osNpcPlayAnimation

* `osNpcPlayAnimation(key npc, string animation)`

This function was added in 0.7.3-post-fixes

### osNpcRemove

* `osNpcRemove(key npc)`

If the NPC is the UUID of any other type of agent (i.e. a user's regular avatar, not an NPC), this function will silently fail, not erasing existing avatar. 
In other words, this function does not work on regular avatars but only on NPCs

### osNpcSay

* `osNpcSay(key npc, integer channel, string message)`
* `osNpcSay(key npc, string message)`

This function was added in 0.7.4-post-fixes

### osNpcSayTo

* `osNpcSayTo(key npc, key target, integer channel, string message)`

This function was added in 0.9.1.0 Dev 
This function is based on llRegionSayTo, it therefore has no range limitation inside the region.

### osNpcSetProfileAbout

* `osNpcSetProfileAbout(key npc, string about)`

This function was added in 0.9.0.1

### osNpcSetProfileImage

* `osNpcSetProfileImage(key npc, string image)`

### osNpcSetRot

* `osNpcSetRot(key npc, rotation rot)`

This function was added in 0.7.2-post-fixes

### osNpcShout

* `osNpcShout(key npc, integer channel, string message)`

This function was added in 0.7.4-post-fixes

### osNpcSit

* `osNpcSit(key npc, key target, integer options)`

This function was added in 0.7.2-post-fixes

### osNpcStand

* `osNpcStand(key npc)`

This function was added in 0.7.2-post-fixes

### osNpcStopAnimation

* `osNpcStopAnimation(key npc, string animation)`

This function was added in 0.7.3-post-fixes

### osNpcStopMoveToTarget

* `osNpcStopMoveToTarget(key npc)`

This function was added in 0.7.2-post-fixes

### osNpcTouch

* `osNpcTouch(key npcKey, key objectKey, integer linkNum)`

This function was added in 0.7.4-post-fixes

### osNpcWhisper

* `osNpcWhisper(key npc, int channel, string message)`

This function was added in 0.7.4-post-fixes

### osParcelJoin

* `osParcelJoin(vector pos1, vector pos2)`

This function was added in 0.7

### osParcelSubdivide

* `osParcelSubdivide(vector pos1, vector pos2)`

This function was added in 0.7

### osParticleSystem

* `osParticleSystem(list rules)`
* `|Test`
* `*`

### osPlaySound

* `osPlaySound(integer linknum, string sound, float volume)`

This function was added in 0.9.0.1

### osPlaySoundSlave

* `osPlaySoundSlave(integer linknum, string sound, float volume)`

A prim can only have one active sound. The osPlaySoundSlave() function should refer to a different prim than the one that was defined as a master or it will remove the master sound and there will be no master sound to which the slave can be synchronized.
This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osPreloadSound

* `osPreloadSound(integer linknum, string sound)`

This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osRegionNotice

* `osRegionNotice(string message)`
* `osRegionNotice(key agentID, string message)`

The version of osRegionNotice that takes a second argument was added in the 0.9.0.1 version of OpenSimulator.

### osRemoveLinkInventory

* `osRemoveLinkInventory(integer linkNumber, string name)`

This function was added in 0.9.3.0

### osResetAllScripts

* `osResetAllScripts(integer AllLinkSet)`

This function was added to 0.9.1.0, Oct 10, 2019

### osRevokeScriptPermissions

* `osRevokeScriptPermissions(key revoked_key, string function)`

### osSetContentType

* `osSetContentType(key id, string type)`

This function was added in 0.7.5-post-fixes.

### osSetEstateSunSettings

* `osSetEstateSunSettings(integer sunFixed, float sunHour)`

### osSetHealth

* `osSetHealth(key avatar, float health)`

This function was added in 0.9.0.1

### osSetInertia

* `osSetInertia(float mass, vector centerOfMass, vector principalInertiaScaled, rotation InertiaRot)`

### osSetInertiaAsBox

* `osSetInertiaAsBox(float mass, vector boxSize, vector centerOfMass, rotation rot)`

### osSetInertiaAsCylinder

* `osSetInertiaAsCylinder(float mass,  float radius, float length, vector centerOfMass, rotation rot)`

This function was added in 0.9.0-post-fixes

### osSetInertiaAsSphere

* `osSetInertiaAsSphere(float mass,  float radius, vector centerOfMass)`

### osSetLinkSitActiveRange

* `osSetLinkSitActiveRange(integer linkNumber, float range)`

This function was added in 0.9.2.0

### osSetLinkStandTarget

* `osSetLinkStandTarget(integer linkNumber, vector feetTarget)`

This function was added in 0.9.2.0

### osSetOwnerSpeed

* `osSetOwnerSpeed(float SpeedModifier)`

|

### osSetParcelDetails

* `osSetParcelDetails(vector pos, list rules)`

This function was added in 0.7.2-post-fixes

### osSetParcelMediaURL

* `osSetParcelMediaURL(string url)`

### osSetParcelMusicURL

* `osSetParcelMusicURL(string url)`

### osSetParcelSIPAddress

* `osSetParcelSIPAddress(string SIPAddress)`

### osSetPrimFloatOnWater

* `osSetPrimFloatOnWater(integer float)`

### osSetPrimitiveParams

* `osSetPrimitiveParams(key prim, list rules)`

This function was added in 0.7

### osSetProjectionParams

* `osSetProjectionParams(integer projection, key texture, float fov, float focus, float ambiance)`
* `osSetProjectionParams(integer linknumber, integer projection, key texture, float fov, float focus, float ambiance)`
* `osSetProjectionParams(key prim, integer projection, key texture, float fov, float focus, float ambiance)`

### osSetRegionSunSettings

* `osSetRegionSunSettings(integer useEstateSun, integer sunFixed, float sunHour)`

### osSetRegionWaterHeight

* `osSetRegionWaterHeight(float height)`

### osSetSitActiveRange

* `osSetSitActiveRange(float range)`

This function was added in 0.9.2.0

### osSetSpeed

* `osSetSpeed(key ID, float SpeedModifier)`

As of 0.7.1.1, you can't apply float numbers to SpeedModifier (it will result in script compile error) due to the bug [http://opensimulator.org/mantis/view.php?id=5564 #5564]. On 0.7.2-dev or later, you will able to do so.
|

### osSetStandTarget

* `osSetStandTarget(vector feetTarget)`

This function was added in 0.9.2.0

### osSetSunParam

* `osSetSunParam(string param, float value)`

This function was added in 0.7.2-post-fixes, And does nothing on 0.9.2

### osSetTerrainTexture

* `osSetTerrainTexture(integer level, key texture)`

This function was added in 0.7.4-post-fixes

### osSetTerrainTextureHeight

* `osSetTerrainTextureHeight(integer corner, float low, float high)`

This function was added in 0.7.4-post-fixes

### osSetTerrainTextures

* `osSetTerrainTextures(list textureKeys, integer types)`

This function was added in 0.9.3.1

### osSetWindParam

* `osSetWindParam(string plugin, string param, float value)`

This function was added in 0.7.2-post-fixes and replaces the deprecated osWindParamSet function.

### osStopSound

* `osStopSound(integer linknum)`

This function was added in 0.9.0.1. 
Until 0.9.2 only one prim could be specified. Now it does handle all LINK_* constants and can stop sounds on several prims on according, note that on large link sets this can be very heavy.

### osTeleportAgent

* `osTeleportAgent(key agent, string regionName, vector position, vector lookat)`
* `osTeleportAgent(key agent, integer regionX, integer regionY, vector position, vector lookat)`
* `osTeleportAgent(key agent, vector position, vector lookat)`

osTeleportAgent has a 0.5 second delay if the teleport is not allowed, or when the destination is to a location in the same region as the Agents current region. A teleport to other region has a 5 second delay 
For teleports within region, in particular NPC agents, consider using osLocalTeleportAgent

### osTeleportOwner

* `osTeleportOwner(string regionName, vector position, vector lookat)`
* `osTeleportOwner(integer regionX, integer regionY, vector position, vector lookat)`
* `osTeleportOwner(vector position, vector lookat)`

This function was added in 0.7.2-post-fixes
osTeleportOwner has a 0.5 second delay if the teleport is not allowed, or when the destination is to a location in the same region as the Agents current region.

### osTerrainFlush

* `osTerrainFlush();`

### osTriggerSound

* `osTriggerSound(integer linknum, string sound, float volume)`

This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osTriggerSoundLimited

* `osTriggerSoundLimited(integer linknum, string sound, float volume, vector north_east_corner, vector south_west_corner)`

This function was added in 0.9.0.1
Since 0.9.1 if target prim inventory does not contain the sound, the inventory of the prim containing the script calling this function is also checked

### osVolumeDetect

* `osVolumeDetect(integer detect)`

This function was added in 0.9.0.1
Since version 0.9.2.0, llDetectedLinkNumber will return the DETECTOR prim link number even on collision events and not 0 as spec. Our llVolumeDetect does the same now 
At current time, this is not persistent (so the on_rez on example) 
This is also lost on child prims if physics state changes or on link/unlink. Script must set it again after such changes 
Note that like with llVolumeDetect, the name Volume is misleading. Detection will only be by volume on some basic shapes like pure spheres or pure boxes. On other shapes it will only be by surface collisions. What prims will do by volume or surface, depends on the physics engine The name of function llDetectedLinkNumber is also misleading, it returns the detector prim link number, not the detected.

