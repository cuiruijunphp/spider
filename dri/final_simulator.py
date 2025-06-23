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
from typing import Optional, Dict, List, Any
from DrissionPage import ChromiumPage, ChromiumOptions

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

# 循环执行配置
LOOP_CONFIG = {
    'min_sleep': 10,  # 最小休眠时间（秒）
    'max_sleep': 30,  # 最大休眠时间（秒）
    'max_loops': 5,   # 最大循环次数，0表示无限循环
}

class FinalAdSimulator:
    """最终版广告点击模拟器"""
    
    def __init__(self, device_type: str = 'pc'):
        """初始化模拟器"""
        self.device_type = device_type
        self.page: Optional[ChromiumPage] = None
        self.ad_iframe_index: Optional[int] = None
        self.device_config = self._get_random_device_config()
        self.setup_browser()
    
    def _get_random_device_config(self) -> Dict[str, Any]:
        """获取随机设备配置"""
        if self.device_type == 'pc':
            # 随机选择PC端User-Agent
            user_agent = random.choice(PC_USER_AGENTS)
            return {
                'name': 'PC',
                'user_agent': user_agent,
                'window_size': (1920, 1080)
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
            
            # 设置用户代理
            co.set_user_agent(self.device_config['user_agent'])
            
            # 设置窗口大小
            width, height = self.device_config['window_size']
            co.set_argument(f'--window-size={width},{height}')
            
            # 其他设置
            co.set_argument('--no-sandbox')
            co.set_argument('--disable-dev-shm-usage')
            co.set_argument('--disable-web-security')  # 允许跨域访问
            co.set_argument('--disable-features=VizDisplayCompositor')
            
            # 添加Linux系统特有的参数
            if platform.system().lower() == 'linux':
                import random
                # user_dir = f'/tmp/dp_user_{os.getpid()}_{random.randint(1000,9999)}'
                # port = random.randint(30000, 40000)
                # co.set_argument('--no-sandbox')
                # co.set_argument('--headless=new')
                # co.set_argument(f'--user-data-dir={user_dir}')
                # co.set_argument(f'--remote-debugging-port={port}')

                user_dir = f'/tmp/dp_user_{os.getpid()}_{random.randint(1000, 9999)}'
                port = random.randint(30000, 40000)
                co.set_argument('--no-sandbox')
                co.set_argument('--headless=new')
                co.set_argument(f'--user-data-dir={user_dir}')
                co.set_argument(f'--remote-debugging-port={port}')
            
            # 创建页面实例
            self.page = ChromiumPage(co)
            
            # 移除反检测JS注入
            # if self.page:
            #     self.page.run_js('''
            #         Object.defineProperty(navigator, 'webdriver', {
            #             get: () => undefined,
            #         });
            #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            #     ''')
            
            logger.info(f"✅ 浏览器初始化完成，设备类型: {self.device_type}, 设备: {self.device_config['name']}")
            
        except Exception as e:
            logger.error(f"❌ 浏览器初始化失败: {e}")
            raise
    
    def simulate_human_behavior(self):
        """模拟人类行为"""
        try:
            logger.info("开始模拟人类行为...")
            
            # 随机等待
            wait_time = random.uniform(2, 5)
            time.sleep(wait_time)
            
            # 随机滚动页面
            scroll_times = random.randint(1, 3)
            for _ in range(scroll_times):
                scroll_y = random.randint(100, 500)
                self.page.run_js(f'window.scrollBy(0, {scroll_y});')
                time.sleep(random.uniform(0.5, 1.5))
            
            # 随机移动鼠标（模拟）
            self.page.run_js('''
                // 模拟鼠标移动
                var event = new MouseEvent('mousemove', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: Math.random() * window.innerWidth,
                    clientY: Math.random() * window.innerHeight
                });
                document.dispatchEvent(event);
            ''')
            
            logger.info("✅ 人类行为模拟完成")
            
        except Exception as e:
            logger.debug(f"人类行为模拟出错: {e}")
    
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
                        
                        // 策略1.2: 模拟鼠标事件（更真实）
                        var rect = iframe.getBoundingClientRect();
                        var centerX = rect.left + rect.width / 2;
                        var centerY = rect.top + rect.height / 2;
                        
                        // 鼠标按下事件
                        var mousedownEvent = new MouseEvent('mousedown', {{
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: centerX,
                            clientY: centerY,
                            button: 0
                        }});
                        iframe.dispatchEvent(mousedownEvent);
                        
                        // 鼠标释放事件
                        var mouseupEvent = new MouseEvent('mouseup', {{
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: centerX,
                            clientY: centerY,
                            button: 0
                        }});
                        iframe.dispatchEvent(mouseupEvent);
                        
                        // 点击事件
                        var clickEvent = new MouseEvent('click', {{
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: centerX,
                            clientY: centerY,
                            button: 0
                        }});
                        iframe.dispatchEvent(clickEvent);
                        
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
    
    def run_simulation(self) -> bool:
        """运行广告点击模拟"""
        if not self.page:
            logger.error("❌ 页面未初始化")
            return False
        try:
            logger.info("🚀 开始广告点击模拟...")
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
    
    loop_count = 0
    
    while True:
        loop_count += 1
        logger.info(f"=" * 50)
        logger.info(f"开始第 {loop_count} 次循环")
        
        # 随机选择设备类型
        if device_type == 'random':
            current_device = random.choice(['pc', 'android', 'ios', 'ipad'])
            logger.info(f"随机选择设备类型: {current_device}")
        else:
            current_device = device_type
        
        simulator = None
        try:
            # 创建模拟器实例
            simulator = FinalAdSimulator(current_device)
            
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

if __name__ == "__main__":
    main() 