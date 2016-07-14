#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

import json
import os

theme_file = ""
color_value = None
default_color_value = "#ffffff"

class Colors:


    # read the json file
    def read_json(self,theme_file):

        self.theme_file = theme_file

        with open(theme_file) as data_file:
            data = json.load(data_file)

        return(data)

    # ask for key and return value
    # if no key is found, return default value
    def get_key_value(self,color_key):

        #print(os.path.dirname(os.path.realpath(self.theme_file)))
        theme_data = self.read_json(self.theme_file)

        if color_key in theme_data:
            color_value = theme_data.get(color_key)
        else:
            color_value = default_color_value
        return(color_value)


objColor = Colors()
print(objColor.read_json('theme1.json'))
print(objColor.get_key_value('color3'))



