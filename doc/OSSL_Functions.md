# OSSL Functions

Source: http://opensimulator.org/wiki/Main_Page
Fetched: 2026-04-17T18:34:12Z

### osAddAgentToGroup

- `osAddAgentToGroup(key AgentID, string GroupName, string RequestedRole)`

Prerequisites 
* The Group must be created
* You must have the Group UUID
* Roles within the group must be defined (default has Everyone & Owners)

### osAdjustSoundVolume

- `osAdjustSoundVolume(integer linknum, float volume)`

Adjust the volume of attached sound for a prim in a linkset.

### osAvatarPlayAnimation

- `osAvatarPlayAnimation(key avatar, string animation)`

This function causes an animation to be played on the specified avatar. 
The variable animation must be the name of an animation within the task inventory. For security reasons, UUIDs are not allowed here.
Instead of the name of an animation in the prim's inventory, you can also use the names of the viewer's [http://wiki.secondlife.com/wiki/Internal_Animations built-in animations].
osAvatarPlayAnimation does not perform any security checks or request animation permissions from the targeted avatar.

### osAvatarStopAnimation

- `osAvatarStopAnimation(key avatar, string animation)`

This function stops the specified animation if it is playing on the avatar given.
The value avatar is a UUID, and the animation value is either the name of an animation in the task inventory or the UUID of an animation. 
If the specified avatar is not logged in or on the same sim as the script, then osAvatarStopAnimation silently fails.

### osCauseDamage

- `osCauseDamage(key avatar, float damage)`

Implemented December 30,2009 by Revolution in GIT# 87959464c9db8948bed89909913400bc2eb7524d - Rev 11850
This is an updated version of Mantis 0003777. It allows for damage on collision, touch, etc.

### osCauseHealing

- `osCauseHealing(key avatar, float healing)`

This does the opposite of osCauseDamage. It gives health to the avatar.

### osClearInertia

- `osClearInertia()`

clears the effect of osSetInertia* functions. Link set total mass, center of mass and inertia will be the values estimated by default from the link set parts.
Caution ! Only supported by ubOde for now

### osCollisionSound

- `osCollisionSound(string impact_sound, float impact_volume)`

Sets collision sound to impact_sound with specified volume.

### osDie

- `osDie(key objectID)`

Deletes an object depending on the target uuid.

### osDropAttachment

- `osDropAttachment()`

Requires script to be granted PERMISSION_ATTACH, drops an attachment like a user-triggered attachment drop.

### osDropAttachmentAt

- `osDropAttachmentAt(vector pos, rotation rot)`

Requires script to be granted PERMISSION_ATTACH, drops an attachment at position pos with rotation rot

### osForceAttachToAvatar

- `osForceAttachToAvatar(integer attachmentPoint)`

Works exactly like llAttachToAvatar() except that PERMISSION_ATTACH is not required.

### osForceAttachToAvatarFromInventory

- `osForceAttachToAvatarFromInventory(string itemName, integer attachmentPoint)`

Attach an inventory item in the object containing this script to the script owner without asking for PERMISSION_ATTACH. 
Nothing happens if the avatar is not in the region.
* itemName - The name of the item. If this is not found then a warning is said to the owner.
* attachmentPoint - The attachment point. For example, ATTACH_CHEST.

### osForceAttachToOtherAvatarFromInventory

- `osForceAttachToOtherAvatarFromInventory(string rawAvatarId, string itemName, integer attachmentPoint)`

Attach an inventory item in the object containing this script to any avatar in the region without asking for PERMISSION_ATTACH. 
Nothing happens if the avatar is not in the region.
* rawAvatarId - The UUID of the avatar to which to attach. Nothing happens if this is not a UUID.
* itemName - The name of the item. If this is not found then a warning is said to the owner.
* attachmentPoint - The attachment point. For example, ATTACH_CHEST.

### osForceBreakAllLinks

- `osForceBreakAllLinks()`

* Identical to llBreakAllLinks() except that it doesn't require the link permission to be granted. Present in 0.8 and later.

### osForceBreakLink

- `osForceBreakLink(integer linknumber)`

* Identical to llBreakLink(integer linknumber) except that it doesn't require the link permission to be granted. Present in 0.8 and later.

### osForceCreateLink

- `osForceCreateLink(key target, integer parent)`

* Idential to llCreateLink() except that it doesn't require the link permission to be granted. Present in 0.8 and later.

### osForceDetachFromAvatar

- `osForceDetachFromAvatar()`

Works exactly like llDetachFromAvatar() except that PERMISSION_ATTACH is not required.

### osForceDropAttachment

- `osForceDropAttachment()`

Drops an attachment like a user-triggered attachment drop without checking if PERMISSION_ATTACH has been granted.

### osForceDropAttachmentAt

- `osForceDropAttachmentAt(vector pos, rotation rot)`

Drops an attachment at position pos with rotation rot without checking if PERMISSION_ATTACH has been granted.

### osForceOtherSit

- `osForceOtherSit(key avatar)`
- `osForceOtherSit(key avatar, key target)`

Forces a sit of targeted avatar onto prim.
* avatar - The key of the avatar to which to attach. Nothing happens if this is not a UUID.
* target - The key of another prim to sit avatar on. Nothing happens if this is not a UUID of prim in region.
In OpenSimulator 0.8.0.1.

### osGetParcelDetails

- `osGetParcelDetails(key parcelID, list rules)`

This function is like [http://wiki.secondlife.com/wiki/LlGetParcelDetails llGetParcelDetails], but using parcel global id (parcelID) instead of position in region.

### osGetParcelID

- `osGetParcelID()`

This function returns the parcel global id (parcelID) of the parcel where host prim is.

### osGetParcelIDs

- `osGetParcelIDs()`

This function returns a list of the parcel global ids of all parcels in region.

### osGiveLinkInventory

- `osGiveLinkInventory(integer linkNumber, key destination, string inventory)`

Give an item located in a child prim inventory.

### osGiveLinkInventoryList

- `osGiveLinkInventoryList(integer linkNumber, key destination, string category, list inventory)`

Give a group of items located in a child prim inventory.

### osGrantScriptPermissions

- `osGrantScriptPermissions(key allowed_key, string function)`

Dynamically allow ossl execution to owner/creator/group by function name.

### osLinkParticleSystem

- `osLinkParticleSystem(LSL_Integer linknumber, LSL_List rules)`

### osListSortInPlace

- `osListSortInPlace(list src, integer stride, integer ascending)`

Identical to llListSort but does the sort on the original list, so using less memory. 
* src: the list to sort
* stride: the list stride.
* ascending: it it is 1 or TRUE, sort in ascending order. If it is any other value, sort in descendent order. 
- Does nothing if the list length is not a multiple of stride. 
- The sort considers the elements that are at indexes that are multiple of stride. The other elements between those multiples are just copied around. 
i.e. if the element at [n * stride] is moved to [m * stride], elements [n * stride + i] are moved to [m * stride + i] for i = 1 to stride -1 (n, m and i integers). 
- if there are different object types (ie some are integer, others string, etc) at the consider indexes [n * stride], each type is considered as a sub list and each sub list is sorted. 
[1,"D",-4,"A","B"] will be [-4,"A",1,"B","D"], in ascending sort and stride 1. 
- Lists with stride 1 and elements all of same type are a lot faster to sort than others, because in that case faster algorithms can be used.

### osListSortInPlaceStrided

- `osListSortInPlaceStrided(list src, integer stride, integer stride_index, integer ascending)`

Identical to llListSortStrided but does the sort on the original list, so using less memory. 
* src: the list to sort
* stride: the list stride.
* stride_index: index of the element to sort by in stride
* ascending: it it is 1 or TRUE, sort in ascending order. If it is any other value, sort in descendent order.

### osLocalTeleportAgent

- `osLocalTeleportAgent(key agentID, vector newPosition, vector newVelocity, vector newLookat, integer optionFlags)`

Teleports an avatar with uuid agentID to the specified newPosition within same region. 
It ignores region teleport settings like Telehub or landpoint 
The avatar must have rights to enter the target position. 
The avatar must had granted PERMISSION_TELEPORT to the script or the owner of the prim containing the script is also be owner of the parcel where the avatar is currently on. 
The function will fail silently if conditions are not meet. 
- If newPosition is outside the region the target will be at nearest region border. 
- newVelocity, if selected with optionFlags bit 0 set, should set a avatar velocity, but may only work with ubOde Physics engine, even so results may be a bit unpredictable. 
It will stop if the avatar collides with anything at destination or if the user presses a movement key. 
It also has a fast decay. This behavior will need future changes. If bit 0 is not set, current velocity is kept 
- newLookAt, if selected with optionFlags bit 1 set, changes the avatar look at direction. 
Bit 2 can alternatively be used to align the look at to the velocity, if that is not zero vector. 
Camera direction will depend on viewer camera state at teleport time (like camera attached to avatar or free). 
Look at is the direction the avatar head will face. Body will face close to that, depending on viewers. Look At Z component is zero. 
If both bits are not set, the look at direction will be the current camera direction 
- OptionFlags is a bit field: 
bit 0 (OS_LTPAG_USEVEL): use newVelocity 
bit 1 (OS_LTPAG_USELOOKAT): use newLookAt 
bit 2 (OS_LTPAG_ALGNLV): align lookat to velocity if it is not zero vector 
bit 3 (OS_LTPAG_FORCEFLY): force fly. 
bit 4 (OS_LTPAG_FORCENOFLY): force no fly. Will not work if viewer has fly after teleport option set 
if both bits 1 and 2 are set bit 2 is ignored 
if both bits 3 and 4 are set bit 4 is ignored

### osLoopSound

- `osLoopSound(integer linknum, string sound, float volume)`

Play the specified sound at the specified volume and loop it indefinitely.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osLoopSoundMaster

- `osLoopSoundMaster(integer linknum, string sound, float volume)`

Play the specified sound at the specified volume and loop it indefinitely.
This sound will be set as a master sound. The playing of the sound in other prims using osLoopSoundSlave will be synchronized to this sound.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osLoopSoundSlave

- `osLoopSoundSlave(integer linknum, string sound, float volume)`

Play the specified sound at the specified volume and loop it indefinitely.
This sound will be set as a slave sound. The playing of a slave sound will be synchronized to the playing of the same sound declared in another prim as the master sound. 
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osMakeNotecard

- `osMakeNotecard(string notecardName, list contents)`
- `osMakeNotecard(string notecardName, string contents)`

Creates a notecard with text in the prim that contains the script. Contents can be either a list or a string.

### osMessageAttachments

- `osMessageAttachments(key avatar, string message, list attachmentPoints, integer options);`

Sends a specified message to the specified avatar's attachments on the specified attachment points.
Behaves as osMessageObject, without the sending script needing to know the attachment keys in advance.
This is incompatible with the normal use of dataserver event on scripts the receiving prim.
Options:
* OS_ATTACH_MSG_INVERT_POINTS invert how the attachment points list should be treated. Will send to all but the listed ones
* OS_ATTACH_MSG_OBJECT_CREATOR send only to those attachments that have the same CreatorID as the script host prim
* OS_ATTACH_MSG_SCRIPT_CREATOR send only to those attachments that have the same CreatorID as the script itself.
This options can be combined with binary or | 
Calling with OS_ATTACH_MSG_ALL in list attachmentPoints will sends the message to attachments on every point. If OS_ATTACH_MSG_INVERT_POINTS is also provide, the message is ignored

### osMessageObject

- `osMessageObject(key primID, string message)`

primID = the UUID of the prim you are messaging. 
message = The string you want to send. 
Sends a message to a prim identified by the given UUID, a script in the prim must implement the dataserver event handler. the dataserver event is passed the UUID of the calling prim and a string message. 
This is incompatible with the normal use of dataserver event on scripts on the receiving prim. 
The dataserver query_id argument should be a unique id of a request. This function just uses it as a sender id. All scripts with dataserver event will receive it with no easy to validate. A normal request may also trigger the event on several scripts of the prim. The target one can compare the query_id and validate it, other scripts can not tell if it is a normal request for other script, or a message. 
this unless the prims can know senders UUIDs and filter based on them

### osNpcLoadAppearance

- `osNpcLoadAppearance(key npc, string notecard)`

Load appearance from a notecard. This notecard must contain appearance data created with one of the save appearance functions.

### osNpcMoveTo

- `osNpcMoveTo(key npc, vector position)`

* Moves npc to the position.

### osNpcMoveToTarget

- `osNpcMoveToTarget(key npc, vector target, integer options)`

Move the NPC to a given target over time. How the NPC will get there depends on the following options.
OS_NPC_FLY - Fly the NPC to the given position. The avatar will not land unless the OS_NPC_LAND_AT_TARGET option is also given.
OS_NPC_NO_FLY - Do not fly to the target. The NPC will attempt to walk to the location. If it's up in the air then the NPC will keep bouncing hopeless until another move target is given or the move is stopped.
OS_NPC_LAND_AT_TARGET - If given and the NPC is flying, then it will land when it reaches the target. If OS_NPC_NO_FLY is given then this option has no effect.
OS_NPC_FLY and OS_NPC_NO_FLY are options that cannot be combined - the NPC will end up doing one or the other. If you want the NPC to fly and land at the target, then OS_NPC_LAND_AT_TARGET must be combined with OS_NPC_FLY.
OS_NPC_RUNNING - make the NPC run to the given position.

### osNpcPlayAnimation

- `osNpcPlayAnimation(key npc, string animation)`

Plays animation on the NPC identified by their key.

### osNpcRemove

- `osNpcRemove(key npc)`

*Removes the NPC specified by key npc.

### osNpcSay

- `osNpcSay(key npc, integer channel, string message)`
- `osNpcSay(key npc, string message)`

npc says message on the given channel (channel is 0 in the second form)

### osNpcSayTo

- `osNpcSayTo(key npc, key target, integer channel, string message)`

npc says message on the given channel to the specified target

### osNpcSetProfileAbout

- `osNpcSetProfileAbout(key npc, string about)`

Set about in created NPC's profile.

### osNpcSetProfileImage

- `osNpcSetProfileImage(key npc, string image)`

Set image in created NPC's profile.
One can use UUID of the texture or name of texture included in prim's inventory.

### osNpcSetRot

- `osNpcSetRot(key npc, rotation rot)`

Set the rotation of the avatar. Only setting the rotation in the Z plane in Euler rotation will have any meaningful effect (turning the avatar to point in one direction or another). Setting X or Y Euler values will result in the avatar rotating in an undefined manner.

### osNpcShout

- `osNpcShout(key npc, integer channel, string message)`

npc shouts message on the given channel.

### osNpcSit

- `osNpcSit(key npc, key target, integer options)`

*Makes an NPC sit on an object. 
*Options - OS_NPC_SIT_NOW. Makes the npc instantly sit on the prim if possible. This is the only option available and is currently always on no matter what is actually specified in the options field.
** If the prim has a sit target then sit always succeeds no matter the distance between the NPC and the prim.
** If the prim has no sit target then
*** If the prim is within 10 meters of the NPC then the sit will always succeed.
*** At OpenSimulator 0.7.5 and later, if the prim is further than 10 meters away then nothing will happen.
*** Before OpenSimulator 0.7.5, if the prim is further than 10 meters away then the avatar will attempt to walk over to the prim but will not sit when it reaches it.

### osNpcStand

- `osNpcStand(key npc)`

*Makes a sitting NPC stand up.

### osNpcStopAnimation

- `osNpcStopAnimation(key npc, string animation)`

Stops an animation that is being played by the NPC identified by their key.

### osNpcStopMoveToTarget

- `osNpcStopMoveToTarget(key npc)`

Stop a current move to a target.

### osNpcTouch

- `osNpcTouch(key npcKey, key objectKey, integer linkNum)`

Only LINK_THIS and LINK_ROOT are valid for this function. Any other of the LINK_* constants will be ignored and no touch takes place.
1. If linkNum is LINK_THIS then the prim with the key objectKey will be touched.
2. If linkNum is LINK_ROOT or 0 then the root prim of the link set will be touched, even if the root prim key is not objectKey
3. For any other value of linkNum a search will be made through the linkset for a prim with that link number. If found that prim will be touched. If no prim is found for that link number the function fails silently and no touch takes place.
The touch is fired as if it came from an old client that does not support face touch detection or (probably) one of the text clients like Metabolt. Since there is no mouse the llDetectedTouch* functions will return the defaults (See the LSL Wiki for full details)
llDetectedTouchBinormal TOUCH_INVALID_VECTOR 
llDetectedTouchFace TOUCH_INVALID_FACE 
llDetectedTouchNormal TOUCH_INVALID_VECTOR 
llDetectedTouchPos TOUCH_INVALID_VECTOR 
llDetectedTouchST TOUCH_INVALID_TEXCOORD 
llDetectedTouchUV TOUCH_INVALID_TEXCOORD 
If the prim is not found or would not allow a normal client to touch it then this function fails silently.

### osNpcWhisper

- `osNpcWhisper(key npc, int channel, string message)`

npc whispers message on the given channel.

### osParcelJoin

- `osParcelJoin(vector pos1, vector pos2)`

Joins two adjacent parcels within the same region.

### osParcelSubdivide

- `osParcelSubdivide(vector pos1, vector pos2)`

Subdivides a parcel into two adjacent parcels within the same region.

### osParticleSystem

- `osParticleSystem(list rules)`

### osPlaySound

- `osPlaySound(integer linknum, string sound, float volume)`

Play the specified sound once at the specified volume.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the prim containing the script calling this function.

### osPlaySoundSlave

- `osPlaySoundSlave(integer linknum, string sound, float volume)`

Play the specified sound at the specified volume.
This sound will be set as a slave sound. The playing of a slave sound will be synchronized to the playing of the same sound declared in another prim as the master sound. 
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osPreloadSound

- `osPreloadSound(integer linknum, string sound)`

Preload the specified sound in viewers of nearby avatars.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osRegionNotice

- `osRegionNotice(string message)`
- `osRegionNotice(key agentID, string message)`

Sends a region notice to the entire current region.

### osRemoveLinkInventory

- `osRemoveLinkInventory(integer linkNumber, string name)`

Remove an item from a child prim inventory.

### osResetAllScripts

- `osResetAllScripts(integer AllLinkSet)`

Resets all the scripts on the same prim if AllLinkSet is FALSE( or 0) or on same linkset if AllLinkSet is TRUE ( or 1 )
This function can be heavy, and can have negative side effects due to the asynchronous nature of script engines.

### osRevokeScriptPermissions

- `osRevokeScriptPermissions(key revoked_key, string function)`

Dynamically allow/disallow ossl execution to owner/creator/group by function name.

### osSetContentType

- `osSetContentType(key id, string type)`

Sets an arbitrary content return type for an [http://wiki.secondlife.com/wiki/LlRequestURL llRequestUrl()].
The threat level was upgraded to Severe as of commit #2c2b887c8a on December 11, 2018.

### osSetEstateSunSettings

- `osSetEstateSunSettings(integer sunFixed, float sunHour)`

This function does nothing on 0.9.2. This function allowed for an estate owner or manager to change the sun settings for the entire estate.

### osSetHealth

- `osSetHealth(key avatar, float health)`

Sets an avatars health by key to the specified float value.

### osSetInertia

- `osSetInertia(float mass, vector centerOfMass, vector principalInertiaScaled, rotation InertiaRot)`

Allows creators to set the major physics dynamic proprieties, replacing the values estimated from the linkset parts. Call osClearInertia to undo
Caution ! Only supported by ubOde for now
===== Arguments: =====
* Mass total mass of link set
* centerOfMass location of center of mass relative to root prim in local frame
* principalInertiaScaled moment of inertia relative to principal axis and center of mass,Ixx, Iyy, Izz divided by mass so it can be changed independently
* InertiaRot rotation of the inertia, relative to local axis

### osSetInertiaAsBox

- `osSetInertiaAsBox(float mass, vector boxSize, vector centerOfMass, rotation rot)`

Allows creators to set the link set total mass, center of mass and moment of inertia. Moment of inertia will be the one of a box of size boxSize, placed at the center of mass and rotated by rot in the root prim local frame. Call osClearInertia to undo.
Caution ! Only supported by ubOde for now
===== Arguments: =====
* Mass new total mass of link set
* centerOfMass new location of center of mass relative to root prim in local frame
* boxSize size of the box used to calculate the new inertia
* rot the rotation of that box in local frame

### osSetInertiaAsCylinder

- `osSetInertiaAsCylinder(float mass,  float radius, float length, vector centerOfMass, rotation rot)`

Allows creators to set the link set total mass, center of mass and moment of inertia. Moment of inertia will be the one of a cylinder of radius and length, placed at the center of mass and rotated by rot in the root prim local frame. Call osClearInertia to undo.
Caution ! Only supported by ubOde for now
===== Arguments: =====
* Mass new total mass of link set
* centerOfMass new location of center of mass relative to root prim in local frame
* radius radius of a cylinder used to calculate the new inertia
* length length of a cylinder used to calculate the new inertia
* rot rotation of the cylinder in the root prim local frame.

### osSetInertiaAsSphere

- `osSetInertiaAsSphere(float mass,  float radius, vector centerOfMass)`

Allows creators to set the link set total mass, center of mass and moment of inertia. Moment of inertia will be the one of a sphere of radius radius, placed at the center of mass. Call osClearInertia to undo. 
Caution ! Only supported by ubOde for now
===== Arguments: =====
* Mass new total mass of link set
* centerOfMass new location of center of mass relative to root prim in local frame
* radius radius of a sphere used to calculate the new inertia

### osSetLinkSitActiveRange

- `osSetLinkSitActiveRange(integer linkNumber, float range)`

sets a limit on how far a avatar can be to have a sit request accepted, or disable sits
* linkNumber is link number of the prim to change or one of LINK_SET,LINK_ROOT, LINK_ALL_OTHERS,LINK_ALL_CHILDREN or LINK_THIS
* range > 0: if a avatar if far from the prim by more than that value, a sit request is silent ignored
* range == 0: disables this limit. Region default is used. Current that is unlimited if a sit target is set or physics can sit the avatar, otherwise 10m
* range < 0: sits are disabled. Requests are silently ignored
this value is stored on the prim, even if the script is removed

### osSetLinkStandTarget

- `osSetLinkStandTarget(integer linkNumber, vector feetTarget)`

Sets a position, relative to prim local frame, where to place the feet of a standing avatar. The final position may not be exactly that.
Setting it to disables it, default stand offset and login are used.
This vector is stored on the prim, even if the script is removed
* linkNumber: the link number of the prim, LINK_THIS or LINK_ROOT
if link number is invalid it will silent fail

### osSetOwnerSpeed

- `osSetOwnerSpeed(float SpeedModifier)`

Implemented september 28, 2018 by Bill Blight in GIT# [http://opensimulator.org/viewgit/?a=commit&p=opensim&h=6d9de17d77d20e078b0e7c7546ac3ec047d334e8 6d9de1] & [http://opensimulator.org/viewgit/?a=commit&p=opensim&h=8812684355de043d7630e327e6180fda4e5271b9 881268] and MANTIS# [http://opensimulator.org/mantis/view.php?id=8383 8383]
This allows for users to speed themselves up. It multiplies the running, walking, rotating and flying of the avatar.
The default value for SpeedModifier is 1.0 and the maximum value is 4.0.
To be precise, it affects physical velocity. If you specify too large or too small number for SpeedModifier, the target will be unmovable, showing the following message in the region console:
:[PHYSICS]: Got a NaN velocity from Scene in a Character

### osSetParcelDetails

- `osSetParcelDetails(vector pos, list rules)`

This function is the counterpart to [http://wiki.secondlife.com/wiki/LlGetParcelDetails llGetParcelDetails]. Currently PARCEL_DETAILS_NAME, PARCEL_DETAILS_DESC, PARCEL_DETAILS_OWNER, PARCEL_DETAILS_GROUP, PARCEL_DETAILS_CLAIMDATE are implemented. Note that the threat levels for PARCEL_DETAILS_NAME and PARCEL_DETAILS_DESC are "High", and those for PARCEL_DETAILS_OWNER, PARCEL_DETAILS_GROUP and PARCEL_DETAILS_CLAIMDATE are "VeryHigh".

### osSetParcelMediaURL

- `osSetParcelMediaURL(string url)`

Sets the Media URL for the parcel the scripted object is in.

### osSetParcelMusicURL

- `osSetParcelMusicURL(string url)`

Sets the Music URL for the parcel the scripted object is in.

### osSetParcelSIPAddress

- `osSetParcelSIPAddress(string SIPAddress)`

### osSetPrimFloatOnWater

- `osSetPrimFloatOnWater(integer float)`

This function does nothing useful

### osSetPrimitiveParams

- `osSetPrimitiveParams(key prim, list rules)`

* Sets the parameters for the prim specified by prim_uuid according to rules.
* This function has the same behave as llSetPrimitiveParams except you can specify target prim anywhere in the scene.
* For general information about rules, see [http://wiki.secondlife.com/wiki/LlSetPrimitiveParams llSetPrimitiveParams in SecondLife Wiki].
* If there is no prim with id prim_uuid in the scene, or the owner of the target prim is different from the owner of the scripted prim, it will fail without error.

### osSetProjectionParams

- `osSetProjectionParams(integer projection, key texture, float fov, float focus, float ambiance)`
- `osSetProjectionParams(integer linknumber, integer projection, key texture, float fov, float focus, float ambiance)`
- `osSetProjectionParams(key prim, integer projection, key texture, float fov, float focus, float ambiance)`

Sets a prim projector parameters, argument projection is TRUE(1) or FALSE(0). The prim can be the host prim on first variant, a prim on the linkset or a prim with giving UUID. 
In last case Threat level is high and controlled by Allow_osSetProjectionParams. The other cases have no threat level check. Note that you may need to set the prim light also.

### osSetRegionSunSettings

- `osSetRegionSunSettings(integer useEstateSun, integer sunFixed, float sunHour)`

This does nothing on 0.9.2. 
Sets the Sun parameters for the Region. 
The useEstateSun flag enables/disables synchronization with the Sun settings for the Estate.
sunFixed determines whether the Sun will remain fixed in place or proceed through its cycle.
sunHour determines the time of day the Sun will be set to.

### osSetRegionWaterHeight

- `osSetRegionWaterHeight(float height)`

Sets the water height for the current region.

### osSetSitActiveRange

- `osSetSitActiveRange(float range)`

sets a limit on how far a avatar can be to have a sit request accepted, or disable sits.
* range > 0: sit request is silently ignored if a avatar is further than range from the prim. 
* range == 0: disables this limit. Region default is used. Currently range is unlimited if a sit target is set or physics can sit the avatar, otherwise 10m.
* range < 0: sits are disabled. Requests are silently ignored.
The range value is stored in the prim, even if the script is removed

### osSetSpeed

- `osSetSpeed(key ID, float SpeedModifier)`

Implemented December 30, 2009 by Revolution in GIT# 87959464c9db8948bed89909913400bc2eb7524d - Rev 11850
This allows for users to speed themselves up. It multiplies the running, walking, rotating and flying of the avatar.
The default value for SpeedModifier is 1.0.
To be precise, it affects physical velocity. If you specify too large or too small number for SpeedModifier, the target will be unmovable, showing the following message in the region console:
:[PHYSICS]: Got a NaN velocity from Scene in a Character

### osSetStandTarget

- `osSetStandTarget(vector feetTarget)`

Sets a position, relative to prim local frame, where to place the feet of a avatar on stand. The final position may not be exactly that.
Setting it to disables it, default stand offset and login are used.
This vector is stored on the prim, even if the script is removed

### osSetSunParam

- `osSetSunParam(string param, float value)`

NOTE&nbsp;: This function does nothing on 0.9.2. It did depend on removed Sun module, This function replaced the deprecated osSunSetParam function.

### osSetTerrainTexture

- `osSetTerrainTexture(integer level, key texture)`

Obsolete use osSetTerrainTextures 
Set the terrain texture of the estate to the texture given as key for legacy viewers and map. The level can be 0, 1, 2 or 3. 
This will not set the textures seen by recent viewers, use instead osSetTerrainTextures

### osSetTerrainTextureHeight

- `osSetTerrainTextureHeight(integer corner, float low, float high)`

Set the terrain texture height for the estate. The corner values are: 0 (Southwest), 1 (Southeast), 2 (Northwest), 3 (Northeast). The values low and high are float values for the altitude measured in meters.

### osSetTerrainTextures

- `osSetTerrainTextures(list textureKeys, integer types)`

Opensimulator regions store two sets of texture or material keys:
* a set of texture keys for legacy viewers and map
* a set of texture or pbr material keys for new viewers. 
so this function allows to change those keys depending on the value of types :
* 0 applies keys for legacy viewers and map, keys must represent textures
* 1 applies keys for new viewers, keys represent either textures or PBR materials
* 2 applies keys to to both, Keys must represent textures
The list textureKeys must contain keys or names of 4 textures or 4 pbr materials. They must be of the same type due to viewers restrictions. 
This defines the textures or materials the viewer will use to draw the terrain texture 
They are ordered from low to high terrain height level, as on viewers World -> Region Details -> Terrain menu tab. 
If an entry is a name, then the material or texture must be present on the prim inventory. 
If an entry is an empty string, then that level is unchanged. 
Uses same threat level as osSetTerrainTexture in ossl_enable.ini

### osSetWindParam

- `osSetWindParam(string plugin, string param, float value)`

Sets value of param property for plugin module.
Available parameters:
{border="1" cellspacing="0" width="100%"
!pluginparamdescriptiondefaultOpenSim.inisetting
-
SimpleRandomWindstrengthwind strength1.0fstrength
-
rowspan="5"ConfigurableWindavgStrengthaverage wind strength in m/s5.0favg_strength
-
avgDirectionaverage wind direction in degrees0.0favg_direction
-
varStrengthallowable variance in wind strength in m/s5.0fvar_strength
-
varDirectionallowable variance in wind direction in +/- degrees30.0fvar_direction
-
rateChangerate of change in seconds1.0frate_change
}

### osStopSound

- `osStopSound(integer linknum)`

Stop the sound playing in the specified prim or prims of a linkset

### osTeleportAgent

- `osTeleportAgent(key agent, string regionName, vector position, vector lookat)`
- `osTeleportAgent(key agent, integer regionX, integer regionY, vector position, vector lookat)`
- `osTeleportAgent(key agent, vector position, vector lookat)`

Teleports an agent to the specified location 
* position is the location relative to destination region reference corner 
* lookAt is the direction the avatar should look. Z value is ignored. For example to face north use 
The first variant is able to teleport to any addressable region, including hypergrid destinations. 
The second variant teleports to a region in the local grid; the region coordinates are specified as region cells (not as global coordinates based on meters). 
The third variant teleports within the current region. Since version 0.9.2.0 it can also teleport to a nearby region if position does point to one
For osTeleportAgent() to work, the owner of the prim containing the script must be the same as the parcel that the avatar is currently on. 
If this isn't the case then the function fails silently.
See also osTeleportOwner, and if you receive an error see how to enable OS functions.

### osTeleportOwner

- `osTeleportOwner(string regionName, vector position, vector lookat)`
- `osTeleportOwner(integer regionX, integer regionY, vector position, vector lookat)`
- `osTeleportOwner(vector position, vector lookat)`

Teleports the owner of the object containing the script to the specified location. 
The first variant is able to teleport to any addressable region, including hypergrid destinations. 
The second variant teleports to a region in the local grid; the region coordinates are specified as region cells (not as global coordinates based on meters). 
The third variant teleports within the current region.
These functions have been added to OpenSimulator with commit r/14355 on November 16, 2010.
See also osTeleportAgent.

### osTerrainFlush

- `osTerrainFlush();`

Function updates terrain changes to OpenSimulator database. This should be called after all the terrain-changes have been done to update Terrain Data. 
Used in conjunction with OsSetTerrainHeight

### osTriggerSound

- `osTriggerSound(integer linknum, string sound, float volume)`

Start playing the specified sound in the viewers of nearby avatars once at the specified volume.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim.

### osTriggerSoundLimited

- `osTriggerSoundLimited(integer linknum, string sound, float volume, vector north_east_corner, vector south_west_corner)`

Start a one time play of the specified sound once at the specified volume in the viewers of avatars located within the box defined by the two vectors.
The sound parameter can be the UUID of a sound or the name of a sound that is in the inventory of the target prim. 
The two vectors are locations in region coordinates.

### osVolumeDetect

- `osVolumeDetect(integer detect)`

If script is on root prim, it is like llVolumeDetect(). On child prims, it will turn just that prim a detector.

