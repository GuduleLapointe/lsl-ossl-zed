# LSL Events

Source: tmp/opensim-git/OpenSim/Region/ScriptEngine/YEngine/MMRIEventHandlers.cs
Generated: 2025-01-07T14:25:29Z

### at_rot_target

- `at_rot_target(integer tnum, rotation targetrot, rotation ourrot)`

### at_target

- `at_target(integer tnum, vector targetpos, vector ourpos)`

### attach

- `attach(string id)`

### changed

- `changed(integer change)`

### collision

- `collision(integer num_detected)`

### collision_end

- `collision_end(integer num_detected)`

### collision_start

- `collision_start(integer num_detected)`

### control

- `control(string id, integer held, integer change)`

### dataserver

- `dataserver(string queryid, string data)`

### email

- `email(string time, string address, string subj, string message, integer num_left)`

### http_request

- `http_request(string request_id, string method, string body)`

### http_response

- `http_response(string request_id, integer status, list metadata, string body)`

### land_collision

- `land_collision(vector pos)`

### land_collision_end

- `land_collision_end(vector pos)`

### land_collision_start

- `land_collision_start(vector pos)`

### link_message

- `link_message(integer sender_num, integer num, string str, string id)`

### linkset_data

- `linkset_data(integer action, string name, string value)`

### listen

- `listen(integer channel, string name, string id, string message)`

### money

- `money(string id, integer amount)`

### moving_end

- `moving_end()`

### moving_start

- `moving_start()`

### no_sensor

- `no_sensor()`

### not_at_rot_target

- `not_at_rot_target()`

### not_at_target

- `not_at_target()`

### object_rez

- `object_rez(string id)`

### on_rez

- `on_rez(integer start_param)`

### path_update

- `path_update(integer type, list data)`

### region_cross

- `region_cross(vector newpos, vector oldpos)`

### remote_data

- `remote_data(integer event_type, string channel, string message_id, string sender, integer idata, string sdata)`

### run_time_permissions

- `run_time_permissions(integer perm)`

### sensor

- `sensor(integer num_detected)`

### state_entry

- `state_entry()`

### state_exit

- `state_exit()`

### timer

- `timer()`

### touch

- `touch(integer num_detected)`

### touch_end

- `touch_end(integer num_detected)`

### touch_start

- `touch_start(integer num_detected)`

### transaction_result

- `transaction_result(string id, integer success, string data)`

