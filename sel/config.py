# -*- coding: utf-8 -*-
"""
用户行为模拟器配置文件
"""

# 设备配置
DEVICE_CONFIGS = {
    'pc': {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'window_size': None,  # 使用默认窗口大小
        'scroll_probability': 0.7,
        'click_ad_probability': 0.6
    },
    'android': {
        'user_agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'window_size': (375, 667),
        'scroll_probability': 0.8,  # 移动端用户更倾向于滚动
        'click_ad_probability': 0.5  # 移动端用户点击广告概率稍低
    },
    'ios': {
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'window_size': (375, 667),
        'scroll_probability': 0.8,
        'click_ad_probability': 0.4  # iOS用户点击广告概率更低
    }
}

# 时间配置
TIMING_CONFIG = {
    'ad_wait_min': 5,      # 等待广告出现的最小时间（秒）
    'ad_wait_max': 15,     # 等待广告出现的最大时间（秒）
    'ad_detection_timeout': 20,  # 广告检测超时时间（秒）
    'page_load_timeout': 30,     # 页面加载超时时间（秒）
    'scroll_delay_min': 1,       # 滚动后等待的最小时间（秒）
    'scroll_delay_max': 3,       # 滚动后等待的最大时间（秒）
    'final_wait': 3              # 最终等待时间（秒）
}

# 滚动配置
SCROLL_CONFIG = {
    'positions': [100, 300, 500, 0],  # 滚动位置列表
    'smooth_scroll': True,            # 是否使用平滑滚动
    'scroll_behavior': 'smooth'       # 滚动行为类型
}

# 广告检测配置
AD_DETECTION_CONFIG = {
    'iframe_index': 1,  # 广告iframe的索引（从0开始）
    'xpath': '/html/iframe[2]',  # 广告iframe的xpath路径
    'check_interval': 1,  # 检查间隔（秒）
    'clickable_selectors': [
        "//*[contains(@onclick, 'click')]",
        "//*[contains(@href, 'http')]",
        "//*[@role='button']",
        "//a",
        "//button",
        "//*[contains(@class, 'click')]",
        "//*[contains(@class, 'btn')]"
    ]
}

# 浏览器配置
BROWSER_CONFIG = {
    'headless': False,           # 是否使用无头模式
    'disable_images': False,     # 是否禁用图片加载
    'disable_javascript': False, # 是否禁用JavaScript
    'proxy': None,              # 代理设置
    'user_data_dir': None,      # 用户数据目录
    'incognito': True,          # 是否使用无痕模式
}

# 日志配置
LOGGING_CONFIG = {
    'level': 'INFO',            # 日志级别
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'file': None,              # 日志文件路径（None表示只输出到控制台）
    'max_bytes': 10 * 1024 * 1024,  # 日志文件最大大小（10MB）
    'backup_count': 5          # 备份文件数量
}

# 目标网站配置
TARGET_SITES = {
    'default': 'http://mon.cuithink.com/',
    'test_sites': [
        'http://mon.cuithink.com/',
        'http://example.com',
        'http://httpbin.org/'
    ]
}

# 错误处理配置
ERROR_HANDLING_CONFIG = {
    'max_retries': 3,          # 最大重试次数
    'retry_delay': 5,          # 重试延迟（秒）
    'continue_on_error': True, # 出错时是否继续执行
    'screenshot_on_error': True # 出错时是否截图
} 