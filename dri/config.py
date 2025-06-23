#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
管理广告点击模拟器的各种设置
"""

# 目标网站配置
TARGET_URL = "http://mon.cuithink.com/"
AD_FRAME_XPATH = "/html/iframe[2]"

# 广告商配置
ADVERTISER_DOMAIN = "https://publishers.monetag.com/"

# 超时配置
AD_FRAME_TIMEOUT = 30  # 广告框等待超时时间（秒）
NEW_TAB_TIMEOUT = 30   # 新标签页等待超时时间（秒）

# 设备配置
DEVICE_CONFIGS = {
    'pc': {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'window_size': (1920, 1080)
    },
    'android': {
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (412, 915)
    },
    'ios': {
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1',
        'window_size': (390, 844)
    }
}

# 人类行为模拟配置
HUMAN_BEHAVIOR_CONFIG = {
    'scroll_probability': 0.7,      # 滚动页面的概率
    'mouse_move_probability': 0.6,  # 移动鼠标的概率
    'click_ad_probability': 0.8,    # 点击广告的概率
    'wait_time_range': (1, 3),      # 等待时间范围（秒）
    'scroll_distance_range': (100, 500),  # 滚动距离范围（像素）
}

# 浏览器配置
BROWSER_CONFIG = {
    'disable_images': True,         # 禁用图片加载
    'disable_webrtc': True,         # 禁用WebRTC
    'anti_detection': True,         # 启用反检测
}

# 日志配置
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'file': 'ad_click_simulator.log',
    'encoding': 'utf-8'
}

# 可点击元素选择器
CLICKABLE_SELECTORS = [
    'a', 'button', '[onclick]', '[role="button"]',
    '.ad-click', '.ad-link', '.clickable',
    '.advertisement', '.banner', '.promo'
] 