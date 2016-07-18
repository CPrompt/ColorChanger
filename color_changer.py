#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

import json
import sys

theme_file = ""
color_value = None
default_color_value = "#ffffff"

class Colors:


    # read the json file
    def read_json(self,theme_file):

        self.theme_file = theme_file

        try:
            with open(theme_file) as data_file:
                data = json.load(data_file)
                return(data)
        except IOError:
                print("File does not exist!")
                return(0)

    # ask for key and return value
    # if no key is found, return default value
    def get_key_value(self,color_key):

        theme_data = self.read_json(self.theme_file)

        try:
            if color_key in theme_data:
                color_value = theme_data.get(color_key)
                return(color_value)
            else:
                color_value = default_color_value
        except TypeError:
            print("No file!!!")

#        return(color_value)



