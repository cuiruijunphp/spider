#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快代理集成示例
演示如何在广告点击模拟器中使用快代理IP池
"""

import sys
import os
import time
import random
import logging

# 添加当前目录到路径
sys.path.append(os.path.dirname(__file__))

from proxy_manager import ProxyManager
from final_simulator import FinalAdSimulator, PROXY_CONFIG, LOOP_CONFIG

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_proxy_connection():
    """测试代理连接"""
    logger.info("🔍 测试代理连接...")
    
    proxy_manager = ProxyManager(
        username=PROXY_CONFIG['username'],
        password=PROXY_CONFIG['password']
    )
    
    # 获取代理
    proxy_config = proxy_manager.get_new_proxy()
    if not proxy_config:
        logger.error("❌ 无法获取代理IP")
        return False
    
    logger.info(f"✅ 获取到代理: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")
    
    # 测试代理
    try:
        simulator = FinalAdSimulator('pc', proxy_config)
        
        # 测试访问一个简单的网站
        logger.info("🌐 测试访问网站...")
        if simulator.page:
            simulator.page.get('https://httpbin.org/ip')
            time.sleep(2)
            
            # 获取页面内容
            content = simulator.page.html
            if content and 'origin' in content:
                logger.info("✅ 代理连接测试成功")
                logger.info(f"当前IP: {content}")
            else:
                logger.warning("⚠️ 代理连接可能有问题")
        else:
            logger.error("❌ 页面未初始化")
        
        simulator.close()
        proxy_manager.cleanup()
        return True
        
    except Exception as e:
        logger.error(f"❌ 代理测试失败: {e}")
        return False

def run_with_proxy():
    """使用代理运行模拟器"""
    logger.info("🚀 启动带代理的广告点击模拟器")
    
    # 代理管理器
    proxy_manager = ProxyManager(
        username=PROXY_CONFIG['username'],
        password=PROXY_CONFIG['password']
    )
    
    loop_count = 0
    max_loops = 3  # 测试用，只运行3次
    
    while loop_count < max_loops:
        loop_count += 1
        logger.info(f"=" * 50)
        logger.info(f"开始第 {loop_count} 次循环")
        
        # 获取新的代理IP
        proxy_config = None
        try:
            proxy_config = proxy_manager.get_new_proxy()
            if proxy_config:
                logger.info(f"✅ 获取新代理IP: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")
            else:
                logger.warning("⚠️ 获取代理IP失败，将使用直连")
        except Exception as e:
            logger.error(f"❌ 获取代理IP时出错: {e}")
        
        # 随机选择设备类型
        device_type = random.choice(['pc', 'android', 'ios', 'ipad'])
        logger.info(f"随机选择设备类型: {device_type}")
        
        simulator = None
        try:
            # 创建模拟器实例
            simulator = FinalAdSimulator(device_type, proxy_config)
            
            # 运行模拟
            success = simulator.run_simulation()
            
            if success:
                logger.info(f"🎉 第 {loop_count} 次循环完成")
            else:
                logger.warning(f"⚠️ 第 {loop_count} 次循环未完全成功")
            
            time.sleep(5)
            
        except Exception as e:
            logger.error(f"❌ 第 {loop_count} 次循环执行出错: {e}")
        
        finally:
            if simulator:
                simulator.close()
        
        # 休眠
        sleep_time = random.uniform(LOOP_CONFIG['min_sleep'], LOOP_CONFIG['max_sleep'])
        logger.info(f"休眠 {sleep_time:.1f} 秒后开始下次循环...")
        time.sleep(sleep_time)
    
    # 清理
    proxy_manager.cleanup()
    logger.info("✅ 程序结束")

def main():
    """主函数"""
    print("快代理集成示例")
    print("=" * 50)
    print("1. 测试代理连接")
    print("2. 运行带代理的模拟器")
    print("3. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-3): ").strip()
        
        if choice == '1':
            test_proxy_connection()
        elif choice == '2':
            run_with_proxy()
        elif choice == '3':
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main() 