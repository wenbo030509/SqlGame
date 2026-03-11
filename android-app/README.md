# SQL学习游戏 - Android版本

## 项目介绍

这是SQL学习游戏的Android原生应用版本，使用Kotlin开发，基于WebView技术加载现有的Web应用。

## 技术栈

- **开发语言**：Kotlin
- **构建工具**：Gradle
- **UI组件**：WebView
- **Web技术**：HTML5, CSS3, JavaScript, SQL.js

## 项目结构

```
android-app/
├── app/
│   ├── src/main/
│   │   ├── java/com/sqlgame/
│   │   │   └── MainActivity.kt    # 主活动
│   │   ├── res/layout/
│   │   │   └── activity_main.xml   # 主布局
│   │   ├── assets/
│   │   │   ├── index.html          # 主HTML文件
│   │   │   ├── sql-wasm.js         # SQL.js库
│   │   │   └── sql-wasm.wasm       # WebAssembly模块
│   │   └── AndroidManifest.xml     # 应用配置
│   └── build.gradle                # 模块配置
└── build.gradle                    # 项目配置
```

## 如何构建和运行

### 前置条件

- Android Studio 4.0+
- JDK 8+
- Android SDK (API Level 24+)

### 构建步骤

1. **打开项目**：在Android Studio中打开 `android-app` 目录
2. **同步依赖**：等待Gradle同步完成
3. **构建项目**：点击 "Build > Build Bundle(s) / APK(s) > Build APK(s)"
4. **安装应用**：将生成的APK文件安装到Android设备

### 运行方式

1. **通过Android Studio运行**：
   - 连接Android设备到电脑
   - 点击 "Run > Run 'app'"
   - 选择目标设备

2. **通过APK安装**：
   - 在 `android-app/app/build/outputs/apk/debug/` 目录找到生成的APK文件
   - 将APK文件传输到Android设备
   - 在设备上安装并运行

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

### WebView配置

- 启用JavaScript
- 启用DOM存储
- 支持文件访问
- 支持缩放
- 处理返回按钮导航

### 本地资源加载

应用使用本地assets目录中的HTML、CSS、JavaScript和SQL.js文件，无需网络连接即可运行。

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
- 分支：feature/android-app

---

**注意**：本项目为学习工具，旨在帮助用户学习SQL语法和查询技巧。