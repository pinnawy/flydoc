#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

@author:     shenghe <shenghe@iflytek.com>
@license:    (C) 2013, shenghe All rights reserved.
@version:    $Id$
"""
import sys
import os
import time
import logging
from logging.handlers import RotatingFileHandler


class LogH:
    @staticmethod
    def getLogger(cfile=None, logname="default"):
        if cfile is None or not os.path.isfile(cfile):
            logfolder = os.path.join(
                os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                "logs"
            )

            if not os.path.isdir(logfolder):
                os.makedirs(logfolder)

            createtime = time.strftime('%Y%m%d%H', time.localtime(time.time()))
            logfile = os.path.join(logfolder, "%s.%s.log" % (logname, createtime))

            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

            hdlr = RotatingFileHandler(
                logfile,
                mode='a',
                maxBytes=10*1024*1024,
                backupCount=4
            )
            hdlr.setFormatter(formatter)

            slr = logging.StreamHandler(sys.stderr)

            logger = logging.getLogger()
            logger.addHandler(hdlr)
            logger.addHandler(slr)
            logger.setLevel(logging.INFO)
        else:
            logging.config.fileConfig(cfile)
            logger = logging.getLogger("root")

        return logger

logger = LogH.getLogger()

if __name__ == '__main__':
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")
