# SQL学习游戏 - iOS版本

## 项目介绍

这是SQL学习游戏的iOS原生应用版本，使用Swift开发，基于WKWebView技术加载现有的Web应用。

## 技术栈

- **开发语言**：Swift
- **构建工具**：Xcode
- **UI组件**：WKWebView
- **Web技术**：HTML5, CSS3, JavaScript, SQL.js

## 项目结构

```
ios-app/
└── SqlGame/
    ├── SqlGame/
    │   ├── ViewController.swift    # 主控制器
    │   ├── Resources/
    │   │   ├── index.html          # 主HTML文件
    │   │   ├── sql-wasm.js         # SQL.js库
    │   │   └── sql-wasm.wasm       # WebAssembly模块
    │   └── Info.plist             # 应用配置
    └── SqlGame.xcodeproj          # Xcode项目文件
```

## 如何构建和运行

### 前置条件

- Xcode 12.0+
- iOS 13.0+
- Mac电脑

### 构建步骤

1. **打开项目**：在Xcode中打开 `SqlGame.xcodeproj` 文件
2. **选择目标设备**：在顶部工具栏选择模拟器或连接的iOS设备
3. **构建项目**：点击 "Product > Build"
4. **运行应用**：点击 "Product > Run" 或使用快捷键 `Cmd+R`

### 运行方式

1. **通过Xcode运行**：连接iOS设备或使用模拟器
2. **通过TestFlight**：（可选）上传到TestFlight进行测试
3. **通过App Store**：（可选）提交到App Store发布

## 功能特性

- ✅ 真实SQL引擎执行（基于SQL.js）
- ✅ 关卡式学习模式
- ✅ 语法学习和提示
- ✅ 表结构查看
- ✅ 答案验证
- ✅ 标签标记功能
- ✅ 响应式布局（适配不同屏幕尺寸）
- ✅ 侧边栏展开/收起功能
- ✅ 触摸事件支持

## 技术实现

### WKWebView配置

- 启用JavaScript
- 启用DOM存储
- 支持文件访问
- 处理导航和错误
- 支持缩放

### 本地资源加载

应用使用本地Resources目录中的HTML、CSS、JavaScript和SQL.js文件，无需网络连接即可运行。

### 性能优化

- 使用WebAssembly提高SQL执行性能
- 启用缓存机制
- 优化WebView配置

## 已知问题

- 在某些旧设备上可能存在WebAssembly兼容性问题
- 首次加载时可能需要较长时间（WebAssembly文件较大）
- 移动设备上的SQL执行性能可能不如桌面端

## 未来计划

- [ ] 添加离线存储功能
- [ ] 优化移动设备性能
- [ ] 添加推送通知
- [ ] 实现原生UI组件

## 联系方式

- 项目地址：https://github.com/wenbo030509/SqlGame
- 分支：feature/ios-app

---

**注意**：本项目为学习工具，旨在帮助用户学习SQL语法和查询技巧。