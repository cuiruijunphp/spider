#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快代理IP池管理器
支持动态获取IP，每次循环使用同一个IP
"""

import os
import time
import string
import random
import logging
import requests
from typing import Optional, Dict, Any
from DrissionPage import ChromiumOptions

logger = logging.getLogger(__name__)

class ProxyManager:
    """快代理IP池管理器"""
    
    def __init__(self, username: str, password: str, api_url: Optional[str] = None):
        """
        初始化代理管理器
        
        Args:
            username: 快代理用户名
            password: 快代理密码
            api_url: 快代理API地址（可选）
        """
        self.username = username
        self.password = password
        self.api_url = api_url or "https://dps.kdlapi.com/api/getdps"
        self.current_proxy = None
        self.proxy_plugin_folder = None
        
    def get_proxy_from_pool(self) -> Optional[Dict[str, str]]:
        """
        从快代理IP池获取一个IP
        
        Returns:
            代理信息字典 {'host': 'ip', 'port': 'port'} 或 None
        """
        try:
            # 构建API请求参数
            params = {
                'secret_id': 'oztt6ms7csmncg9o2358',
                'signature': 'lb95dxyd9t95nnksssux9x7c3mteu92v',
                'num': 1,  # 获取1个IP
                'format': 'json',
                'sep': 1
            }
            
            logger.info("正在从快代理IP池获取IP...")
            response = requests.get(self.api_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 0:  # 成功
                    proxy_list = data.get('data', {}).get('proxy_list', [])
                    if proxy_list:
                        proxy_info = proxy_list[0]
                        # 解析代理信息
                        if ':' in proxy_info:
                            host, port = proxy_info.split(':', 1)
                            proxy = {
                                'host': host.strip(),
                                'port': port.strip()
                            }
                            logger.info(f"✅ 成功获取代理IP: {proxy['host']}:{proxy['port']}")
                            return proxy
                        else:
                            logger.error(f"❌ 代理信息格式错误: {proxy_info}")
                    else:
                        logger.error("❌ IP池中没有可用IP")
                else:
                    logger.error(f"❌ 获取IP失败: {data.get('msg', '未知错误')}")
            else:
                logger.error(f"❌ API请求失败: HTTP {response.status_code}")
                
        except Exception as e:
            logger.error(f"❌ 获取代理IP时出错: {e}")
            
        return None
    
    def create_proxy_extension(self, proxy_host: str, proxy_port: str, scheme: str = 'http') -> str:
        """
        创建代理认证扩展
        
        Args:
            proxy_host: 代理主机
            proxy_port: 代理端口
            scheme: 代理协议 (http/https)
            
        Returns:
            扩展文件夹路径
        """
        plugin_folder = f'kdl_proxy_{proxy_host}_{proxy_port}'
        
        if not os.path.exists(plugin_folder):
            os.makedirs(plugin_folder)
            
        # 创建manifest.json
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "KDL Proxy Extension",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking",
                "browsingData"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """
        
        # 创建background.js
        background_js = string.Template("""
        var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
            },
            bypassList: []
            }
        };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        """).substitute(
            host=proxy_host,
            port=proxy_port,
            username=self.username,
            password=self.password,
            scheme=scheme,
        )
        
        # 写入文件
        with open(os.path.join(plugin_folder, "manifest.json"), "w", encoding='utf-8') as f:
            f.write(manifest_json)
        with open(os.path.join(plugin_folder, "background.js"), "w", encoding='utf-8') as f:
            f.write(background_js)
            
        logger.info(f"✅ 代理扩展创建成功: {plugin_folder}")
        return plugin_folder
    
    def get_new_proxy(self) -> Optional[Dict[str, Any]]:
        """
        获取新的代理配置
        
        Returns:
            代理配置字典，包含代理信息和扩展路径
        """
        # 清理旧的扩展文件夹
        if self.proxy_plugin_folder and os.path.exists(self.proxy_plugin_folder):
            try:
                import shutil
                shutil.rmtree(self.proxy_plugin_folder)
                logger.info(f"清理旧代理扩展: {self.proxy_plugin_folder}")
            except Exception as e:
                logger.debug(f"清理旧扩展失败: {e}")
        
        # 获取新代理
        proxy = self.get_proxy_from_pool()
        if not proxy:
            return None
            
        # 创建代理扩展
        try:
            plugin_folder = self.create_proxy_extension(
                proxy_host=proxy['host'],
                proxy_port=proxy['port']
            )
            
            self.current_proxy = proxy
            self.proxy_plugin_folder = plugin_folder
            
            # 打印新获取的代理IP
            logger.info(f"🔄 获取新代理IP: {proxy['host']}:{proxy['port']}")
            
            return {
                'proxy': proxy,
                'plugin_folder': plugin_folder
            }
            
        except Exception as e:
            logger.error(f"❌ 创建代理扩展失败: {e}")
            return None
    
    def apply_proxy_to_options(self, co: ChromiumOptions, proxy_config: Dict[str, Any]) -> bool:
        """
        将代理配置应用到ChromiumOptions
        
        Args:
            co: ChromiumOptions实例
            proxy_config: 代理配置
            
        Returns:
            是否成功应用
        """
        try:
            if not proxy_config or 'plugin_folder' not in proxy_config:
                return False
                
            plugin_folder = proxy_config['plugin_folder']
            if not os.path.exists(plugin_folder):
                logger.error(f"❌ 代理扩展文件夹不存在: {plugin_folder}")
                return False
                
            # 添加扩展
            co.add_extension(plugin_folder)
            logger.info(f"✅ 代理已应用到浏览器选项: {proxy_config['proxy']['host']}:{proxy_config['proxy']['port']}")
            return True
            
        except Exception as e:
            logger.error(f"❌ 应用代理配置失败: {e}")
            return False
    
    def get_current_proxy_info(self) -> Optional[Dict[str, str]]:
        """获取当前代理信息"""
        return self.current_proxy
    
    def cleanup(self):
        """清理资源"""
        if self.proxy_plugin_folder and os.path.exists(self.proxy_plugin_folder):
            try:
                import shutil
                shutil.rmtree(self.proxy_plugin_folder)
                logger.info(f"清理代理扩展: {self.proxy_plugin_folder}")
            except Exception as e:
                logger.debug(f"清理代理扩展失败: {e}")


# 测试函数
def test_proxy_manager():
    """测试代理管理器"""
    # 配置信息
    username = 'd4476434639'
    password = 'a34pvq6n'
    
    proxy_manager = ProxyManager(username, password)
    
    # 获取代理
    proxy_config = proxy_manager.get_new_proxy()
    if proxy_config:
        print(f"获取到代理: {proxy_config['proxy']}")
        print(f"扩展文件夹: {proxy_config['plugin_folder']}")
        
        # 测试应用到浏览器选项
        co = ChromiumOptions()
        success = proxy_manager.apply_proxy_to_options(co, proxy_config)
        print(f"应用代理成功: {success}")
        
        # 清理
        proxy_manager.cleanup()
    else:
        print("获取代理失败")


if __name__ == "__main__":
    test_proxy_manager() 