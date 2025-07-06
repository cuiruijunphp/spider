#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的代理测试脚本
用于验证代理功能是否正常工作
"""

import requests
import json
import time

def test_proxy_api():
    """测试快代理API"""
    print("🔍 测试快代理API连接...")
    
    # 快代理API参数
    params = {
        'secret_id': 'oztt6ms7csmncg9o2358',
        'signature': 'lb95dxyd9t95nnksssux9x7c3mteu92v',
        'num': 1,
        'format': 'json',
        'sep': 1
    }
    
    api_url = 'https://dps.kdlapi.com/api/getdps'
    
    try:
        print(f"请求URL: {api_url}")
        print(f"参数: {params}")
        
        response = requests.get(api_url, params=params, timeout=10)
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"JSON数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
            
            if data.get('code') == 0:
                proxy_list = data.get('data', {}).get('proxy_list', [])
                if proxy_list:
                    print(f"✅ 成功获取代理: {proxy_list[0]}")
                    return True
                else:
                    print("❌ 代理列表为空")
            else:
                print(f"❌ API返回错误: {data.get('msg', '未知错误')}")
        else:
            print(f"❌ HTTP请求失败: {response.status_code}")
            
    except Exception as e:
        print(f"❌ 请求出错: {e}")
    
    return False

def test_httpbin():
    """测试httpbin.org"""
    print("\n🌐 测试httpbin.org连接...")
    
    try:
        response = requests.get('https://httpbin.org/ip', timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 当前IP: {data.get('origin', '未知')}")
            return True
        else:
            print(f"❌ httpbin请求失败: {response.status_code}")
    except Exception as e:
        print(f"❌ httpbin请求出错: {e}")
    
    return False

def main():
    """主函数"""
    print("快代理API测试")
    print("=" * 50)
    
    # 测试网络连接
    if test_httpbin():
        print("✅ 网络连接正常")
    else:
        print("❌ 网络连接有问题")
        return
    
    # 测试代理API
    if test_proxy_api():
        print("✅ 代理API测试成功")
    else:
        print("❌ 代理API测试失败")
        print("\n可能的原因:")
        print("1. 快代理账户信息不正确")
        print("2. 账户余额不足")
        print("3. API权限未开通")
        print("4. 网络连接问题")

if __name__ == "__main__":
    main() 