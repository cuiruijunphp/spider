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
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    
    # Edge浏览器
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0',
    
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
]

# Android设备配置
ANDROID_DEVICES = [
    {
        'name': 'Samsung Galaxy S24',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Samsung Galaxy S23',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Samsung Galaxy S22',
        'user_agent': 'Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Google Pixel 8',
        'user_agent': 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Google Pixel 7',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'OnePlus 11',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Xiaomi 13',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; 2211133C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'OPPO Find X6',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; PEXM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'vivo X90',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; V2241A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Huawei P60',
        'user_agent': 'Mozilla/5.0 (Linux; Android 12; ALH-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Samsung Galaxy A54',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    {
        'name': 'Redmi Note 12',
        'user_agent': 'Mozilla/5.0 (Linux; Android 12; 23049RAD8C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    { 'name': 'Huawei Pura 70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Pura 70 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Pura 70 Ultra', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Pura 70 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei P60', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI P60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei P60 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI P60 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Nova 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Nova 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Mate 70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Mate 70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Mate 70 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HUAWEI Mate 70 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Mate 60', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI Mate 60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Huawei Mate 60 Pro', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HUAWEI Mate 60 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Honor Play9C', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HONOR Play9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Honor Play9T', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; HONOR Play9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Honor X60', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HONOR X60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Honor 400', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; HONOR 400) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'vivo X200', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo X200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'vivo Y200GT', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo Y200GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'vivo S20', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; vivo S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Xiaomi 15', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; MI 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Redmi Note 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi Note 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Redmi Note 13', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; Redmi Note 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Redmi K80', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi K80) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Xiaomi 14', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; MI 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Redmi K70', 'user_agent': 'Mozilla/5.0 (Linux; Android 14; Redmi K70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) },
    { 'name': 'Xiaomi 13', 'user_agent': 'Mozilla/5.0 (Linux; Android 13; MI 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36', 'window_size': (412, 915) }

]

# iOS设备配置
IOS_DEVICES = [
    {
        'name': 'iPhone 15 Pro Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (430, 932)
    },
    {
        'name': 'iPhone 15 Pro',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (393, 852)
    },
    {
        'name': 'iPhone 15',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (393, 852)
    },
    {
        'name': 'iPhone 15 Plus',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (430, 932)
    },
    {
        'name': 'iPhone 14 Pro Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (430, 932)
    },
    {
        'name': 'iPhone 14 Pro',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (393, 852)
    },
    {
        'name': 'iPhone 14',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (393, 852)
    },
    {
        'name': 'iPhone 14 Plus',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (430, 932)
    },
    {
        'name': 'iPhone 13 Pro Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (428, 926)
    },
    {
        'name': 'iPhone 13 Pro',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
    {
        'name': 'iPhone 13',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
    {
        'name': 'iPhone 13 mini',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },
    {
        'name': 'iPhone 12 Pro Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (428, 926)
    },
    {
        'name': 'iPhone 12 Pro',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
    {
        'name': 'iPhone 12',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    },
    {
        'name': 'iPhone 12 mini',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },
    {
        'name': 'iPhone 11 Pro Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (414, 896)
    },
    {
        'name': 'iPhone 11 Pro',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },
    {
        'name': 'iPhone 11',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (414, 896)
    },
    {
        'name': 'iPhone XS Max',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (414, 896)
    },
    {
        'name': 'iPhone XS',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },
    {
        'name': 'iPhone XR',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (414, 896)
    },
    {
        'name': 'iPhone X',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 812)
    },
    {
        'name': 'iPhone 8 Plus',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (414, 736)
    },
    {
        'name': 'iPhone 8',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 667)
    },
    {
        'name': 'iPhone SE (3rd generation)',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 667)
    },
    {
        'name': 'iPhone SE (2nd generation)',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (375, 667)
    }
]

# iPad设备配置
IPAD_DEVICES = [
    {
        'name': 'iPad Pro 12.9-inch (6th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (1024, 1366)
    },
    {
        'name': 'iPad Pro 11-inch (4th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (834, 1194)
    },
    {
        'name': 'iPad Air (5th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (820, 1180)
    },
    {
        'name': 'iPad (10th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (820, 1180)
    },
    {
        'name': 'iPad (9th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (810, 1080)
    },
    {
        'name': 'iPad mini (6th generation)',
        'user_agent': 'Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (768, 1024)
    }
] 