# 广告点击模拟器

使用Python的DrissionPage库模拟真实用户的点击行为，支持PC端、安卓端、IOS端。

## 功能特点

- 🖥️ **多设备支持**: 支持PC、Android、iOS三种设备类型
- 🎯 **真实行为模拟**: 模拟人类滚动、鼠标移动、点击等行为
- ⏱️ **智能等待**: 自动等待广告框出现和新标签页加载
- 🛡️ **反检测机制**: 内置多种反检测技术，避免触发风控
- 📊 **详细日志**: 完整的操作日志记录
- ⚙️ **灵活配置**: 支持自定义各种参数

## 安装依赖

```bash
pip install -r requirements.txt
```

## 快速开始

### 基本使用

```python
from ad_click_simulator import AdClickSimulator

# 创建模拟器实例
simulator = AdClickSimulator(device_type='pc')

# 运行模拟
success = simulator.run_simulation()

# 关闭浏览器
simulator.close()
```

### 运行示例

```bash
# 运行主程序
python ad_click_simulator.py

# 运行使用示例
python example.py
```

## 程序流程

1. **打开目标网站**: 访问 `http://mon.cuithink.com/`
2. **等待广告框**: 等待右上角广告框出现（XPath: `/html/iframe[2]`）
3. **模拟人类行为**: 随机滚动页面、移动鼠标
4. **点击广告**: 点击广告区域（80%概率）
5. **等待新标签页**: 等待新标签页打开并加载完成
6. **完成模拟**: 验证新标签页URL不为空

## 配置说明

### 设备配置

在 `config.py` 中可以配置不同设备的参数：

```python
DEVICE_CONFIGS = {
    'pc': {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...',
        'window_size': (1920, 1080)
    },
    'android': {
        'user_agent': 'Mozilla/5.0 (Linux; Android 13; ...)',
        'window_size': (412, 915)
    },
    'ios': {
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS ...)',
        'window_size': (390, 844)
    }
}
```

### 人类行为配置

```python
HUMAN_BEHAVIOR_CONFIG = {
    'scroll_probability': 0.7,      # 滚动页面的概率
    'mouse_move_probability': 0.6,  # 移动鼠标的概率
    'click_ad_probability': 0.8,    # 点击广告的概率
    'wait_time_range': (1, 3),      # 等待时间范围（秒）
    'scroll_distance_range': (100, 500),  # 滚动距离范围（像素）
}
```

### 超时配置

```python
AD_FRAME_TIMEOUT = 30  # 广告框等待超时时间（秒）
NEW_TAB_TIMEOUT = 30   # 新标签页等待超时时间（秒）
```

## 反检测特性

### 浏览器配置

- 禁用自动化检测标识
- 禁用WebRTC以防止IP泄露
- 禁用图片加载以提高速度
- 随机用户代理字符串

### 行为模拟

- 随机等待时间
- 随机鼠标移动
- 随机页面滚动
- 真实点击行为（非JavaScript点击）

## 日志记录

程序会生成详细的日志文件 `ad_click_simulator.log`，包含：

- 操作步骤信息
- 错误和警告信息
- 调试信息
- 成功/失败状态

## 注意事项

1. **网络环境**: 确保网络连接稳定
2. **Chrome浏览器**: 需要安装Chrome浏览器
3. **权限问题**: 确保有足够的系统权限
4. **广告商风控**: 避免频繁运行，建议间隔一定时间
5. **法律合规**: 请确保使用符合相关法律法规

## 错误处理

程序包含完善的错误处理机制：

- 广告框未出现时自动结束
- 新标签页加载失败时的处理
- 浏览器异常时的清理
- 网络超时的重试机制

## 扩展功能

### 自定义选择器

可以在 `config.py` 中添加更多可点击元素选择器：

```python
CLICKABLE_SELECTORS = [
    'a', 'button', '[onclick]', '[role="button"]',
    '.ad-click', '.ad-link', '.clickable',
    '.advertisement', '.banner', '.promo',
    # 添加更多选择器...
]
```

### 自定义行为

可以修改 `simulate_human_behavior()` 方法来添加更多人类行为模拟。

## 技术支持

如果遇到问题，请检查：

1. 依赖是否正确安装
2. Chrome浏览器是否可用
3. 网络连接是否正常
4. 日志文件中的错误信息

## 许可证

本项目仅供学习和研究使用，请遵守相关法律法规。 