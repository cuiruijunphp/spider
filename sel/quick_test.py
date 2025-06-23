#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试脚本 - 模拟单个设备类型的用户行为
"""

import sys
import time
from user_behavior_simulator import UserBehaviorSimulator

def quick_test(device_type='pc', url="http://mon.cuithink.com/"):
    """
    快速测试函数
    
    Args:
        device_type: 设备类型 ('pc', 'android', 'ios')
        url: 要访问的网址
    """
    print(f"开始快速测试 - 设备类型: {device_type.upper()}")
    print(f"目标网址: {url}")
    print("-" * 50)
    
    try:
        # 创建模拟器
        simulator = UserBehaviorSimulator(user_agent_type=device_type)
        
        # 执行用户行为模拟
        simulator.simulate_user_behavior(url)
        
        print("测试完成！")
        
    except Exception as e:
        print(f"测试过程中出现错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 获取命令行参数
    device_type = 'pc'  # 默认PC端
    url = "http://mon.cuithink.com/"  # 默认网址
    
    if len(sys.argv) > 1:
        device_type = sys.argv[1].lower()
    
    if len(sys.argv) > 2:
        url = sys.argv[2]
    
    # 验证设备类型
    valid_devices = ['pc', 'android', 'ios']
    if device_type not in valid_devices:
        print(f"错误: 设备类型必须是 {', '.join(valid_devices)} 之一")
        print(f"用法: python quick_test.py [device_type] [url]")
        sys.exit(1)
    
    # 执行测试
    quick_test(device_type, url) 