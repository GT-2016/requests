#!/usr/bin/python
# -*- coding: utf8 -*-
import random
import binascii
import time
import string

# 随机字符串生成
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))       # lVfo

# 10进制数组转普通字符串
def arr2str(arr):
    return ''.join(chr(x) for x in arr)

# 把10进制数组转为16进制字符串
def arr2hex(arr):
    h = ''
    for i in arr:
        a = hex(i)[2:]
        if len(a) < 2:
            h += ('0' * (2-len(a)) +a)
        else:
            h += a
    return h

# 把普通字符串转为10进制数组
def str2arr(str):
    arr = []
    for x in str:
        arr.append(ord(x))
    return arr

# 普通字符串转16进制字符串
def str2hex(str):
    return arr2hex(str2arr(str))

# 16进制字符串转10进制数组
def hex2arr(hex):
    list = []
    while len(hex) > 1:
        list.append(int(hex[0:2], 16))
        hex = hex[2:len(hex)]
    return list

# 16进制字符串转字符串
def hex2str(hex):
    str = ''
    while len(hex) > 1:
        str += chr(int(hex[0:2], 16))
        hex = hex[2:len(hex)]
    return str

def float2int(f):
    fs = str(f)
    fa = fs.split('.')
    return fa[0]+fa[1]

def encry_keyValue(keyValue):
    j = 0
    newKeyValue = []
    str1 = "g?ol0d!en@s7ec.1u8r$ityf*e#rr3*yw&a^y"
    str2 = "3g!#d34&fddf*d4adfd8)de+^dad*d57#daTga"
    str3 = "*dne71#dc&ia?yad>lad,ad3h*aducat3~da3)d"
    str4 = "-vdg9e*dqa1cF?Ka3,d3emca*^1p)u5i]ag2r*de"
    for i in range(len(keyValue)):
        # print 'i:',i
        if (i % 2) == 0:
            if (i % 5) == 0:
                newKeyValue.append(keyValue[i] ^ ord(str1[j]))
            else:
                newKeyValue.append(keyValue[i] ^ ord(str2[j]))
        else:
            if (i % 3) == 0:
                newKeyValue.append(keyValue[i] ^ ord(str3[j]))
            else:
                newKeyValue.append(keyValue[i] ^ ord(str4[j]))
        j += 1
        if j > 36:
            j = 0
    return newKeyValue
# hash之后的转为真实值
def hash2real(h):
    return arr2hex(encry_keyValue(hex2arr(h)))

def insertMysql(_id, i):
    str1 = 'INSERT INTO `authentication_info` VALUES (\''
    user_id = str(_id)
    user_name = 'node_wgd0%d'%i
    phone = user_name
    email = user_name
    user_type = '0'
    password = 'qtec@123'
    status = '0'
    t = time.time()
    t_len = len(float2int(t))
    root_key_id = str2hex(random_char(16))
    print('root_key_id（真实值）', root_key_id,'长度:', len(root_key_id))
    root_key_value = str2hex(float2int(t))+str2hex(random_char(32-t_len))
    print('安全网关root_key_value值（真实值）',root_key_value,'长度:', len(root_key_value))
    root_key_enc = arr2hex(encry_keyValue(hex2arr(root_key_value)))
    # print(u'数据库插入root_key_value值（hash之后的）:', root_key_enc,'长度:', len(root_key_enc))

    req_authkey_id = str2hex(random_char(16))
    print('req_authkey_id（真实值）', req_authkey_id,'长度:', len(req_authkey_id))
    req_authkey_value = str2hex(float2int(t))+str2hex(random_char(32-t_len))
    print('安全网关req_authkey_value值（真实值）', req_authkey_value,'长度:', len(req_authkey_value))
    req_authkey_enc = arr2hex(encry_keyValue(hex2arr(req_authkey_value)))
    # print('数据库插入req_authkey_enc值（hash之后的）:',req_authkey_enc,'长度:', len(req_authkey_enc))

    res_authkey_id = str2hex(random_char(16))
    print('res_authkey_id（真实值）', res_authkey_id,'长度:', len(req_authkey_id))
    res_authkey_value = str2hex(float2int(t))+str2hex(random_char(32-t_len))
    print('安全网关res_authkey_value值（真实值）', res_authkey_value, '长度:', len(res_authkey_value))
    res_authkey_enc = arr2hex(encry_keyValue(hex2arr(res_authkey_value)))
    # print('数据库插入res_authkey_enc值（hash之后的）:',res_authkey_enc,'长度:', len(res_authkey_enc))

    password_value = arr2hex(encry_keyValue(str2arr(password)))
    print(str1 + user_id + '\',\'' + user_name + '\',\'' + phone + '\',\'' + email + '\',\'' + user_type + '\',\'' + password_value + '\',0x' + root_key_id + ',0x' + root_key_enc + ',0x' + req_authkey_id + ',0x' + req_authkey_enc + ',0x' + res_authkey_id + ',0x' + res_authkey_enc + ',\'' + status + '\');')

if __name__ == "__main__":
    # 插入多少个用户，输入信息（id, 名称后缀中的数字node_wgd1）
    for i in range(1):
        insertMysql(20000+i, i)