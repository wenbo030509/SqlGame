# iOS应用构建指南

本指南将详细说明如何在Xcode中设置和运行SQL学习游戏的iOS应用。

## 前置条件

- **Xcode**：版本 12.0 或更高
- **iOS**：版本 13.0 或更高
- **Mac电脑**：运行macOS 10.15 (Catalina) 或更高

## 步骤1：创建Xcode项目

1. 启动 Xcode
2. 点击 "Create a new Xcode project"
3. 选择 "iOS" > "App"
4. 点击 "Next"
5. 填写项目信息：
   - Product Name: SqlGame
   - Team: 选择您的开发团队（如果没有，可稍后设置）
   - Organization Identifier: com.sqlgame
   - Interface: Storyboard
   - Language: Swift
   - 取消勾选 "Use Core Data" 和 "Include Tests"
6. 点击 "Next"
7. 选择保存位置：导航到 `SQL/ios-app` 目录
8. 点击 "Create"

## 步骤2：配置项目

1. **添加WebKit框架**：
   - 点击左侧项目导航栏中的 "SqlGame"
   - 选择 "General" 标签
   - 在 "Frameworks, Libraries, and Embedded Content" 部分点击 "+"
   - 搜索并添加 "WebKit"

2. **添加资源文件**：
   - 在左侧项目导航栏中，右键点击 "SqlGame" 文件夹
   - 选择 "Add Files to 'SqlGame'..."
   - 导航到 `SQL/ios-app/SqlGame/SqlGame/Resources` 目录
   - 选择 `index.html`、`sql-wasm.js` 和 `sql-wasm.wasm` 文件
   - 确保勾选 "Copy items if needed"
   - 点击 "Add"

3. **替换ViewController.swift**：
   - 在左侧项目导航栏中，右键点击 "ViewController.swift"
   - 选择 "Delete" > "Move to Trash"
   - 右键点击 "SqlGame" 文件夹
   - 选择 "Add Files to 'SqlGame'..."
   - 导航到 `SQL/ios-app/SqlGame/SqlGame` 目录
   - 选择 `ViewController.swift` 文件
   - 点击 "Add"

4. **更新Info.plist**：
   - 在左侧项目导航栏中，右键点击 "Info.plist"
   - 选择 "Open As" > "Source Code"
   - 替换内容为 `SQL/ios-app/SqlGame/SqlGame/Info.plist` 文件的内容

5. **更新Main.storyboard**：
   - 在左侧项目导航栏中，右键点击 "Main.storyboard"
   - 选择 "Delete" > "Move to Trash"
   - 右键点击 "SqlGame" 文件夹
   - 选择 "Add Files to 'SqlGame'..."
   - 导航到 `SQL/ios-app/SqlGame/SqlGame` 目录
   - 选择 `Main.storyboard` 文件
   - 点击 "Add"

## 步骤3：构建和运行

1. **选择目标设备**：
   - 在Xcode顶部工具栏，选择模拟器或连接的iOS设备

2. **构建项目**：
   - 点击 "Product" > "Build"
   - 等待构建完成

3. **运行应用**：
   - 点击 "Product" > "Run" 或使用快捷键 `Cmd+R`
   - 应用会在模拟器或设备上启动

## 步骤4：测试应用

1. **验证功能**：
   - 检查SQL执行是否正常
   - 测试关卡切换功能
   - 验证侧边栏展开/收起功能
   - 测试触摸操作是否流畅

2. **性能测试**：
   - 检查首次加载时间
   - 测试SQL查询执行速度
   - 验证应用在不同屏幕尺寸上的表现

## 故障排除

### 常见问题

1. **构建失败**
   - 检查是否添加了WebKit框架
   - 验证资源文件是否正确添加
   - 清理项目：点击 "Product" > "Clean Build Folder"

2. **应用崩溃**
   - 检查设备是否满足最低iOS版本要求（iOS 13.0+）
   - 查看控制台中的错误信息

3. **SQL.js加载失败**
   - 确保 `sql-wasm.js` 和 `sql-wasm.wasm` 文件已正确添加到项目中
   - 检查文件是否被正确复制到应用包中

4. **WebView不显示内容**
   - 检查HTML文件路径是否正确
   - 验证WebView配置是否正确

## 技术支持

如果遇到构建或运行问题，请参考以下资源：

- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Swift Documentation](https://docs.swift.org/swift-book/)
- [WKWebView Documentation](https://developer.apple.com/documentation/webkit/wkwebview)

---

**注意**：本应用基于WKWebView技术，首次启动时可能需要较长时间加载WebAssembly文件。