# LSL Constants

Source: MediaWiki export

---

### ACTIVE

* `integer ACTIVE = 0x2`

If it is contained in the result of llDetectedType(), it means it is physical tasks. (Physical objects & agents) 
If it is used as an filter of llSensor() or llSensorRepeat(), it will search for physical objects that are moving or objects containing an active script. Thus, it is using SL server resources now.

### AGENT

* `integer AGENT = 0x1`

If it is contained in the result of llDetectedType, it means it is avatar. If it is used as an filter of llSensor or llSensorRepeat, it will search for avatars by legacy name. Use of this constant in this context is not recommended as is more informative.

### AGENT_ALWAYS_RUN

* `integer AGENT_ALWAYS_RUN = 0x1000`

Used with llGetAgentInfo to determine if the queried avatar has 'always running' set.

### AGENT_ATTACHMENTS

* `integer AGENT_ATTACHMENTS = 0x0002`

### AGENT_AUTOMATED

* `integer AGENT_AUTOMATED = 0x4000`

Identifies an avatar as having been registered with Linden Lab as an automated/scripted agent, i.e. a 'bot.
Registration is (currently) done via the user's control panel on the [https://secondlife.com/my/account/sisa.php Scripted Agent Status] tab.
'Bots are not illegal in Second Life per se, but, according to the new scripted agent privacy policy, failing to register a 'bot as such is indeed forbidden.
Also note that from the perspective of the grid, it matters not how the 'bot is implemented; do not assume any technology behind it, just because an avatar has been flagged as an 'automated agent'. The flag essentially reflects the user's (voluntary) self-identification as a 'bot, without the requirement of giving any explanation, and there are a handful of different ways to "automate" an agent.
Linden Lab, at their discretion, and based on abuse reports or direct observation, may also flag an avatar as being an automated agent, which will set the AGENT_AUTOMATED bit as well. False positives can happen; feel free to file a ticket with Linden Lab's support if your avatar was erroneously flagged as an automated agent and you cannot change it from the SL control panel.
|pa
|pb

### AGENT_AUTOPILOT

* `integer AGENT_AUTOPILOT = 0x2000`

This value is set when the user selects "Go Here" on the ground, or uses the optional Double-Click Auto-Pilot feature.
Under Viewer 2.0 and later, it is also set when:
* the user selects "Sit Here" on the ground.
* an object is selected or edited, and that selection can trigger a control (CONTROL_ROT_RIGHT and CONTROL_ROT_LEFT can be activated when selecting an object near the far right or left edge of the screen).
|pa
|pb

### AGENT_AWAY

* `integer AGENT_AWAY = 0x0040`

Indicates that the agent has either toggled away or has been inactive for too long.

### AGENT_BUSY

* `integer AGENT_BUSY = 0x0800`

### AGENT_BY_LEGACY_NAME

* `integer AGENT_BY_LEGACY_NAME = 0x1`

If it is contained in the result of llDetectedType, it means it is avatar. If it is used as an filter of llSensor or llSensorRepeat, it will search for avatars by legacy name.

### AGENT_BY_USERNAME

* `integer AGENT_BY_USERNAME = 0x10`

See Avatar Names

### AGENT_CROUCHING

* `integer AGENT_CROUCHING = 0x0400`

### AGENT_FLOATING_VIA_SCRIPTED_ATTACHMENT

* `integer AGENT_FLOATING_VIA_SCRIPTED_ATTACHMENT = 0x8000`

Indicates that the agent is floating because of a scripted attachment using either llSetHoverHeight or llGroundRepel.

### AGENT_FLYING

* `integer AGENT_FLYING = 0x0001`

Used with llGetAgentInfo to determine if the queried avatar is flying.

### AGENT_IN_AIR

* `integer AGENT_IN_AIR = 0x0100`

### AGENT_LIST_PARCEL

* `integer AGENT_LIST_PARCEL = 1`

Agents on the same parcel where the script is running.

### AGENT_LIST_PARCEL_OWNER

* `integer AGENT_LIST_PARCEL_OWNER = 2`

Agents on any parcel in the region where the parcel owner is the same as the owner of the parcel under the scripted object.

### AGENT_LIST_REGION

* `integer AGENT_LIST_REGION = 4`

Returns any/all agents in the region.

### AGENT_MOUSELOOK

* `integer AGENT_MOUSELOOK = 0x0008`

### AGENT_ON_OBJECT

* `integer AGENT_ON_OBJECT = 0x0020`

### AGENT_SCRIPTED

* `integer AGENT_SCRIPTED = 0x0004`

Carrying scripted objects

### AGENT_SITTING

* `integer AGENT_SITTING = 0x0010`

### AGENT_TYPING

* `integer AGENT_TYPING = 0x0200`

### AGENT_WALKING

* `integer AGENT_WALKING = 0x0080`

Used with llGetAgentInfo to determine if the queried avatar is walking.

### ALL_SIDES

* `integer ALL_SIDES = -1`

Selects all sides of an object in an applicable function.

### ANIM_ON

* `integer ANIM_ON = 0x01`

Enables a texture animation.
|examples

### ATTACH_AVATAR_CENTER

* `integer ATTACH_AVATAR_CENTER = 40
|desc
|examples
|functions
|events`

### ATTACH_BACK

* `integer ATTACH_BACK = 9
|desc
|examples
|functions
|events`

### ATTACH_BELLY

* `integer ATTACH_BELLY = 28
|desc
|examples
|functions
|events`

### ATTACH_CHEST

* `integer ATTACH_CHEST = 1
|desc
|examples
|functions
|events`

### ATTACH_CHIN

* `integer ATTACH_CHIN = 12`

This constant is returned when the attachment point is the chin. 
|examples
|functions
|events

### ATTACH_FACE_JAW

* `integer ATTACH_FACE_JAW = 47
|desc
|examples
|functions
|events`

### ATTACH_FACE_LEAR

* `integer ATTACH_FACE_LEAR = 48
|desc
|examples
|functions
|events`

### ATTACH_FACE_LEYE

* `integer ATTACH_FACE_LEYE = 50
|desc
|examples
|functions
|events`

### ATTACH_FACE_REAR

* `integer ATTACH_FACE_REAR = 49
|desc
|examples
|functions
|events`

### ATTACH_FACE_REYE

* `integer ATTACH_FACE_REYE = 51
|desc
|examples
|functions
|events`

### ATTACH_FACE_TONGUE

* `integer ATTACH_FACE_TONGUE = 52
|desc
|examples
|functions
|events`

### ATTACH_GROIN

* `integer ATTACH_GROIN = 53
|desc
|examples
|functions
|events`

### ATTACH_HEAD

* `integer ATTACH_HEAD = 2
|desc
|examples
|functions
|events`

### ATTACH_HIND_LFOOT

* `integer ATTACH_HIND_LFOOT = 54
|desc
|examples
|functions
|events`

### ATTACH_HIND_RFOOT

* `integer ATTACH_HIND_RFOOT = 55
|desc
|examples
|functions
|events`

### ATTACH_HUD_BOTTOM

* `integer ATTACH_HUD_BOTTOM = 37
|desc
|examples
|functions
|events`

### ATTACH_HUD_BOTTOM_LEFT

* `integer ATTACH_HUD_BOTTOM_LEFT = 36
|desc
|examples
|functions
|events`

### ATTACH_HUD_BOTTOM_RIGHT

* `integer ATTACH_HUD_BOTTOM_RIGHT = 38
|desc
|examples
|functions
|events`

### ATTACH_HUD_CENTER_1

* `integer ATTACH_HUD_CENTER_1 = 35
|desc
|examples
|functions
|events`

### ATTACH_HUD_CENTER_2

* `integer ATTACH_HUD_CENTER_2 = 31
|desc
|examples
|functions
|events`

### ATTACH_HUD_TOP_CENTER

* `integer ATTACH_HUD_TOP_CENTER = 33
|desc
|examples
|functions
|events`

### ATTACH_HUD_TOP_LEFT

* `integer ATTACH_HUD_TOP_LEFT = 34
|desc
|examples
|functions
|events`

### ATTACH_HUD_TOP_RIGHT

* `integer ATTACH_HUD_TOP_RIGHT = 32
|desc
|examples
|functions
|events`

### ATTACH_LEAR

* `integer ATTACH_LEAR = 13`

Left ear
|examples
|functions
|events

### ATTACH_LEFT_PEC

* `integer ATTACH_LEFT_PEC = 29
|desc
|examples
|functions
|events`

### ATTACH_LEYE

* `integer ATTACH_LEYE = 15
|desc
|examples
|functions
|events`

### ATTACH_LFOOT

* `integer ATTACH_LFOOT = 7
|desc
|examples
|functions
|events`

### ATTACH_LHAND

* `integer ATTACH_LHAND = 5
|desc
|examples
|constants
|functions
|events`

### ATTACH_LHAND_RING1

* `integer ATTACH_LHAND_RING1 = 41
|desc
|examples
|functions
|events`

### ATTACH_LHIP

* `integer ATTACH_LHIP = 25`

Left Hip
|examples
|functions
|events

### ATTACH_LLARM

* `integer ATTACH_LLARM = 21`

Lower Left Arm
|examples
|functions
|events

### ATTACH_LLLEG

* `integer ATTACH_LLLEG = 27`

Left lower leg
|examples
|functions
|events

### ATTACH_LSHOULDER

* `integer ATTACH_LSHOULDER = 3
|desc
|examples
|functions
|events`

### ATTACH_LUARM

* `integer ATTACH_LUARM = 20`

Left Upper Arm
|examples
|functions
|events

### ATTACH_LULEG

* `integer ATTACH_LULEG = 26`

Left Upper Leg
|examples
|functions
|events

### ATTACH_LWING

* `integer ATTACH_LWING = 45
|desc
|examples
|functions
|events`

### ATTACH_MOUTH

* `integer ATTACH_MOUTH = 11
|desc
|examples
|functions
|events`

### ATTACH_NECK

* `integer ATTACH_NECK = 39
|desc
|examples
|functions
|events`

### ATTACH_NOSE

* `integer ATTACH_NOSE = 17
|desc
|examples
|functions
|events`

### ATTACH_PELVIS

* `integer ATTACH_PELVIS = 10
|desc
|examples
|functions
|events`

### ATTACH_REAR

* `integer ATTACH_REAR = 14`

Right ear
|examples
|functions
|events

### ATTACH_REYE

* `integer ATTACH_REYE = 16
|desc
|examples
|functions
|events`

### ATTACH_RFOOT

* `integer ATTACH_RFOOT = 8
|desc
|examples
|functions
|events`

### ATTACH_RHAND

* `integer ATTACH_RHAND = 6`

Indicates the right hand attach point, which just so happens to be the default attach point.
|examples
|constants
|functions
|events

### ATTACH_RHAND_RING1

* `integer ATTACH_RHAND_RING1 = 42
|desc
|examples
|functions
|events`

### ATTACH_RHIP

* `integer ATTACH_RHIP = 22
|desc
|examples
|functions
|events`

### ATTACH_RIGHT_PEC

* `integer ATTACH_RIGHT_PEC = 30
|desc
|examples
|functions
|events`

### ATTACH_RLARM

* `integer ATTACH_RLARM = 19`

Right lower arm
|examples
|functions
|events

### ATTACH_RLLEG

* `integer ATTACH_RLLEG = 24
|desc
|examples
|functions
|events`

### ATTACH_RSHOULDER

* `integer ATTACH_RSHOULDER = 4
|desc
|examples
|functions
|events`

### ATTACH_RUARM

* `integer ATTACH_RUARM = 18`

Right upper arm
|examples
|functions
|events

### ATTACH_RULEG

* `integer ATTACH_RULEG = 23`

Right upper leg
|examples
|functions
|events

### ATTACH_RWING

* `integer ATTACH_RWING = 46
|desc
|examples
|functions
|events`

### ATTACH_TAIL_BASE

* `integer ATTACH_TAIL_BASE = 43
|desc
|examples
|functions
|events`

### ATTACH_TAIL_TIP

* `integer ATTACH_TAIL_TIP = 44
|desc
|examples
|functions
|events`

### CAMERA_ACTIVE

* `integer CAMERA_ACTIVE = 12
|desc
|examples`

### CAMERA_BEHINDNESS_ANGLE

* `integer CAMERA_BEHINDNESS_ANGLE = 8
|desc
|examples`

### CAMERA_BEHINDNESS_LAG

* `integer CAMERA_BEHINDNESS_LAG = 9
|desc
|examples`

### CAMERA_DISTANCE

* `integer CAMERA_DISTANCE = 7
|desc
|examples`

### CAMERA_FOCUS

* `integer CAMERA_FOCUS = 17
|desc
|examples`

### CAMERA_FOCUS_LAG

* `integer CAMERA_FOCUS_LAG = 6
|desc
|examples`

### CAMERA_FOCUS_LOCKED

* `integer CAMERA_FOCUS_LOCKED = 22
|desc
|examples`

### CAMERA_FOCUS_OFFSET

* `integer CAMERA_FOCUS_OFFSET = 1
|desc
|examples`

### CAMERA_FOCUS_THRESHOLD

* `integer CAMERA_FOCUS_THRESHOLD = 11
|desc
|examples`

### CAMERA_PITCH

* `integer CAMERA_PITCH = 0
|desc
|examples`

### CAMERA_POSITION

* `integer CAMERA_POSITION = 13
|desc
|examples`

### CAMERA_POSITION_LAG

* `integer CAMERA_POSITION_LAG = 5
|desc
|examples`

### CAMERA_POSITION_LOCKED

* `integer CAMERA_POSITION_LOCKED = 21
|desc
|examples`

### CAMERA_POSITION_THRESHOLD

* `integer CAMERA_POSITION_THRESHOLD = 10
|desc
|examples`

### CHANGED_ALLOWED_DROP

* `integer CHANGED_ALLOWED_DROP = 0x40`

A user other then the owner (or the owner if the object is no-mod) has added inventory to the prim. This is only possible if enabled with llAllowInventoryDrop.

### CHANGED_COLOR

* `integer CHANGED_COLOR = 0x2`

Prim Blinn-Phong color or alpha parameters have changed

### CHANGED_INVENTORY

* `integer CHANGED_INVENTORY = 0x1`

Prim inventory has changed by someone who has modification rights to a prim.
Inventory changes that cause this event are:
*Inventory item is added or deleted
*Inventory item name is changed
*Inventory item permissions are changed
*A different script in inventory is recompiled
*A notecard in inventory is saved
This event does not occur when:
*A no-copy inventory item is moved to user inventory
*A script in inventory is reset
*A user without modification rights drops an object into a prim's inventory due to llAllowInventoryDrop.
**In this situation the CHANGED_ALLOWED_DROP flag is set instead of CHANGED_INVENTORY.
*An object that was rezzed from inventory is saved back to object contents
Important : This event is triggered in the root prim by a change in any child prim, unless the child prim has a handler for it. It is not triggered in any other linked prim.

### CHANGED_LINK

* `integer CHANGED_LINK = 0x20`

The number of prims making up the object or avatars seated on the object have changed. This event also occurs when duplicating a linked object or when a prim in an object changes type or shape. This event does not occur when: an object is attached or detached, in an attachment when the avatar sits or unsits, in an attachment when another object is attached or detached, or when a single prim is duplicated.

### CHANGED_MEDIA

* `integer CHANGED_MEDIA = 0x800`

on the prim has changed.
|notes

### CHANGED_OWNER

* `integer CHANGED_OWNER = 0x80`

The object has changed owners. This event occurs in the original object when a user takes it or takes a copy of it or when the owner deeds it to a group. The event occurs in the new object when it is first rezzed. 
Counter-intuitively, this event also occurs in the original object when it is purchased or a copy of it is purchased (although the original object does not in fact change owner). The event does not occur in the original object when its contents are purchased.

### CHANGED_REGION

* `integer CHANGED_REGION = 0x100`

The object has changed region by crossing a region boundary (or by teleporting, if attached). This event only occurs in the root prim of a linkset. This event does not occur in child prims of objects when they cross a region boundary.

### CHANGED_REGION_START

* `integer CHANGED_REGION_START = 0x400`

The region containing the object has just come online.

### CHANGED_RENDER_MATERIAL

* `integer CHANGED_RENDER_MATERIAL = 0x1000`

Prim material ID or material overrides have changed on one or more faces.

### CHANGED_SCALE

* `integer CHANGED_SCALE = 0x8`

The prim scale of at least one prim in the linked object has changed. Only the root prim will receive this event.

### CHANGED_SHAPE

* `integer CHANGED_SHAPE = 0x4`

PRIM_TYPE (box, prism, torus, taper, twist, cut &hellip;) has changed.

### CHANGED_TELEPORT

* `integer CHANGED_TELEPORT = 0x200`

The avatar this object is attached to has teleported. This event only occurs in the root prim of an attachment when the user has teleported. This event does not occur in child prims of attachments, nor does it occur due to a "sit teleport". If the user teleports into a parcel where their scripts are disabled then the CHANGED_TELEPORT event is queued and occurs after the user moves to a script-enabled parcel.

### CHANGED_TEXTURE

* `integer CHANGED_TEXTURE = 0x10`

Prim texture parameters (shine/bump setting, repeats, flip, rotation, or offset) have changed. 
Transparency or color changes trigger a CHANGED_COLOR event not a CHANGED_TEXTURE event.

### CHARACTER_ACCOUNT_FOR_SKIPPED_FRAMES

* `integer CHARACTER_ACCOUNT_FOR_SKIPPED_FRAMES = |desc
|examples`

### CHARACTER_AVOIDANCE_MODE

* `integer CHARACTER_AVOIDANCE_MODE = 5`

Used in the functions of pathfinding . Is combined with a mask bit flags. The default is AVOID_CHARACTERS with AVOID_DYNAMIC_OBSTACLES.
Allows you to specify that a character should not try to avoid other characters, should not try to avoid dynamic obstacles (relatively fast moving objects and avatars), or both.
|examples

### CHARACTER_DESIRED_SPEED

* `integer CHARACTER_DESIRED_SPEED = 1`

Constant used to indicate that the following argument is the desired speed for a Pathfinding character.
|examples

### CHARACTER_DESIRED_TURN_SPEED

* `integer CHARACTER_DESIRED_TURN_SPEED = 12`

Used in the functions of pathfinding . Is combined with a float. The default 6 meters/second
Specifies the character's maximum speed while turning 
|examples

### CHARACTER_LENGTH

* `integer CHARACTER_LENGTH = 3`

Constant used to indicate that the following argument is the length of the capsule for a Pathfinding character. This is used to help denote the size of the character.
|examples

### CHARACTER_MAX_ACCEL

* `integer CHARACTER_MAX_ACCEL = 8`

Used in the functions of pathfinding . Is combined with a float. The default 20 meters/s(-2).
Specifies the character's maximum acceleration rate. 
|examples

### CHARACTER_MAX_DECEL

* `integer CHARACTER_MAX_DECEL = 9`

Used in the functions of pathfinding . Is combined with a float. The default 30 meters/s(-2).
Specifies the character's maximum deceleration rate. 
|examples

### CHARACTER_MAX_SPEED

* `integer CHARACTER_MAX_SPEED = 13`

Used in the functions of pathfinding . Is combined with a float. The default is 20 meters/second
Specifies the character's maximum speed .
Can t be inferior to 0.2 meters/second and can't be superior to 50 meters/second
|examples

### CHARACTER_MAX_TURN_RADIUS

* `integer CHARACTER_MAX_TURN_RADIUS = 10`

Used in the functions of pathfinding . Is combined with a float. The default 1.25 meter.
Specifies the character's radius when the characters turns at the speed CHARACTER_DESIRED_TURN_SPEED
|examples

### CHARACTER_ORIENTATION

* `integer CHARACTER_ORIENTATION = 4`

Constant used to indicate that the following argument is the orientation of the capsule for a Pathfinding character. This is used to help denote how to interpret the size of a character.
|examples

### CHARACTER_RADIUS

* `integer CHARACTER_RADIUS = 2`

Constant used to indicate that the following argument is the radius of the capsule for a Pathfinding character. This is used to help denote the size of the character.
|examples

### CHARACTER_STAY_WITHIN_PARCEL

* `integer CHARACTER_STAY_WITHIN_PARCEL = 15`

Default setting is FALSE, leading to traditional pathfinding behavior. If a parcel allows scripts and objects and the character does not have the CHARACTER_STAY_WITHIN_PARCEL option enabled, it can freely cross the parcel boundary in both directions. Characters which have CHARACTER_STAY_WITHIN_PARCEL set to TRUE treat the parcel boundaries as one-way obstacles. Pathfinding wander, flee, evade, and pursue behaviors will only choose goal points within their starting parcel. If a character somehow manages to escape its original parcel (e.g. it was 'pushed' out), it will be able to return to the original parcel, but will be unable to leave the original parcel afterwards. 
|examples

### CHARACTER_TYPE

* `integer CHARACTER_TYPE = 6`

Used in combination with one of the character type flags. The default is CHARACTER_TYPE_NONE, other options are CHARACTER_TYPE_A, CHARACTER_TYPE_B, CHARACTER_TYPE_C and CHARACTER_TYPE_D. Note that the character type is not used to describe the behavior of the Pathfinding object but is used to describe the kind of surface and terrain that it prefers to travel. For example, a cow designed for a field should use character type B, but sheep designed to be herded along a road should use character type C.
|examples

### CHARACTER_TYPE_A

* `integer CHARACTER_TYPE_A = 0`

Used for character types that you prefer move in a way consistent with humanoids.
|examples

### CHARACTER_TYPE_B

* `integer CHARACTER_TYPE_B = 1`

Used for character types that you prefer move in a way consistent with wild animals or off road vehicles.
|examples

### CHARACTER_TYPE_C

* `integer CHARACTER_TYPE_C = 2`

Used for mechanical character types or road going vehicles.
|examples

### CHARACTER_TYPE_D

* `integer CHARACTER_TYPE_D = 3`

Used for character types that are not consistent with the A, B, or C type.
|examples

### CHARACTER_TYPE_NONE

* `integer CHARACTER_TYPE_NONE = 4`

Used to set no specific character type.
|examples

### CLICK_ACTION_BUY

* `integer CLICK_ACTION_BUY = 2
|desc
|examples`

### CLICK_ACTION_DISABLED

* `integer CLICK_ACTION_DISABLED = 8
|desc
|examples`

### CLICK_ACTION_IGNORE

* `integer CLICK_ACTION_IGNORE = 9
|desc
|examples`

### CLICK_ACTION_NONE

* `integer CLICK_ACTION_NONE = 0
|desc
|examples`

### CLICK_ACTION_OPEN

* `integer CLICK_ACTION_OPEN = 4
|desc
|examples`

### CLICK_ACTION_OPEN_MEDIA

* `integer CLICK_ACTION_OPEN_MEDIA = 6
|desc
|examples`

### CLICK_ACTION_PAY

* `integer CLICK_ACTION_PAY = 3
|desc
|examples`

### CLICK_ACTION_PLAY

* `integer CLICK_ACTION_PLAY = 5
|desc
|examples`

### CLICK_ACTION_SIT

* `integer CLICK_ACTION_SIT = 1
|desc
|examples`

### CLICK_ACTION_TOUCH

* `integer CLICK_ACTION_TOUCH = 0
|desc
|examples`

### CLICK_ACTION_ZOOM

* `integer CLICK_ACTION_ZOOM = 7
|desc
|examples`

### CONTROL_BACK

* `integer CONTROL_BACK = 0x2`

### CONTROL_DOWN

* `integer CONTROL_DOWN = 0x20`

### CONTROL_FWD

* `integer CONTROL_FWD = 0x1`

### CONTROL_LBUTTON

* `integer CONTROL_LBUTTON = 0x10000000`

### CONTROL_LEFT

* `integer CONTROL_LEFT = 0x4`

### CONTROL_ML_LBUTTON

* `integer CONTROL_ML_LBUTTON = 0x40000000`

### CONTROL_RIGHT

* `integer CONTROL_RIGHT = 0x8`

### CONTROL_ROT_LEFT

* `integer CONTROL_ROT_LEFT = 0x100`

### CONTROL_ROT_RIGHT

* `integer CONTROL_ROT_RIGHT = 0x200`

### CONTROL_UP

* `integer CONTROL_UP = 0x10`

### DAMAGEABLE

* `integer DAMAGEABLE = 0x20`

If it is contained in the result of llDetectedType, it means what was detected is either an agent that can take damage, or is an object containing a script with either on_damage or final_damage events (able to process damage).
If it is used as a filter of llSensor or llSensorRepeat, it will search for agents or objects which match the same criteria mentioned above.

### DATA_BORN

* `integer DATA_BORN = 3`

Used with llRequestAgentData to return a string that contains the date the user joined SL, it is the format of "YYYY-MM-DD". It is based on Pacific Time, not UTC. 
|pa
|pb
|examples

### DATA_NAME

* `integer DATA_NAME = 2`

Used with llRequestAgentData to return a string containing the avatars legacy name.
* For legacy accounts (those with a first and last name). The format is "FirstName LastName".
* For modern accounts (those with only a first name). The format is "FirstName Resident".
|examples

### DATA_ONLINE

* `integer DATA_ONLINE = 1`

Used with llRequestAgentData to return a string that contains the integer boolean for if the user is online (or not). TRUE if online, FALSE if offline.

### DATA_PAYINFO

* `integer DATA_PAYINFO = 8`

Used with llRequestAgentData to return a string that contains the integer mask that can contain either of these two constants: PAYMENT_INFO_ON_FILE, PAYMENT_INFO_USED
It is important to know that it is possible to have PAYMENT_INFO_USED but currently not have PAYMENT_INFO_ON_FILE (payment info can be removed after being used).
|pa
|pb
|examples

### DATA_RATING

* `integer DATA_RATING = 4`

Used with llRequestAgentData to return the string "0, 0, 0, 0, 0, 0". 
The CSV list returned used to contain the positive and negative ratings the user has acquired before ratings were removed from SL.
|pa
|pb
|pc
|examples

### DATA_SIM_POS

* `integer DATA_SIM_POS = 5`

returns vector in global coordinates

### DATA_SIM_RATING

* `integer DATA_SIM_RATING = 7`

returns string simulator rating "PG", "MATURE", "ADULT" or "UNKNOWN"

### DATA_SIM_STATUS

* `integer DATA_SIM_STATUS = 6`

Returns one of these strings.
* "up": simulator currently up and running
* "down": simulator currently down
* "starting": simulator currently starting
* "stopping": simulator currently stopping
* "crashed": simulator has crashed
* "unknown": simulator status unknown or unknown simulator

### DEG_TO_RAD

* `float DEG_TO_RAD = 0.017453292519943295769236907684886f`

When multiplied by, converts a value in degrees to radians. Precise value is PI/180.
|examples
|events
|functions

### EOF

* `EOF`

EOF is a value returned by the dataserver event, as a result of a call to llGetNotecardLine, specifically when the requested line is past the end of the notecard. The value returned equals "\n\n\n", which is to say, three newline characters (0x0a).
Essentially, it is used to let you know when you have finished reading information (usually user configurable parameters) from a notecard, and are ready to move onto the next stage or state of the script.

### ERR_GENERIC

* `integer ERR_GENERIC = -1`

{ 
- 
! Function
! Indicates...
-
 llReturnObjectsByIDllReturnObjectsByOwner
 A nebulous and inexplicable error, nothing is known about it.
}
|notes
|examples

### ERR_MALFORMED_PARAMS

* `integer ERR_MALFORMED_PARAMS = -3`

Return Value for llReturnObject* functions. Indicates function Parameters are malformed.
|examples

### ERR_PARCEL_PERMISSIONS

* `integer ERR_PARCEL_PERMISSIONS = -2`

Return Value for llReturnObject* functions. Indicates Permission lacked to perform task on specified parcel. 
|examples

### ERR_RUNTIME_PERMISSIONS

* `integer ERR_RUNTIME_PERMISSIONS = -4`

Return Value for llReturnObject* functions. Indicates Script lacks the runtime permission to perform the requested task.
|examples

### ERR_THROTTLED

* `integer ERR_THROTTLED = -5`

Return Value for llReturnObject* functions. Indicates Task has been throttled. Try again later.
|examples

### ESTATE_ACCESS_ALLOWED_AGENT_ADD

* `integer ESTATE_ACCESS_ALLOWED_AGENT_ADD = 4`

Used in input parameters of llManageEstateAccess . Add an agent to this estate's Allowed Residents list
|examples
|constants

### ESTATE_ACCESS_ALLOWED_AGENT_REMOVE

* `integer ESTATE_ACCESS_ALLOWED_AGENT_REMOVE = 8`

Used in input parameters of llManageEstateAccess . Remove an agent to this estate's Allowed Residents list
|examples
|constants

### ESTATE_ACCESS_ALLOWED_GROUP_ADD

* `integer ESTATE_ACCESS_ALLOWED_GROUP_ADD = 16`

Used in input parameters of llManageEstateAccess .Add a group to this estate's Allowed groups list.
|examples
|constants

### ESTATE_ACCESS_ALLOWED_GROUP_REMOVE

* `integer ESTATE_ACCESS_ALLOWED_GROUP_REMOVE = 32`

Used in input parameters of llManageEstateAccess . Remove the group from this estate's Allowed groups list.
|examples
|constants

### ESTATE_ACCESS_BANNED_AGENT_ADD
|inject-1={{Issues/SCR-293}}

* `integer ESTATE_ACCESS_BANNED_AGENT_ADD
|inject-1={{Issues/SCR-293}} = 64`

Used in input parameters of llManageEstateAccess. Add the agent to this estate's Banned residents list.
|examples
|constants

### ESTATE_ACCESS_BANNED_AGENT_REMOVE

* `integer ESTATE_ACCESS_BANNED_AGENT_REMOVE = 128`

Used in input parameters of llManageEstateAccess . Remove the agent from this estate's Banned residents list.
|examples
|constants

### FALSE

* `integer FALSE = 0`

Constant used to define the FALSE value in conditional structures or variables/constants in general. Usually it's used because it is more readable, indicating a boolean value instead a integer value (0).

### FORCE_DIRECT_PATH

* `integer FORCE_DIRECT_PATH = 1`

### GAME_CONTROL_AXIS_LEFTX

* `integer GAME_CONTROL_AXIS_LEFTX = 0x0`

### GAME_CONTROL_AXIS_LEFTY

* `integer GAME_CONTROL_AXIS_LEFTY = 0x1`

### GAME_CONTROL_AXIS_RIGHTX

* `integer GAME_CONTROL_AXIS_RIGHTX = 0x2`

### GAME_CONTROL_AXIS_RIGHTY

* `integer GAME_CONTROL_AXIS_RIGHTY = 0x3`

### GAME_CONTROL_AXIS_TRIGGERLEFT

* `integer GAME_CONTROL_AXIS_TRIGGERLEFT = 0x4`

### GAME_CONTROL_AXIS_TRIGGERRIGHT

* `integer GAME_CONTROL_AXIS_TRIGGERRIGHT = 0x5`

### GAME_CONTROL_BUTTON_A

* `integer GAME_CONTROL_BUTTON_A = 0x1`

### GAME_CONTROL_BUTTON_B

* `integer GAME_CONTROL_BUTTON_B = 0x2`

### GAME_CONTROL_BUTTON_BACK

* `integer GAME_CONTROL_BUTTON_BACK = 0x10`

### GAME_CONTROL_BUTTON_DPAD_DOWN

* `integer GAME_CONTROL_BUTTON_DPAD_DOWN = 0x1000`

### GAME_CONTROL_BUTTON_DPAD_LEFT

* `integer GAME_CONTROL_BUTTON_DPAD_LEFT = 0x2000`

### GAME_CONTROL_BUTTON_DPAD_RIGHT

* `integer GAME_CONTROL_BUTTON_DPAD_RIGHT = 0x4000`

### GAME_CONTROL_BUTTON_DPAD_UP

* `integer GAME_CONTROL_BUTTON_DPAD_UP = 0x800`

### GAME_CONTROL_BUTTON_GUIDE

* `integer GAME_CONTROL_BUTTON_GUIDE = 0x20`

### GAME_CONTROL_BUTTON_LEFTSHOULDER

* `integer GAME_CONTROL_BUTTON_LEFTSHOULDER = 0x200`

### GAME_CONTROL_BUTTON_LEFTSTICK

* `integer GAME_CONTROL_BUTTON_LEFTSTICK = 0x80`

### GAME_CONTROL_BUTTON_MISC1

* `integer GAME_CONTROL_BUTTON_MISC1 = 0x8000`

### GAME_CONTROL_BUTTON_PADDLE1

* `integer GAME_CONTROL_BUTTON_PADDLE1 = 0x10000`

### GAME_CONTROL_BUTTON_PADDLE2

* `integer GAME_CONTROL_BUTTON_PADDLE2 = 0x20000`

### GAME_CONTROL_BUTTON_PADDLE3

* `integer GAME_CONTROL_BUTTON_PADDLE3 = 0x40000`

### GAME_CONTROL_BUTTON_PADDLE4

* `integer GAME_CONTROL_BUTTON_PADDLE4 = 0x80000`

### GAME_CONTROL_BUTTON_RIGHTSHOULDER

* `integer GAME_CONTROL_BUTTON_RIGHTSHOULDER = 0x400`

### GAME_CONTROL_BUTTON_RIGHTSTICK

* `integer GAME_CONTROL_BUTTON_RIGHTSTICK = 0x100`

### GAME_CONTROL_BUTTON_START

* `integer GAME_CONTROL_BUTTON_START = 0x40`

### GAME_CONTROL_BUTTON_TOUCHPAD

* `integer GAME_CONTROL_BUTTON_TOUCHPAD = 0x100000`

### GAME_CONTROL_BUTTON_X

* `integer GAME_CONTROL_BUTTON_X = 0x4`

### GAME_CONTROL_BUTTON_Y

* `integer GAME_CONTROL_BUTTON_Y = 0x8`

### HORIZONTAL

* `integer HORIZONTAL = 1`

Constant to indicate that the orientation of the capsule for a Pathfinding character is horizontal.
|examples

### HTTP_ACCEPT

* `integer HTTP_ACCEPT = 8
|desc
|examples`

### HTTP_BODY_MAXLENGTH

* `integer HTTP_BODY_MAXLENGTH = 2`

Used with llHTTPRequest to set the maximum size the script will accept* for an HTTP body. The largest value this can be set to depends upon the VM that is being used.
* See caveats
===Mono===
*Maximum: 16KiB
===LSO===
*Maximum: 4KiB
|examples

### HTTP_BODY_TRUNCATED

* `integer HTTP_BODY_TRUNCATED = 0`

Truncation point in bytes
|examples
|functions

### HTTP_CUSTOM_HEADER

* `integer HTTP_CUSTOM_HEADER = 5
|hvalue
|desc
|examples`

### HTTP_EXTENDED_ERROR

* `integer HTTP_EXTENDED_ERROR = 9
|desc
|examples`

### HTTP_METHOD

* `integer HTTP_METHOD = 0
|desc
|examples`

### HTTP_MIMETYPE

* `integer HTTP_MIMETYPE = 1
|desc
|examples`

### HTTP_PRAGMA_NO_CACHE

* `integer HTTP_PRAGMA_NO_CACHE = 6
|hvalue
|desc`

### HTTP_USER_AGENT

* `integer HTTP_USER_AGENT = 7
|desc
|examples`

### HTTP_VERBOSE_THROTTLE

* `integer HTTP_VERBOSE_THROTTLE = 4
|desc`

### HTTP_VERIFY_CERT

* `integer HTTP_VERIFY_CERT = 3`

### INVENTORY_ALL

* `integer INVENTORY_ALL = -1`

Used with Inventory functions and specifies ALL TYPES of inventory items will be retrieved by the function.
|examples

### INVENTORY_ANIMATION

* `integer INVENTORY_ANIMATION = 20`

Used with Inventory functions and specifies inventory items of ANIMATION type will be retrieved by the function.

### INVENTORY_BODYPART

* `integer INVENTORY_BODYPART = 13`

Used with Inventory functions and specifies inventory items of BODYPART type will be retrieved by the function.

### INVENTORY_CLOTHING

* `integer INVENTORY_CLOTHING = 5`

Used with Inventory functions and specifies inventory items of CLOTHING type will be retrieved by the function.

### INVENTORY_GESTURE

* `integer INVENTORY_GESTURE = 21`

Used with Inventory functions and specifies inventory items of GESTURE type will be retrieved by the function.

### INVENTORY_LANDMARK

* `integer INVENTORY_LANDMARK = 3`

Used with Inventory functions and specifies inventory items of LANDMARK type will be retrieved by the function.

### INVENTORY_MATERIAL

* `integer INVENTORY_MATERIAL = 57
|desc`

Used with Inventory functions and specifies inventory items of MATERIAL type will be retrieved by the function.

### INVENTORY_NONE

* `integer INVENTORY_NONE = -1`

Value returned by Inventory functions, to indicate that the inventory item doesn't exist.

### INVENTORY_NOTECARD

* `integer INVENTORY_NOTECARD = 7
|desc`

Used with Inventory functions and specifies inventory items of NOTECARD type will be retrieved by the function.

### INVENTORY_OBJECT

* `integer INVENTORY_OBJECT = 6
|desc`

Used with Inventory functions and specifies inventory items of OBJECT type will be retrieved by the function.

### INVENTORY_SCRIPT

* `integer INVENTORY_SCRIPT = 10
|desc`

Used with Inventory functions and specifies inventory items of SCRIPT type will be retrieved by the function.

### INVENTORY_SETTING

* `integer INVENTORY_SETTING = 56`

Used with Inventory functions and specifies inventory items of SETTING type will be retrieved by the function.

### INVENTORY_SOUND

* `integer INVENTORY_SOUND = 1
|desc`

Used with Inventory functions and specifies inventory items of SOUND type will be retrieved by the function.

### INVENTORY_TEXTURE

* `integer INVENTORY_TEXTURE = 0
|desc`

Used with Inventory functions and specifies inventory items of TEXTURE type will be retrieved by the function.

### JSON_APPEND

* `integer JSON_APPEND = -1`

A special specifier for llJsonSetValue which indicates the given value should be appended to the array at the specified level. Care should be taken, as if the value at that level is not an array, the existing data will be overwritten and replaced with the array meant for appending.
|constants
|examples

### JSON_ARRAY

* `string JSON_ARRAY = "﷒"`

Used with the llList2Json function to indicate that the provided list (which may be empty) is to be used to encode and return a string serialization of a Json array.
Also a possible return value for the llJsonValueType function that indicates the Json data type of at the specifier location within a given Json text is, in fact, a Json array.

### JSON_DELETE

* `string JSON_DELETE = "�"`

A constant used to delete a value within a [http://www.json.org/ JSON] text string.

### JSON_FALSE

* `string JSON_FALSE = "�"`

Return value for llJsonValueType function indicating the data type of a given address specifier in a given string-serialized JSON object.
Also used to set the bare word 'false' as a Value within a Json text using llJsonSetValue and llList2Json.

### JSON_INVALID

* `string JSON_INVALID = "﷐"`

A return value that indicates an invalid 'type' was specified to the llList2Json function. Also a return value for llJsonValueType function indicating the data type of a given address specifier in a given string-serialized JSON object.
 Also a return value for llJsonGetValue to signify a specifier list attempting to access a nonexistent location within a Json text (see Examples).

### JSON_NULL

* `string JSON_NULL = "�"`

Return value for llJsonValueType function indicating the Json data type of a given address specifier in a given string-serialized JSON text.
Also the return string value for llJsonGetValue function when the bare word 'null' is at the given address specifier in a given string-serialized JSON text.
Also used to encode the bare word 'null' within a Json text to signify an empty, valueless placeholder Value at that location (the empty LSL String, "", can be used as well for that).

### JSON_NUMBER

* `string JSON_NUMBER = "�"`

Return value for llJsonValueType function indicating the data type of a given address specifier in a given string-serialized JSON object.

### JSON_OBJECT

* `string JSON_OBJECT = "﷑"`

Used with the llList2Json function to indicate that the list provided is a strided list of "Key", Value pairs (which may be empty), and that a string representing a Json object will be returned.
Also a possible return value for the llJsonValueType function that indicates the Json data type of at the specifier location within a given Json text is, in fact, a JSON_OBJECT.

### JSON_STRING

* `string JSON_STRING = "�"`

Return value for llJsonValueType function indicating the data type of a given address specifier in a given string-serialized JSON object.

### JSON_TRUE

* `string JSON_TRUE = "�"`

Return value for llJsonValueType function indicating the data type of a given address specifier in a given string-serialized JSON object.
Also used to set the bare word 'true' as a Value within a JSON text using llJsonSetValue and llList2Json.

### KFM_CMD_PAUSE

* `integer KFM_CMD_PAUSE = 2`

Command used in the options parameter llSetKeyframedMotion .Stops the animation but doesn t reset it at the start of motion.
|examples

### KFM_CMD_PLAY

* `integer KFM_CMD_PLAY = 0`

Command used in the options parameter llSetKeyframedMotion .Resumes the animation previously stopped by KFM_CMD_STOP or KFM_CMD_PAUSE
|examples

### KFM_CMD_STOP

* `integer KFM_CMD_STOP = 1`

Command used in the options parameter llSetKeyframedMotion .Stops the animation and resets it at the start of motion.
|examples

### KFM_COMMAND

* `integer KFM_COMMAND = 0`

Command used in the options parameter of llSetKeyframedMotion .followed by one of: KFM_CMD_STOP, KFM_CMD_PLAY, KFM_CMD_PAUSE to play , stop or pause the motion . 
|examples

### KFM_DATA

* `integer KFM_DATA = 2`

Flag used in the options parameter llSetKeyframedMotion : is a flag followed by a bitwise combination of: KFM_TRANSLATION and KFM_ROTATION. If absent, both rotations and translations must be provided in the first parameter of llSetKeyframedMotion .
|examples

### KFM_FORWARD

* `integer KFM_FORWARD = 0`

specify the playback mode used in llSetKeyframedMotion . It s the default playback mode . It plays the frames in this order frame1, frame2 .. frame N And stops after
|examples

### KFM_LOOP

* `integer KFM_LOOP = 1`

specify the playback mode used in llSetKeyframedMotion : will play the frames in the order number 1 , number 2 ... number N , returns to
the intitial position , plays number 1 , nummber 2 ..
|examples

### KFM_MODE

* `integer KFM_MODE = 1`

used in llSetKeyframedMotion . followed by one of: KFM_LOOP, KFM_REVERSE, KFM_FORWARD, or KFM_PING_PONG will specify the playback mode. Defaults to KFM_FORWARD. Must be specified when the keyframe list is provided.
|examples

### KFM_PING_PONG

* `integer KFM_PING_PONG = 2`

specify the playback mode used in llSetKeyframedMotion 
|examples

### KFM_REVERSE

* `integer KFM_REVERSE = 3`

specify the playback mode used in llSetKeyframedMotion . It plays the frames in this order frameN, frameN-1 .. frame 2 , frame 1 . And stops after
|examples

### KFM_ROTATION

* `integer KFM_ROTATION = 0x1`

Specifies the type of data in the list of moves for llSetKeyframedMotion
|examples

### KFM_TRANSLATION

* `integer KFM_TRANSLATION = 0x2`

specifies the type of data in the list of moves for the function llSetKeyframedMotion
|examples

### LAND_LEVEL

* `integer LAND_LEVEL = 0`

### LAND_LOWER

* `integer LAND_LOWER = 2`

### LAND_NOISE

* `integer LAND_NOISE = 4`

Randomize the land - makes it rough

### LAND_RAISE

* `integer LAND_RAISE = 1`

### LAND_REVERT

* `integer LAND_REVERT = 5`

### LAND_SMOOTH

* `integer LAND_SMOOTH = 3`

### LINK_ALL_CHILDREN

* `integer LINK_ALL_CHILDREN = -3`

Targets all the prims in the linkset, except the root.
|examples

### LINK_ALL_OTHERS

* `integer LINK_ALL_OTHERS = -2`

Targets all the other prims in the linkset, except the one the script resides in.
The opposite of LINK_THIS.
|examples

### LINK_ROOT

* `integer LINK_ROOT = 1`

Targets the root prim in the linkset.

### LINK_SET

* `integer LINK_SET = -1`

Targets all the prims in the linkset.
|examples

### LINK_THIS

* `integer LINK_THIS = -4`

Targets the prim the script resides in. 
The opposite flag of this is LINK_ALL_OTHERS.
|examples

### LIST_STAT_GEOMETRIC_MEAN

* `integer LIST_STAT_GEOMETRIC_MEAN = 9`

Returns the geometric mean of a list of numbers.
float geometric_mean = llListStatistics( LIST_STAT_GEOMETRIC_MEAN, numList );
For two numbers, a and b, the geometric mean is llSqrt(a*b). For a list of n numbers, the geometric mean is the n-th root of their product. It indicates the central tendency or typical value to expect. It only works for positive numbers.
In comparison, the arithmetic mean (known as the average) is the sum of the numbers divided by how many numbers there are.

### LIST_STAT_MAX

* `integer LIST_STAT_MAX = 2`

Retrieves the largest number in the list.
|pa
|pb

### LIST_STAT_MEAN

* `integer LIST_STAT_MEAN = 3`

Calculates the mean (average) of the numbers in the list.
|pa
|pb

### LIST_STAT_MEDIAN

* `integer LIST_STAT_MEDIAN = 4`

Calculates the median number in the list.
float median = llListStatistics( LIST_STAT_MEDIAN, numList );
The median is the number for which half the values are less and half are greater. For example, the median of [1,1,1,2,1000,1000,1000] is 2, while the mean is 429.3.

### LIST_STAT_MIN

* `integer LIST_STAT_MIN = 1`

Retrieves the smallest number in the list.

### LIST_STAT_NUM_COUNT

* `integer LIST_STAT_NUM_COUNT = 8`

Retrieves the number of float and integer elements.

### LIST_STAT_RANGE

* `integer LIST_STAT_RANGE = 0`

Calculates the range of the list. (max - min)

### LIST_STAT_STD_DEV

* `integer LIST_STAT_STD_DEV = 5`

Calculates the sample standard deviation of a list of numbers.
float sample_standard_deviation = llListStatistics( LIST_STAT_STD_DEV, numList );
Standard deviation is a measure of how spread out the values are, and is defined as the square root of the average of the squares of the numbers:
integer count = (integer)llListStatistics( LIST_STAT_NUM_COUNT, numList );
float standard_deviation = llSqrt( llListStatistics( LIST_STAT_SUM_SQUARES , numList ) ) / count;
The sample standard deviation is used when the list doesn't (or can't) include the entire set of numbers, like the mass of every prim in SL. The true standard deviation is therefore estimated by using the sample standard deviation, which is defined by,
integer count = (integer)llListStatistics( LIST_STAT_NUM_COUNT, numList );
float sample_standard_deviation = llSqrt( llListStatistics( LIST_STAT_SUM_SQUARES , numList ) ) / (count - 1);
Another way to calculate the sample standard deviation is 
 list numList = [1,1,1,2,1000,1000,1000];
 integer count = llGetListLength( numList );
 float sum = 0;
 float mean = llListStatistics( LIST_STAT_MEAN, numList );
 integer i = 0;
 for (; i 
|pa
|text
|pb

### LIST_STAT_SUM

* `integer LIST_STAT_SUM = 6`

Calculates the sum of the numbers in a list.
|pa
|pb

### LIST_STAT_SUM_SQUARES

* `integer LIST_STAT_SUM_SQUARES = 7`

Calculates the sum of the squares of the numbers in a list.
float sum_of_squares = llListStatistics( LIST_STAT_SUM_SQUARES, numList );
That is, for each number N_i in a list of k elements, it calculates N_1*N_1 + N_2*N_2 + ... + N_k * N_k.

### LOOP

* `integer LOOP = 0x02`

Causes a texture animation to loop.
|examples

### MASK_BASE

* `integer MASK_BASE = 0`

### MASK_EVERYONE

* `integer MASK_EVERYONE = 3`

### MASK_GROUP

* `integer MASK_GROUP = 2`

### MASK_NEXT

* `integer MASK_NEXT = 4`

### MASK_OWNER

* `integer MASK_OWNER = 1`

### NAK

* `NAK`

NAK is a value returned by the llGetNotecardLineSync function when the requested notecard data is not available due to the notecard not being in the region notecard cache. The value returned equals the characters with codes "10, 21, 10", which is to say the ASCII "NAK" character surrounded by two newline characters.
If the NAK response is encountered, the card can be fetched into the region notecard cache by using the llGetNotecardLine or llGetNumberOfNotecardLines functions. If the notecard doesn't exist at all, further llGetNotecardLineSync calls will continue returning NAK.

### NULL_KEY

* `string NULL_KEY = "00000000-0000-0000-0000-000000000000"`

NULL_KEY is a string. However it is only really useful as a key.
For tests, NULL_KEY evaluates to TRUE like other strings.
For list search (like llListFindList), NULL_KEY won't match null keys whose type is key without typecasting.

### OBJECT_ATTACHED_POINT

* `integer OBJECT_ATTACHED_POINT = 19`

Used with llGetObjectDetails, returns the value llGetAttached would return.
|examples

### OBJECT_ATTACHED_SLOTS_AVAILABLE

* `integer OBJECT_ATTACHED_SLOTS_AVAILABLE = 35`

This is a flag used with llGetObjectDetails to gets the avatar's available attachment slot count.
If id is not an avatar, 0.0 is returned.
|examples

### OBJECT_DAMAGE

* `integer OBJECT_DAMAGE = 51`

Gets the damage amount delivered by a prim on collision.

### OBJECT_DAMAGE_TYPE

* `integer OBJECT_DAMAGE_TYPE = 52`

Gets the damage type that is applied when this prim collides with another object. Can match one of the DAMAGE_TYPE_* constants, be a custom damage type or be a repurposed damage field.

### OBJECT_HEALTH

* `integer OBJECT_HEALTH = 50`

Gets the health of the object.
This property can only be changed by a call to llSetPrimitiveParams or llSetLinkPrimitiveParams with PRIM_HEALTH. Damaging an object (with llDamage or collision by damage-enabled object) will not directly affect its health.

### OBJECT_HOVER_HEIGHT

* `integer OBJECT_HOVER_HEIGHT = 25`

This is a flag used with llGetObjectDetails to get the hover height of the avatar.
If id is not an avatar, 0.0 is returned. Normal values are in the range {{Interval

### OBJECT_OMEGA

* `integer OBJECT_OMEGA = 29`

Used with llGetObjectDetails to get the objects rotational velocity.

### OBJECT_PATHFINDING_TYPE

* `integer OBJECT_PATHFINDING_TYPE = |desc
|examples`

### OBJECT_PHANTOM

* `integer OBJECT_PHANTOM = 22`

This is a flag used with llGetObjectDetails to get the object's phantom attribute.
If the object being queried is an avatar or attachment, 0 is returned.
|examples

### OBJECT_PHYSICS

* `integer OBJECT_PHYSICS = 21`

This is a flag used with llGetObjectDetails to get the object's physics attribute.
If the object being queried is an avatar or attachment, 0 is returned.
|examples

### OBJECT_POS

* `integer OBJECT_POS = 3`

This is a flag used with llGetObjectDetails to get the object position.
|examples

### OBJECT_RENDER_WEIGHT

* `integer OBJECT_RENDER_WEIGHT = 24`

This is a flag used with llGetObjectDetails to get the Avatar_Rendering_Cost of an avatar, based on values reported by nearby viewers. If no data is available, -1 is returned. The maximum render weight stored by the simulator is 500000. When called against an object, 0 is returned.
|examples

### OBJECT_RETURN_PARCEL

* `integer OBJECT_RETURN_PARCEL = 1`

For llReturnObjectsByOwner, sets the scope to return all objects on the same parcel as the script which are owned by 'owner'. The script must be owned by an estate manager or over a parcel owned by the owner of the script.
|examples

### OBJECT_RETURN_PARCEL_OWNER

* `integer OBJECT_RETURN_PARCEL_OWNER = 2`

For llReturnObjectsByOwner, sets the scope to return all objects owned by 'owner' which are over parcels owned by the owner of the script. 
|examples

### OBJECT_RETURN_REGION

* `integer OBJECT_RETURN_REGION = 4`

For llReturnObjectsByOwner, sets the scope to return all objects in the region owned by 'owner' - only works when the script is owned by the estate owner or an estate manager. 
|examples

### OBJECT_ROOT

* `integer OBJECT_ROOT = |desc
|examples`

### OBJECT_TEMP_ON_REZ

* `integer OBJECT_TEMP_ON_REZ = 23`

This is a flag used with llGetObjectDetails to get the object's temporary attribute.
|examples

### OPT_AVATAR

* `integer OPT_AVATAR = |desc
|examples`

### OPT_CHARACTER

* `integer OPT_CHARACTER = |desc
|examples`

### OPT_EXCLUSION_VOLUME

* `integer OPT_EXCLUSION_VOLUME = 6
|hvalue
|desc
|examples
|caveats`

### OPT_LEGACY_LINKSET

* `integer OPT_LEGACY_LINKSET = |desc
|examples`

### OPT_MATERIAL_VOLUME

* `integer OPT_MATERIAL_VOLUME = 5
|hvalue
|desc
|examples
|caveats`

### OPT_OTHER

* `integer OPT_OTHER = |desc
|examples`

### OPT_STATIC_OBSTACLE

* `integer OPT_STATIC_OBSTACLE = |desc
|examples`

### OPT_WALKABLE

* `integer OPT_WALKABLE = |desc
|examples`

### PARCEL_FLAG_ALLOW_CREATE_OBJECTS

* `PARCEL_FLAG_ALLOW_CREATE_OBJECTS`

This is a flag used with llGetParcelFlags to check if anyone can create objects on the parcel.
|examples

### PARCEL_FLAG_ALLOW_DAMAGE

* `PARCEL_FLAG_ALLOW_DAMAGE`

This is a flag used with llGetParcelFlags to check if damage is enabled on the parcel.
|examples

### PARCEL_FLAG_ALLOW_FLY

* `PARCEL_FLAG_ALLOW_FLY`

This is a flag used with llGetParcelFlags to check if flying is allowed on the parcel.
|examples

### PARCEL_FLAG_ALLOW_SCRIPTS

* `PARCEL_FLAG_ALLOW_SCRIPTS`

This is a flag used with llGetParcelFlags to check if scripts are allowed to run on the parcel.
|examples

### PARCEL_FLAG_ALLOW_TERRAFORM

* `PARCEL_FLAG_ALLOW_TERRAFORM`

This is a flag used with llGetParcelFlags to check if anyone is allowed to terraform the parcel.
|examples

### PARCEL_MEDIA_COMMAND_AGENT

* `integer PARCEL_MEDIA_COMMAND_AGENT = 7`

Applies the media command to the specified agent only.
|examples

### PARCEL_MEDIA_COMMAND_AUTO_ALIGN

* `integer PARCEL_MEDIA_COMMAND_AUTO_ALIGN = 9`

Sets the parcel option 'Auto scale content'.
|examples

### PARCEL_MEDIA_COMMAND_DESC

* `integer PARCEL_MEDIA_COMMAND_DESC = 12`

Use this to get or set the parcel media description.
|examples

### PARCEL_MEDIA_COMMAND_LOOP

* `integer PARCEL_MEDIA_COMMAND_LOOP = 3`

Start the media stream playing from the current frame. When the end is reached, loop to the beginning and continue.
|examples

### PARCEL_MEDIA_COMMAND_LOOP_SET

* `integer PARCEL_MEDIA_COMMAND_LOOP_SET = 13`

Use this to get or set the parcel's media loop duration. It may not be functional. See for detail.
|examples

### PARCEL_MEDIA_COMMAND_PAUSE

* `integer PARCEL_MEDIA_COMMAND_PAUSE = 1`

Pause the media stream (stop playing but stay on current frame).
|examples

### PARCEL_MEDIA_COMMAND_PLAY

* `integer PARCEL_MEDIA_COMMAND_PLAY = 2`

Start the media stream playing from the current frame and stop when the end is reached.
|examples

### PARCEL_MEDIA_COMMAND_SIZE

* `integer PARCEL_MEDIA_COMMAND_SIZE = 11`

Use this to get or set the parcel media pixel resolution.
|examples

### PARCEL_MEDIA_COMMAND_STOP

* `integer PARCEL_MEDIA_COMMAND_STOP = 0`

Stop the media stream and go back to the first frame.
|examples

### PARCEL_MEDIA_COMMAND_TEXTURE

* `integer PARCEL_MEDIA_COMMAND_TEXTURE = 4`

Use this to get or set the parcel's media texture.
|examples

### PARCEL_MEDIA_COMMAND_TIME

* `integer PARCEL_MEDIA_COMMAND_TIME = 6`

Move a media stream to a specific time in (floating point) seconds.
|examples

### PARCEL_MEDIA_COMMAND_TYPE

* `integer PARCEL_MEDIA_COMMAND_TYPE = 10`

Use this to get or set the parcel media MIME type (e.g. "text/html").
|examples

### PARCEL_MEDIA_COMMAND_UNLOAD

* `integer PARCEL_MEDIA_COMMAND_UNLOAD = 8`

Completely unloads the movie and restores the original texture.
|examples

### PARCEL_MEDIA_COMMAND_URL

* `integer PARCEL_MEDIA_COMMAND_URL = 5`

Used to get or set the parcel's media url.
|examples

### PASSIVE

* `integer PASSIVE = 0x4`

If it is contained in the result of llDetectedType(), it means it is non-physical objects. 
If it is used as an filter of llSensor() or llSensorRepeat(), it will search for non-scripted or script is inactive and non-physical or, if physical, not moving. Thus, it is not using SL server resources now.

### PASS_ALWAYS

* `integer PASS_ALWAYS = 1`

The applicable event group will always be triggered in the the root prim. Whether or not is handled in the child prim is irrelevant.
|examples

### PASS_IF_NOT_HANDLED

* `integer PASS_IF_NOT_HANDLED = 0`

The applicable event group will be triggered in the the root prim if it is not handled in this child prim.
|examples

### PASS_NEVER

* `integer PASS_NEVER = 2`

The applicable event group will never be triggered in the the root prim. Whether or not is handled in the child prim is irrelevant.
|examples

### PATROL_PAUSE_AT_WAYPOINTS

* `integer PATROL_PAUSE_AT_WAYPOINTS = 0`

Option parameter for llPatrolPoints function. Can be set TRUE or FALSE (the default). When set TRUE, characters will slow down and momentarily pause at each waypoint. When set FALSE, characters will continue to move to the next waypoint at full speed, with no pause.
|examples

### PAYMENT_INFO_ON_FILE

* `integer PAYMENT_INFO_ON_FILE = 0x1`

If payment info is on file.

### PAYMENT_INFO_USED

* `integer PAYMENT_INFO_USED = 0x2`

If payment info has been used.

### PAY_DEFAULT

* `integer PAY_DEFAULT = -2`

Uses the default value for a pay button.
|examples

### PAY_HIDE

* `integer PAY_HIDE = -1`

Hides a pay button completely.
|examples

### PERMISSION_ATTACH

* `integer PERMISSION_ATTACH = 0x20
|desc
|examples`

### PERMISSION_CHANGE_LINKS

* `integer PERMISSION_CHANGE_LINKS = 0x80`

### PERMISSION_CONTROL_CAMERA

* `integer PERMISSION_CONTROL_CAMERA = 0x800`

### PERMISSION_DEBIT

* `integer PERMISSION_DEBIT = |desc
|examples`

### PERMISSION_OVERRIDE_ANIMATIONS

* `integer PERMISSION_OVERRIDE_ANIMATIONS = 0x8000
|desc
|examples`

### PERMISSION_PRIVILEGED_LAND_ACCESS

* `integer PERMISSION_PRIVILEGED_LAND_ACCESS = 524288`

Required Permission to use the llSetParcelForSale() function.
|examples

### PERMISSION_RETURN_OBJECTS

* `integer PERMISSION_RETURN_OBJECTS = 65536`

Required Permission to use the llReturnObject* functions.
|examples

### PERMISSION_SILENT_ESTATE_MANAGEMENT

* `integer PERMISSION_SILENT_ESTATE_MANAGEMENT = 0x4000`

A script with this permission does not notify the object owner when it modifies estate access rules via llManageEstateAccess.
|examples

### PERMISSION_TAKE_CONTROLS

* `integer PERMISSION_TAKE_CONTROLS = |desc
|examples`

### PERMISSION_TELEPORT

* `integer PERMISSION_TELEPORT = 0x1000`

Permission required to use llTeleportAgent.
|examples

### PERMISSION_TRACK_CAMERA

* `integer PERMISSION_TRACK_CAMERA = 0x400`

### PERMISSION_TRIGGER_ANIMATION

* `integer PERMISSION_TRIGGER_ANIMATION = 0x10
|desc
|examples`

### PERM_ALL

* `integer PERM_ALL = 0x7FFFFFFF`

### PERM_COPY

* `integer PERM_COPY = 0x00008000`

### PERM_MODIFY

* `integer PERM_MODIFY = 0x00004000`

### PERM_MOVE

* `integer PERM_MOVE = 0x00080000`

### PERM_TRANSFER

* `integer PERM_TRANSFER = 0x00002000`

### PI

* `float PI = 3.1415926535897932384626433832795f`

. The number of radians in a half circle.
|examples
|events

### PING_PONG

* `integer PING_PONG = 0x08`

Causes a texture animation to play forward first, then in reverse.
|examples

### PI_BY_TWO

* `float PI_BY_TWO = 1.5707963267948966192313216916398f`

PI/2. The number of radians in a quarter circle.
|examples
|events
|functions

### PRIM_ALLOW_UNSIT

* `integer PRIM_ALLOW_UNSIT = 39`

When set on a prim that is running a script as part of an experience an avatar that is seated on the sit target and has agreed to participate in the experience will be unable to stand or select another prim to sit on. The restriction remains in place until one of the following conditions is met:
* PRIM_ALLOW_UNSIT is changed to TRUE
* llUnSit( ) is called forcing the avatar to stand.
* llSitOnLink( ) is called moving this avatar to a new sit target. 
* The avatar teleports or is teleported by the experience.
* The agent signs off.
* The agent disables the experience.
* The prim the avatar is seated on is destroyed.
* The agent is unseated for any reason.
This flag has no effect on agents who had seated manually (i.e. not via llSitOnLink using experience permissions).
If the linkset moves to a region that has not enabled the experience this value will be ignored and standing will behave as normal, without restriction. If the linkset moves to a parcel that the avatar does not have access to, the avatar will be forced to stand and the unsit restriction will be removed.

### PRIM_ALPHA_MODE

* `integer PRIM_ALPHA_MODE = 38`

Used to specify how the alpha channel of the diffuse texture should affect rendering of a prim’s face.
|examples
|constants

### PRIM_ALPHA_MODE_BLEND

* `integer PRIM_ALPHA_MODE_BLEND = 1`

Used with PRIM_ALPHA_MODE. Prims faces set to this type use alpha blending for diffuse texture rendering (assuming the alpha channel exists).
|examples
|constants
|functions
|events
|location
|history

### PRIM_ALPHA_MODE_EMISSIVE

* `integer PRIM_ALPHA_MODE_EMISSIVE = 3`

Used with PRIM_ALPHA_MODE. Prims faces set to this type render with an emissivity corresponding to the opacity of each pixel of the diffuse texture. The more opaque a pixel is, the brighter it renders under all lighting conditions. A fully-opaque pixel will effectively render as 'full bright'.
|examples
|constants
|functions
|events
|location
|history

### PRIM_ALPHA_MODE_MASK

* `integer PRIM_ALPHA_MODE_MASK = 2`

Used with PRIM_ALPHA_MODE. Prims faces set to this type render as either completely opaque or completely transparent on a per-pixel basis. Pixels which are less opaque than the specified mask_cutoff are rendered as completely transparent, and the rest are rendered as fully opaque.
|examples
|constants
|functions
|events
|location
|history

### PRIM_ALPHA_MODE_NONE

* `integer PRIM_ALPHA_MODE_NONE = 0`

Used with PRIM_ALPHA_MODE. Prims faces set to this type ignore the alpha channel of the diffuse texture, and render as completely opaque.
|examples
|constants
|functions
|events
|location
|history

### PRIM_BUMP_BARK

* `integer PRIM_BUMP_BARK = 4`

### PRIM_BUMP_BLOBS

* `integer PRIM_BUMP_BLOBS = 12`

### PRIM_BUMP_BRICKS

* `integer PRIM_BUMP_BRICKS = 5`

### PRIM_BUMP_BRIGHT

* `integer PRIM_BUMP_BRIGHT = 1`

### PRIM_BUMP_CHECKER

* `integer PRIM_BUMP_CHECKER = 6`

### PRIM_BUMP_CONCRETE

* `integer PRIM_BUMP_CONCRETE = 7`

### PRIM_BUMP_DARK

* `integer PRIM_BUMP_DARK = 2`

### PRIM_BUMP_DISKS

* `integer PRIM_BUMP_DISKS = 10`

### PRIM_BUMP_GRAVEL

* `integer PRIM_BUMP_GRAVEL = 11`

### PRIM_BUMP_LARGETILE

* `integer PRIM_BUMP_LARGETILE = 14`

### PRIM_BUMP_NONE

* `integer PRIM_BUMP_NONE = 0`

### PRIM_BUMP_SHINY

* `integer PRIM_BUMP_SHINY = 19`

Used to get or set the Bump Mapping and shiny settings of the prim's face.
{{LSL_Constants/PrimitiveParams/bumpshiny

### PRIM_BUMP_SIDING

* `integer PRIM_BUMP_SIDING = 13`

### PRIM_BUMP_STONE

* `integer PRIM_BUMP_STONE = 9`

### PRIM_BUMP_STUCCO

* `integer PRIM_BUMP_STUCCO = 15`

### PRIM_BUMP_SUCTION

* `integer PRIM_BUMP_SUCTION = 16`

### PRIM_BUMP_TILE

* `integer PRIM_BUMP_TILE = 8`

### PRIM_BUMP_WEAVE

* `integer PRIM_BUMP_WEAVE = 17`

### PRIM_BUMP_WOOD

* `integer PRIM_BUMP_WOOD = 3`

### PRIM_CLICK_ACTION

* `integer PRIM_CLICK_ACTION = 43`

Which action will be taken when left-clicking the prim. Followed by one of these flags:

### PRIM_COLOR

* `integer PRIM_COLOR = 18`

Used to get or set the Blinn-Phong color and alpha of a prim's face.

### PRIM_DAMAGE

* `integer PRIM_DAMAGE = 51`

Sets the damage amount and damage type delivered by a prim on collision.

### PRIM_DESC

* `integer PRIM_DESC = 28`

Used to get or set the prim's description.

### PRIM_FLEXIBLE

* `integer PRIM_FLEXIBLE = 21`

Used to get or set the prim's flexible configuration.

### PRIM_FULLBRIGHT

* `integer PRIM_FULLBRIGHT = 20`

Used to get or set the full-bright setting of a prim's face.

### PRIM_GLOW

* `integer PRIM_GLOW = 25`

PRIM_GLOW is used to get or set the glow status of the face. Use the integer number 25 if the compiler rejects the named constant.

### PRIM_GLTF_ALPHA_MODE_BLEND

* `integer PRIM_GLTF_ALPHA_MODE_BLEND = 1`

Alpha blending rendering mode for GLTF materials, used with PRIM_GLTF_BASE_COLOR. Transparency from the texture is applied and multiplied by the material's opacity multiplier, in linear color space.
|examples

### PRIM_GLTF_ALPHA_MODE_MASK

* `integer PRIM_GLTF_ALPHA_MODE_MASK = 2`

Alpha masked rendering mode for GLTF materials, used with PRIM_GLTF_BASE_COLOR. Transparency from the texture is compared to the material's alpha cutoff, with pixels above the cutoff fully opaque and pixels below it fully transparent.
|examples

### PRIM_GLTF_ALPHA_MODE_OPAQUE

* `integer PRIM_GLTF_ALPHA_MODE_OPAQUE = 0`

Opaque rendering mode for GLTF materials, used with PRIM_GLTF_BASE_COLOR. No transparency.
|examples

### PRIM_GLTF_BASE_COLOR

* `texture PRIM_GLTF_BASE_COLOR = 48`

Used to get or set the GLTF base color override of an object's face.

### PRIM_GLTF_EMISSIVE

* `texture PRIM_GLTF_EMISSIVE = 46`

Used to get or set the GLTF emission override of an object's face.

### PRIM_GLTF_METALLIC_ROUGHNESS

* `texture PRIM_GLTF_METALLIC_ROUGHNESS = 47`

Used to get or set the GLTF occlusion/metallic/roughness override of an object's face.

### PRIM_GLTF_NORMAL

* `texture PRIM_GLTF_NORMAL = 45`

Used to get or set the GLTF normal map override of an object's face.

### PRIM_HEALTH

* `integer PRIM_HEALTH = 52`

Used to get or set the health of the object. Objects start with 0 health by default.
This property can only be changed by a call to llSetPrimitiveParams or llSetLinkPrimitiveParams. Damaging an object (with llDamage or collision by damage-enabled object) will not directly affect its health.

### PRIM_HOLE_CIRCLE

* `integer PRIM_HOLE_CIRCLE = 0x10`

Used with certain PRIM_TYPE_* flags to make a circular hole, via the hole_shape parameter.

### PRIM_HOLE_DEFAULT

* `integer PRIM_HOLE_DEFAULT = 0x00`

Used with certain PRIM_TYPE_* flags to make a hole the same shape as the outer shape, via the hole_shape parameter.

### PRIM_HOLE_SQUARE

* `integer PRIM_HOLE_SQUARE = 0x20`

Used with certain PRIM_TYPE_* flags to make a squarish hole, via the hole_shape parameter.

### PRIM_HOLE_TRIANGLE

* `integer PRIM_HOLE_TRIANGLE = 0x30`

Used with certain PRIM_TYPE_* flags to make a triangular hole, via the hole_shape parameter.

### PRIM_LINK_TARGET

* `integer PRIM_LINK_TARGET = 34`

Used to get or set multiple links with a single PrimParameters call.

### PRIM_MATERIAL

* `integer PRIM_MATERIAL = 2`

Sets the prim material. Material does not affect mass, but does affect friction, bounce (elasticity), and collision sound. On a wood incline of 33 degrees, the example script below gave the following results:
{ class="sortable" 
+ Table detailing maximum velocity and distance traveled down the incline. 
- 
!Type
!Velocity (m/s) 
!Distance (m) 
-
Stone
0.453181
0.361655
-
Metal
5.475444
10.211180
-
Glass
6.483150
11.678304
-
Wood
2.154549
9.433724
-
Flesh
0.351543
0.188043
-
Plastic
4.502428
9.590952
-
Rubber
0.374964
0.187106
-
}

### PRIM_MATERIAL_FLESH

* `integer PRIM_MATERIAL_FLESH = 4`

### PRIM_MATERIAL_GLASS

* `integer PRIM_MATERIAL_GLASS = 2`

Very low friction

### PRIM_MATERIAL_LIGHT

* `integer PRIM_MATERIAL_LIGHT = 7`

This constant and it's underlying functionality is deprecated. Light is no longer a prim property, it is now a face property. The same functionality is reproduced with [ PRIM_FULLBRIGHT, ALL_SIDES, TRUE ]

### PRIM_MATERIAL_METAL

* `integer PRIM_MATERIAL_METAL = 1`

### PRIM_MATERIAL_PLASTIC

* `integer PRIM_MATERIAL_PLASTIC = 5`

### PRIM_MATERIAL_RUBBER

* `integer PRIM_MATERIAL_RUBBER = 6`

### PRIM_MATERIAL_STONE

* `integer PRIM_MATERIAL_STONE = 0`

### PRIM_MATERIAL_WOOD

* `integer PRIM_MATERIAL_WOOD = 3`

### PRIM_MEDIA_ALT_IMAGE_ENABLE

* `integer PRIM_MEDIA_ALT_IMAGE_ENABLE = 0
|desc`

### PRIM_MEDIA_AUTO_LOOP

* `integer PRIM_MEDIA_AUTO_LOOP = 4
|desc`

### PRIM_MEDIA_AUTO_PLAY

* `integer PRIM_MEDIA_AUTO_PLAY = 5
|desc`

### PRIM_MEDIA_AUTO_SCALE

* `integer PRIM_MEDIA_AUTO_SCALE = 6
|desc`

### PRIM_MEDIA_AUTO_ZOOM

* `integer PRIM_MEDIA_AUTO_ZOOM = 7
|desc`

### PRIM_MEDIA_CURRENT_URL

* `integer PRIM_MEDIA_CURRENT_URL = 2
|desc
|examples
|functions
|events`

### PRIM_MEDIA_FIRST_CLICK_INTERACT

* `integer PRIM_MEDIA_FIRST_CLICK_INTERACT = 8
|desc`

### PRIM_MEDIA_HEIGHT_PIXELS

* `integer PRIM_MEDIA_HEIGHT_PIXELS = 10
|desc
|examples
|functions
|events`

### PRIM_MEDIA_HOME_URL

* `integer PRIM_MEDIA_HOME_URL = 3
|desc
|examples
|functions
|events`

### PRIM_MEDIA_PERMS_CONTROL

* `integer PRIM_MEDIA_PERMS_CONTROL = 14
|desc
|examples
|functions
|events`

### PRIM_MEDIA_PERMS_INTERACT

* `integer PRIM_MEDIA_PERMS_INTERACT = 13
|desc
|examples
|functions
|events`

### PRIM_MEDIA_PERM_ANYONE

* `integer PRIM_MEDIA_PERM_ANYONE = 0x4`

### PRIM_MEDIA_PERM_GROUP

* `integer PRIM_MEDIA_PERM_GROUP = 0x2`

### PRIM_MEDIA_PERM_NONE

* `integer PRIM_MEDIA_PERM_NONE = 0x0`

### PRIM_MEDIA_PERM_OWNER

* `integer PRIM_MEDIA_PERM_OWNER = 0x1`

### PRIM_MEDIA_WHITELIST

* `integer PRIM_MEDIA_WHITELIST = 12
|desc
|examples
|functions
|events`

### PRIM_MEDIA_WHITELIST_ENABLE

* `integer PRIM_MEDIA_WHITELIST_ENABLE = 11
|desc`

### PRIM_MEDIA_WIDTH_PIXELS

* `integer PRIM_MEDIA_WIDTH_PIXELS = 9
|desc
|examples
|functions
|events`

### PRIM_NAME

* `integer PRIM_NAME = 27`

Used to get or set the prim's name.

### PRIM_NORMAL

* `texture PRIM_NORMAL = 37`

Used to get or set the Blinn-Phong normal map texture settings of a prim's face.

### PRIM_OMEGA

* `integer PRIM_OMEGA = 32`

Used to make the object spin at the specified axis and rate, or retrieve spin settings. See llTargetOmega for specification.

### PRIM_PHANTOM

* `integer PRIM_PHANTOM = 5`

Used to get or set the object's phantom status.

### PRIM_PHYSICS

* `integer PRIM_PHYSICS = 3`

Used to get or set the object's physics status. When enabled the object responds to SL physics.

### PRIM_PHYSICS_SHAPE_CONVEX

* `integer PRIM_PHYSICS_SHAPE_CONVEX = 2`

Used with PRIM_PHYSICS_SHAPE_TYPE. Prims of this type use the convex hull of the prim shape for physics (this is the default for mesh objects)

### PRIM_PHYSICS_SHAPE_NONE

* `integer PRIM_PHYSICS_SHAPE_NONE = 1`

Used with PRIM_PHYSICS_SHAPE_TYPE. Prims of this type are ignored by the physics engine. Read more details on PRIM_PHYSICS_SHAPE_TYPE

### PRIM_PHYSICS_SHAPE_PRIM

* `integer PRIM_PHYSICS_SHAPE_PRIM = 0`

Used with PRIM_PHYSICS_SHAPE_TYPE. Prims of this type use the normal prim shape for physics (this is the default for all non-mesh objects)

### PRIM_PHYSICS_SHAPE_TYPE

* `integer PRIM_PHYSICS_SHAPE_TYPE = 30`

Used to set the type of shape the physics engine should use for the prim. This is primarily used to do Physics Optimization.
|examples
|constants

### PRIM_POINT_LIGHT

* `integer PRIM_POINT_LIGHT = 23`

PRIM_POINT_LIGHT is used to configure the point light configuration of the prim

### PRIM_POSITION

* `integer PRIM_POSITION = 6`

PRIM_POSITION is used to get or set the prim's position.

### PRIM_POS_LOCAL

* `integer PRIM_POS_LOCAL = 33`

PRIM_POS_LOCAL is used to get or set the prim's local position.

### PRIM_PROJECTOR

* `integer PRIM_PROJECTOR = 42`

The light projection settings for this prim. If the prim is not a projector the texture key will be NULL_KEY.

### PRIM_REFLECTION_PROBE

* `integer PRIM_REFLECTION_PROBE = 44`

PRIM_REFLECTION_PROBE is used to change the reflection probe configuration of the prim.
A reflection probe is a volume used for image-based lighting (IBL). It takes an image of its surroundings and uses it as the basis for reflection effects (shiny surfaces) and ambiance effects (light bouncing).
Typically, the viewer automatically places reflection probes. Prim-based probes enable artists to provide hints to the render engine to improve the quality of image based lighting. Only objects in the probe's influence volume are affected.
Lighting is most accurate when the edges of a probe volume are near the geometry that appears in reflections. For example, objects inside a room with a box shaped reflection probe that hugs the walls, floor, and ceiling would show accurate reflections and ambient lighting from the walls of the room.

### PRIM_REFLECTION_PROBE_BOX

* `integer PRIM_REFLECTION_PROBE_BOX = 1`

Used with PRIM_REFLECTION_PROBE. A reflection probe is a sphere by default, otherwise a box if this flag is set on the corresponding prim.
|examples
|constants
|functions
|events
|location

### PRIM_REFLECTION_PROBE_DYNAMIC

* `integer PRIM_REFLECTION_PROBE_DYNAMIC = 2`

Used with PRIM_REFLECTION_PROBE. A reflection probe does not image avatars by default, otherwise it images avatars if this flag is set on the corresponding prim. Imaging avatars in reflection probes has a performance cost.
|examples
|constants
|functions
|events
|location

### PRIM_REFLECTION_PROBE_MIRROR

* `integer PRIM_REFLECTION_PROBE_MIRROR = 4`

Used with PRIM_REFLECTION_PROBE. When enabled, objects with low-roughness PBR materials objects act as a mirror. Note that mirrors do not reflect avatars unless PRIM_REFLECTION_PROBE_DYNAMIC is also set. Rendering mirrors has a performance cost.
|examples
|constants
|functions
|events
|location

### PRIM_RENDER_MATERIAL

* `material PRIM_RENDER_MATERIAL = 49`

Used to get or set the material settings of a prim's face.

### PRIM_ROTATION

* `integer PRIM_ROTATION = 8`

PRIM_ROTATION is used to get or set the prim's rotation.

### PRIM_ROT_LOCAL

* `integer PRIM_ROT_LOCAL = 29`

PRIM_ROT_LOCAL is used to get or set the prim's local rotation.

### PRIM_SCRIPTED_SIT_ONLY

* `integer PRIM_SCRIPTED_SIT_ONLY = 40`

Agents may only be seated on this prim using llSitOnLink. Attempts to do a manual sit will fail. This flag applies even outside of an experience enabled region.
If any prim in a linkset has PRIM_SCRIPTED_SIT_ONLY set and no other prim in the linkset has a sit target then an avatar cannot manually sit on the object.
If some other prim in the linkset does have a sit target (that is not filled or marked PRIM_SCRIPTED_SIT_ONLY), the agent can sit on that prim.

### PRIM_SCULPT_FLAG_ANIMESH

* `integer PRIM_SCULPT_FLAG_ANIMESH = 0x20`

PRIM_SCULPT_FLAG_ANIMESH is a read-only flag set when the object is an Animated mesh 
Sculpted Prims: FAQ
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_FLAG_INVERT

* `integer PRIM_SCULPT_FLAG_INVERT = 0x40`

PRIM_SCULPT_FLAG_INVERT will cause the sculpted prim to render inside out. It works by inverting the Normal of each polygon that makes up the sculpted prim. 
Sculpted Prims: FAQ
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_FLAG_MIRROR

* `integer PRIM_SCULPT_FLAG_MIRROR = 0x80`

PRIM_SCULPT_FLAG_MIRROR will cause a mirror of the sculpted prim to rendered. The sculpted prim is mirrored over the X axis. 
Sculpted Prims: FAQ
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_CYLINDER

* `integer PRIM_SCULPT_TYPE_CYLINDER = 4`

When used in conjunction with a cylinder type sculpty is produced. It does this by stitching the left side to right.
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_MASK

* `integer PRIM_SCULPT_TYPE_MASK = 7`

PRIM_SCULPT_TYPE_MASK can be used when parsing the output of llGetPrimitiveParams when dealing with sculpted prims (PRIM_TYPE_SCULPT) to separate the sculpted type from the flags (PRIM_SCULPT_FLAG_INVERT and PRIM_SCULPT_FLAG_MIRROR) that can modify it. 
Sculpted Prims: FAQ
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_MESH

* `integer PRIM_SCULPT_TYPE_MESH = 5`

When used in conjunction with a Mesh object produced.
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_PLANE

* `integer PRIM_SCULPT_TYPE_PLANE = 3`

When used in conjunction with a plane type sculpty is produced. No stitching or converging is performed.
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_SPHERE

* `integer PRIM_SCULPT_TYPE_SPHERE = 1`

When used in conjunction with a sphere type sculpty is produced. It does this by stitching the left side to right then separately converging the top & bottom.
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SCULPT_TYPE_TORUS

* `integer PRIM_SCULPT_TYPE_TORUS = 2`

When used in conjunction with a torus type sculpty is produced. It does this by stitching the top to bottom and the left side to right.
{{LSL_Constants/PrimitiveParams/sculpt_types

### PRIM_SHINY_HIGH

* `integer PRIM_SHINY_HIGH = 3`

Sets the highest intensity legacy shininess.

### PRIM_SHINY_LOW

* `integer PRIM_SHINY_LOW = 1`

Sets the lowest intensity legacy shininess.

### PRIM_SHINY_MEDIUM

* `integer PRIM_SHINY_MEDIUM = 2`

Sets a medium intensity legacy shininess.

### PRIM_SHINY_NONE

* `integer PRIM_SHINY_NONE = 0`

Disables legacy shininess.

### PRIM_SIT_TARGET

* `integer PRIM_SIT_TARGET = 41`

The sit target, if any defined for this prim. If the active value is 0 the sit target is deactivated. If it is nonzero the prim's sit target is set to the indicated offset and rotation. As with llLinkSitTarget(), these values are relative to the prim. However, unlike llLinkSitTarget() an offset of may be explicitly set.

### PRIM_SIZE

* `integer PRIM_SIZE = 7`

Returns or sets the prim's size.

### PRIM_SLICE

* `integer PRIM_SLICE = 35`

Used to get or set the prim's slice values (a shape attribute, equivalent to ).

### PRIM_SPECULAR

* `texture PRIM_SPECULAR = 36`

Used to get or set the Blinn-Phong specular map texture settings of a prim's face.

### PRIM_TEMP_ON_REZ

* `integer PRIM_TEMP_ON_REZ = 4`

Used to get or set the object's temporary status. It lives until the next garbage collection cycle (about 1 minute). Does not count against normal prim limits. There are limits to the number of temporary objects that can exist in a region and the garbage collector may run sooner than expected.

### PRIM_TEXGEN

* `integer PRIM_TEXGEN = 22`

PRIM_TEXGEN is used to get and set the configure the texture mapping mode of the face.
{{LSL_Constants/PrimitiveParams/texgen

### PRIM_TEXGEN_DEFAULT

* `integer PRIM_TEXGEN_DEFAULT = 0`

Used with PRIM_TEXGEN to set the texture mapping mode, specifically that the texture repeats units are in texture repeats per face.

### PRIM_TEXGEN_PLANAR

* `integer PRIM_TEXGEN_PLANAR = 1`

Used with PRIM_TEXGEN to set the texture mapping mode, specifically that the texture repeats units are in texture repeats per half meter. This is in contrast to the in-world editing tool, in which the planar texture scaling units are repeats per meter.

### PRIM_TEXT

* `integer PRIM_TEXT = 26`

Used to get or set the object's floating text.

### PRIM_TEXTURE

* `texture PRIM_TEXTURE = 17`

Used to get or set the Blinn-Phong diffuse texture settings of a prim's face.

### PRIM_TYPE

* `integer PRIM_TYPE = 9`

Gets or sets the of the prim and associated type .
|examples

### PRIM_TYPE_BOX

* `integer PRIM_TYPE_BOX = 0`

PRIM_TYPE_BOX is a parameter of PRIM_TYPE used to make prim into a box and to change specific properties that define the shape of that box.

### PRIM_TYPE_CYLINDER

* `integer PRIM_TYPE_CYLINDER = 1`

PRIM_TYPE_CYLINDER is a parameter of PRIM_TYPE used to make prim into a cylinder and to change specific properties that define the shape of that cylinder.

### PRIM_TYPE_PRISM

* `integer PRIM_TYPE_PRISM = 2`

PRIM_TYPE_PRISM is a parameter of PRIM_TYPE used to make prim into a prism and to change specific properties that define the shape of that prism.

### PRIM_TYPE_RING

* `integer PRIM_TYPE_RING = 6`

PRIM_TYPE_RING is a parameter of PRIM_TYPE used to make prim into a ring and to change specific properties that define the shape of that ring.

### PRIM_TYPE_SCULPT

* `integer PRIM_TYPE_SCULPT = 7`

PRIM_TYPE_SCULPT is a parameter of PRIM_TYPE used to make a prim into a sculpty of specific shape and type. 
Sculpted Prims: FAQ

### PRIM_TYPE_SPHERE

* `integer PRIM_TYPE_SPHERE = 3`

PRIM_TYPE_SPHERE is a parameter of PRIM_TYPE used to make prim into a sphere and to change specific properties that define the shape of that sphere.

### PRIM_TYPE_TORUS

* `integer PRIM_TYPE_TORUS = 4`

PRIM_TYPE_TORUS is a parameter of PRIM_TYPE used to make prim into a torus and to change specific properties that define the shape of that torus.

### PRIM_TYPE_TUBE

* `integer PRIM_TYPE_TUBE = 5`

PRIM_TYPE_TUBE is a parameter of PRIM_TYPE used to make prim into a tube and to change specific properties that define the shape of that tube.

### PROFILE_NONE

* `integer PROFILE_NONE = 0`

Disables script profiling.
|pa
|pb
|examples

### PROFILE_SCRIPT_MEMORY

* `integer PROFILE_SCRIPT_MEMORY = 1`

Enables script memory profiling, tracking the maximum amount of memory consumed while it is active.
|pa
|pb
|examples

### RAD_TO_DEG

* `float RAD_TO_DEG = 57.295779513082320876798154814105f`

When multiplied by, converts a value in radians to degrees. Precise value is 180/PI.
|examples
|events
|functions

### RCERR_CAST_TIME_EXCEEDED

* `integer RCERR_CAST_TIME_EXCEEDED = -3
|desc
|examples`

### RCERR_SIM_PERF_LOW

* `integer RCERR_SIM_PERF_LOW = -2
|desc
|examples`

### RCERR_UNKNOWN

* `integer RCERR_UNKNOWN = -1
|desc
|examples`

### RC_DATA_FLAGS

* `integer RC_DATA_FLAGS = 2
|desc
|examples`

### RC_DETECT_PHANTOM

* `integer RC_DETECT_PHANTOM = 1
|desc
|examples`

### RC_GET_LINK_NUM

* `integer RC_GET_LINK_NUM = 4
|desc
|examples`

### RC_GET_NORMAL

* `integer RC_GET_NORMAL = 1
|desc
|examples`

### RC_GET_ROOT_KEY

* `integer RC_GET_ROOT_KEY = 2
|desc
|examples`

### RC_MAX_HITS

* `integer RC_MAX_HITS = 3
|desc
|examples`

### RC_REJECT_AGENTS

* `integer RC_REJECT_AGENTS = 1
|desc
|examples`

### RC_REJECT_LAND

* `integer RC_REJECT_LAND = 8
|desc
|examples`

### RC_REJECT_NONPHYSICAL

* `integer RC_REJECT_NONPHYSICAL = 4
|desc
|examples`

### RC_REJECT_PHYSICAL

* `integer RC_REJECT_PHYSICAL = 2
|desc
|examples`

### RC_REJECT_TYPES

* `integer RC_REJECT_TYPES = 0
|desc
|examples`

### REGION_FLAG_ALLOW_DAMAGE

* `REGION_FLAG_ALLOW_DAMAGE`

This is a flag used with llGetRegionFlags to check if the region is entirely damage enabled.
|examples

### REGION_FLAG_ALLOW_DIRECT_TELEPORT

* `REGION_FLAG_ALLOW_DIRECT_TELEPORT`

This is a flag used with llGetRegionFlags to check if direct teleportation is allowed in the region.
|examples

### REGION_FLAG_BLOCK_FLY

* `REGION_FLAG_BLOCK_FLY`

This is a flag used with llGetRegionFlags to check if flying is disabled in the region.
|examples

### REGION_FLAG_BLOCK_TERRAFORM

* `REGION_FLAG_BLOCK_TERRAFORM`

This is a flag used with llGetRegionFlags to check if terraforming is disabled in the region.
|examples

### REGION_FLAG_DISABLE_COLLISIONS

* `REGION_FLAG_DISABLE_COLLISIONS`

This is a flag used with llGetRegionFlags to check if collisions have been disabled in the region.
|examples

### REGION_FLAG_DISABLE_PHYSICS

* `REGION_FLAG_DISABLE_PHYSICS`

This is a flag used with llGetRegionFlags to check if physics has been disabled in the region.
|examples

### REGION_FLAG_FIXED_SUN

* `REGION_FLAG_FIXED_SUN`

This is a flag used with llGetRegionFlags to check if the sun's position has been fixed in the region.
|examples

### REGION_FLAG_RESTRICT_PUSHOBJECT

* `REGION_FLAG_RESTRICT_PUSHOBJECT`

This is a flag used with llGetRegionFlags to check if llPushObject is restricted in the region.
|examples

### REGION_FLAG_SANDBOX

* `REGION_FLAG_SANDBOX`

This is a flag used with llGetRegionFlags to check if the region is a sandbox.
|examples

### REMOTE_DATA_CHANNEL

* `integer REMOTE_DATA_CHANNEL = 1
|desc
|examples`

### REMOTE_DATA_REPLY

* `integer REMOTE_DATA_REPLY = 3
|desc
|examples`

### REMOTE_DATA_REQUEST

* `integer REMOTE_DATA_REQUEST = 2
|desc
|examples`

### REVERSE

* `integer REVERSE = 0x04`

Reverses the direction of a texture animation, playing it from end to start.
|examples

### REZ_DAMAGE

* `integer REZ_DAMAGE = 8`

Sets the damage amount delivered by a prim on collision when the object is rezzed.

### REZ_DAMAGE_TYPE

* `integer REZ_DAMAGE_TYPE = 12`

Sets the damage type when rezzed to apply  when this prim collides with another object. Can match one of the DAMAGE_TYPE_* constants, be a custom damage type or be a repurposed damage field.

### ROTATE

* `integer ROTATE = 0x20`

Causes a texture animation to change the texture's rotation. Cannot be combined with SCALE.
|examples

### SCALE

* `integer SCALE = 0x40`

Causes a texture animation to change the texture's scale. Cannot be combined with ROTATE.
|examples

### SCRIPTED

* `integer SCRIPTED = 0x8`

If it is contained in the result of llDetectedType(), it means what was detected has at least one active script. If it is used as a filter of llSensor() or llSensorRepeat(), it will search for objects that has any script, which is doing anything in simulator just now.

### SIM_STAT_ACTIVE_SCRIPT_COUNT

* `integer SIM_STAT_ACTIVE_SCRIPT_COUNT = 12
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_AGENT_COUNT

* `integer SIM_STAT_AGENT_COUNT = 10
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_AGENT_MS

* `integer SIM_STAT_AGENT_MS = 7
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_AGENT_UPDATES

* `integer SIM_STAT_AGENT_UPDATES = 2
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_AI_MS

* `integer SIM_STAT_AI_MS = 26
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_ASSET_DOWNLOADS

* `integer SIM_STAT_ASSET_DOWNLOADS = 15
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_ASSET_UPLOADS

* `integer SIM_STAT_ASSET_UPLOADS = 16
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_CHILD_AGENT_COUNT

* `integer SIM_STAT_CHILD_AGENT_COUNT = 11
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_FRAME_MS

* `integer SIM_STAT_FRAME_MS = 3
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_IMAGE_MS

* `integer SIM_STAT_IMAGE_MS = 8
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_IO_PUMP_MS

* `integer SIM_STAT_IO_PUMP_MS = 24
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_NET_MS

* `integer SIM_STAT_NET_MS = 4
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_OTHER_MS

* `integer SIM_STAT_OTHER_MS = 5
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PACKETS_IN

* `integer SIM_STAT_PACKETS_IN = 13
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PACKETS_OUT

* `integer SIM_STAT_PACKETS_OUT = 14
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PCT_CHARS_STEPPED

* `integer SIM_STAT_PCT_CHARS_STEPPED = 0
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PHYSICS_FPS

* `integer SIM_STAT_PHYSICS_FPS = 1
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PHYSICS_MS

* `integer SIM_STAT_PHYSICS_MS = 6
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PHYSICS_OTHER_MS

* `integer SIM_STAT_PHYSICS_OTHER_MS = 20
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PHYSICS_SHAPE_MS

* `integer SIM_STAT_PHYSICS_SHAPE_MS = 19
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_PHYSICS_STEP_MS

* `integer SIM_STAT_PHYSICS_STEP_MS = 18
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_SCRIPT_EPS

* `integer SIM_STAT_SCRIPT_EPS = 21
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_SCRIPT_MS

* `integer SIM_STAT_SCRIPT_MS = 9
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_SCRIPT_RUN_PCT

* `integer SIM_STAT_SCRIPT_RUN_PCT = 25
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_SLEEP_MS

* `integer SIM_STAT_SLEEP_MS = 23
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_SPARE_MS

* `integer SIM_STAT_SPARE_MS = 22
|hvalue
|desc
|examples
|caveats`

### SIM_STAT_UNACKED_BYTES

* `integer SIM_STAT_UNACKED_BYTES = 17
|hvalue
|desc
|examples
|caveats`

### SMOOTH

* `integer SMOOTH = 0x010`

Causes a texture animation to move smoothly between frames, instead of instant changes.
|examples

### SQRT2

* `float SQRT2 = 1.4142135623730950488016887242097f`

The square root of two.
|examples
|events

### STATUS_BOUNDS_ERROR

* `integer STATUS_BOUNDS_ERROR = 1002
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_INTERNAL_ERROR

* `integer STATUS_INTERNAL_ERROR = 1999
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_MALFORMED_PARAMS

* `integer STATUS_MALFORMED_PARAMS = 1000
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_NOT_FOUND

* `integer STATUS_NOT_FOUND = 1003
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_NOT_SUPPORTED

* `integer STATUS_NOT_SUPPORTED = 1004
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_OK

* `integer STATUS_OK = 0
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_PHANTOM

* `integer STATUS_PHANTOM = 0x10`

This property (set FALSE by default) when set TRUE turns the object un-solid (objects and avatars can pass through it).

### STATUS_PHYSICS

* `integer STATUS_PHYSICS = 0x1`

This property (set FALSE by default) if set TRUE allows that the object is subject to and can offer physical interactions and forces.

### STATUS_ROTATE_X

* `integer STATUS_ROTATE_X = 0x2`

This property (set TRUE by default), if set FALSE, attempts to stop physical rotation on the objects local X axis.

### STATUS_ROTATE_Y

* `integer STATUS_ROTATE_Y = 0x4`

This property (set TRUE by default), if set FALSE, attempts to stop physical rotation on the objects local Y axis.

### STATUS_ROTATE_Z

* `integer STATUS_ROTATE_Z = 0x8`

This property (set TRUE by default), if set FALSE, attempts to stop physical rotation on the objects local Z axis.

### STATUS_TYPE_MISMATCH

* `integer STATUS_TYPE_MISMATCH = 1001
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STATUS_WHITELIST_FAILED

* `integer STATUS_WHITELIST_FAILED = 2001
|desc
|examples
|functions
|events
|cat1
|cat2
|cat3
|cat4
|self`

### STRING_TRIM

* `integer STRING_TRIM = 0x03`

Trim spaces off the beginning and the end. Equal to STRING_TRIM_HEAD | STRING_TRIM_TAIL 
|examples

### STRING_TRIM_HEAD

* `integer STRING_TRIM_HEAD = 0x01`

Trim spaces off the beginning
|examples

### STRING_TRIM_TAIL

* `integer STRING_TRIM_TAIL = 0x02`

Trim spaces off the end
|examples

### TARGETED_EMAIL_OBJECT_OWNER

* `integer TARGETED_EMAIL_OBJECT_OWNER = 2`

Causes the message to be sent to the owner of the calling object
|examples

### TEXTURE_BLANK

* `string TEXTURE_BLANK = "5748decc-f629-461c-9a36-a35a221fe21f"`

UUID for the "Blank" texture
|examples
|notes

### TEXTURE_MEDIA

* `string TEXTURE_MEDIA = "8b5fec65-8d8d-9dc5-cda8-8fdf2716e361"`

UUID for the "Default Media" texture
|examples
|notes

### TEXTURE_PLYWOOD

* `string TEXTURE_PLYWOOD = "89556747-24cb-43ed-920b-47caed15465f"`

UUID for the default "Plywood" texture

### TEXTURE_TRANSPARENT

* `string TEXTURE_TRANSPARENT = "8dcd4a48-2d37-4909-9f78-f7a9eb4ef903"`

UUID for "*Default Transparent Texture" in the library, also included with viewers.
|examples
|notes

### TOUCH_INVALID_FACE

* `TOUCH_INVALID_FACE`

Returned by llDetectedTouchFace when the touch position is not valid.
Specifically when...
* The avatar's viewer does not support face touch detection.
* The touch has moved off the surface of the prim.
* The triggering event is not a touch event.
|examples

### TOUCH_INVALID_TEXCOORD

* `TOUCH_INVALID_TEXCOORD`

Returned by llDetectedTouchUV and llDetectedTouchST when the touch position is not valid. 
|examples

### TOUCH_INVALID_VECTOR

* `TOUCH_INVALID_VECTOR`

Returned by llDetectedTouchPos, llDetectedTouchNormal, and llDetectedTouchBinormal when the touch position is not valid.

### TRAVERSAL_TYPE

* `integer TRAVERSAL_TYPE = 7`

Used in combination with one of the traversal type flags. The default is TRAVERSAL_TYPE_SLOW, other options are TRAVERSAL_TYPE_FAST and TRAVERSAL_TYPE_NONE. 
|examples

### TRUE

* `integer TRUE = 1`

Constant used to define the TRUE value in conditional structures or variables/constants in general. Usually it's used because it is more readable, indicating a boolean value instead a integer value (1). However, this is an arbitrary distinction in LSL which uses integers to represent Boolean values anyway. It is probably better to consider TRUE and FALSE as mnemonic constants for the integer values 1 and 0.

### TWO_PI

* `float TWO_PI = 6.283185307179586476925286766559f`

Two times PI. The number of radians in a full circle.
|examples
|events
|functions

### TYPE_FLOAT

* `integer TYPE_FLOAT = 2`

|pa
|pb
|examples

### TYPE_INTEGER

* `integer TYPE_INTEGER = 1`

|pa
|pb
|examples

### TYPE_INVALID

* `integer TYPE_INVALID = 0`

|pa
|pb
|examples

### TYPE_KEY

* `integer TYPE_KEY = 4`

|pa
|pb
|examples

### TYPE_ROTATION

* `integer TYPE_ROTATION = 6`

|pa
|pb
|examples

### TYPE_STRING

* `integer TYPE_STRING = 3`

|pa
|pb
|examples

### TYPE_VECTOR

* `integer TYPE_VECTOR = 5`

|pa
|pb
|examples

### URL_REQUEST_DENIED

* `URL_REQUEST_DENIED`

### URL_REQUEST_GRANTED

* `URL_REQUEST_GRANTED`

### VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY

* `integer VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY = 32`

slider between 0 (no deflection) and 1 (maximum strength)
-->

### VEHICLE_ANGULAR_DEFLECTION_TIMESCALE

* `integer VEHICLE_ANGULAR_DEFLECTION_TIMESCALE = 33`

exponential timescale for the vehicle to achieve full angular deflection
-->

### VEHICLE_ANGULAR_FRICTION_TIMESCALE

* `integer VEHICLE_ANGULAR_FRICTION_TIMESCALE = 17`

vector of timescales for exponential decay of angular velocity about the three vehicle axes
-->

### VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE

* `integer VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE = 35`

exponential timescale (in seconds) for the angular motor's effectiveness to decay toward zero
-->

### VEHICLE_ANGULAR_MOTOR_DIRECTION

* `integer VEHICLE_ANGULAR_MOTOR_DIRECTION = 19`

vector of angular velocity (in radian/second) that the vehicle will try to achieve
-->

### VEHICLE_ANGULAR_MOTOR_TIMESCALE

* `integer VEHICLE_ANGULAR_MOTOR_TIMESCALE = 34`

exponential timescale for the angular motor to achieve full power
-->

### VEHICLE_BANKING_EFFICIENCY

* `integer VEHICLE_BANKING_EFFICIENCY = 38`

slider between -1.00 (leans out of turns), 0 (no banking) and +1.00 (leans into turns). This parameter makes banking affect steering, not the other way around. Use vehicle angular motors to bank the vehicle.
-->

### VEHICLE_BANKING_MIX

* `integer VEHICLE_BANKING_MIX = 39`

slider between 0 (static banking) and 1 (dynamic banking)
-->

### VEHICLE_BANKING_TIMESCALE

* `integer VEHICLE_BANKING_TIMESCALE = 40`

exponential timescale for the banking behaviour to take full effect
-->

### VEHICLE_BUOYANCY

* `integer VEHICLE_BUOYANCY = 27`

slider between -1 (double gravity) and 1 (full anti-gravity)
-->

### VEHICLE_FLAG_BLOCK_INTERFERENCE

* `integer VEHICLE_FLAG_BLOCK_INTERFERENCE = 0x400`

When set, this flag prevents the vehicle you're sitting on from being pushed by an attachment you're wearing.
|example

### VEHICLE_FLAG_CAMERA_DECOUPLED

* `integer VEHICLE_FLAG_CAMERA_DECOUPLED = 0x200`

This flag only has an effect when steering a vehicle with mouselook. In other words, only when either VEHICLE_FLAG_MOUSELOOK_STEER or VEHICLE_FLAG_MOUSELOOK_BANK are also set. When it is in effect it has zero server-side consequences, except that a bit is set in the flags field in the vehicle's ObjectUpdate message sent from server to client. The client uses the flag as a hint for how to compute its mouselook camera orientation as vehicle moves under the seated avatar.
When the flag is NOT set the avatar's mouselook camera will move in the world-frame as the vehicle changes its own world-frame orientation. The avatar's mouselook camera is effectively at an offset relative to the vehicle's local-frame.
When the flag IS set the avatar's mouselook camera will be unaffected by the motion of the vehicle itself: it moves only in the world-frame according to user input.
|example
-->

### VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT

* `integer VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT = 0x010`

Hover at global height instead of height above ground or water. 
If you wanted to make a boat you should set the VEHICLE_FLAG_HOVER_WATER_ONLY flag, or if you wanted to drive a hover tank under water you would use the VEHICLE_FLAG_HOVER_TERRAIN_ONLY flag instead. Finally, if you wanted to make a submarine or a balloon you would use the VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT. 
The vehicle flags are independent of each other and that setting two contradictory flags will have undefined behavior. The flags are set using the script call llSetVehicleFlags.

### VEHICLE_FLAG_HOVER_TERRAIN_ONLY

* `integer VEHICLE_FLAG_HOVER_TERRAIN_ONLY = 0x008`

Makes the vehicle float over land.
If you wanted to make a boat you should set the VEHICLE_FLAG_HOVER_WATER_ONLY flag, or if you wanted to drive a hover tank under water you would use the VEHICLE_FLAG_HOVER_TERRAIN_ONLY flag instead. Finally, if you wanted to make a submarine or a balloon you would use the VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT. 
The vehicle flags are independent of each other and that setting two contradictory flags will have undefined behavior. The flags are set using the script call llSetVehicleFlags.

### VEHICLE_FLAG_HOVER_UP_ONLY

* `integer VEHICLE_FLAG_HOVER_UP_ONLY = 0x020`

### VEHICLE_FLAG_HOVER_WATER_ONLY

* `integer VEHICLE_FLAG_HOVER_WATER_ONLY = 0x004`

Makes the vehicle over water.
If you wanted to make a boat you should set the VEHICLE_FLAG_HOVER_WATER_ONLY flag, or if you wanted to drive a hover tank under water you would use the VEHICLE_FLAG_HOVER_TERRAIN_ONLY flag instead. Finally, if you wanted to make a submarine or a balloon you would use the VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT. 
The vehicle flags are independent of each other and that setting two contradictory flags will have undefined behavior. The flags are set using the script call llSetVehicleFlags.

### VEHICLE_FLAG_LIMIT_MOTOR_UP

* `integer VEHICLE_FLAG_LIMIT_MOTOR_UP = 0x040`

### VEHICLE_FLAG_LIMIT_ROLL_ONLY

* `integer VEHICLE_FLAG_LIMIT_ROLL_ONLY = 0x002`

### VEHICLE_FLAG_MOUSELOOK_BANK

* `integer VEHICLE_FLAG_MOUSELOOK_BANK = 0x100`

### VEHICLE_FLAG_MOUSELOOK_STEER

* `integer VEHICLE_FLAG_MOUSELOOK_STEER = 0x080`

### VEHICLE_FLAG_NO_DEFLECTION_UP

* `integer VEHICLE_FLAG_NO_DEFLECTION_UP = 0x001`

### VEHICLE_HOVER_EFFICIENCY

* `integer VEHICLE_HOVER_EFFICIENCY = 25`

slider between 0 (bouncy) and 1 (critically damped) hover behaviour
-->

### VEHICLE_HOVER_HEIGHT

* `integer VEHICLE_HOVER_HEIGHT = 24`

height the vehicle will try to hover above ground. Set to zero to disable hover.
-->

### VEHICLE_HOVER_TIMESCALE

* `integer VEHICLE_HOVER_TIMESCALE = 26`

Period of time (in seconds) for the vehicle to achieve its hover height
|examples

### VEHICLE_LINEAR_DEFLECTION_EFFICIENCY

* `integer VEHICLE_LINEAR_DEFLECTION_EFFICIENCY = 28`

slider between 0 (no deflection) and 1 (maximum strength)
-->

### VEHICLE_LINEAR_DEFLECTION_TIMESCALE

* `integer VEHICLE_LINEAR_DEFLECTION_TIMESCALE = 31`

exponential timescale for the vehicle to redirect its velocity to its x-axis
-->

### VEHICLE_LINEAR_FRICTION_TIMESCALE

* `integer VEHICLE_LINEAR_FRICTION_TIMESCALE = 16`

vector of timescales for exponential decay of linear velocity about the three vehicle axes

### VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE

* `integer VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE = 31`

exponential timescale (in seconds) for the linear motor's effectiveness to decay toward zero
-->

### VEHICLE_LINEAR_MOTOR_DIRECTION

* `integer VEHICLE_LINEAR_MOTOR_DIRECTION = 18`

Vector of linear velocity (in meters/second) that the vehicle will try to achieve.
May conflict with any active llTargetOmega set in the root prim and prevent vehicle turns. Call llTargetOmega with a gain of 0 to disable it.
|example
-->

### VEHICLE_LINEAR_MOTOR_OFFSET

* `integer VEHICLE_LINEAR_MOTOR_OFFSET = 20`

Used with llSetVehicleVectorParam to set the offset for where the linear motor is to be applied from the vehicle's center of mass.
If the vehicle does not set the VEHICLE_LINEAR_MOTOR_OFFSET, then it defaults to .

### VEHICLE_LINEAR_MOTOR_TIMESCALE

* `integer VEHICLE_LINEAR_MOTOR_TIMESCALE = 30`

exponential timescale for the vehicle to achieve its full linear motor velocity
-->

### VEHICLE_REFERENCE_FRAME

* `integer VEHICLE_REFERENCE_FRAME = 44`

Used to set the rotation of vehicle axes relative to local frame.

### VEHICLE_TYPE_NONE

* `integer VEHICLE_TYPE_NONE = 0`

Turns off vehicle support 
-->

### VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY

* `integer VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY = 36`

slider between 0 (bouncy) and 1 (critically damped) attraction of vehicle's z-axis to orient to the world's z axis (up)
-->

### VEHICLE_VERTICAL_ATTRACTION_TIMESCALE

* `integer VEHICLE_VERTICAL_ATTRACTION_TIMESCALE = 37`

exponential timescale (in seconds) for the vehicle to align its z-axis to the world z-axis
-->

### VERTICAL

* `integer VERTICAL = 0`

Constant to indicate that the orientation of the capsule for a Pathfinding character is vertical.
|examples

### ZERO_ROTATION

* `ZERO_ROTATION`

Represents a rotation that causes no change, that is, an identity rotation. The default value for a variable of rotation type.
|examples
|functions
|events
|cat2
|cat3
|cat4

### ZERO_VECTOR

* `ZERO_VECTOR`

The default value for a variable of vector type.

### {{#var:cname}}

* `{{#var:type}} {{#var:cname}} = 0x0`

Chat channel that broadcasts to all nearby users & objects. This channel is sometimes referred to as: open chat, local chat and public chat.
If used with a llRegionSayTo, it goes to the specified user or prim. Unlike private channels, the user's attachments do not receive the message.

### {{PAGENAMEE}}

* `integer {{PAGENAMEE}} = 1
|examples`

Simple vehicle that bumps along the ground, and likes to move along it’s local x-axis.
===Effects===
Setting the vehicle type to sled enables the vehicle system and additionally has the same effect of executing the following:
 // most friction for left-right, least for up-down
llSetVehicleVectorParam( VEHICLE_LINEAR_FRICTION_TIMESCALE, );
// no angular friction
llSetVehicleVectorParam( VEHICLE_ANGULAR_FRICTION_TIMESCALE, );
// no linear motor
llSetVehicleVectorParam( VEHICLE_LINEAR_MOTOR_DIRECTION, );
llSetVehicleFloatParam( VEHICLE_LINEAR_MOTOR_TIMESCALE, 1000.0 );
llSetVehicleFloatParam( VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE, 120.0 );
// no agular motor
llSetVehicleVectorParam( VEHICLE_ANGULAR_MOTOR_DIRECTION, );
llSetVehicleFloatParam( VEHICLE_ANGULAR_MOTOR_TIMESCALE, 1000.0 );
llSetVehicleFloatParam( VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE, 120.0 );
// no hover (but with timescale of 10 sec if enabled)
llSetVehicleFloatParam( VEHICLE_HOVER_HEIGHT, 0.0 );
llSetVehicleFloatParam( VEHICLE_HOVER_EFFICIENCY, 10.0 );
llSetVehicleFloatParam( VEHICLE_HOVER_TIMESCALE, 10.0 );
llSetVehicleFloatParam( VEHICLE_BUOYANCY, 0.0 );
// maximum linear deflection with timescale of 1 second
llSetVehicleFloatParam( VEHICLE_LINEAR_DEFLECTION_EFFICIENCY, 1.0 );
llSetVehicleFloatParam( VEHICLE_LINEAR_DEFLECTION_TIMESCALE, 1.0 );
// no angular deflection
llSetVehicleFloatParam( VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY, 0.0 );
llSetVehicleFloatParam( VEHICLE_ANGULAR_DEFLECTION_TIMESCALE, 10.0 );
// no vertical attractor (doesn’t mind flipping over)
llSetVehicleFloatParam( VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY, 1.0 );
llSetVehicleFloatParam( VEHICLE_VERTICAL_ATTRACTION_TIMESCALE, 1000.0 );
// no banking
llSetVehicleFloatParam( VEHICLE_BANKING_EFFICIENCY, 0.0 );
llSetVehicleFloatParam( VEHICLE_BANKING_MIX, 1.0 );
llSetVehicleFloatParam( VEHICLE_BANKING_TIMESCALE, 10.0 );
// default rotation of local frame
llSetVehicleRotationParam( VEHICLE_REFERENCE_FRAME, );
// remove these flags
llRemoveVehicleFlags( VEHICLE_FLAG_HOVER_WATER_ONLY
 | VEHICLE_FLAG_HOVER_TERRAIN_ONLY
 | VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT
 | VEHICLE_FLAG_HOVER_UP_ONLY );
// until banking is enabled, if ever)
llSetVehicleFlags( VEHICLE_FLAG_NO_DEFLECTION_UP
 | VEHICLE_FLAG_LIMIT_ROLL_ONLY
 | VEHICLE_FLAG_LIMIT_MOTOR_UP );

