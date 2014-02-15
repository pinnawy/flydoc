#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" IFLYTEK Education Division Architecture Team

@author:     shenghe <shenghe@iflytek.com>
@license:    (C) 2013, iFlyTEK CO.Ltd. All rights reserved.
              IFLYTEK Education Division Architecture Team
@version:    $Id$
"""
import os
import sys
import codecs
import shutil
import markdown
from jinja2 import Template
from common.logH import logger
from common.configH import ConfigH
from common.treeH import TreeH


settings = ConfigH.load(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
)


class Main:
    @staticmethod
    def main(argc, argv):
        rootFolder = os.path.dirname(os.path.realpath(__file__))

        # 获取默认文件夹
        inputFolder = os.path.join(rootFolder, "docs")
        outputFolder = os.path.join(rootFolder, "build")

        if argc == 2:
            inputFolder = argv[1]
        elif argc >= 3:
            inputFolder = argv[1]
            outputFolder = argv[2]

        if not os.path.isdir(inputFolder):
            logger.error("please input the correct folder.")
            return

        tplFolder = os.path.join(rootFolder, "themes", settings.get("themes", "default"))
        tpl = os.path.join(tplFolder, "doc.html")
        if not os.path.isfile(tpl):
            logger.error("the template file can't be found.")
            return

        tplContent = ""
        with open(tpl, "rb") as fs:
            tplContent = fs.read()

        # 获取待转换文档的目录树
        rooturl = settings.get("rooturl", ".")
        filters = settings.get("ignore", {"files": [], "folders": []})
        trees = TreeH.getTree(
            inputFolder,
            rooturl=rooturl,
            rootpath=outputFolder,
            filters=filters
        )

        staticsFolder = os.path.join(tplFolder, "statics")
        if os.path.isdir(staticsFolder):
            targetStaticsFolder = os.path.join(outputFolder, "statics")
            if os.path.isdir(targetStaticsFolder):
                shutil.rmtree(targetStaticsFolder)

            shutil.copytree(staticsFolder, targetStaticsFolder)

        Main.parse(trees, tplContent)

    @staticmethod
    def parse(trees, tplContent):
        for tree in trees:
            targetFolder = os.path.split(tree["output"])[0]
            if not os.path.isdir(targetFolder):
                os.makedirs(targetFolder)

            if tree["children"]:
                Main.parse(tree["children"], tplContent)

            if not os.path.isfile(tree["path"]):
                continue

            #读取markdown内容
            content = ""
            if settings.get("catalog", True) and tree["catalog"]:
                content = """
[CATALOG]
"""
            with open(tree["path"], "rb") as fs:
                content += fs.read()

            m2html = markdown.markdown(content, [
                'fenced_code',
                'codehilite(linenums=True, guess_lang=False)',
                u'toc(anchorlink=True, marker=[CATALOG], title=目录)',
                'tables',
                'abbr',
                'footnotes',
                'nl2br',
                'meta',
                'sane_lists'],
                safe_mode='escape',
                output_format="html5"
            )

            #根据内容渲染模版
            o = {
                "title": settings.get("title", ""),
                "description": settings.get("description", "%s created by flydoc" % tree["name"]),
                "author": settings.get("author", "flydoc"),
                "header": settings.get("header", {}),
                "filename": tree["name"],
                "createtime": tree["date"],
                "markdown": m2html,
                "links": settings.get("links", {}),
                "trees": trees
            }

            templateO = Template(tplContent)
            html = templateO.render(**o)

            #把渲染出的内容写入指定位置
            with codecs.open(tree["output"], "wb", "utf-8") as fs:
                fs.write(html)

if __name__ == '__main__':
    Main.main(len(sys.argv), sys.argv)
