#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安装脚本
帮助用户快速设置广告点击模拟器环境
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """检查Python版本"""
    print("检查Python版本...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ 需要Python 3.7或更高版本")
        print(f"当前版本: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro}")
        return True

def check_chrome():
    """检查Chrome浏览器"""
    print("检查Chrome浏览器...")
    
    system = platform.system().lower()
    
    if system == "windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
        ]
    elif system == "darwin":  # macOS
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    else:  # Linux
        chrome_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium-browser",
            "/usr/bin/chrome"
        ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✅ Chrome浏览器已找到: {path}")
            return True
    
    print("❌ 未找到Chrome浏览器")
    print("请安装Chrome浏览器后再运行此脚本")
    return False

def install_dependencies():
    """安装依赖包"""
    print("安装依赖包...")
    
    try:
        # 升级pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("✅ pip已升级")
        
        # 安装依赖
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖包安装完成")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 依赖包安装失败: {e}")
        return False

def test_imports():
    """测试导入"""
    print("测试模块导入...")
    
    try:
        import DrissionPage
        print("✅ DrissionPage导入成功")
        
        from DrissionPage import ChromiumPage, ChromiumOptions
        print("✅ DrissionPage组件导入成功")
        
        return True
        
    except ImportError as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def create_test_script():
    """创建测试脚本"""
    test_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单测试脚本
"""

from ad_click_simulator import AdClickSimulator
import time

def test():
    print("开始测试...")
    
    simulator = None
    try:
        # 创建模拟器（不实际运行）
        simulator = AdClickSimulator(device_type='pc')
        print("✅ 模拟器创建成功")
        
        # 简单测试
        print("✅ 测试完成")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
    
    finally:
        if simulator:
            simulator.close()

if __name__ == "__main__":
    test()
'''
    
    with open("test_installation.py", "w", encoding="utf-8") as f:
        f.write(test_script)
    
    print("✅ 测试脚本已创建: test_installation.py")

def main():
    """主函数"""
    print("=" * 50)
    print("广告点击模拟器 - 环境安装脚本")
    print("=" * 50)
    
    # 检查Python版本
    if not check_python_version():
        return False
    
    # 检查Chrome浏览器
    if not check_chrome():
        return False
    
    # 安装依赖包
    if not install_dependencies():
        return False
    
    # 测试导入
    if not test_imports():
        return False
    
    # 创建测试脚本
    create_test_script()
    
    print("\n" + "=" * 50)
    print("✅ 环境安装完成！")
    print("=" * 50)
    
    print("\n下一步操作:")
    print("1. 运行测试: python test_installation.py")
    print("2. 运行主程序: python ad_click_simulator.py")
    print("3. 查看示例: python example.py")
    print("4. 查看文档: README.md")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 