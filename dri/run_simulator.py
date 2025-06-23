#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
广告点击模拟器启动脚本
提供友好的命令行界面，支持循环执行和随机设备类型
"""

import sys
import os
import argparse
import subprocess

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='广告点击模拟器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python run_simulator.py                    # 随机设备类型，无限循环
  python run_simulator.py --device pc        # PC端，无限循环
  python run_simulator.py --device android   # Android端，无限循环
  python run_simulator.py --device ios       # iOS端，无限循环
  python run_simulator.py --device ipad      # iPad端，无限循环
  python run_simulator.py --loops 10         # 随机设备，执行10次循环
  python run_simulator.py --device pc --loops 5  # PC端，执行5次循环
  python run_simulator.py --sleep 20-60      # 自定义休眠时间范围
        """
    )
    
    parser.add_argument(
        '--device', 
        choices=['pc', 'android', 'ios', 'ipad', 'random'],
        default='random',
        help='设备类型 (默认: random)'
    )
    
    parser.add_argument(
        '--loops',
        type=int,
        default=0,
        help='最大循环次数，0表示无限循环 (默认: 0)'
    )
    
    parser.add_argument(
        '--sleep',
        type=str,
        default='10-30',
        help='休眠时间范围，格式: 最小值-最大值 (默认: 10-30)'
    )
    
    parser.add_argument(
        '--config',
        action='store_true',
        help='显示当前配置信息'
    )
    
    args = parser.parse_args()
    
    # 解析休眠时间
    try:
        min_sleep, max_sleep = map(int, args.sleep.split('-'))
        if min_sleep < 0 or max_sleep < min_sleep:
            raise ValueError("休眠时间格式错误")
    except:
        print("❌ 休眠时间格式错误，请使用 '最小值-最大值' 格式，如: 10-30")
        return
    
    # 显示配置信息
    if args.config:
        print("📋 当前配置:")
        print(f"  设备类型: {args.device}")
        print(f"  最大循环次数: {'无限' if args.loops == 0 else args.loops}")
        print(f"  休眠时间: {min_sleep}-{max_sleep} 秒")
        print()
    
    # 修改配置文件中的循环配置
    config_file = 'final_simulator.py'
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 更新循环配置
            import re
            pattern = r"LOOP_CONFIG = \{[^}]*\}"
            replacement = f"LOOP_CONFIG = {{\n    'min_sleep': {min_sleep},  # 最小休眠时间（秒）\n    'max_sleep': {max_sleep},  # 最大休眠时间（秒）\n    'max_loops': {args.loops},   # 最大循环次数，0表示无限循环\n}}"
            
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ 配置已更新: 休眠{min_sleep}-{max_sleep}秒，循环{args.loops if args.loops > 0 else '无限'}次")
            
        except Exception as e:
            print(f"❌ 更新配置文件失败: {e}")
            return
    
    # 启动模拟器
    print(f"🚀 启动广告点击模拟器...")
    print(f"   设备类型: {args.device}")
    print(f"   循环次数: {'无限' if args.loops == 0 else args.loops}")
    print(f"   休眠时间: {min_sleep}-{max_sleep} 秒")
    print()
    
    try:
        # 运行模拟器
        cmd = [sys.executable, 'final_simulator.py', args.device]
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n⏹️  用户中断程序")
    except subprocess.CalledProcessError as e:
        print(f"❌ 程序执行失败: {e}")
    except Exception as e:
        print(f"❌ 启动失败: {e}")

if __name__ == "__main__":
    main() 