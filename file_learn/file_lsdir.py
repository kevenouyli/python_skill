# -*- coding: utf-8 -*- 
import os

path='D:\迅雷下载'
def test(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print(path)
        if os.path.isdir(path):
            test(path)
if __name__ =='__main__':
    test(path)
