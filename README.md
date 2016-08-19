# Theme Manager for i3pystatus
A script that will allow you to easily change the color of each module.

To use this script, first it must be placed in your i3pystatus folder in your home directory.
(i.e. ~/.i3/i3pystatus/)
ONLY put the "colors" directory here.  The rest is for testing.

Once you place this in your i3pystatus directory, you can change your configuration files for i3pystatus color
variables. For instance:
	status.register("pulseaudio",
			color_unmuted = pulse_audio,
			format = "{volue}",
		       )

Now in our __init__.py file for the colors directory, we can set:
	pulse_audio = objColor.get_key_value("pulse_audio")

Lastly, in our theme that we declared in __init__.py we can add :
	{
		"pulse_audio" : "#458588"
	}


From this point on, we can create new theme files (standard json files) and change the theme that is being used in the __init__.py file for
colors.



