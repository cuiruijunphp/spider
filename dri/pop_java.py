#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模拟真实用户点击 http://java.cuithink.com/ 页面广告，支持PC/Android/iOS多端，集成快代理。
"""
import os
import sys
import random
import time
import platform
import logging
from typing import Optional
from DrissionPage import ChromiumPage, ChromiumOptions
import argparse

# 导入设备UA配置
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
from devices import PC_USER_AGENTS, ANDROID_DEVICES, IOS_DEVICES

# 导入快代理管理器
from proxy_manager import ProxyManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 快代理账号信息（请替换为你的账号密码）
KDL_USERNAME = 'd4476434639'
KDL_PASSWORD = 'a34pvq6n'

# 目标网址
TARGET_URL = 'http://java.cuithink.com/'

# --- 设备类型选择 ---
DEVICE_TYPES = ['pc', 'android', 'ios']

def get_random_device(device_type: str):
    """根据类型随机获取UA和窗口大小"""
    if device_type == 'pc':
        user_agent = random.choice(PC_USER_AGENTS)
        window_size = (random.randint(1280, 1920), random.randint(720, 1080))
    elif device_type == 'android':
        device = random.choice(ANDROID_DEVICES)
        user_agent = device['user_agent']
        window_size = device['window_size']
    elif device_type == 'ios':
        device = random.choice(IOS_DEVICES)
        user_agent = device['user_agent']
        window_size = device['window_size']
    else:
        raise ValueError('未知设备类型')
    return user_agent, window_size

def setup_browser(user_agent, window_size, proxy_config=None):
    """初始化浏览器，应用UA、窗口、代理"""
    co = ChromiumOptions()
    co.set_user_agent(user_agent)
    width, height = window_size
    co.set_argument(f'--window-size={width},{height}')
    co.set_argument('--no-sandbox')
    co.set_argument('--disable-dev-shm-usage')
    co.set_argument('--disable-web-security')
    co.set_argument('--disable-features=VizDisplayCompositor')
    # Linux下防止端口冲突
    if platform.system().lower() == 'linux':
        user_dir = f'/tmp/dp_user_{os.getpid()}_{random.randint(1000, 9999)}'
        port = random.randint(30000, 40000)
        co.set_argument('--headless=new')
        co.set_argument(f'--user-data-dir={user_dir}')
        co.set_argument(f'--remote-debugging-port={port}')
    # 应用代理扩展
    if proxy_config:
        from proxy_manager import ProxyManager
        proxy_manager = ProxyManager(KDL_USERNAME, KDL_PASSWORD)
        proxy_manager.apply_proxy_to_options(co, proxy_config)
    page = ChromiumPage(co)
    return page

def simulate_scroll(page, min_scroll=200, max_scroll=1000):
    """模拟用户下拉页面"""
    scroll_y = random.randint(min_scroll, max_scroll)
    page.run_js(f'window.scrollTo(0, {scroll_y});')
    time.sleep(random.uniform(0.5, 1.5))

def find_clickable_elements(page):
    """查找可点击的非导航菜单a标签"""
    a_tags = page.eles('a')
    candidates = []
    for a in a_tags:
        # 调试输出类型
        # print(type(a), a)
        if not hasattr(a, 'attr') or not callable(a.attr):
            continue
        # 排除属于 div#monavber 下的 a 标签
        parent = getattr(a, 'parent', None)
        is_in_monavber = False
        while parent:
            if hasattr(parent, 'attr') and callable(parent.attr):
                pid = parent.attr('id')
                if pid == 'monavber':
                    is_in_monavber = True
                    break
            parent = getattr(parent, 'parent', None)
        if is_in_monavber:
            continue
        href = a.attr('href')
        href = str(href) if href is not None else ''
        text = (a.text or '').strip() if hasattr(a, 'text') else ''
        if not href or href.startswith('#') or href.startswith('javascript'):
            continue
        if any(x in (text or '').lower() for x in ['首页','关于','联系我们','登录','注册','导航','menu','home','contact','about']):
            continue
        if hasattr(a, 'parent') and a.parent and hasattr(a.parent, 'attr'):
            parent_class = a.parent.attr('class')
            if parent_class and 'nav' in parent_class.lower():
                continue
        candidates.append(a)
    return candidates

def get_all_pages(page):
    """获取所有标签页和所有窗口对象的合集"""
    tabs = page.get_tabs() if hasattr(page, 'get_tabs') else []
    windows = page.get_windows() if hasattr(page, 'get_windows') else []
    # 合并去重
    all_pages = list({id(p): p for p in (tabs + windows)}.values())
    return all_pages

def wait_for_new_page(page, old_pages, timeout=30):
    """等待新标签页或新窗口出现并返回新页面对象"""
    start = time.time()
    while time.time() - start < timeout:
        pages = get_all_pages(page)
        new_pages = [p for p in pages if p not in old_pages]
        for new_page in new_pages:
            try:
                if hasattr(new_page, 'url') and new_page.url:
                    if hasattr(page, 'switch_to'):
                        page.switch_to(new_page)
                    return new_page
            except Exception:
                continue
        time.sleep(0.5)
    return None

def simulate_ad_browsing(ad_page):
    """广告页停留2-5秒并随机下拉"""
    stay = random.uniform(2, 5)
    logger.info(f"广告页停留 {stay:.2f} 秒并随机下拉")
    time.sleep(stay/2)
    simulate_scroll(ad_page, min_scroll=100, max_scroll=800)
    time.sleep(stay/2)

def main():
    # 随机选择设备类型
    device_type = random.choice(DEVICE_TYPES)
    user_agent, window_size = get_random_device(device_type)
    logger.info(f"本次模拟设备类型: {device_type}, UA: {user_agent}, 窗口: {window_size}")

    # 获取快代理
    # proxy_manager = ProxyManager(KDL_USERNAME, KDL_PASSWORD)
    # proxy_config = proxy_manager.get_new_proxy()
    # if not proxy_config:
    #     logger.error("获取代理失败，退出")
    #     return
    # logger.info(f"本次代理IP: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")

    # 启动浏览器
    # page = setup_browser(user_agent, window_size, proxy_config)
    page = setup_browser(user_agent, window_size)
    try:
        page.get(TARGET_URL)
        time.sleep(random.uniform(1, 2))
        simulate_scroll(page)
        # 查找可点击元素
        candidates = find_clickable_elements(page)
        if not candidates:
            logger.warning("未找到可点击的非导航a标签，退出")
            return
        target = random.choice(candidates)
        logger.info(f"随机点击标签: {target.text} -> {target.attr('href')}")
        old_pages = get_all_pages(page)
        target.click()
        # 等待新页面（tab或window）
        ad_page = wait_for_new_page(page, old_pages, timeout=30)
        if not ad_page:
            logger.warning("未检测到新页面或广告页url为空，退出")
            return
        logger.info(f"新页面url: {ad_page.url}")
        simulate_ad_browsing(ad_page)
        logger.info("本次广告浏览完成")
    except Exception as e:
        logger.error(f"模拟过程中出错: {e}")
    finally:
        page.close()
        # proxy_manager.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量模拟用户点击广告")
    parser.add_argument('--loops', type=int, default=1, help='循环次数，默认1次')
    args = parser.parse_args()
    loops = args.loops
    if loops < 1:
        try:
            loops = int(input('请输入循环次数（正整数）：'))
        except Exception:
            loops = 1
    for i in range(loops):
        logger.info(f"\n===== 开始第 {i+1}/{loops} 次模拟 =====")
        try:
            main()
        except Exception as e:
            logger.error(f"第 {i+1} 次模拟发生异常: {e}")
        time.sleep(random.uniform(2, 5))  # 每次循环间隔2-5秒 