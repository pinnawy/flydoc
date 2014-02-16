#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

@author:     shenghe
@license:    (C) 2013, shenghe All rights reserved.
@version:    $Id$
"""
import sys
import os
import re
import simplejson
from logH import logger


class ConfigH:
    @staticmethod
    def load(configfile):
        if not os.path.isfile(configfile):
            logger.debug("%s don't found!" % configfile)
            return {}

        try:
            # remove all simgle line comments
            jsonStr = "{}"
            with open(configfile, "rb") as fh:
                jsonStr = fh.read()

                p = re.compile(r"\s+//[^\n|\r]*")
                jsonStr = p.sub("", jsonStr)
            return simplejson.loads(jsonStr)
        except Exception as e:
            logger.error(str(e))
        return {}

    @staticmethod
    def set(configfile, key, value):
        try:
            json = ConfigH.load(configfile)
            json[key] = value

            simplejson.dump(json, fp=open(configfile, "wb"))
        except Exception as e:
            logger.error(str(e))
            return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please input config file!")
    else:
        print("----------------get json --------------")
        configfile = sys.argv[1]
        print(ConfigH.load(configfile))
        # Config.set(configfile, "file", "test now !")
