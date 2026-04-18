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

### osAESEncrypt

- `list osAESEncrypt(string Secret, string plainText)`

### osAESEncryptTo

- `list osAESEncryptTo(string Secret, string plainText, string ivString)`

### osAgentSaveAppearance

- `key osAgentSaveAppearance(key agentId, string notecard)`
- `key osAgentSaveAppearance(key agentId, string notecard, integer includeHuds)`

Save an arbitrary avatar's appearance to a notecard in the prim's inventory. 
This includes body part data, clothing items and attachments. If a notecard with the same name already exists then it is replaced. 
The avatar must be present in the region when this function is invoked. 
The baked textures for the avatar (necessary to recreate appearance on the NPC) are saved permanently. 
The first variant will include HUDs, the second variant allows control that. incluceHuds 1 (TRUE) will include 0(FALSE) will not

### osAngleBetween

- `float osAngleBetween(vector a, vector b)`

returns a angle between 0 and PI

### osApproxEquals

- `integer osApproxEquals(float fa, float fb)`
- `integer osApproxEquals(vector va, vector vb)`
- `integer osApproxEquals(rotation ra, rotation rb)`
- `integer osApproxEquals(float fa, float fb, float margin)`
- `integer osApproxEquals(vector va, vector vb, float margin)`
- `integer osApproxEquals(rotation ra, rotation rb, float margin)`

Returns 1 (true) if the quantities or all their components do not differ by the margin value, or 1e-6 (0.000001), if margin is not provided. Returns 0 (false) otherwise.

### osAvatarName2Key

- `key osAvatarName2Key(string FirstName, string LastName)`

Returns an avatar's key, based on his/her first and last name.

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

### osAvatarType

- `integer osAvatarType(key avatarKey)`
- `integer osAvatarType(string avatarFirstName, string avatarLastName)`

Returns the type of a avatar in region:
* < 0 in case of error
* 0 if avatar not found in region
* 1 if it is a normal avatar
* 2 if it is a NPC

### osCauseDamage

- `osCauseDamage(key avatar, float damage)`

Implemented December 30,2009 by Revolution in GIT# 87959464c9db8948bed89909913400bc2eb7524d - Rev 11850
This is an updated version of Mantis 0003777. It allows for damage on collision, touch, etc.

### osCauseHealing

- `osCauseHealing(key avatar, float healing)`

This does the opposite of osCauseDamage. It gives health to the avatar.

### osCheckODE

- `integer osCheckODE()`

That it checks if physics engine is legacy ODE and returns 1 ( TRUE ) it is, or 0 ( FALSE ) if not.

### osClearInertia

- `osClearInertia()`

clears the effect of osSetInertia* functions. Link set total mass, center of mass and inertia will be the values estimated by default from the link set parts.
Caution ! Only supported by ubOde for now

### osClearObjectAnimations

- `integer osClearObjectAnimations()`

Clears all animations on the prim, returning how many it had running.

### osCollisionSound

- `osCollisionSound(string impact_sound, float impact_volume)`

Sets collision sound to impact_sound with specified volume.

### osConsoleCommand

- `integer osConsoleCommand(string command)`

This function allows an LSL script to directly execute a command to opensim's console. Even if the function is available, only administrators/gods can successfully execute it.
In addition, one can further restrict this function to only certain administrators/gods. See Threat level for more information on how to do this.
If the script owner does have the necessary permissions to call this function, then they can do anything someone with direct access to the command console could do, such as changing the avatar passwords, deleting sims, changing the terrain, etc.
This command represents the highest security threat of any OSSL function, giving it a threat level of Severe. 
Do not use or allow this function unless you are absolutely sure of what you're doing!

### osDetectedCountry

- `string osDetectedCountry(integer index)`

Returns a string that indicates the country in which the avatar is located.

### osDie

- `osDie(key objectID)`

Deletes an object depending on the target uuid.

### osDrawEllipse

- `string osDrawEllipse(string drawList, integer width, integer height)`

Appends an Ellipse drawing command to the string provided in drawList and returns the result.
The ellipse is drawn with the current pen size and color, with the specified width and height (in pixels), centered on a point which is (width/2) pixels to the right of the pen's current X position, and (height/2) pixels below the pen's current Y position. After the ellipse is drawn, the width and height values are added to the pen's X and Y position, respectively.

### osDrawFilledEllipse

- `string osDrawFilledEllipse(string drawList, integer width, integer height)`

Appends an FillEllipse drawing command to the string provided in drawList and returns the result.
The filled ellipse is drawn with the current pen size and color, with the specified width and height (in pixels), centered on a point which is (width/2) pixels to the right of the pen's current X position, and (height/2) pixels below the pen's current Y position. After the filled ellipse is drawn, the width and height values are added to the pen's X and Y position, respectively.

### osDrawFilledPolygon

- `string osDrawFilledPolygon(string drawList, list xpoints, list ypoints)`

Appends a FillPolygon drawing command to the string provided in drawList and returns the result. This fills in the interior of the specified polygon.
The polygon is drawn with the current pen size and filled with the current color. So (x[0],y[0]),(x[1],y[1]),(x[2],y[2]) would be an example of a polygon. T

### osDrawFilledRectangle

- `string osDrawFilledRectangle(string drawList, integer width, integer height)`

Appends a FillRectangle drawing command to the string provided in drawList and returns the result.
The filled rectangle is drawn with the current pen size and color, at the specified width and height (in pixels), with the upper left corner of the rectangle placed at the pen's current position. After the rectangle is drawn, the width and height values are added to the pen's X and Y position, respectively (that is, the pen is positioned at the lower right corner of the rectangle.

### osDrawImage

- `string osDrawImage(string drawList, integer width, integer height, string imageUrl)`

Appends an Image drawing command to the string provided in drawList and returns the result.
Retrieves an image specified by the imageUrl parameter and draws it at the specified height and width, with the upper left corner of the image placed at the pen's current position. After the image is drawn, the width and height values are added to the pen's X and Y position, respectively (that is, the pen's current position is set to the lower right corner of the image). 
If imageUrl points to an invalid location, an image type not supported by libgdi, or a non-image MIME type, nothing is drawn. If either or both of the width or height parameters are zero or negative, nothing is drawn, but the image is still retrieved.

### osDrawLine

- `string osDrawLine(string drawList, integer startX, integer startY, integer endX, integer endY)`
- `string osDrawLine(string drawList, integer endX, integer endY)`

Depending on the form, appends a LineTo drawing command, or MoveTo and LineTo commands, to the string provided in drawList and returns the result.
In the longer form, draws a line using the current pen size and color from to the coordinates indicated by startX and startY to the coordinates indicated by endX and endY.
In the shorter form, draws a line using the current pen size and color from the pen's current position to the coordinates indicated by endX and endY.
After the line is drawn, the pen's X and Y coordinates are set to endX and endY, respectively.

### osDrawPolygon

- `string osDrawPolygon(string drawList, list xpoints, list ypoints)`

*Appends a Polygon drawing command to the string provided in drawList and returns the result.
*The polygon is drawn with the current pen size and color on the x,y point pairs that comes from LSL list.
*It will be converted into the drawing command "Polygon x[0],y[0],x[1],y[1],x[2],y[2],...". See Drawing commands#Polygon to know what the command will actually do.

### osDrawRectangle

- `string osDrawRectangle(string drawList, integer width, integer height)`

Appends a Rectangle drawing command to the string provided in drawList and returns the result.
The outline of a rectangle is drawn with the current pen size and color, at the specified width and height (in pixels), with the upper left corner of the rectangle placed at the pen's current position. After the rectangle is drawn, the width and height values are added to the pen's X and Y position, respectively (that is, the pen is positioned at the lower right corner of the rectangle.

### osDrawResetTransform

- `string osDrawResetTransform(string drawList)`

Reset all transforms.

### osDrawRotationTransform

- `string osDrawRotationTransform(string drawList, float x)`

...

### osDrawScaleTransform

- `string osDrawScaleTransform(string drawList, float x, float y)`

...

### osDrawText

- `string osDrawText(string drawList, string text)`

Appends a Text drawing command to the string provided in drawList and returns the result.
The specified text will be drawn with the current pen color, using the currently defined font, size and properties (which default to regular 14-point Arial).
The text will be drawn with the upper left corner of the first glyph at the pen's current position (however, note that glyphs within the font may be defined to extend to the left of their origin point).
If you need to include a semicolon in the text to be displayed, you will need to directly manipulate the draw list string using the drawing commands rather than the dynamic texture convenience functions, then specify an alternate data delimiter in the extraParams parameter to the osSetDynamicTexture* functions. The convenience functions (including osDrawImage) are hardcoded to terminate each command with a semicolon.
The text may or may not be antialiased, depending on the system settings of the machine upon which the simulator is running. Furthermore, if the system is configured to use LCD subpixel antialiasing (e.g. ClearType), the text may have colored fringes on the smoothed pixels, which may result in a less than optimum image.
Please note that the pen position is not updated after this call.

### osDrawTranslationTransform

- `string osDrawTranslationTransform(string drawList, float x, float y)`

...

### osDropAttachment

- `osDropAttachment()`

Requires script to be granted PERMISSION_ATTACH, drops an attachment like a user-triggered attachment drop.

### osDropAttachmentAt

- `osDropAttachmentAt(vector pos, rotation rot)`

Requires script to be granted PERMISSION_ATTACH, drops an attachment at position pos with rotation rot

### osEjectFromGroup

- `integer osEjectFromGroup(key user)`

Eject the given user from the group the object is set to.
The object owner must have the right to eject users from the group the object is set to.
The group member who is ejected can be offline. The user gets an instant message, that he/she has been ejected from that group. 
The result is TRUE, if the user could be ejected, otherwise FALSE.

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

### osFormatString

- `string osFormatString(string format,list params)`

Return the string with parameters substituted into it. These parameters need to be incrementing numbers, starting at zero, and surrounded by single accolades (also known as curly brackets).

### osGetAgentCountry

- `string osGetAgentCountry(key avatarID)`

Returns a string that indicates the country in which an avatar is located.

### osGetAgentIP

- `string osGetAgentIP(key uuid);`

Requires: key uuid of agent to get IP address for.
Returns: string representing the IP address returned. 
Possible Exceptions thrown:
 System.Exception: OSSL Runtime Error: osGetAgentIP permission denied. Allowed threat level is VeryLow but function threat level is High.
Notes:
Unknown if this function requires a valid Detect event such as touch or collision. 
Unknown what is returned for IPv6. 
osGetAgentIP is always restricted to Administrators

### osGetAgents

- `list osGetAgents()`

Returns a list of all the agents names in the region.

### osGetApparentRegionTime

- `float osGetApparentRegionTime()`

Returns region time in seconds since midnight.

### osGetApparentRegionTimeString

- `string osGetApparentRegionTimeString(integer format24)`

Returns a string with current region sun hour. Will use 12 or 24 hour format if format24 is 0 or 1, respectible.

### osGetApparentTime

- `float osGetApparentTime()`

Returns parcel time in seconds since midnight. If parcel does not have own enviroment, region time is returned

### osGetApparentTimeString

- `string osGetApparentTimeString(integer format24)`

Returns a string with current parcel sun hour. 
Will use 12 or 24 hour format if format24 is 0 or 1, respectible. 
If parcel does not have own evironment, region hour is returned.

### osGetAvatarHomeURI

- `string osGetAvatarHomeURI(key avatarId)`

Returns an avatar's Home URI.

### osGetAvatarList

- `list osGetAvatarList()`

Returns a strided list of the UUID, position, and name of each avatar in the region except the owner.
This function is similar to osGetAgents but returns enough info for a radar.

### osGetCurrentSunHour

- `float osGetCurrentSunHour()`

Returns a float value of the current region sun hour (24 hour clock).

### osGetDrawStringSize

- `vector osGetDrawStringSize(string contentType, string text, string fontName, integer fontSize)`

Returns a vector containing the horizontal and vertical dimensions in pixels of the specified text, if drawn in the specified font and at the specified point size. The horizontal extent is returned in the .x component of the vector, and the vertical extent is returned in .y. The .z component is not used.
The contentType parameter should be "vector".
If the osSetFontSize() function has not been used, and neither the FontName nor FontProp commands have been added to the draw list, specify "Arial" as the font name, and 14 as the font size.

### osGetGender

- `string osGetGender(key id)`

Returns a string with one of the following values: "male", "female", or "unknown". 
This value is determined by the value selected for the avatar shape in the appearance dialog in the user's viewer. 
If that value cannot be found for any reason (avatar is not in the region, improperly formatted key, etc.), "unknown" is returned.

### osGetGridCustom

- `string osGetGridCustom(string key)`

Returns the value of the GridInfo key as a string.

### osGetGridGatekeeperURI

- `string osGetGridGatekeeperURI()`

Returns the current grid's Gatekeeper URI as a string. If HG is not configured, returns empty string.

### osGetGridHomeURI

- `string osGetGridHomeURI()`

Returns the current grid's home URI as a string. if HG is not configured, returns empty string

### osGetGridLoginURI

- `string osGetGridLoginURI()`

Returns the current grid's login URI as a string.

### osGetGridName

- `string osGetGridName()`
- `|`
- `ossl_example =<source lang="lsl">`
- `//`
- `// Example of osGetGridName()`
- `// returns the value of gridname = "Hippogrid" in OpenSim.ini under [GridInfo] section`
- `//`
- `default`
- `{`
- `state_entry()`
- `{`
- `llSay(0, "Grid Name = "+osGetGridName());`
- `}`
- `}`
- `</source>`

Returns the current grid's name as a string.

### osGetGridNick

- `string osGetGridNick()`

Returns the current grid's nickname as a string.

### osGetHealRate

- `float osGetHealRate(key avatar)`

Gets the current automatic healing rate in % per second.
Default heal rate is now around 0.5% per second. 
A value of zero can disable automatic heal, current maximum value is 100 % per second.

### osGetHealth

- `float osGetHealth(key avatar)`

Gets an avatars health by key and returns the value as a float.

### osGetInertiaData

- `list osGetInertiaData()`

Caution ! Only supported by ubOde for now. 
This fonction retrun a list of inertia data.
 [
 float mass, // the total mass of the linkset
 vector center, // the center of mass offset relative to root prim
 vector Idiag, // diagonal elements of inertia
 vector Ioffdiag // off diagonal elements of inertia
 ]
Mass maybe -1 if inertia data is invalid or not avaiable

### osGetInventoryDesc

- `string osGetInventoryDesc(string itemName_or_itemId)`

Returns a string that is the description of inventory item with id "itemName_or_itemId" if that parameter is a valid key or with that name if not.

### osGetInventoryItemKey

- `key osGetInventoryItemKey(string name)`
- `key osGetLinkInventoryItemKey(integer linkNumber, string name)`

Returns id(key) of a inventory item within a prim inventory. If name is not unique result maybe unpredictable. Note that unlike llGetInventoryKey, this function returns the item ID, not ID of its asset.. Returns NULL_KEY if the item is not found or Owner has no rights

### osGetInventoryItemKeys

- `list osGetInventoryItemKeys(integer type)`
- `list osGetLinkInventoryItemKeys(integer linkNumber, integer type)`

Return a list of the items UUIDs by type (or INVENTORY_ALL) located in the host or child prim prim inventory.
List ordering is arbitrary. Successive calls may return different orders. 
Note that unlike llGetInventoryKey, this function returns the item ID, not ID of its asset.

### osGetInventoryLastOwner

- `key osGetInventoryLastOwner(string itemName_or_itemId)`

Returns the id(key) of the last owner of inventory item with id "itemName_or_itemId" if that parameter is a valid key or with that name if not.

### osGetInventoryName

- `string osGetInventoryName(key itemId)`

Returns a string that is the name of inventory item

### osGetInventoryNames

- `list osGetInventoryNames(integer type)`

Return a list of items names by type (or INVENTORY_ALL) located in the prim inventory.
List ordering is arbitrary. Successive calls may return different orders.

### osGetLastChangedEventKey

- `key osGetLastChangedEventKey()`

### osGetLinkInventoryDesc

- `string osGetLinkInventoryDesc(integer linkNumber, string itemNameorid)`

Return the description of an item located in a child prim inventory.

### osGetLinkInventoryKey

- `key osGetLinkInventoryKey(integer linkNumber, string name)`

Returns id(key) of a inventory item asset within a prim inventory. If name is not unique result maybe unpredictable. This function extends llGetInventoryKey( string name ) to links. Returns NULL_KEY if the item is not found or Owner has no rights

### osGetLinkInventoryName

- `string osGetLinkInventoryName(integer linkNumber, key itemId)`

Return the name of an item located in a child prim inventory.

### osGetLinkInventoryNames

- `list osGetLinkInventoryNames(integer linkNumber, integer type)`

Return a list of items names by type (or INVENTORY_ALL) located in a child prim inventory.
List ordering is arbitrary. Successive calls may return different orders.

### osGetLinkNumber

- `integer osGetLinkNumber(string name)`

returns the link number of the prim or sitting avatar with name "name" on the link set or -1 if the name is not found.
* if names are not unique, the one with lower link number should be return
* names "Object" and "Primitive" are ignored

### osGetLinkPrimitiveParams

- `list osGetLinkPrimitiveParams(integer linknumber, list rules)`

Returns the primitive parameters for the linkset prim or prims specified by linknumber. It is possible to use the linkset constants (e.g. LINK_SET, LINK_ALL_CHILDREN) in place of a specific link number, in which case the requested parameters of each relevant prim are concatenated to the end of the list. Otherwise, the usage is identical to llGetPrimitiveParams().

### osGetLinkSitActiveRange

- `float osGetLinkSitActiveRange(integer linkNumber)`

returns the sit active range of the selected prim, see osSetLinkSitActiveRange
* linkNumber: the link number of the prim, LINK_THIS or LINK_ROOT
* range > 0: if a avatar if far from the prim by more than that value, a sit request is silent ignored
* range == 0: disables this limit. Region default is used. Current that is unlimited if a sit target is set or physics can sit the avatar, otherwise 10m
* range < 0: sits are disabled. Requests are silently ignored
if link number is invalid it returns -2147483648 (int min value)

### osGetLinkStandTarget

- `vector osGetLinkStandTarget(integer linkNumber)`

Returns the stand target set on the prim see osSetLinkStandTarget.
* linkNumber: the link number of the prim, LINK_THIS or LINK_ROOT
If return is vector the stand target is disabled. Default stand offset and login are used.
It will also return if linkNumber is invalid.

### osGetMapTexture

- `key osGetMapTexture()`

Returns the UUID of the map texture of the current region.

### osGetNotecard

- `string osGetNotecard(string name)`

This function directly reads the entire contents of a notecard if it exists within the task inventory, and dumps it into a string. It skips the dataserver event, thereby reducing code complexity.

### osGetNotecardLine

- `string osGetNotecardLine(string name, integer line)`

This function directly reads a line of text from the specified notecard, if it exists within the task inventory, and returns the text as a string. It skips the dataserver event, thereby reducing code complexity.

### osGetNPCList

- `list osGetNPCList()`

Returns a strided list of the UUID, position, and name of each NPC in the region. Only available after 0.9 Commit # e53f43, July 26,2017 
This function is similar to OsGetAvatarList.

### osGetNumberOfAttachments

- `list osGetNumberOfAttachments(key avatar, list attachmentPoints);`

Returns a strided list of the specified attachment points and the number of attachments on those points.

### osGetNumberOfNotecardLines

- `integer osGetNumberOfNotecardLines(string name)`

This function directly reads how many lines a notecard has if the specified notecard exists within the task inventory, bypassing the dataserver event to reduce code complexity.

### osGetParcelDetails

- `osGetParcelDetails(key parcelID, list rules)`

This function is like [http://wiki.secondlife.com/wiki/LlGetParcelDetails llGetParcelDetails], but using parcel global id (parcelID) instead of position in region.

### osGetParcelDwell

- `integer osGetParcelDwell(vector pos)`

This function allows you to get parcel dwell.
Alternatively you can also use PARCEL_DETAILS_DWELL with the function llGetParcelDetails.

### osGetParcelID

- `osGetParcelID()`

This function returns the parcel global id (parcelID) of the parcel where host prim is.

### osGetParcelIDs

- `osGetParcelIDs()`

This function returns a list of the parcel global ids of all parcels in region.

### osGetPhysicsEngineName

- `string osGetPhysicsEngineName()`

This function returns a string containing the name and version number of the physics engine.

### osGetPhysicsEngineType

- `string osGetPhysicsEngineType()`

This function returns a string containing the name of the Physics Engine.

### osGetPrimCount

- `integer osGetPrimCount()`
- `integer osGetPrimCount(key objectID)`

returns the number of prims of the current linkset or of the linkset that includes a prim with UUID objectID.
Unlike ll* versions, does not count sitting avatars and does work on attachments.

### osGetPrimitiveParams

- `list osGetPrimitiveParams(key primId, list rules)`

* Gets the parameters for the prim specified by primId according to rules.
* This function has the same behave as llGetPrimitiveParams except you can specify target prim anywhere in the scene.
* For general information about rules, see [http://wiki.secondlife.com/wiki/LlGetPrimitiveParams llGetPrimitiveParams in SecondLife Wiki].
* If there is prim with id primId in the scene, or the owner of the target prim is different from the owner of the scripted prim, it will fail without error.

### osGetPSTWallclock

- `float osGetPSTWallclock()`

returns the current PST or PDT time in seconds since midnight

### osGetRegionMapTexture

- `key osGetRegionMapTexture(string regionNameOrID)`

This function retrieves the key of the texture used to represent a region on the world map. regionNameOrID can be the region UUID or its name. If empty string, will return the current region map texture key, but in that case you should use osGetMapTexture().

### osGetRegionSize

- `vector osGetRegionSize()`

Returns the size of the region in meters.
Usually this function returns: 
However, when called in a var/mega region it returns the size of the entire simulator.

### osGetRegionStats

- `list osGetRegionStats()`

Returns a list of float values representing a number of region statistics (many of the values shown in the "Stats Bar" of LL-based clients). Provides similar functionality to llGetRegionFPS() and llGetRegionTimeDilation(), but returns 21 statistics simultaneously.
The elements in the list may be referred to by the following new LSL constants:

### osGetRezzingObject

- `key osGetRezzingObject()`

Get the key of the object that rezzed this object.
Will return NULL_KEY if rezzed by agent or otherwise unknown source.
Should only be reliable inside the on_rez event.

### osGetScriptEngineName

- `string osGetScriptEngineName()`

Returns the name of the script engine which is currently enabled on the server.

### osGetSimulatorMemory

- `integer osGetSimulatorMemory();`

Implemented December 12,2009 by Adam Frisby in GIT# 87e89efbf9727b294658f149c6494fd49608bc12 - Rev 11700

### osGetSimulatorMemoryKB

- `integer osGetSimulatorMemoryKB();`

### osGetSimulatorVersion

- `string osGetSimulatorVersion()`

This function returns a string containing the current simulator version.

### osGetSitActiveRange

- `float osGetSitActiveRange()`

returns the sit active range of the prim see osSetSitActiveRange 
* range > 0: if a avatar if far from the prim by more than that value, a sit request is silent ignored
* range == 0: disables this limit. Region default is used. Current that is unlimited if a sit target is set or physics can sit the avatar, otherwise 10m
* range < 0: sits are disabled. Requests are silently ignored

### osGetSitTargetPos

- `vector osGetSitTargetPos()`

Return the sit target location as set by llSitTarget.

### osGetSitTargetRot

- `rotation osGetSitTargetRot()`

Return the sit target rotation as set by llSitTarget.

### osGetSittingAvatarsCount

- `integer osGetSittingAvatarsCount()`
- `integer osGetSittingAvatarsCount(key objectID)`

returns the number of sitting avatars on the current linkset or on the linkset that includes a prim with UUID objectID.

### osGetStandTarget

- `vector osGetStandTarget()`

Returns the stand target set on the prim see osSetStandTarget.
If return is vector the stand target is disabled. Default stand offset and login are used.

### osGetSunParam

- `float osGetSunParam(string param)`

NOTE : This function should not be used in 0.9.2.0. It did depend on Sun module, removed on 0.9.2. This function did replace the deprecated OsSunGetParam function. 
Since version 0.9.2.0 parameter "day_length" will return the same as llGetDayLength(), ie, the day length on the prim location. Other parameters return fixed dummy values.

### osGetTerrainHeight

- `float osGetTerrainHeight(integer x, integer y)`

NOTE&nbsp;: This function replaces the deprecated OsTerrainGetHeight function.

### osGetWindParam

- `float osGetWindParam(string plugin, string param)`

*Gets the value of param property for plugin module.

### osGiveLinkInventory

- `osGiveLinkInventory(integer linkNumber, key destination, string inventory)`

Give an item located in a child prim inventory.

### osGiveLinkInventoryList

- `osGiveLinkInventoryList(integer linkNumber, key destination, string category, list inventory)`

Give a group of items located in a child prim inventory.

### osGrantScriptPermissions

- `osGrantScriptPermissions(key allowed_key, string function)`

Dynamically allow ossl execution to owner/creator/group by function name.

### osInviteToGroup

- `integer osInviteToGroup(key user)`

Invite the given user to the group the object is set to. 
The object must have a group set and can not be group owned. 
The object owner must have the right to invite new users to the group the object is set to. 
The user with the given key has to be online in that region. 
The user gets a normal group invitation, showing the owner of the object as sender. The invitation can be accepted or rejected and the user can open the corresponding group window. 
Returns TRUE (1), if the invitation could be sent, otherwise FALSE (0). 
Since version 0.9.2, it will return 2 if user is already member of the group.

### osIsNotValidNumber

- `integer osIsNotValidNumber(float d)`

Returns 0 (false) if d is a valid float, else returns: 
1 - if it is a NaN 
2 - if it is a Negative Infinity 
3 - if it is a Positive Infinity

### osIsNpc

- `integer osIsNpc(key npc)`

Returns NPC status on the provided key
* Returns TRUE (1) / FALSE (0) if key provided is an NPC
* Returns FALSE (0) if the key provided doesn't exist in the scene.

### osIsUUID

- `integer osIsUUID(string thing)`

Returns 1 if the supplied string can be converted to key (uuid), returns 0 otherwise.

### osKey2Name

- `string osKey2Name(key id)`

Returns the avatar's name, based on their UUID.

### osKickAvatar

- `void osKickAvatar(string FirstName,string SurName, string alert)`
- `void osKickAvatar(key agentId, string alert)`

Kicks the selected avatar, closing its connection.
Agent key argument version added February 20, 2019

### osLinkParticleSystem

- `osLinkParticleSystem(LSL_Integer linknumber, LSL_List rules)`

### osList2Double

- `float osList2Double(list src, integer index)`

Caution! This function no not exist in OpenSimulator source code ...

### osListAsInteger

- `integer osListAsInteger(list src, integer index)`
- `float osListAsFloat(list src, integer index)`
- `string osListAsString(list src, integer index)`
- `vector osListAsVector(list src, integer index)`
- `rotation osListAsRotation(list src, integer index)`

Return the element at index as integer, float, string, vector or rotation. Index must me >= 0 and the element on at that position must be of the requested type. Because of this restrictions, This should be a bit faster than the llList2* functions

### osListenRegex

- `integer osListenRegex(integer channelID, string name, key ID, string msg, integer regexBitfield)`

Allows the server to filter listen events by regular expressions. name or message parameters can be regular expressions, these are behaviours are controlled via the regexBitField parameter using the constants OS_LISTEN_REGEX_NAME and OS_LISTEN_REGEX_MESSAGE.
If the regex strings are invalid, an error will be shouted on the debug channel.

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

### osLoadedCreationDate

- `string osLoadedCreationDate()`

*This function returns a string containing the date that a sim was first created. An example of the string returned is "Monday, December 07, 2009".
* It will return empty string if the region hasn't been created by oar import, or the region uses SQLite for region database.

### osLoadedCreationID

- `string osLoadedCreationID()`

* This function returns a string containing the UUID that a sim was originally created with.
* It will return empty string if the region hasn't been created by oar import, or the region uses SQLite as region database.

### osLoadedCreationTime

- `string osLoadedCreationTime()`

*This function returns a string containing the time that a sim was first created. An example of the string returned is "2:06:48 AM". 
* It will return empty string if the region hasn't been created by oar import, or the region uses SQLite for region database.

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

### osMatchString

- `list osMatchString(string src, string pattern, integer start)`

This function returns a list containing the matches from the given string.

### osMax

- `float osMax(float a, float b)`

Returns the larger of two numbers. Wraps to system Math.Max()

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

### osMin

- `float osMin(float a, float b)`

Returns the smaller of two numbers. Wraps to the system Math.Min() function.

### osMovePen

- `string osMovePen(string drawList, integer x, integer y)`

Appends a MoveTo drawing command to the string provided in drawList and returns the result.
This moves the pen's location to the coordinates specified by the x and y parameters, without drawing anything.

### osNpcCreate

- `key osNpcCreate(string firstname, string lastname, vector position, string cloneFrom)`
- `key osNpcCreate(string firstname, string lastname, vector position, string cloneFrom, integer options)`

*Creates an NPC named firstname lastname at position from avatar appearance resource cloneFrom

### osNpcGetOwner

- `key osNpcGetOwner(key npc)`

Gets the NPC's owner's UUID

### osNpcGetPos

- `vector osNpcGetPos(key npc)`

Return the current position of the NPC.

### osNpcGetRot

- `rotation osNpcGetRot(key npc)`

Gets the rotation of the avatar. Only the rotation around the Z plane in Euler rotation (horizontal rotation) has any meaning.

### osNpcLoadAppearance

- `osNpcLoadAppearance(key npc, string notecard)`

Load appearance from a notecard. This notecard must contain appearance data created with one of the save appearance functions.

### osNpcLookAt

- `integer osNpcLookAt(key npckey, integer type, key targetkey, vector offset)`

Caution ! still experimental, subject to changes
* npckey : The key of the npc.
* type : the type of the lookat
* targetkey : a object or avatar target
* offset : a offset relative to that target in that target local coordinates, or if target is nullkey a GLOBAL position.
This sends a viewer lookat effect relative to that npc to all avatars in region. 
This will make those viewers turn the npc head and eyes to the target position plus offset, if the current head animation priority is lower than the viewers defined head movement priority, usually 1.
type defines what kind of event or attention. They have viewer defined priorities relative to each other
Only the one with higher priority will play.
type constants:
* NPCLOOKAT_NONE = 0; nothing
* NPCLOOKAT_IDLE = 1; mouse movements
* NPCLOOKAT_LISTEN = 2; listing to nearby chat
* NPCLOOKAT_FREELOOK = 3;
* NPCLOOKAT_RESPOND = 4; begin of typing
* NPCLOOKAT_HOVER = 5; mouse hovering on a object
* NPCLOOKAT_CONVERSATION = 6;
* NPCLOOKAT_SELECT = 7; object grabbed
* NPCLOOKAT_FOCUS = 8; focused on a object or point
* NPCLOOKAT_MOUSELOOK = 9; mouse look
* NPCLOOKAT_CLEAR = 10; should clear current one ?
What does happen to the npc is viewer dependent and also may also depend on the npc gender.
For example to set normal look forward like idle mouse 
 osNpcLookAt(npckey, NPCLOOKAT_IDLE, npckey, ); // (looks to npc position plus 2.5m on x that is its front direction)
function will return a integer < 0 on error
 -1 invalid type
 -2 could not parse npckey
 -3 npc not found on region
 -4 could not parse targetkey
 -5 target key is not null key, or there is no agent or object with that key in region

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

### osNpcSaveAppearance

- `key osNpcSaveAppearance(key npc, string notecard)`
- `key osNpcSaveAppearance(key npc, string notecard, integer includeHuds)`

Save the NPC's current appearance to a notecard in the prim's inventory. This includes body part data, clothing items and attachments. If a notecard with the same name already exists then it is replaced. The avatar must be present in the region when this function is invoked. The baked textures for the avatar (necessary to recreate appearance) are saved permanently. 
first variant will include huds on the save appearence. Second variant alloes control of that. incluceHuds 1 (TRUE) will include 0(FALSE) will not

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

### osOwnerSaveAppearance

- `key osOwnerSaveAppearance(string notecard)`
- `key osOwnerSaveAppearance(string notecard, integer includeHuds)`

Save the owner's current appearance to a notecard in the prim's inventory. 
This includes body part data, clothing items and attachments. 
If a notecard with the same name already exists then it is replaced. 
The owner must be present in the region when this function is invoked. 
The baked textures for the owner (necessary to recreate appearance on the NPC) are saved permanently. 
The first variant will include HUDs, the second variant allows control that. incluceHuds 1 (TRUE) will include 0(FALSE) will not

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

### osRegexIsMatch

- `integer osRegexIsMatch(string input, string pattern)`

Returns 1 if the input string matches the regular expression pattern. Wraps to Regex.IsMatch()

### osRegionNotice

- `osRegionNotice(string message)`
- `osRegionNotice(key agentID, string message)`

Sends a region notice to the entire current region.

### osRegionRestart

- `integer osRegionRestart(float seconds)`
- `integer osRegionRestart(float seconds, string message)`

Restarts a region after a specified timeout. Only estate managers and administrators can successfully execute this function.
The string in the second version of this function will be used in the warning messages sent to all users in-the region about the region restart instead of the default warning message.

### osRemoveLinkInventory

- `osRemoveLinkInventory(integer linkNumber, string name)`

Remove an item from a child prim inventory.

### osReplaceAgentEnvironment

- `integer osReplaceAgentEnvironment(key agentKey, integer transition, string daycycle)`

Forces a dayclycle on a agent. Will do nothing if the agent is using a viewer local environment 
* If parameter daycycle is NULL_KEY or "", agent will see normal environment for parcel or region,
* daycycle can be a name of a daycycle asset on prim contents. If it is a UUID it can also be grid asset. 
* if return value is negative, it failed.
* transition should be the viewer transition time to the new one. May not work on most viewers.
 The errors returned are: 
 return 0 : Never 0 for now
 return 1 : if daycycle applied with success
 return -1 : Never -1
 return -2 : if no ossl rights
 return -3 : if daycycle asset not found
 return -4 : if agent not found
 return -5 : if fail to decode daycycle asset

### osReplaceParcelEnvironment

- `integer osReplaceParcelEnvironment(integer transition, string daycycle)`

Replaces parcel daycycle. 
* If parameter daycycle is NULL_KEY or "", parcel environment is removed,
* daycycle can be a name of a daycycle asset on prim contents. If it is a UUID it can also be grid asset. 
* if return value is negative, it failed.
* transition should be the viewer transition time to the new one. May not work on most viewers.
 The errors returned are: 
 return 0 : Never 0 for now
 return 1 : if daycycle applied with success
 return -1 : if "Parcel Owners May Override Environment" isn't checked
 (See menu "World/Region Details" on tab "Environment")
 return -2 : if parcel not found (This is a bad thingy)
 return -3 : if no rights to edit parcel
 return -4 : if daycycle asset not found
 return -5 : if fail to decode daycycle asset

### osReplaceRegionEnvironment

- `integer osReplaceRegionEnvironment(integer transition, string daycycle, float daylenght, float dayoffset, float altitude1, float altitude2, float altitude3)`

Replaces region dayclycle. 
* If parameter daycycle is NULL_KEY or "", current environment is used as base,
* daycycle can be a name of a daycycle asset on prim contents. If it is a UUID it can also be grid asset. 
* daylenght in hours - if zero, current is used. Range 4 to 168
* dayoffset in hours - offset from UTC. Range -11.5 to 11.5. if outside range current is used
* altitudes in meters - defines environment transition altitudes 1 to 3 levels. Range 1 to 4000. If 0, current is used. Please keep them sorted ( 1 < 2 < 3)
* if return value is negative, it failed.
* transition should be the viewer transition time to the new one. May not work on most viewers.
 The errors returned are: 
 return 0 : Never 0 for now
 return 1 : if daycycle applied with success
 return -1 : never -1, it is on parcel only
 return -2 : never -2, it is on parcel only
 return -3 : if no estate rights
 return -4 : if daycycle asset not found
 return -5 : if fail to decode daycycle asset

### osReplaceString

- `string osReplaceString(string src, string pattern, string replace, integer count, integer start)`

This function is for regular expression-based string replacement. The count parameter specifies the total number of replacements to make where -1 makes all possible replacements.

### osRequestSecureURL

- `key osRequestSecureURL(list options)`

Requests one HTTPS:// url (opensim version 0.9 or over)
Option supported : "allowXss" - Add 'Access-Control-Allow-Origin: *' to response header

### osRequestURL

- `key osRequestURL(list options)`

Requests one HTTP:// url (opensim version 0.9 or over)
Option supported : "allowXss" - Add 'Access-Control-Allow-Origin: *' to response header

### osResetAllScripts

- `osResetAllScripts(integer AllLinkSet)`

Resets all the scripts on the same prim if AllLinkSet is FALSE( or 0) or on same linkset if AllLinkSet is TRUE ( or 1 )
This function can be heavy, and can have negative side effects due to the asynchronous nature of script engines.

### osResetEnvironment

- `integer osResetEnvironment(integer ParcelOrRegion, integer transition)`

Resets parcel or region environment. 
* if ParcelOrRegion == 1 parcel environment is removed, region will be used, else region environment is set to the default.
* transition should be the viewer transition time to the new one. May not work on most viewers.
* if return is negative the operation failed.
 The errors returned on region are: 
 return 0 : never 0 for now
 return 1 : if daycycle applied with success
 return -1 : never -1, it is on parcel only
 return -2 : never -2, it is on parcel only
 return -3 : if no rights to edit region
 The errors returned on parcel are: 
 return 0 : Never 0 for now
 return 1 : if daycycle applied with success
 return -1 : if "Parcel Owners May Override Environment" isn't checked
 (See menu "World/Region Details" on tab "Environment")
 return -2 : if parcel not found (This is a bad thingy)
 return -3 : if no rights to edit parcel

### osRevokeScriptPermissions

- `osRevokeScriptPermissions(key revoked_key, string function)`

Dynamically allow/disallow ossl execution to owner/creator/group by function name.

### osRound

- `float osRound(float value, integer ndigits)`

returns the value rounded to the number with a number if decimal places set by ndigits. ndigits = 0 is same as llRound(), max value is 15.

### osSetContentType

- `osSetContentType(key id, string type)`

Sets an arbitrary content return type for an [http://wiki.secondlife.com/wiki/LlRequestURL llRequestUrl()].
The threat level was upgraded to Severe as of commit #2c2b887c8a on December 11, 2018.

### osSetDynamicTextureData

- `key osSetDynamicTextureData(string dynamicID, string contentType, string data, string extraParams, integer timer)`

*Renders a dynamically created texture on the prim containing the script and returns the UUID of the newly created texture.
*If you use this feature, you have to turn on any cache. If not, you'll see complete white texture.

### osSetDynamicTextureDataBlend

- `key osSetDynamicTextureDataBlend(string dynamicID, string contentType, string data, string extraParams, integer timer, integer alpha)`

Renders a dynamically created texture on the faces of a prim containing the script, possibly blending it with the texture that is already set. Only use if all faces have same texture! 
. Returns UUID of the generated texture.

### osSetDynamicTextureDataBlendFace

- `key osSetDynamicTextureDataBlendFace(string dynamicID, string contentType, string data, string extraParams, integer blend, integer disp, integer timer, integer alpha, integer face)`

Renders a dynamically created texture on the face of a prim containing the script, possibly blending it with the texture that is already set for the face. Returns UUID of the generated texture.

### osSetDynamicTextureDataFace

- `key osSetDynamicTextureDataFace(string dynamicID, string contentType, string data, string extraParams, integer timer, integer face);`

...

### osSetDynamicTextureURL

- `string osSetDynamicTextureURL(string dynamicID, string contentType, string url, string extraParams, integer timer)`

*Renders a web texture on the prim containing the script and returns the UUID of the newly created texture. 
*If you use this feature, you have to turn on any cache. If not, you'll see complete white texture. Flotsam cache performs better than cenome cache(default).

### osSetDynamicTextureURLBlend

- `string osSetDynamicTextureURLBlend(string dynamicID, string contentType, string url, string extraParams, integer timer, integer alpha)`

### osSetDynamicTextureURLBlendFace

- `string osSetDynamicTextureURLBlendFace(string dynamicID, string contentType, string url, string extraParams, integer blend, integer disp, integer timer, integer alpha, integer face)`

### osSetEstateSunSettings

- `osSetEstateSunSettings(integer sunFixed, float sunHour)`

This function does nothing on 0.9.2. This function allowed for an estate owner or manager to change the sun settings for the entire estate.

### osSetFontName

- `string osSetFontName(string drawList, string fontName)`

Set the name of the font that will be used by osDrawText.

### osSetFontSize

- `string osSetFontSize(string drawList, integer fontSize)`

Appends a FontSize drawing command to the string provided in drawList and returns the result.
Sets the size of the font used by subsequent osDrawTextText() calls. The fontSize parameter represents the font height in points. 
Please note that the font height is given in points, not in pixels. The resulting size of the font in pixels may vary depending on the system settings, specifically the display system's "dots per inch" metric. A system set to 96dpi will produce differently sized text than a system set to 120dpi. If precise text size is required, consider using the osGetDrawStringSize() function to help calculate the proper fontSize value to use.
If a negative fontSize parameter is specified, any text subsequently added will be displayed upside down and to the right of the point of origin.
Please note that the pen position is not updated after this call.

### osSetHealRate

- `float osSetHealRate(key avatar, float healrate)`

Sets the automatic healing rate in % per second.
Default heal rate is now around 0.5% per second. 
A value of zero can disable automatic heal, current maximum value is 100 % per second.

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

### osSetPenCap

- `string osSetPenCap(string drawList, string direction, string type)`

*** This method works only on Windows for now. libgdi+ has a fake implementation and will not draw it. ***
Appends a PenCap drawing command to the string provided in drawList and returns the result.
This sets the pen's start or/and end cap to either "diamond", "arrow", "round", or default "flat" shape. It can set them in the "end" or "start" of the line, or "both". Possible values are (case insensitive):
Type:
*"arrow"
*"diamond"
*"round"
*"flat"
Direction:
*"start"
*"end"
*"both"

### osSetPenColor

- `string osSetPenColor(string drawList, string color)`
- `string osSetPenColor(string drawList, vector color)`
- `string osSetPenColor(string drawList, vector color, float alpha)`

* osSetPenColor(string drawList, string color) Appends a PenColor drawing command to the string provided in drawList and returns the result. 
This sets the pen's drawing color to either the specified [http://msdn.microsoft.com/en-us/library/aa358802.aspx named .NET color] [https://docs.microsoft.com/en-us/dotnet/api/system.windows.media.colors?view=windowsdesktop-6.0 named colors] or to a 32-bit color value (formatted as eight hexadecimal digits in the format aarrggbb, representing the eight-bit alpha, red, green and blue channels). 
For full opacity, use an alpha value of FF (e.g. FFFF0000 for red); for varying degrees of transparency, reduce the alpha value (e.g. 800000FF for semi-transparent blue). 
The color names and hexadecimal color representations are not case-sensitive. 
* osSetPenColor(string drawList, vector color) converts vector color to the hexadecimal color with a alpha of 1.0 (FF) and appends the drawing command.
* osSetPenColor(string drawList, vector color, float alpha) converts vector color and alpha to the hexadecimal color and appends the drawing command.
NOTE : This function replaces the deprecated OsSetPenColour function.

### osSetPenSize

- `string osSetPenSize(string drawList, integer penSize)`

Appends a PenSize drawing command to the string provided in drawList and returns the result.
This sets the pen size to a square of penSize pixels by penSize pixels. If penSize is an odd number, the pen will be exactly centered on the coordinates provided in the various drawing commands; if it is an even number, it will be centered slightly higher and to the left of the actual coordinates.

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

### osSetSoundRadius

- `void osSetSoundRadius(integer linknum, float radius)`

Establishes a hard cut-off radius for audibility of scripted sounds (both attached and triggered) in the specified prim of a linkset.

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

### osSetTerrainHeight

- `integer osSetTerrainHeight(integer x, integer y, float val)`

NOTE' : This function replaces the deprecated OsTerrainSetHeight function.
Sets terrain height X & Y Values. Returns TRUE(1) if success, FALSE(0) if failed
osTerrainFlush should be called after all the terrain-changes have been done to update Terrain Data.

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

### osSHA256

- `string osSHA256(string input)`

Generate a hash value (string input). Returns a string containing the calculated string input as lowercase.

### osSlerp

- `rotation osSlerp(rotation a, rotation b, float ratio);`

Slerp is shorthand for spherical linear interpolation, introduced by Ken Shoemake in the context of quaternion interpolation for the purpose of animating 3D rotation.
It refers to constant-speed motion along a unit-radius great circle arc, given the ends and an interpolation parameter between 0 and 1.
osSlerp Returns a rotation that is the spherical interpolation of a and b, according to ratio that can be from 0.0 (result is a) to 1.0 (result is b)

### osStopSound

- `osStopSound(integer linknum)`

Stop the sound playing in the specified prim or prims of a linkset

### osStringEndsWith

- `integer osStringEndsWith(string src, string start, integer ignore_case)`

Returns 1 if the string in src ends with the characters in start. Case is ignored if ignore_case is 1 otherwise the case of the characters matters.

### osStringIndexOf

- `integer osStringIndexOf(string src, string value, integer ignoreCase)`

Reports the zero-based index of the first occurrence of string value withing string scr. returns -1 if not found. It can compare ignoring case with ignoreCase TRUE(1) or considering case if FALSE(0);

### osStringLastIndexOf

- `integer osStringLastIndexOf(string src, string value, integer ignoreCase)`

Reports the zero-based index of the last occurrence of string value withing string scr. returns -1 if not found. It can compare ignoring case with ignoreCase TRUE(1) or considering case if FALSE(0);

### osStringRemove

- `string osStringRemove(string src, integer offset, integer count)`

...

### osStringReplace

- `string osStringReplace(string src, string oldvalue, string newvalue)`

Returns a string in which all occurrences of the string oldvalue in string src are replaced by string newvalue

### osStringStartsWith

- `integer osStringStartsWith(string src, string start, integer ignore_case)`

Returns 1 if the string in src starts with the characters in start. Case is ignored if ignore_case is 1 otherwise the case of the characters matters.

### osStringSubString

- `string osStringSubString(string src, integer offset)`
- `string osStringSubString(string src, integer offset, integer length)`

...

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

### osTeleportObject

- `integer osTeleportObject(key objectID, vector targetPos, rotation rot, integer flags)`

...
===== Arguments: =====
* objectID the id of the linkset to teleport
* targetPos target position in region local coords
* rot a rotation.
* flags
===== Flags: =====
* OSTPOBJ_NONE it is just 0
* OSTPOBJ_STOPATTARGET object is stopped at destination
* OSTPOBJ_STOPONFAIL stops at start point if tp fails (still does nothing)
* OSTPOBJ_SETROT the rotation is the final object rotation, otherwise is a added rotation

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

### osUnixTimeToTimestamp

- `string osUnixTimeToTimestamp(integer epoch);`

This function allows an input Unix time to be converted to an llGetTimeStamp() format. 
Please note that there will be no second fractions. 
This is because the implementation works with seconds only.

### osVecDistSquare

- `float osVecDistSquare(vector a, vector b)`

returns the square of norm of vector, or distance vector, (a - b), when expensive square root math operation is not needed. 
for example to check if distance is larger than 10, check if the square is larger than 100

### osVecMagSquare

- `float osVecMagSquare(vector a)`

returns the square of the magnitude of vector a. 
This saves a square root math operation that is relative slow, when is not needed. 
for example to check if magnitude is larger than 10, check if the square is larger than 100

### osVolumeDetect

- `osVolumeDetect(integer detect)`

If script is on root prim, it is like llVolumeDetect(). On child prims, it will turn just that prim a detector.

### osWindActiveModelPluginName

- `string osWindActiveModelPluginName()`

Gets active wind plugin name, specified by "wind_plugin" in OpenSim.ini ("SimpleRandomWind" or "ConfigurableWind").

