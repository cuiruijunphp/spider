#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安装脚本 - 自动安装用户行为模拟器所需的依赖
"""

import subprocess
import sys
import os

def run_command(command, description):
    """运行命令并处理错误"""
    print(f"正在{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description}成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description}失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False

def check_python_version():
    """检查Python版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("✗ Python版本过低，需要Python 3.7或更高版本")
        print(f"当前版本: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python版本检查通过: {version.major}.{version.minor}.{version.micro}")
    return True

def install_python_dependencies():
    """安装Python依赖包"""
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "安装Python依赖包"
    )

def check_chrome():
    """检查Chrome浏览器是否安装"""
    try:
        # 尝试导入selenium来检查是否安装成功
        import selenium
        print("✓ Selenium已安装")
        return True
    except ImportError:
        print("✗ Selenium未安装")
        return False

def main():
    """主安装函数"""
    print("=" * 50)
    print("用户行为模拟器 - 安装脚本")
    print("=" * 50)
    
    # 检查Python版本
    if not check_python_version():
        sys.exit(1)
    
    # 安装Python依赖
    if not install_python_dependencies():
        print("请手动安装依赖: pip install -r requirements.txt")
        sys.exit(1)
    
    # 检查Chrome
    if not check_chrome():
        print("请确保Chrome浏览器已安装")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("安装完成！")
    print("=" * 50)
    print("\n使用方法:")
    print("1. 运行完整测试: python user_behavior_simulator.py")
    print("2. 快速测试: python quick_test.py [pc|android|ios]")
    print("\n注意事项:")
    print("- 确保Chrome浏览器已安装")
    print("- 确保网络连接正常")
    print("- 首次运行可能需要较长时间")

if __name__ == "__main__":
    main() 