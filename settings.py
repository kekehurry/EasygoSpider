#! /usr/local/bin/python3
# coding: utf-8
# __author__ = "Brady Hu"
# __date__ = 2017/10/16 16:11

import os

#爬虫参数设置

xy_name = "data.txt"

#下面设置文件存目录，不要设置在系统盘，不然会出现问题
#当前目录用"."表示，如"./example/"
filepath = r"./wushan/"
if not os.path.exists(filepath):
	os.makedirs(filepath)
filename = "wushan"

#爬取的间隔时间
sleeptime = 3600 #单位是秒，7200秒即为2小时
#下面这个设置每个qq号抓取的次数
fre = 80

#每次爬取方格的边长（单位：km）
edge = 1.1


#下面的参数不用设置
lng_delta = 0.01167*edge
lat_delta = 0.009*edge
#是否手动识别验证码，如需手动识别验证码，设置为True，否则设置为False，遇到验证码直接跳过
CAPTCHA_RECOGNIZ = False

#mail user
mail_host="smtp.qq.com"
mail_user="837082742@qq.com"
mail_pass="octczhomrehsbcif" 
