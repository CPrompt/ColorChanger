#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

import json

theme_data = ""
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

        if color_key in theme_data:
            color_value = theme_data.get(color_key)
        else:
            color_value = default_color_value

        return(color_value)



'''
objColors = Colors()

# read the entire datafile
theme_data = objColors.read_json("theme1.json")


def get_key_value(color_key):

    if color_key in theme_data:
        color_value = theme_data.get(color_key)
    else:
        # if the called key does not exist or contain a value
        # return default value
        color_value = default_color_value

    return(color_value)
'''
