# 增强版广告点击模拟器

基于 `final_simulator.py` 的增强版本，支持循环执行、随机设备类型和配置文件管理。

## 🆕 新增功能

### 1. 循环执行
- 支持无限循环或指定次数循环
- 每次循环结束后随机休眠 10-30 秒（可自定义）
- 自动重启浏览器，避免内存泄漏

### 2. 随机设备类型
- 支持 PC、Android、iOS、iPad 四种设备类型
- 每次循环随机选择设备类型
- 每种设备类型都有多个预置配置

### 3. 配置文件管理
- PC端：20+ 种不同的 User-Agent（Chrome、Firefox、Edge、Safari等）
- Android：12+ 种热门机型（Samsung、Google Pixel、OnePlus、Xiaomi等）
- iOS：25+ 种iPhone机型（iPhone 8到iPhone 15 Pro Max）
- iPad：6种iPad机型

## 📁 文件结构

```
dri/
├── final_simulator.py      # 增强版主程序
├── run_simulator.py        # 启动脚本（推荐使用）
├── config/
│   └── devices.py          # 设备配置文件
└── README_enhanced.md      # 本文件
```

## 🚀 使用方法

### 方法一：使用启动脚本（推荐）

```bash
# 随机设备类型，无限循环
python run_simulator.py

# 指定设备类型
python run_simulator.py --device pc
python run_simulator.py --device android
python run_simulator.py --device ios
python run_simulator.py --device ipad

# 指定循环次数
python run_simulator.py --loops 10
python run_simulator.py --device pc --loops 5

# 自定义休眠时间
python run_simulator.py --sleep 20-60

# 查看帮助
python run_simulator.py --help

# 显示当前配置
python run_simulator.py --config
```

### 方法二：直接运行主程序

```bash
# 随机设备类型
python final_simulator.py random

# 指定设备类型
python final_simulator.py pc
python final_simulator.py android
python final_simulator.py ios
python final_simulator.py ipad
```

## ⚙️ 配置说明

### 循环配置
在 `final_simulator.py` 中修改 `LOOP_CONFIG`：

```python
LOOP_CONFIG = {
    'min_sleep': 10,  # 最小休眠时间（秒）
    'max_sleep': 30,  # 最大休眠时间（秒）
    'max_loops': 0,   # 最大循环次数，0表示无限循环
}
```

### 设备配置
在 `config/devices.py` 中可以：
- 添加新的 User-Agent
- 添加新的设备型号
- 修改窗口尺寸

## 📊 设备配置详情

### PC端 User-Agent
- Chrome浏览器（Windows/macOS/Linux）
- Firefox浏览器（Windows/Linux）
- Edge浏览器（Windows）
- Safari浏览器（macOS）

### Android设备
- Samsung Galaxy S24/S23/S22/A54
- Google Pixel 8/7
- OnePlus 11
- Xiaomi 13
- OPPO Find X6
- vivo X90
- Huawei P60
- Redmi Note 12

### iOS设备
- iPhone 15 Pro Max/Pro/Plus
- iPhone 14 Pro Max/Pro/Plus
- iPhone 13 Pro Max/Pro/mini
- iPhone 12 Pro Max/Pro/mini
- iPhone 11 Pro Max/Pro
- iPhone XS Max/XS/XR/X
- iPhone 8 Plus/8
- iPhone SE (2nd/3rd generation)

### iPad设备
- iPad Pro 12.9-inch/11-inch
- iPad Air (5th generation)
- iPad (10th/9th generation)
- iPad mini (6th generation)

## 🔧 高级配置

### 修改休眠时间
```bash
# 设置休眠时间为30-60秒
python run_simulator.py --sleep 30-60
```

### 限制循环次数
```bash
# 只执行5次循环
python run_simulator.py --loops 5
```

### 组合使用
```bash
# PC端，执行10次循环，每次休眠20-40秒
python run_simulator.py --device pc --loops 10 --sleep 20-40
```

## 📝 日志输出

程序会输出详细的日志信息：
- 每次循环的设备类型和具体设备
- 休眠时间
- 执行结果
- 错误信息

日志文件：`final_simulator.log`

## ⚠️ 注意事项

1. **内存管理**：每次循环都会重新启动浏览器，避免内存泄漏
2. **反检测**：每次使用不同的设备配置，降低被检测风险
3. **随机性**：休眠时间、设备选择都是随机的，模拟真实用户行为
4. **错误处理**：单次循环失败不会影响整体执行

## 🛠️ 故障排除

### 导入错误
如果遇到 `devices` 模块导入错误，确保：
1. `config` 目录存在
2. `config/devices.py` 文件存在
3. 在 `dri` 目录下运行程序

### 浏览器启动失败
1. 检查 Chrome 浏览器是否安装
2. 检查 DrissionPage 是否正确安装
3. 检查网络连接

### 循环中断
- 使用 `Ctrl+C` 可以安全中断程序
- 程序会自动关闭浏览器

## 📈 性能优化建议

1. **合理设置休眠时间**：避免过于频繁的请求
2. **监控系统资源**：长时间运行注意内存和CPU使用
3. **定期检查日志**：及时发现和处理错误
4. **网络环境**：确保网络稳定，避免连接超时

## 🔄 更新日志

### v2.0 (当前版本)
- ✅ 新增循环执行功能
- ✅ 新增随机设备类型选择
- ✅ 新增设备配置文件
- ✅ 新增启动脚本
- ✅ 优化日志输出
- ✅ 增强错误处理

### v1.0 (原版本)
- ✅ 基础广告点击功能
- ✅ 多策略点击
- ✅ 反检测机制 