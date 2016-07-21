#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

"""
This is an example of how to use this class
Import the class
initialize the class
set the theme to be used (objColor.read_json('theme1.json')
output the color value where you want it
if the key or value do not exist, it will output the default value
default value is set to #ffffff (white)

make sure the theme file is in the same directory as the main script
"""

from colors.color_changer import *

objColor = Colors()
objColor.read_json('theme1.json')

cmus_color = objColor.get_key_value('color3')
pulse_color = objColor.get_key_value('color1')

print(cmus_color)
print(pulse_color)
#print(objColor.get_key_value('color2'))

# testing a key that does not exist
#print(objColor.get_key_value('color12'))
