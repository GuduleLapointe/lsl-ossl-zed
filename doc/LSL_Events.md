# LSL Events

Source: https://wiki.secondlife.com/wiki/Main_Page
Fetched: 2026-04-18T16:05:35Z

### at_rot_target

- `at_rot_target(integer handle, rotation targetrot, rotation ourrot)`

Result of llRotTarget library function call

### at_target

- `at_target(integer tnum, vector targetpos, vector ourpos)`

Result of library function call

### attach

- `attach(key id)`

Triggered in an object when the object attaches or detaches from agent.

### changed

- `changed(integer change)`

Various changes to the object/prim trigger this event.

### collision

- `collision(integer num_detected|p1_desc)`

Triggered while task is colliding with another task.

### collision_end

- `collision_end(integer num_detected|p1_desc)`

Triggered when task stops colliding with another task

### collision_start

- `collision_start(integer num_detected|p1_desc)`

Triggered when task starts colliding with another task

### control

- `control(key id|p1_desc, integer level, integer edge)`

Result of llTakeControls library function call and user input.

### dataserver

- `dataserver(key queryid, string data)`

Triggered when task receives asynchronous data

### email

- `email(string time, string address|p2_desc, string subject|p3_desc, string message|p4_desc, integer num_left)`

Triggered as a result of calling llGetNextEmail where there is a matching email in the email queue.

### experience_permissions

- `experience_permissions(key agent_id)`

The agent has approved an experience permissions request. This may be through interaction with the experience permission dialog or the experience profile, or automatically if the agent has previously approved the experience.

### experience_permissions_denied

- `experience_permissions_denied(key agent_id, integer reason)`

The agent has denied experience permission or generated under other cases.

### final_damage

- `final_damage(integer num_detected)`

This event is triggered after all on_damage events in all scripts and attachments have processed and damage has been applied to the avatar or distributed to all seated avatars.
All llDetected* functions that are normally available within a collision event are available while processing this event. Additionally the llDetectedDamage methods may be called while processing this event.

### game_control

- `game_control(key id, integer button_levels, list axes)`

Triggered when compatible viewer sends fresh GameControlInput message, but only for scripts on attachments or seat.

### http_request

- `http_request(key request_id, string method, string body)`

Triggered when task receives an HTTP request.

### http_response

- `http_response(key request_id, integer status, list metadata, string body|p4_desc)`

Triggered when task receives a response to one of its llHTTPRequest s

### land_collision

- `land_collision(vector pos)`

Triggered in the root when physical object or attached avatar is colliding with land

### land_collision_end

- `land_collision_end(vector pos)`

Triggered in the root when a physical object or attached avatar stops colliding with land

### land_collision_start

- `land_collision_start(vector pos)`

Triggered in the root when a physical object or attached avatar starts colliding with land

### link_message

- `link_message(integer sender_num, integer num, string str, key id)`

Triggered when the script receives a link message that was sent by a call to llMessageLinked. llMessageLinked is used to send messages from one script to another.

### linkset_data

- `linkset_data(integer action, string name, string value)`

The linkset_data event fires in all scripts in a linkset whenever the datastore has been modified through a call to one of the llLinksetData functions.

### listen

- `listen(integer channel, string name, key id|p3_desc, string message)`

Triggered by chat, use llListen to enable and filter

### money

- `money(key id, integer amount)`

Triggered when money is paid to the prim in the amount by id.

### moving_end

- `moving_end()`

Triggered when task stops moving

### moving_start

- `moving_start()`

Triggered when task begins moving

### no_sensor

- `no_sensor()`

Result of a call to llSensor or llSensorRepeat.

### not_at_rot_target

- `not_at_rot_target()`

Result of library function call

### not_at_target

- `not_at_target()`

Triggered if an object has not yet reached the target set by the call to llTarget.

### object_rez

- `object_rez(key id)`

Triggered when the object rezzes an object.

### on_damage

- `on_damage(integer num_detected)`

This event is triggered when damage has been inflicted on an avatar or task in the world but before damage has been applied or distributed.
All llDetected* functions that are normally available within a collision event are available while processing this event. Additionally the llDetectedDamage and llAdjustDamage methods may be called while processing this event.

### on_death

- `on_death()`

This event is triggered on all attachments worn by an avatar when that avatar's health reaches 0.

### on_rez

- `on_rez(integer start_param)`

Triggered when an object is rezzed (by script or by user). Also triggered in attachments when a user logs in, or when the object is attached from inventory.

### path_update

- `path_update(integer type, list reserved)`

Event description goes here.

### remote_data

- `remote_data(integer event_type|p1_desc, key channel, key message_id|p3_desc, string sender|p4_desc, integer idata|p5_desc, string sdata|p6_desc)`

Triggered by various calls.

### run_time_permissions

- `run_time_permissions(integer perm)`

Triggered when an agent grants run time permissions to this script.

### sensor

- `sensor(integer num_detected)`

Results from a call to either llSensor or llSensorRepeat.

### state_entry

- `state_entry()`

Triggered on any state transition and startup

### state_exit

- `state_exit()`

Triggered on a qualifying state transition.

### timer

- `timer()`

Repeats the code in the timer(). Result of the llSetTimerEvent library function call.

### touch

- `touch(integer num_detected|p1_desc)`

Triggered whilst an agent is clicking the task. It will continue to be triggered until the the prim/object is stopped being clicked (it triggers multiple times).
Triggered on touch start, each minimum event delay while held, and touch end.

### touch_end

- `touch_end(integer num_detected|p1_desc)`

Triggered when agent stops clicking on task

### touch_start

- `touch_start(integer num_detected)`

Triggered by the start of agent clicking on task

### transaction_result

- `transaction_result(key id, integer success, string data)`

Triggered when task receives asynchronous data

