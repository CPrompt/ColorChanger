#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

"""

"""

from color_changer import *

objColors = Colors()

# read the entire datafile
theme_data = objColors.read_json("theme1.json")
print(theme_data)
print(objColors.get_key_value("color1"))
