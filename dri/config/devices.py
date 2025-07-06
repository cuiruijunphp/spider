#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
设备配置文件
包含PC、Android、iOS的各种User-Agent和机型配置
"""

# PC端User-Agent配置
PC_USER_AGENTS = [
    # Chrome浏览器
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    
    # Firefox浏览器
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
    
    # Edge浏览器
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    # Safari浏览器 (macOS)
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
    #
    # # Chrome浏览器 (macOS)
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    
    # # Linux系统
    # 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    # 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
]

# Chrome浏览器 (Windows) 120及以上版本
PC_USER_AGENTS += [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
]

# Android设备配置
ANDROID_DEVICES = [
    # 真实荣耀-uc浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; U; Android 14; zh-CN; ALP-AN00 Build/HONORALP-AN00T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/17.7.6.1407 Mobile Safari/537.36',
        'window_size': (370, 676)
    },
    # 真实荣耀-默认浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; ALP-AN00 Build/HONORALP-AN00T;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.38 SP-engine/2.76.0 languageType/0 bdh_dvt/0 bdh_de/0 bdh_ds/0 bdapp/1.0 (bdhonorbrowser; bdhonorbrowser) bdhonorbrowser/9.1.0.3 (P1 14) NABar/1.0',
        'window_size': (370, 664)
    },
    # 真实荣耀-谷歌浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        'window_size': (370, 778)
    },
    # 真实荣耀-360浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; ALP-AN00 Build/HONORALP-AN00T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36',
        'window_size': (370, 675)
    },
    # 真实荣耀-悟空浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; ALP-AN00 Build/HONORALP-AN00T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36 aid/6589 bytedancewebview/d8a21c6 JsSdk/2 NewsArticle/12.9.3 GoldBrowser/12.9.3 NetType/wifi',
        'window_size': (370, 683)
    },
    # 真实荣耀-百度浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; ALP-AN00 Build/HONORALP-AN00T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 Mobile Safari/537.36 SP-engine/2.81.0 matrixstyle/0 flyflow/6.59.0.30 lite baiduboxapp/6.59.0.30 (Baidu; P1 14) NABar/1.0',
        'window_size': (370, 698)
    },
    # 真实荣耀-qq浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; U; Android 14; zh-cn; ALP-AN00 Build/HONORALP-AN00T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.260 MQQBrowser/19.1 Mobile Safari/537.36',
        'window_size': (370, 662)
    },
    # 真实荣耀-夸克浏览器
    {
        'name': 'ALP-AN00',
        'user_agent': 'Mozilla/5.0 (Linux; U; Android 14; zh-Hans-CN; ALP-AN00 Build/HONORALP-AN00T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/7.13.6.861 Mobile Safari/537.36',
        'window_size': (370, 718)
    },
     # 真实华为-默认浏览器
    {
        'name': 'mate40',
        'user_agent': 'Mozilla/5.0 (Linux; Android 12; HarmonyOS; TAS-AL00; HMSCore 6.15.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.6.301 Mobile Safari/537.36',
        'window_size': (360, 633)
    },
     # 真实华为-夸克浏览器
    {
        'name': 'mate40',
        'user_agent': 'Mozilla/5.0 (Linux; U; Android 12; zh-Hans-CN; TAS-AL00 Build/HUAWEITAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 Quark/7.13.2.852 Mobile Safari/537.36',
        'window_size': (360, 686)
    },

    # 下面这些先注释掉
   # {
   #      'name': 'Samsung Galaxy S24',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Samsung Galaxy S23',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Samsung Galaxy S22',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Google Pixel 8',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Google Pixel 7',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'OnePlus 11',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Xiaomi 13',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; 2211133C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'OPPO Find X6',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; PEXM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'vivo X90',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; V2241A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Huawei P60',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 12; ALH-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Samsung Galaxy A54',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  {
   #      'name': 'Redmi Note 12',
   #      'user_agent': 'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
   #      'window_size': (412, 915)
   #  },
   #  { 'name': 'Huawei Pura 70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Pura 70 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Pura 70 Ultra', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei P60', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI P60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei P60 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI P60 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Nova 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Nova 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Mate 70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Mate 70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Mate 70 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Mate 70 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Mate 60', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI Mate 60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Huawei Mate 60 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI Mate 60 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Honor Play9C', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HONOR Play9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Honor Play9T', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HONOR Play9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Honor X60', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HONOR X60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Honor 400', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HONOR 400) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'vivo X200', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo X200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'vivo Y200GT', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo Y200GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'vivo S20', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Xiaomi 15', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; MI 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Redmi Note 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi Note 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Redmi Note 13', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; Redmi Note 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Redmi K80', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi K80) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Xiaomi 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; MI 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Redmi K70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi K70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
   #  { 'name': 'Xiaomi 13', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; MI 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) }

]

# iOS设备配置
IOS_DEVICES = [

    # 先注释掉生成的浏览器版本和OS版本

    # iPhone 13系列 - iOS 18.2
    # {
    #     'name': 'iPhone 13 (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },
    # {
    #     'name': 'iPhone 13 (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },
    # {
    #     'name': 'iPhone 13 mini (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (375, 812)
    # },
    # {
    #     'name': 'iPhone 13 mini (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (375, 812)
    # },
    # {
    #     'name': 'iPhone 13 Pro (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },
    # {
    #     'name': 'iPhone 13 Pro (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },
    # {
    #     'name': 'iPhone 13 Pro Max (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (428, 926)
    # },
    # {
    #     'name': 'iPhone 13 Pro Max (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (428, 926)
    # },
    #
    # # iPhone 14系列 - iOS 18.2
    # {
    #     'name': 'iPhone 14 (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14 (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14 Plus (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 14 Plus (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 14 Pro (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14 Pro (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14 Pro Max (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 14 Pro Max (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    #
    # # iPhone 15系列 - iOS 18.2
    # {
    #     'name': 'iPhone 15 (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15 (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15 Plus (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Plus (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Pro (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15 Pro (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15 Pro Max (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Pro Max (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    #
    # # iPhone 16系列 - iOS 18.2
    # {
    #     'name': 'iPhone 16 (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 16 (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 16 Plus (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 16 Plus (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 16 Pro (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 16 Pro (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 16 Pro Max (Safari)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 16 Pro Max (Chrome)',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    #
    # # 保留原有的部分配置作为备用
    # {
    #     'name': 'iPhone 15 Pro Max',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Pro Max',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/137.0.7151.107 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Pro Max',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 15 Pro',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 15 Plus',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 14 Pro Max',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 14 Pro',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (393, 852)
    # },
    # {
    #     'name': 'iPhone 14 Plus',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (430, 932)
    # },
    # {
    #     'name': 'iPhone 13 Pro Max',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (428, 926)
    # },
    # {
    #     'name': 'iPhone 13 Pro',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },
    # {
    #     'name': 'iPhone 13',
    #     'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (390, 844)
    # },


    {
        # 真实 version 默认浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
    {
        # 真实  CriOS 谷歌浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/137.0.7151.107 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
   {
        # 真实  QQ浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 MQQBrowser/19.1.7 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1',
        'window_size': (390, 659)
    },
   {
        # 真实  火狐浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/140.2 Mobile/15E148 Safari/605.1.15',
        'window_size': (390, 659)
    },
   {
        # 真实  夸克浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X; zh-cn) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20E252 Quark/7.13.2.2490 Mobile',
        'window_size': (390, 698)
    },
   {
        # 真实  uc浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X; zh-CN) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 UCBrowser/17.7.7.2646 Mobile AliApp(TUnionSDK/0.1.20.4)',
        'window_size': (390, 663)
    },
    {
        # 真实  鲨鱼浏览器
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4.1 Mobile/15E148 Safari/605.1.15 PowerfulBrowser/9.3',
        'window_size': (390, 678)
    },
    {
        'name': 'iPhone 13 mini',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },


]

# iPad设备配置
IPAD_DEVICES = [
    # 真实ipaid-默认浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
        'window_size': (760, 810)
    },
    # 真实ipaid-谷歌浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/137.0.7151.107 Mobile/15E148 Safari/604.1',
        'window_size': (1080, 810)
    },
    # 真实ipaid-火狐浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
        'window_size': (1080, 790)
    },
    # 真实ipaid- QQ浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MQBHD/6.9.8 Safari/537.22',
        'window_size': (1080, 715)
    },
    # 真实ipaid-夸克浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/20D67 Quark/6.10.5.415 Mobile',
        'window_size': (1080, 730)
    },
    # 真实ipaid-uc浏览器
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X; zh-CN) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 UCBrowser/17.1.5.7027 Mobile AliApp(TUnionSDK/0.1.20.4)',
        'window_size': (1080, 659)
    },

    # 先注释掉非真实的
    # {
    #     'name': 'iPad Pro 12.9-inch (6th generation)',
    #     'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (1024, 1366)
    # },
    # {
    #     'name': 'iPad Pro 11-inch (4th generation)',
    #     'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (834, 1194)
    # },
    # {
    #     'name': 'iPad Air (5th generation)',
    #     'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (820, 1180)
    # },
    # {
    #     'name': 'iPad (10th generation)',
    #     'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (820, 1180)
    # },
    # {
    #     'name': 'iPad (9th generation)',
    #     'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
    #     'window_size': (810, 1080)
    # },
] 