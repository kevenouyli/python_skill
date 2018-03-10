# -*- coding:UTF-8 -*-
import os,re
s = os.sep
root = s+'home'
# for rt, dirs, files in os.walk(root):
#     print(rt)
#     for f in files:
#         print ('ok',f)
#         fname = os.path.splitext(f)
#         new = fname[0] + 'b' + fname[1]
#         os.rename(os.path.join(rt,f),os.path.join(rt,new))
# #給所有文件加了后缀‘b’

for rt, dirs, files in os.walk(root):
    # print(rt)
    for f in files:
        # print('ok', f)
        fname = os.path.splitext(f)
        a=fname[0]

        strinfo = re.compile('.*b$')
        b = strinfo.match(a)
        if b is not None:
            print(dirs)
            print(a)

        # new = b + fname[1]
        # print(os.path.join(rt+new))


        # os.rename(os.path.join(rt, f), os.path.join(rt, new))
#给加了‘b’后缀的文件复原
# a='wordtoword.python'
# strinfo = re.compile('word\.')
# b = strinfo.sub('',a)
# print (b)
# #正则表达式测试
