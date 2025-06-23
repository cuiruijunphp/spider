# 用户行为模拟器

这是一个Python程序，用于模拟真实用户的点击行为，特别针对网站广告弹窗的检测和交互。

## 功能特性

- **多设备支持**: 支持PC端、Android端和iOS端的用户行为模拟
- **真实用户行为**: 模拟人类滚动、点击等自然行为
- **广告弹窗检测**: 自动检测并处理广告iframe弹窗
- **智能点击**: 自动识别广告区域的可点击元素
- **页面跳转处理**: 处理新标签页的打开和页面加载
- **随机化行为**: 模拟用户的不确定性（是否滚动、是否点击广告等）
- **HTTP支持**: 支持访问不支持HTTPS的网站

## 安装要求

### 系统要求
- Python 3.7+
- Chrome浏览器
- ChromeDriver（与Chrome版本匹配）

### 安装步骤

1. **安装Python依赖**
```bash
pip install -r requirements.txt
```

2. **安装ChromeDriver**
   - 访问 [ChromeDriver官网](https://chromedriver.chromium.org/)
   - 下载与你的Chrome浏览器版本匹配的ChromeDriver
   - 将ChromeDriver添加到系统PATH中

## 使用方法

### 基本使用

```python
from sel.user_behavior_simulator import UserBehaviorSimulator

# 创建PC端用户行为模拟器
simulator = UserBehaviorSimulator(user_agent_type='pc')
simulator.simulate_user_behavior("http://mon.cuithink.com/")
```

### 模拟不同设备

```python
# PC端
simulator_pc = UserBehaviorSimulator(user_agent_type='pc')

# Android端
simulator_android = UserBehaviorSimulator(user_agent_type='android')

# iOS端
simulator_ios = UserBehaviorSimulator(user_agent_type='ios')
```

### 运行完整测试

```bash
python user_behavior_simulator.py
```

这将依次模拟PC、Android和iOS设备的用户行为。

### 快速测试

```bash
# 测试PC端
python quick_test.py pc

# 测试Android端
python quick_test.py android

# 测试iOS端
python quick_test.py ios

# 测试自定义URL
python quick_test.py pc "http://example.com"
```

## 程序流程

1. **初始化**: 根据设备类型设置相应的用户代理和窗口大小
2. **访问网页**: 打开目标网站（支持HTTP协议）
3. **模拟滚动**: 随机执行页面滚动行为（70%概率）
4. **等待广告**: 等待5-15秒后检查广告弹窗
5. **处理广告**: 
   - 如果检测到广告弹窗，60%概率点击广告区域
   - 如果点击，等待新页面加载完成
6. **清理资源**: 关闭浏览器

## 配置选项

### 用户代理设置
程序内置了三种设备的用户代理：
- PC: Windows Chrome
- Android: Samsung Galaxy S10 Chrome
- iOS: iPhone Safari

### 行为概率设置
- 滚动概率: 70%
- 点击广告概率: 60%
- 广告检测超时: 20秒
- 页面加载超时: 30秒

### 安全设置
程序已配置以下Chrome选项来处理HTTP网站：
- `--ignore-ssl-errors`: 忽略SSL错误
- `--ignore-certificate-errors`: 忽略证书错误
- `--allow-running-insecure-content`: 允许不安全内容
- `--disable-web-security`: 禁用Web安全限制

## 日志输出

程序会输出详细的日志信息，包括：
- 设备类型和初始化状态
- 用户行为选择（滚动、点击等）
- 广告检测结果
- 页面跳转状态
- 错误和警告信息

## 注意事项

1. **ChromeDriver版本**: 确保ChromeDriver版本与Chrome浏览器版本匹配
2. **网络连接**: 确保网络连接稳定，程序需要访问目标网站
3. **HTTP网站**: 程序已配置支持访问不支持HTTPS的网站
4. **反爬虫机制**: 程序已内置基本的反检测机制，但某些网站可能有更严格的反爬虫措施
5. **广告变化**: 网站广告可能会变化，可能需要调整检测逻辑

## 故障排除

### 常见问题

1. **ChromeDriver错误**
   - 确保ChromeDriver在PATH中
   - 检查ChromeDriver版本是否与Chrome浏览器匹配

2. **HTTPS连接错误**
   - 程序已配置忽略SSL错误，支持HTTP网站
   - 如果仍有问题，检查网络连接

3. **广告检测失败**
   - 检查网站是否仍然使用相同的iframe结构
   - 调整`wait_for_ad_popup`方法的超时时间

4. **页面加载超时**
   - 检查网络连接
   - 增加`wait_for_page_load`方法的超时时间

## 许可证

本项目仅供学习和研究使用，请遵守相关网站的使用条款和robots.txt规定。 