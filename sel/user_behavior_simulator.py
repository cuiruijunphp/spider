import time
import random
import platform
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class UserBehaviorSimulator:
    def __init__(self, user_agent_type='pc'):
        """
        初始化用户行为模拟器
        
        Args:
            user_agent_type: 用户代理类型 ('pc', 'android', 'ios')
        """
        self.user_agent_type = user_agent_type
        self.driver = None
        self.original_window = None
        self.setup_driver()
    
    def setup_driver(self):
        """设置WebDriver配置"""
        chrome_options = Options()
        
        # 根据设备类型设置用户代理
        user_agents = {
            'pc': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'android': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'ios': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        }
        
        chrome_options.add_argument(f'--user-agent={user_agents.get(self.user_agent_type, user_agents["pc"])}')
        
        # 移动端设置
        if self.user_agent_type in ['android', 'ios']:
            chrome_options.add_argument('--window-size=375,667')  # 移动端窗口大小
        
        # 安全设置 - 允许不安全连接
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-insecure-localhost')
        
        # 其他设置
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # 禁用安全警告
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.original_window = self.driver.current_window_handle
            logger.info(f"WebDriver初始化成功 - 设备类型: {self.user_agent_type}")
        except Exception as e:
            logger.error(f"WebDriver初始化失败: {e}")
            raise
    
    def simulate_human_scroll(self):
        """模拟人类滚动行为"""
        try:
            # 随机滚动
            scroll_actions = [
                lambda: self.driver.execute_script("window.scrollTo(0, 100)"),
                lambda: self.driver.execute_script("window.scrollTo(0, 300)"),
                lambda: self.driver.execute_script("window.scrollTo(0, 500)"),
                lambda: self.driver.execute_script("window.scrollTo(0, 0)"),
            ]
            
            # 随机选择是否滚动
            if random.random() < 0.7:  # 70%概率会滚动
                action = random.choice(scroll_actions)
                action()
                time.sleep(random.uniform(1, 3))
                logger.info("执行了页面滚动")
            else:
                logger.info("用户选择不滚动页面")
                
        except Exception as e:
            logger.warning(f"滚动操作失败: {e}")
    
    def wait_for_ad_popup(self, timeout=20):
        """
        等待广告弹窗出现
        
        Args:
            timeout: 超时时间（秒）
        
        Returns:
            bool: 是否检测到广告弹窗
        """
        logger.info("等待广告弹窗出现...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # 检查iframe是否存在
                iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                if len(iframes) >= 2:
                    # 检查第二个iframe（广告框）
                    ad_iframe = iframes[1]
                    if ad_iframe.is_displayed():
                        logger.info("检测到广告弹窗")
                        return True
                
                time.sleep(1)
            except Exception as e:
                logger.debug(f"检查广告弹窗时出错: {e}")
                time.sleep(1)
        
        logger.warning(f"在{timeout}秒内未检测到广告弹窗")
        return False
    
    def click_ad_area(self):
        """
        点击广告区域
        
        Returns:
            bool: 是否成功点击并跳转
        """
        try:
            # 查找广告iframe
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            if len(iframes) < 2:
                logger.warning("未找到广告iframe")
                return False
            
            ad_iframe = iframes[1]
            
            # 切换到广告iframe
            self.driver.switch_to.frame(ad_iframe)
            
            # 查找可点击的元素
            clickable_elements = self.driver.find_elements(By.XPATH, "//*[contains(@onclick, 'click') or contains(@href, 'http') or @role='button']")
            
            if not clickable_elements:
                # 如果没有找到明显的可点击元素，尝试点击iframe的中心区域
                actions = ActionChains(self.driver)
                actions.move_by_offset(100, 100).click().perform()
                logger.info("点击了广告iframe的中心区域")
            else:
                # 点击第一个可点击元素
                clickable_elements[0].click()
                logger.info("点击了广告区域的可点击元素")
            
            # 切回主文档
            self.driver.switch_to.default_content()
            
            # 等待新窗口打开
            time.sleep(2)
            
            # 检查是否有新窗口打开
            all_windows = self.driver.window_handles
            if len(all_windows) > 1:
                # 切换到新窗口
                new_window = [window for window in all_windows if window != self.original_window][0]
                self.driver.switch_to.window(new_window)
                logger.info("成功跳转到新页面")
                return True
            else:
                logger.warning("点击后未检测到新窗口打开")
                return False
                
        except Exception as e:
            logger.error(f"点击广告区域时出错: {e}")
            # 确保切回主文档
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False
    
    def wait_for_page_load(self, timeout=30):
        """
        等待新页面加载完成
        
        Args:
            timeout: 超时时间（秒）
        
        Returns:
            bool: 页面是否加载完成
        """
        logger.info("等待新页面加载完成...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                current_url = self.driver.current_url
                if current_url and current_url != "about:blank" and current_url != "data:,":
                    logger.info(f"页面加载完成，当前URL: {current_url}")
                    return True
                time.sleep(1)
            except Exception as e:
                logger.debug(f"检查页面加载状态时出错: {e}")
                time.sleep(1)
        
        logger.warning(f"页面在{timeout}秒内未完全加载")
        return False
    
    def simulate_user_behavior(self, url="http://mon.cuithink.com/"):
        """
        模拟完整的用户行为
        
        Args:
            url: 要访问的网址
        """
        try:
            logger.info(f"开始模拟用户行为 - 设备类型: {self.user_agent_type}")
            logger.info(f"访问网址: {url}")
            
            # 访问网页
            self.driver.get(url)
            logger.info("页面加载完成")
            
            # 模拟人类滚动行为
            self.simulate_human_scroll()
            
            # 等待广告弹窗出现（5-15秒随机延迟）
            delay = random.uniform(5, 15)
            logger.info(f"等待 {delay:.1f} 秒后检查广告弹窗...")
            time.sleep(delay)
            
            # 检查广告弹窗
            if self.wait_for_ad_popup():
                # 用户可能点击也可能不点击广告
                if random.random() < 0.6:  # 60%概率点击广告
                    logger.info("用户选择点击广告区域")
                    if self.click_ad_area():
                        # 等待新页面加载
                        if self.wait_for_page_load():
                            logger.info("新页面加载完成，模拟成功")
                        else:
                            logger.warning("新页面加载超时")
                    else:
                        logger.warning("点击广告区域失败")
                else:
                    logger.info("用户选择不点击广告区域")
            else:
                logger.info("未检测到广告弹窗")
            
            # 最终等待
            time.sleep(3)
            
        except Exception as e:
            logger.error(f"模拟用户行为时出错: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """清理资源"""
        try:
            if self.driver:
                self.driver.quit()
                logger.info("WebDriver已关闭")
        except Exception as e:
            logger.error(f"关闭WebDriver时出错: {e}")

def main():
    """主函数"""
    # 模拟不同设备类型的用户行为
    device_types = ['pc', 'android', 'ios']
    
    for device_type in device_types:
        logger.info(f"\n{'='*50}")
        logger.info(f"开始模拟 {device_type.upper()} 设备用户行为")
        logger.info(f"{'='*50}")
        
        simulator = UserBehaviorSimulator(user_agent_type=device_type)
        simulator.simulate_user_behavior()
        
        # 设备间间隔
        time.sleep(2)

if __name__ == "__main__":
    main() 