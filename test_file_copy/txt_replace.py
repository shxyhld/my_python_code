#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import argparse

reload(sys)
sys.setdefaultencoding("utf-8")

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path')             #输入文件路径
parser.add_argument('-e', '--extend')           #文件扩展名
parser.add_argument('-s', '--srcStr')           #原字符串
parser.add_argument('-d', '--destStr')          #目标字符串

args = parser.parse_args()

pathStr = args.path
extendStr = args.extend
srcStr = args.srcStr
destStr = args.destStr

''' 采用输入参数的形式
if len(sys.argv) != 5:
    print('param is  error')
    exit()


pathStr = sys.argv[1]
extendStr = sys.argv[2]
srcStr = sys.argv[3]
destStr = sys.argv[4]
'''


def file_text_replace(file_name):
        with open(file_name,"r") as r:
            lines = r.readlines()
        with open(file_name,"w") as w:
            for l in lines:
                w.write(l.replace(srcStr,destStr))
        r.close()
        w.close()

def print_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir, topdown=True):
        for name in files:
            (shotname,extension) = os.path.splitext(name)
            if extension == extendStr:
                file_text_replace(os.path.join(root,name))

if __name__ == "__main__":
    print pathStr,extendStr,srcStr,destStr
    print_file_name(str(pathStr))
