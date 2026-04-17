// Test LSL script
// Example osTeleportAgent Script

string Destination = "LBSA Plaza"; // your target destination here (SEE NEXT LINES) Can Be
vector LandingPoint = <128.0, 128.0, 50.0>; // X,Y,Z landing point for avatar to arrive at
vector LookAt = <0.0, 1.0, 0.0>; // which way they look at when arriving

default
{
	on_rez(integer start_param)
	{
		llResetScript();
	}

  changed(integer change) // something changed, take action
  {
    if(change & CHANGED_OWNER)
      llResetScript();
    else if (change & CHANGED_REGION_START) // that bit is set during a region restart
      llResetScript();
  }

  state_entry()
  {
    llWhisper(0, "LSL Test");
  }

  touch_start(integer num_detected)
  {
    key avatar = llDetectedKey(0);
    llRegionSayTo(avatar, 0,"Teleporting you to : "+Destination);
  }
}
