#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试代理IP打印功能
"""

import sys
import os
import time
import logging

# 添加当前目录到路径
sys.path.append(os.path.dirname(__file__))

from proxy_manager import ProxyManager
from final_simulator import FinalAdSimulator, PROXY_CONFIG

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_proxy_ip_print():
    """测试代理IP打印功能"""
    logger.info("🧪 测试代理IP打印功能")
    
    # 创建代理管理器
    proxy_manager = ProxyManager(
        username=PROXY_CONFIG['username'],
        password=PROXY_CONFIG['password']
    )
    
    # 获取代理配置
    proxy_config = proxy_manager.get_new_proxy()
    if not proxy_config:
        logger.error("❌ 无法获取代理IP")
        return False
    
    logger.info(f"✅ 获取到代理配置: {proxy_config['proxy']}")
    
    # 创建模拟器
    simulator = FinalAdSimulator('pc', proxy_config)
    
    # 运行模拟（会打印代理IP）
    success = simulator.run_simulation()
    
    # 清理资源
    simulator.close()
    proxy_manager.cleanup()
    
    return success

def test_multiple_loops():
    """测试多次循环的代理IP打印"""
    logger.info("🔄 测试多次循环的代理IP打印")
    
    # 代理管理器
    proxy_manager = ProxyManager(
        username=PROXY_CONFIG['username'],
        password=PROXY_CONFIG['password']
    )
    
    for i in range(3):  # 测试3次循环
        logger.info(f"=" * 50)
        logger.info(f"开始第 {i+1} 次循环测试")
        
        # 获取新代理
        proxy_config = proxy_manager.get_new_proxy()
        if proxy_config:
            logger.info(f"✅ 第 {i+1} 次循环使用代理IP: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")
            
            # 创建模拟器
            simulator = FinalAdSimulator('pc', proxy_config)
            
            # 运行模拟
            success = simulator.run_simulation()
            
            # 清理
            simulator.close()
            
            if success:
                logger.info(f"🎉 第 {i+1} 次循环完成")
            else:
                logger.warning(f"⚠️ 第 {i+1} 次循环未完全成功")
        else:
            logger.warning("⚠️ 获取代理IP失败")
        
        # 休眠
        time.sleep(5)
    
    # 清理
    proxy_manager.cleanup()
    logger.info("✅ 多次循环测试完成")

def main():
    """主函数"""
    print("代理IP打印功能测试")
    print("=" * 50)
    print("1. 测试单次代理IP打印")
    print("2. 测试多次循环代理IP打印")
    print("3. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-3): ").strip()
        
        if choice == '1':
            test_proxy_ip_print()
        elif choice == '2':
            test_multiple_loops()
        elif choice == '3':
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main() 