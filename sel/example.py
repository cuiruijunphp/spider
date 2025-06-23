#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户行为模拟器 - 使用示例
"""

from user_behavior_simulator import UserBehaviorSimulator
import time

def example_basic_usage():
    """基本使用示例"""
    print("=== 基本使用示例 ===")
    
    # 创建PC端模拟器
    simulator = UserBehaviorSimulator(user_agent_type='pc')
    
    # 模拟用户行为
    simulator.simulate_user_behavior("http://mon.cuithink.com/")

def example_mobile_devices():
    """移动设备示例"""
    print("=== 移动设备示例 ===")
    
    # 测试Android设备
    print("测试Android设备...")
    android_simulator = UserBehaviorSimulator(user_agent_type='android')
    android_simulator.simulate_user_behavior()
    
    time.sleep(2)
    
    # 测试iOS设备
    print("测试iOS设备...")
    ios_simulator = UserBehaviorSimulator(user_agent_type='ios')
    ios_simulator.simulate_user_behavior()

def main():
    """主函数 - 运行示例"""
    print("用户行为模拟器 - 使用示例")
    print("=" * 50)
    
    try:
        # 运行基本示例
        example_basic_usage()
        time.sleep(2)
        
        # 运行移动设备示例
        example_mobile_devices()
        
    except KeyboardInterrupt:
        print("\n用户中断执行")
    except Exception as e:
        print(f"执行过程中出现错误: {e}")
    
    print("\n所有示例执行完成！")

if __name__ == "__main__":
    main() 