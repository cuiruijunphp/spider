# 快代理IP池集成说明

## 概述

本项目已集成快代理IP池功能，支持在广告点击模拟过程中动态切换IP地址，提高反检测能力。

## 功能特点

- ✅ **动态IP切换**: 每次循环自动获取新IP
- ✅ **代理认证**: 自动处理快代理的用户名密码认证
- ✅ **资源管理**: 自动清理代理扩展文件
- ✅ **错误处理**: 代理失败时自动降级为直连
- ✅ **日志记录**: 详细的代理使用日志

## 文件结构

```
dri/
├── proxy_manager.py      # 代理管理器
├── final_simulator.py    # 集成代理的模拟器
├── proxy_example.py      # 使用示例
└── README_proxy.md       # 本说明文档
```

## 配置说明

### 1. 代理配置

在 `final_simulator.py` 中修改 `PROXY_CONFIG`:

```python
PROXY_CONFIG = {
    'enabled': True,  # 是否启用代理
    'username': 'your_username',  # 快代理用户名
    'password': 'your_password',  # 快代理密码
    'api_url': 'https://dps.kdlapi.com/api/getdps'  # 快代理API地址
}
```

### 2. 循环配置

```python
LOOP_CONFIG = {
    'min_sleep': 10,  # 最小休眠时间（秒）
    'max_sleep': 30,  # 最大休眠时间（秒）
    'max_loops': 20,   # 最大循环次数，0表示无限循环
}
```

## 使用方法

### 方法1: 直接运行模拟器

```bash
# 使用PC设备
python final_simulator.py pc

# 使用随机设备
python final_simulator.py random

# 使用Android设备
python final_simulator.py android
```

### 方法2: 使用示例程序

```bash
python proxy_example.py
```

然后选择：
1. 测试代理连接
2. 运行带代理的模拟器
3. 退出

### 方法3: 在代码中使用

```python
from proxy_manager import ProxyManager
from final_simulator import FinalAdSimulator

# 创建代理管理器
proxy_manager = ProxyManager(
    username='your_username',
    password='your_password'
)

# 获取代理配置
proxy_config = proxy_manager.get_new_proxy()

# 创建模拟器（传入代理配置）
simulator = FinalAdSimulator('pc', proxy_config)

# 运行模拟
success = simulator.run_simulation()

# 清理资源
simulator.close()
proxy_manager.cleanup()
```

## 工作原理

### 1. IP获取流程

1. 调用快代理API获取新IP
2. 创建Chrome扩展进行代理认证
3. 将扩展添加到浏览器选项
4. 启动浏览器使用代理

### 2. 循环机制

- **每次循环**: 获取新的代理IP
- **同一循环内**: 使用同一个IP进行所有操作
- **循环结束**: 清理代理资源，准备下次循环

### 3. 错误处理

- 代理获取失败 → 使用直连
- 代理连接失败 → 自动重试或降级
- 扩展创建失败 → 记录错误并继续

## 日志输出示例

```
2024-01-01 10:00:00 - INFO - 启动广告点击模拟器
2024-01-01 10:00:00 - INFO - 代理管理器已初始化
2024-01-01 10:00:01 - INFO - ==================================================
2024-01-01 10:00:01 - INFO - 开始第 1 次循环
2024-01-01 10:00:01 - INFO - 正在从快代理IP池获取IP...
2024-01-01 10:00:02 - INFO - ✅ 成功获取代理IP: 1.2.3.4:8080
2024-01-01 10:00:02 - INFO - ✅ 代理扩展创建成功: kdl_proxy_1.2.3.4_8080
2024-01-01 10:00:02 - INFO - ✅ 获取新代理IP: 1.2.3.4:8080
2024-01-01 10:00:02 - INFO - 随机选择设备类型: pc
2024-01-01 10:00:02 - INFO - 开始初始化浏览器，设备类型: pc, 设备: PC
2024-01-01 10:00:03 - INFO - ✅ 代理已应用到浏览器选项: 1.2.3.4:8080
2024-01-01 10:00:03 - INFO - ✅ 浏览器初始化完成，设备类型: pc, 设备: PC, 会话ID: a1b2c3d4
```

## 注意事项

### 1. 快代理账户

- 确保快代理账户有足够的IP配额
- 检查账户余额和有效期
- 确认API权限已开通

### 2. 网络环境

- 确保服务器能访问快代理API
- 检查防火墙设置
- 验证网络连接稳定性

### 3. 资源管理

- 代理扩展文件会自动清理
- 建议定期检查临时文件
- 监控磁盘空间使用

### 4. 性能优化

- 合理设置循环间隔
- 避免频繁切换IP
- 监控代理响应时间

## 故障排除

### 1. 代理获取失败

```
❌ 获取IP失败: 账户余额不足
```

**解决方案**: 检查快代理账户余额

### 2. 代理连接超时

```
❌ API请求失败: HTTP 408
```

**解决方案**: 检查网络连接，增加超时时间

### 3. 扩展创建失败

```
❌ 创建代理扩展失败: Permission denied
```

**解决方案**: 检查文件权限，确保有写入权限

### 4. 浏览器启动失败

```
❌ 浏览器初始化失败: 端口被占用
```

**解决方案**: 检查端口占用情况，修改端口配置

## 技术支持

如遇到问题，请检查：

1. 快代理账户状态
2. 网络连接情况
3. 日志输出信息
4. 系统资源使用

## 更新日志

- **v1.0**: 初始版本，支持基本代理功能
- **v1.1**: 增加错误处理和资源管理
- **v1.2**: 优化日志输出和配置管理 