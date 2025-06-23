import platform
import os
import random
from DrissionPage import ChromiumPage, ChromiumOptions
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_browser(user_agent, window_size):
    try:
        logger.info(f"开始初始化浏览器，user_agent: {user_agent}, window_size: {window_size}")
        co = ChromiumOptions()
        co.set_user_agent(user_agent)
        width, height = window_size
        co.set_argument(f'--window-size={width},{height}')
        co.set_argument('--no-sandbox')  # 以root运行时必须，禁用沙盒
        co.set_argument('--disable-dev-shm-usage')  # 避免/dev/shm空间不足导致崩溃
        co.set_argument('--disable-web-security')  # 允许跨域访问，部分广告需要
        co.set_argument('--disable-features=VizDisplayCompositor')  # 兼容部分无界面环境

        if platform.system().lower() == 'linux':
            user_dir = f'/tmp/dp_user_{os.getpid()}_{random.randint(1000, 9999)}'
            port = random.randint(30000, 40000)
            co.set_argument('--no-sandbox')
            co.set_argument('--headless=new')
            co.set_argument(f'--user-data-dir={user_dir}')
            co.set_argument(f'--remote-debugging-port={port}')
        page = ChromiumPage(co)
        logger.info("✅ 浏览器初始化完成")
        return page
    except Exception as e:
        logger.error(f"❌ 浏览器初始化失败: {e}")
        raise

if __name__ == "__main__":
    # 示例参数，可根据需要修改
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    window_size = (1920, 1080)
    page = setup_browser(user_agent, window_size)
    page.get('https://www.baidu.com')
    print(page.title)
    page.close() 