#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import re

#-----------------------------------------------------------------------------
#   集合型を利用したフラグ管理
#   https://github.com/kds1024/set.git
#-----------------------------------------------------------------------------

allSet = {'1', '2', '3'}
onSet = set()

print('allSet->' + str(allSet))
print('onSet->' + str(onSet))

# ONのものを追加
onSet.add('1')
onSet.add('2')
print('onSet->' + str(onSet))

# allSetと差を取る
offSet = allSet - onSet

# allSetからonSetの差を取るとoffの集合が取れる
print('offSet->' + str(offSet))

