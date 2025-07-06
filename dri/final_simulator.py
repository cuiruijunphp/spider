#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终版广告点击模拟器
智能检测广告iframe内容，多种触发策略，支持动态等待和内容加载
支持循环执行、随机设备类型和配置文件
"""

import time
import random
import logging
import sys
import os
import datetime
import platform
import hashlib
from typing import Optional, Dict, List, Any, Tuple
from DrissionPage import ChromiumPage, ChromiumOptions

# 导入代理管理器
from proxy_manager import ProxyManager

# 添加配置文件路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
from devices import PC_USER_AGENTS, ANDROID_DEVICES, IOS_DEVICES, IPAD_DEVICES

# 配置日志
log_dir = os.path.join(os.path.dirname(__file__), 'log')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 配置常量
TARGET_URL = "http://mon.cuithink.com/"
AD_FRAME_TIMEOUT = 45  # 增加超时时间
NEW_TAB_TIMEOUT = 30
CONTENT_LOAD_TIMEOUT = 10

# 循环执行配置 - 优化版
LOOP_CONFIG = {
    'min_sleep': 10,  # 最小休眠时间（秒）
    'max_sleep': 30,  # 最大休眠时间（秒）
    'max_loops': 60,   # 最大循环次数，0表示无限循环
}

# 代理配置
PROXY_CONFIG = {
    'enabled': True,  # 是否启用代理
    'username': 'd4476434639',  # 快代理用户名
    'password': 'a34pvq6n',  # 快代理密码
    'api_url': 'https://dps.kdlapi.com/api/getdps'  # 快代理API地址
}

class FinalAdSimulator:
    """最终版广告点击模拟器"""
    
    def __init__(self, device_type: str = 'pc', proxy_config: Optional[Dict[str, Any]] = None):
        """初始化模拟器"""
        self.device_type = device_type
        self.page: Optional[ChromiumPage] = None
        self.ad_iframe_index: Optional[int] = None
        self.device_config = self._get_random_device_config()
        self.session_id = self._generate_session_id()  # 添加随机会话ID
        self.proxy_config = proxy_config  # 代理配置（本次循环唯一）
        self.current_proxy_ip = None
        if proxy_config and 'proxy' in proxy_config:
            self.current_proxy_ip = f"{proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}"
        self.proxy_manager = None  # 代理管理器
        self.setup_browser()
    
    def _generate_session_id(self) -> str:
        """生成唯一的会话ID"""
        timestamp = str(time.time())
        random_num = str(random.randint(1000, 9999))
        return hashlib.md5(f"{timestamp}{random_num}".encode()).hexdigest()[:8]
    
    def _get_random_device_config(self) -> Dict[str, Any]:
        """获取随机设备配置"""
        if self.device_type == 'pc':
            # 随机选择PC端User-Agent
            user_agent = random.choice(PC_USER_AGENTS)
            # 随机屏幕分辨率 - 增加随机性
            resolutions = [
                (1920, 1080), (1366, 768), (1440, 900), 
                (1536, 864), (1280, 720), (1600, 900),
                (1920, 1200), (1680, 1050), (1440, 960),
                (1494, 894)
            ]
            return {
                'name': 'PC',
                'user_agent': user_agent,
                'window_size': random.choice(resolutions),
                'color_depth': random.choice([24, 32]),
                'pixel_ratio': random.choice([1, 1.25, 1.5, 2])
            }
        elif self.device_type == 'android':
            # 随机选择Android设备
            device = random.choice(ANDROID_DEVICES)
            return device
        elif self.device_type == 'ios':
            # 随机选择iOS设备
            device = random.choice(IOS_DEVICES)
            return device
        elif self.device_type == 'ipad':
            # 随机选择iPad设备
            device = random.choice(IPAD_DEVICES)
            return device
        else:
            # 默认PC配置
            return {
                'name': 'PC',
                'user_agent': random.choice(PC_USER_AGENTS),
                'window_size': (1920, 1080)
            }
    
    def setup_browser(self):
        """设置浏览器配置"""
        try:
            logger.info(f"开始初始化浏览器，设备类型: {self.device_type}, 设备: {self.device_config['name']}")
            
            # 创建浏览器选项
            co = ChromiumOptions()

            # 设置代理（如果启用）
            if self.proxy_config:
                from proxy_manager import ProxyManager
                self.proxy_manager = ProxyManager(
                    username=PROXY_CONFIG['username'],
                    password=PROXY_CONFIG['password'],
                    api_url=PROXY_CONFIG['api_url']
                )
                self.proxy_manager.apply_proxy_to_options(co, self.proxy_config)
            
            # 设置用户代理
            co.set_user_agent(self.device_config['user_agent'])
            
            # 设置窗口大小
            width, height = self.device_config['window_size']
            co.set_argument(f'--window-size={width},{height}')
            
            # 基础设置
            co.set_argument('--no-sandbox')  # 以root运行时必须，禁用沙盒
            co.set_argument('--disable-dev-shm-usage')  # 避免/dev/shm空间不足导致崩溃
            co.set_argument('--disable-web-security')  # 允许跨域访问，部分广告需要
            co.set_argument('--disable-features=VizDisplayCompositor')  # 兼容部分无界面环境
            
            # 增强反检测设置
            co.set_argument('--disable-blink-features=AutomationControlled')  # 禁用自动化控制特征
            co.set_argument('--disable-extensions')  # 禁用扩展
            co.set_argument('--disable-plugins')  # 禁用插件
            co.set_argument('--disable-default-apps')  # 禁用默认应用
            co.set_argument('--disable-sync')  # 禁用同步
            co.set_argument('--disable-background-timer-throttling')  # 禁用后台定时器限制
            co.set_argument('--disable-backgrounding-occluded-windows')  # 禁用后台窗口限制
            co.set_argument('--disable-renderer-backgrounding')  # 禁用渲染器后台限制
            co.set_argument('--disable-field-trial-config')  # 禁用字段试验配置
            co.set_argument('--disable-ipc-flooding-protection')  # 禁用IPC洪水保护
            
            # 设置语言和时区
            co.set_argument('--lang=zh-CN,zh;q=0.9,en;q=0.8')  # 设置语言
            co.set_argument('--timezone=Asia/Shanghai')  # 设置时区
            
            # 添加Linux系统特有的参数
            if platform.system().lower() == 'linux':
                user_dir = f'/tmp/dp_user_{self.session_id}_{random.randint(1000, 9999)}'
                port = random.randint(30000, 40000)
                co.set_argument('--no-sandbox')
                co.set_argument('--headless=new')
                co.set_argument(f'--user-data-dir={user_dir}')
                co.set_argument(f'--remote-debugging-port={port}')
            
            # 创建页面实例
            self.page = ChromiumPage(co)
            
            # 注入增强反检测脚本
            self._inject_anti_detection_scripts()
            
            logger.info(f"✅ 浏览器初始化完成，设备类型: {self.device_type}, 设备: {self.device_config['name']}, 会话ID: {self.session_id}")
            
        except Exception as e:
            logger.error(f"❌ 浏览器初始化失败: {e}")
            raise
    
    def _inject_anti_detection_scripts(self):
        """注入增强反检测脚本"""
        if not self.page:
            return
            
        try:
            self.page.run_js('''
                // 移除webdriver属性
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined,
                });
                
                // 移除Chrome自动化标识
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                
                // 伪造插件信息
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                
                // 伪造语言信息
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['zh-CN', 'zh', 'en'],
                });
                
                // 伪造硬件并发数
                Object.defineProperty(navigator, 'hardwareConcurrency', {
                    get: () => 4,
                });
                
                // 伪造设备内存
                Object.defineProperty(navigator, 'deviceMemory', {
                    get: () => 8,
                });
                
                // 伪造连接信息
                Object.defineProperty(navigator, 'connection', {
                    get: () => ({
                        effectiveType: '4g',
                        rtt: 50,
                        downlink: 10,
                        saveData: false
                    }),
                });
                
                // 伪造权限状态
                const originalQuery = window.navigator.permissions.query;
                window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                        Promise.resolve({ state: Notification.permission }) :
                        originalQuery(parameters)
                );
                
                // 伪造WebGL信息
                const getParameter = WebGLRenderingContext.prototype.getParameter;
                WebGLRenderingContext.prototype.getParameter = function(parameter) {
                    if (parameter === 37445) {
                        return 'Intel Inc.';
                    }
                    if (parameter === 37446) {
                        return 'Intel(R) Iris(TM) Graphics 6100';
                    }
                    return getParameter.call(this, parameter);
                };
                
                // 伪造Canvas指纹
                const originalGetContext = HTMLCanvasElement.prototype.getContext;
                HTMLCanvasElement.prototype.getContext = function(type, ...args) {
                    const context = originalGetContext.call(this, type, ...args);
                    if (type === '2d') {
                        const originalFillText = context.fillText;
                        context.fillText = function(...args) {
                            return originalFillText.apply(this, args);
                        };
                    }
                    return context;
                };
                
                // 伪造音频指纹
                const originalGetChannelData = AudioBuffer.prototype.getChannelData;
                AudioBuffer.prototype.getChannelData = function(channel) {
                    const data = originalGetChannelData.call(this, channel);
                    return data;
                };
                
                console.log('增强反检测脚本注入完成');
            ''')
            
            logger.info("✅ 增强反检测脚本注入完成")
            
        except Exception as e:
            logger.debug(f"反检测脚本注入出错: {e}")
    
    def simulate_human_behavior(self):
        """模拟真实人类行为 - 增强版"""
        try:
            logger.info("开始模拟真实人类行为...")
            
            # 随机等待时间（更真实）
            wait_time = random.uniform(3, 8)
            time.sleep(wait_time)
            
            # 模拟页面浏览行为
            self._simulate_page_browsing()
            
            # 模拟鼠标移动轨迹
            self._simulate_mouse_movement()
            
            # 模拟键盘输入（随机）
            if random.random() < 0.3:
                self._simulate_keyboard_input()
            
            logger.info("✅ 真实人类行为模拟完成")
            
        except Exception as e:
            logger.debug(f"人类行为模拟出错: {e}")
    
    def _simulate_page_browsing(self):
        """模拟页面浏览行为"""
        try:
            # 随机滚动次数和距离
            scroll_times = random.randint(2, 5)
            for i in range(scroll_times):
                # 随机滚动距离
                scroll_y = random.randint(50, 300)
                scroll_direction = random.choice([1, -1])  # 向上或向下
                
                # 平滑滚动
                self.page.run_js(f'''
                    window.scrollBy({{
                        top: {scroll_y * scroll_direction},
                        left: 0,
                        behavior: 'smooth'
                    }});
                ''')
                
                # 随机等待
                time.sleep(random.uniform(1, 3))
                
                # 偶尔暂停
                if random.random() < 0.2:
                    time.sleep(random.uniform(2, 5))
            
            # 偶尔回到顶部
            if random.random() < 0.3:
                self.page.run_js('window.scrollTo({top: 0, behavior: "smooth"});')
                time.sleep(random.uniform(1, 2))
                
        except Exception as e:
            logger.debug(f"页面浏览模拟出错: {e}")
    
    def _simulate_mouse_movement(self):
        """模拟鼠标移动轨迹 - 使用贝塞尔曲线"""
        try:
            # 生成贝塞尔曲线轨迹点
            points = self._generate_bezier_curve_points()
            
            for point in points:
                self.page.run_js(f'''
                    var event = new MouseEvent('mousemove', {{
                        view: window,
                        bubbles: true,
                        cancelable: true,
                        clientX: {point[0]},
                        clientY: {point[1]},
                        movementX: {point[0]} - (window.lastX !== undefined ? window.lastX : 0),
                        movementY: {point[1]} - (window.lastY !== undefined ? window.lastY : 0)
                    }});
                    document.dispatchEvent(event);
                    window.lastX = {point[0]};
                    window.lastY = {point[1]};
                ''')
                time.sleep(random.uniform(0.01, 0.05))
                
        except Exception as e:
            logger.debug(f"鼠标移动模拟出错: {e}")
    
    def _generate_bezier_curve_points(self) -> List[Tuple[int, int]]:
        """生成贝塞尔曲线轨迹点"""
        points = []
        width = self.device_config['window_size'][0]
        height = self.device_config['window_size'][1]
        
        # 生成控制点
        p0 = (random.randint(0, width//4), random.randint(0, height//4))
        p1 = (random.randint(width//4, width//2), random.randint(height//4, height//2))
        p2 = (random.randint(width//2, 3*width//4), random.randint(height//2, 3*height//4))
        p3 = (random.randint(3*width//4, width), random.randint(3*height//4, height))
        
        # 生成曲线点
        for t in range(0, 101, 5):
            t = t / 100.0
            x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
            y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
            points.append((int(x), int(y)))
        
        return points
    
    def _simulate_keyboard_input(self):
        """模拟键盘输入"""
        try:
            # 随机按键
            keys = ['Tab', 'Space', 'ArrowDown', 'ArrowUp', 'Home', 'End']
            key = random.choice(keys)
            
            self.page.run_js(f'''
                var event = new KeyboardEvent('keydown', {{
                    key: '{key}',
                    code: 'Key{key}',
                    keyCode: 9,
                    which: 9,
                    bubbles: true,
                    cancelable: true
                }});
                document.dispatchEvent(event);
            ''')
            
            time.sleep(random.uniform(0.1, 0.3))
            
        except Exception as e:
            logger.debug(f"键盘输入模拟出错: {e}")
    
    def get_a_tag_xpaths(self) -> list:
        """收集页面所有<a>标签的xpath列表"""
        a_xpaths = self.page.run_js('''
            var xpaths = [];
            var all = document.getElementsByTagName('a');
            for (var i = 0; i < all.length; i++) {
                var el = all[i];
                var xpath = '';
                var elem = el;
                while (elem && elem.nodeType === 1) {
                    var sibCount = 0;
                    var sibIndex = 1;
                    for (var sib = elem.previousSibling; sib; sib = sib.previousSibling) {
                        if (sib.nodeType === 1 && sib.nodeName === elem.nodeName) {
                            sibCount++;
                        }
                    }
                    if (sibCount > 0) {
                        sibIndex = sibCount + 1;
                    }
                    xpath = '/' + elem.nodeName.toLowerCase() + (sibIndex > 1 ? '[' + sibIndex + ']' : '') + xpath;
                    elem = elem.parentNode;
                }
                xpaths.push(xpath);
            }
            return xpaths;
        ''')
        return a_xpaths or []
    
    def simulate_entry_behavior(self):
        """用户进入页面时的三种初始行为：点击<a>、下拉、不操作"""
        action = random.choice(['click_a', 'scroll', 'none'])
        logger.info(f"初始行为选择: {action}")
        if action == 'click_a':
            a_xpaths = self.get_a_tag_xpaths()
            if a_xpaths:
                xpath = random.choice(a_xpaths)
                logger.info(f"随机点击<a>标签，xpath: {xpath}")
                try:
                    self.page.ele(f'xpath:{xpath}').click()
                    time.sleep(3)  # 等待跳转页面加载
                    self.page.back()  # 返回原页面
                    time.sleep(1)
                except Exception as e:
                    logger.warning(f"点击<a>标签失败: {e}")
            else:
                logger.info("页面无<a>标签，跳过点击")
        elif action == 'scroll':
            scroll_y = random.randint(200, 800)
            logger.info(f"初始行为：下拉滚动{scroll_y}像素")
            self.page.run_js(f'window.scrollBy(0, {scroll_y});')
            time.sleep(random.uniform(0.5, 1.5))
        else:
            logger.info("初始行为：不做任何操作")
    
    def wait_for_ad_frame_with_content(self, timeout: int = AD_FRAME_TIMEOUT) -> bool:
        """等待广告iframe出现并包含可点击内容"""
        logger.info(f"等待广告框出现并加载内容，超时时间: {timeout}秒...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # 获取所有iframe信息
                iframe_info = self.page.run_js('''
                    return Array.from(document.getElementsByTagName("iframe")).map((f, index) => {
                        try {
                            var rect = f.getBoundingClientRect();
                            var score = 0;
                            var reasons = [];
                            
                            // 评分逻辑
                            if (f.offsetWidth > 100 && f.offsetHeight > 100) {
                                score += 20;
                                reasons.push("尺寸合适(" + f.offsetWidth + "x" + f.offsetHeight + ")");
                            }
                            
                            if (f.style.display !== 'none' && f.style.visibility !== 'hidden') {
                                score += 15;
                                reasons.push("可见");
                            }
                            
                            var zIndex = parseInt(f.style.zIndex) || 0;
                            if (zIndex > 1000) {
                                score += 25;
                                reasons.push("高z-index(" + zIndex + ")");
                            }
                            
                            if (f.style.position === 'fixed') {
                                score += 20;
                                reasons.push("固定定位");
                            }
                            
                            if (f.style.right && f.style.top) {
                                score += 15;
                                reasons.push("右上角位置");
                            }
                            
                            // 检查src特征
                            var src = f.src.toLowerCase();
                            if (src.includes('ad') || src.includes('banner') || src.includes('monetag')) {
                                score += 30;
                                reasons.push("广告src特征");
                            }
                            
                            // 尝试访问iframe内容
                            var contentInfo = {};
                            try {
                                if (f.contentWindow && f.contentWindow.document) {
                                    var doc = f.contentWindow.document;
                                    contentInfo.hasContent = true;
                                    
                                    // 获取可点击元素
                                    var clickableElements = doc.querySelectorAll('a, button, [onclick], [role="button"], [tabindex], input[type="button"], input[type="submit"], img');
                                    contentInfo.clickableCount = clickableElements.length;
                                    
                                    // 获取图片
                                    var images = doc.querySelectorAll('img');
                                    contentInfo.imageCount = images.length;
                                    
                                    // 获取链接
                                    var links = doc.querySelectorAll('a');
                                    contentInfo.linkCount = links.length;
                                    
                                    // 检查是否有内容
                                    if (doc.body) {
                                        contentInfo.bodyText = doc.body.textContent || '';
                                        contentInfo.hasText = contentInfo.bodyText.length > 10;
                                    }
                                    
                                    // 如果有可点击元素，增加分数
                                    if (contentInfo.clickableCount > 0) {
                                        score += 40;
                                        reasons.push("有可点击元素(" + contentInfo.clickableCount + "个)");
                                    }
                                    
                                    if (contentInfo.imageCount > 0) {
                                        score += 20;
                                        reasons.push("有图片(" + contentInfo.imageCount + "个)");
                                    }
                                    
                                    if (contentInfo.hasText) {
                                        score += 15;
                                        reasons.push("有文本内容");
                                    }
                                } else {
                                    contentInfo.hasContent = false;
                                }
                            } catch(e) {
                                contentInfo.hasContent = false;
                                contentInfo.error = e.message;
                            }
                            
                            return {
                                index: index,
                                src: f.src || '',
                                width: f.offsetWidth || 0,
                                height: f.offsetHeight || 0,
                                zIndex: zIndex,
                                position: f.style.position || '',
                                score: score,
                                reasons: reasons,
                                contentInfo: contentInfo
                            };
                        } catch(e) {
                            return {
                                index: index,
                                error: e.message,
                                score: 0
                            };
                        }
                    });
                ''')
                
                if not iframe_info:
                    time.sleep(1)
                    continue
                
                logger.info(f"当前检测到 {len(iframe_info)} 个iframe")
                
                # 查找最佳广告iframe
                best_candidate = None
                for iframe in iframe_info:
                    if iframe.get('score', 0) >= 50:  # 提高阈值
                        if not best_candidate or iframe['score'] > best_candidate['score']:
                            best_candidate = iframe
                
                if best_candidate:
                    logger.info(f"✅ 检测到广告iframe候选:")
                    logger.info(f"    分数: {best_candidate['score']}")
                    logger.info(f"    原因: {', '.join(best_candidate['reasons'])}")
                    logger.info(f"    尺寸: {best_candidate['width']}x{best_candidate['height']}")
                    logger.info(f"    src: {best_candidate['src']}")
                    logger.info(f"    位置: {best_candidate['position']}")
                    logger.info(f"    z-index: {best_candidate['zIndex']}")
                    
                    content_info = best_candidate.get('contentInfo', {})
                    if content_info.get('hasContent'):
                        logger.info(f"    iframe内容: 可点击元素{content_info.get('clickableCount', 0)}个, 图片{content_info.get('imageCount', 0)}个, 链接{content_info.get('linkCount', 0)}个")
                        
                        # 如果内容已经加载，保存索引并返回
                        if (content_info.get('clickableCount', 0) > 0 or 
                            content_info.get('imageCount', 0) > 0 or 
                            content_info.get('hasText', False)):
                            
                            self.ad_iframe_index = best_candidate['index']
                            return True
                        else:
                            logger.info("    iframe内容正在加载中...")
                    else:
                        logger.info("    iframe内容不可访问，等待加载...")
                
                time.sleep(1)
                
            except Exception as e:
                logger.debug(f"检测iframe时出错: {e}")
                time.sleep(1)
        
        logger.warning(f"⚠️ 在{timeout}秒内未找到合适的广告iframe")
        return False
    
    def click_ad_with_multiple_strategies(self) -> bool:
        """使用多种策略点击广告"""
        if not self.page:
            logger.error("❌ 页面未初始化")
            return False
            
        try:
            logger.info("准备点击广告区域...")
            
            # 策略1: 如果有保存的iframe索引，使用增强点击策略
            if self.ad_iframe_index is not None:
                logger.info(f"使用保存的iframe索引: {self.ad_iframe_index}")
                success = self.page.run_js(f'''
                    try {{
                        var iframes = document.getElementsByTagName("iframe");
                        var iframe = iframes[{self.ad_iframe_index}];
                        
                        if (!iframe) {{
                            return false;
                        }}
                        
                        // 策略1.1: 直接点击iframe元素
                        iframe.click();
                        
                        // 策略1.2: 增强的鼠标事件序列（更真实）
                        var rect = iframe.getBoundingClientRect();
                        var centerX = rect.left + rect.width / 2;
                        var centerY = rect.top + rect.height / 2;
                        
                        // 添加随机偏移，模拟真实点击
                        centerX += Math.random() * 20 - 10;
                        centerY += Math.random() * 20 - 10;
                        
                        // 完整的鼠标事件序列
                        var events = [
                            'mouseenter',
                            'mouseover', 
                            'mousedown',
                            'mouseup',
                            'click'
                        ];
                        
                        events.forEach(function(eventType, index) {{
                            setTimeout(function() {{
                                var event = new MouseEvent(eventType, {{
                                    view: window,
                                    bubbles: true,
                                    cancelable: true,
                                    clientX: centerX + Math.random() * 6 - 3,
                                    clientY: centerY + Math.random() * 6 - 3,
                                    button: 0,
                                    buttons: eventType === 'mousedown' ? 1 : 0
                                }});
                                iframe.dispatchEvent(event);
                            }}, index * 30);
                        }});
                        
                        // 策略1.3: 尝试进入iframe内部点击
                        try {{
                            if (iframe.contentWindow && iframe.contentWindow.document) {{
                                var doc = iframe.contentWindow.document;
                                var clickableElements = doc.querySelectorAll('a, button, [onclick], [role="button"], img');
                                var images = doc.querySelectorAll('img');
                                if (images.length > 1) {{
                                    // 多张图片时随机点击一张
                                    var idx = Math.floor(Math.random() * images.length);
                                    try {{
                                        images[idx].click();
                                        console.log("随机点击了iframe内部图片: " + idx);
                                    }} catch(e) {{}}
                                }} else if (clickableElements.length > 0) {{
                                    try {{
                                        clickableElements[0].click();
                                        console.log("点击了iframe内部元素: " + clickableElements[0].tagName);
                                    }} catch(e) {{}}
                                }} else if (doc.body) {{
                                    doc.body.click();
                                    console.log("点击了iframe body");
                                }}
                            }}
                        }} catch(e) {{
                            console.log("无法访问iframe内容: " + e.message);
                        }}
                        
                        return true;
                    }} catch(e) {{
                        return false;
                    }}
                ''')
                
                if success:
                    logger.info("✅ 通过iframe索引点击成功")
                    return True
            
            # 策略2: 重新扫描并点击最佳候选
            logger.info("重新扫描iframe并点击...")
            success = self.page.run_js('''
                try {
                    var iframes = document.getElementsByTagName("iframe");
                    var bestCandidate = null;
                    var bestScore = 0;
                    for (var i = 0; i < iframes.length; i++) {
                        var f = iframes[i];
                        var score = 0;
                        if (f.offsetWidth > 100 && f.offsetHeight > 100) score += 20;
                        if (f.style.display !== 'none' && f.style.visibility !== 'hidden') score += 15;
                        if (parseInt(f.style.zIndex) > 1000) score += 25;
                        if (f.style.position === 'fixed') score += 20;
                        if (f.style.right && f.style.top) score += 15;
                        var src = f.src.toLowerCase();
                        if (src.includes('ad') || src.includes('banner') || src.includes('monetag')) score += 30;
                        try {
                            if (f.contentWindow && f.contentWindow.document) {
                                var doc = f.contentWindow.document;
                                var clickableElements = doc.querySelectorAll('a, button, [onclick], [role="button"], img');
                                var images = doc.querySelectorAll('img');
                                if (images.length > 1) score += 10;
                                if (clickableElements.length > 0) score += 40;
                            }
                        } catch(e) {}
                        if (score > bestScore) {
                            bestScore = score;
                            bestCandidate = f;
                        }
                    }
                    if (bestCandidate && bestScore >= 50) {
                        bestCandidate.scrollIntoView({behavior: 'smooth', block: 'center'});
                        setTimeout(function() {
                            bestCandidate.click();
                            var rect = bestCandidate.getBoundingClientRect();
                            var centerX = rect.left + rect.width / 2;
                            var centerY = rect.top + rect.height / 2;
                            var mousedownEvent = new MouseEvent('mousedown', {
                                view: window,
                                bubbles: true,
                                cancelable: true,
                                clientX: centerX,
                                clientY: centerY,
                                button: 0
                            });
                            bestCandidate.dispatchEvent(mousedownEvent);
                            var mouseupEvent = new MouseEvent('mouseup', {
                                view: window,
                                bubbles: true,
                                cancelable: true,
                                clientX: centerX,
                                clientY: centerY,
                                button: 0
                            });
                            bestCandidate.dispatchEvent(mouseupEvent);
                            var clickEvent = new MouseEvent('click', {
                                view: window,
                                bubbles: true,
                                cancelable: true,
                                clientX: centerX,
                                clientY: centerY,
                                button: 0
                            });
                            bestCandidate.dispatchEvent(clickEvent);
                            try {
                                if (bestCandidate.contentWindow && bestCandidate.contentWindow.document) {
                                    var doc = bestCandidate.contentWindow.document;
                                    var clickableElements = doc.querySelectorAll('a, button, [onclick], [role="button"], img');
                                    var images = doc.querySelectorAll('img');
                                    if (images.length > 1) {
                                        var idx = Math.floor(Math.random() * images.length);
                                        try {
                                            images[idx].click();
                                        } catch(e) {}
                                    } else if (clickableElements.length > 0) {
                                        try {
                                            clickableElements[0].click();
                                        } catch(e) {}
                                    } else if (doc.body) {
                                        doc.body.click();
                                    }
                                }
                            } catch(e) {}
                        }, 500);
                        return true;
                    }
                    return false;
                } catch(e) {
                    return false;
                }
            ''')
            
            if success:
                logger.info("✅ 通过重新扫描点击成功")
                return True
            
            # 策略3: 尝试通过JavaScript直接触发广告跳转
            logger.info("尝试通过JavaScript直接触发广告跳转...")
            success = self.page.run_js('''
                try {
                    var iframes = document.getElementsByTagName("iframe");
                    var triggered = false;
                    
                    for (var i = 0; i < iframes.length; i++) {
                        var f = iframes[i];
                        
                        if (f.offsetWidth > 100 && f.offsetHeight > 100 && 
                            f.style.display !== 'none' && f.style.visibility !== 'hidden') {
                            
                            // 尝试多种触发方式
                            try {
                                // 方式1: 直接设置location
                                if (f.contentWindow) {
                                    f.contentWindow.location.href = f.src;
                                }
                            } catch(e) {}
                            
                            try {
                                // 方式2: 触发load事件
                                f.dispatchEvent(new Event('load'));
                            } catch(e) {}
                            
                            try {
                                // 方式3: 模拟双击
                                var rect = f.getBoundingClientRect();
                                var centerX = rect.left + rect.width / 2;
                                var centerY = rect.top + rect.height / 2;
                                
                                var dblclickEvent = new MouseEvent('dblclick', {
                                    view: window,
                                    bubbles: true,
                                    cancelable: true,
                                    clientX: centerX,
                                    clientY: centerY,
                                    button: 0
                                });
                                f.dispatchEvent(dblclickEvent);
                            } catch(e) {}
                            
                            // 方式4: 尝试触发广告脚本
                            try {
                                if (f.contentWindow && f.contentWindow.document) {
                                    var doc = f.contentWindow.document;
                                    var scripts = doc.querySelectorAll('script');
                                    for (var j = 0; j < scripts.length; j++) {
                                        if (scripts[j].src && scripts[j].src.includes('ad')) {
                                            var newScript = doc.createElement('script');
                                            newScript.src = scripts[j].src;
                                            doc.head.appendChild(newScript);
                                        }
                                    }
                                }
                            } catch(e) {}
                            
                            triggered = true;
                        }
                    }
                    
                    return triggered;
                } catch(e) {
                    return false;
                }
            ''')
            
            if success:
                logger.info("✅ 通过JavaScript触发跳转成功")
                return True
            
            logger.warning("⚠️ 所有点击策略都失败了")
            return False
            
        except Exception as e:
            logger.error(f"❌ 点击广告区域失败: {e}")
            return False
    
    def wait_for_new_tab(self, timeout: int = NEW_TAB_TIMEOUT) -> bool:
        """等待新标签页打开"""
        logger.info(f"等待新标签页打开，超时时间: {timeout}秒...")
        start_time = time.time()
        
        # 记录初始标签页数量
        try:
            initial_tabs = len(self.page.get_tabs())
        except:
            initial_tabs = 1
        
        while time.time() - start_time < timeout:
            try:
                current_tabs = len(self.page.get_tabs())
                if current_tabs > initial_tabs:
                    logger.info(f"✅ 检测到新标签页打开，当前标签页数量: {current_tabs}")
                    return True
                
                time.sleep(1)
                
            except Exception as e:
                logger.debug(f"检查新标签页时出错: {e}")
                time.sleep(1)
        
        logger.warning(f"⚠️ 新标签页在{timeout}秒内未加载完成")
        return False
    
    def print_proxy_ip(self):
        """打印当前循环使用的代理IP"""
        if self.current_proxy_ip:
            logger.info(f"🌐 当前循环使用代理IP: {self.current_proxy_ip}")
        else:
            logger.info("🌐 当前使用直连（无代理）")
    
    def run_simulation(self) -> bool:
        """运行广告点击模拟"""
        if not self.page:
            logger.error("❌ 页面未初始化")
            return False
        try:
            logger.info("🚀 开始广告点击模拟...")
            self.print_proxy_ip()
            # 1. 打开目标网站
            logger.info(f"打开目标网站: {TARGET_URL}")
            self.page.get(TARGET_URL)
            time.sleep(3)
            logger.info("✅ 网站加载完成")
            # 2. 初始三种行为
            self.simulate_entry_behavior()
            # 3. 模拟人类行为
            self.simulate_human_behavior()
            # 4. 等待广告iframe出现并包含内容
            if not self.wait_for_ad_frame_with_content():
                logger.warning("⚠️ 未找到广告iframe")
                return False
            # 5. 再次模拟人类行为
            self.simulate_human_behavior()
            # 6. 用户选择是否点击广告（80%概率）
            if random.random() < 0.8:
                logger.info("用户选择点击广告")
                # 7. 点击广告区域
                if not self.click_ad_with_multiple_strategies():
                    logger.warning("⚠️ 广告点击失败")
                    return False
                # 8. 等待新标签页打开
                if not self.wait_for_new_tab():
                    logger.warning("⚠️ 新标签页未打开")
                    return False
                logger.info("✅ 广告点击模拟成功完成")
                return True
            else:
                logger.info("用户选择不点击广告")
                return True
        except Exception as e:
            logger.error(f"❌ 广告点击模拟过程中出错: {e}")
            return False
    
    def close(self):
        """关闭浏览器"""
        try:
            if self.page:
                self.page.quit()
                logger.info("✅ 浏览器已关闭")
            
            # 清理代理资源
            if self.proxy_manager:
                self.proxy_manager.cleanup()
                logger.info("✅ 代理资源已清理")
                
        except Exception as e:
            logger.error(f"❌ 关闭浏览器时出错: {e}")

def main():
    """主函数 - 支持循环执行和随机设备类型"""
    import sys
    
    # 获取设备类型参数，支持随机选择
    device_type = sys.argv[1] if len(sys.argv) > 1 else 'random'
    
    # 支持的设备类型
    supported_devices = ['pc', 'android', 'ios', 'ipad', 'random']
    
    if device_type not in supported_devices:
        logger.error(f"❌ 不支持的设备类型: {device_type}")
        logger.info(f"支持的设备类型: {', '.join(supported_devices)}")
        return
    
    logger.info(f"启动广告点击模拟器")
    logger.info(f"循环配置: 休眠{LOOP_CONFIG['min_sleep']}-{LOOP_CONFIG['max_sleep']}秒")
    if LOOP_CONFIG['max_loops'] > 0:
        logger.info(f"最大循环次数: {LOOP_CONFIG['max_loops']}")
    else:
        logger.info("无限循环模式")
    
    # 代理管理器（全局）
    proxy_manager = None
    if PROXY_CONFIG['enabled']:
        proxy_manager = ProxyManager(
            username=PROXY_CONFIG['username'],
            password=PROXY_CONFIG['password'],
            api_url=PROXY_CONFIG['api_url']
        )
        logger.info("✅ 代理管理器已初始化")
    
    loop_count = 0
    
    while True:
        loop_count += 1
        logger.info(f"=" * 50)
        logger.info(f"开始第 {loop_count} 次循环")
        
        # 获取新的代理配置（每次循环使用新IP）
        proxy_config = None
        if proxy_manager:
            try:
                proxy_config = proxy_manager.get_new_proxy()
                if proxy_config:
                    logger.info(f"✅ 第 {loop_count} 次循环使用代理IP: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")
                else:
                    logger.warning("⚠️ 获取代理IP失败，将使用直连")
            except Exception as e:
                logger.error(f"❌ 获取代理IP时出错: {e}")
        
        # 随机选择设备类型
        if device_type == 'random':
            current_device = random.choice(['pc', 'android', 'ios', 'ipad'])
            logger.info(f"随机选择设备类型: {current_device}")
        else:
            current_device = device_type
        
        simulator = None
        try:
            # 创建模拟器实例（传入代理配置）
            simulator = FinalAdSimulator(current_device, proxy_config)
            
            # 运行模拟
            success = simulator.run_simulation()
            
            if success:
                logger.info(f"🎉 第 {loop_count} 次循环完成")
            else:
                logger.warning(f"⚠️ 第 {loop_count} 次循环未完全成功")
            
            # 等待一段时间
            time.sleep(5)
            
        except Exception as e:
            logger.error(f"❌ 第 {loop_count} 次循环执行出错: {e}")
        
        finally:
            # 确保浏览器被关闭
            if simulator:
                simulator.close()
        
        # 检查是否达到最大循环次数
        if LOOP_CONFIG['max_loops'] > 0 and loop_count >= LOOP_CONFIG['max_loops']:
            logger.info(f"达到最大循环次数 {LOOP_CONFIG['max_loops']}，程序结束")
            break
        
        # 随机休眠
        sleep_time = random.uniform(LOOP_CONFIG['min_sleep'], LOOP_CONFIG['max_sleep'])
        logger.info(f"休眠 {sleep_time:.1f} 秒后开始下次循环...")
        time.sleep(sleep_time)
    
    # 清理代理管理器
    if proxy_manager:
        proxy_manager.cleanup()
        logger.info("✅ 代理管理器已清理")

if __name__ == "__main__":
    main() 