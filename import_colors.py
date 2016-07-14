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
"""

from color_changer import *

objColor = Colors()
print(objColor.read_json('theme1.json'))
print(objColor.get_key_value('color3'))
print(objColor.get_key_value('color2'))
print(objColor.get_key_value('color12'))
