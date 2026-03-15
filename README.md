# SQL学习游戏客户端

一款本地运行、游戏化、交互式的SQL学习客户端，通过"语法按钮拼接+关卡闯关"的形式，降低学习门槛，提升学习趣味性。

## 功能特点

- **本地运行**：无需联网，无需安装数据库，开箱即用
- **真实SQL引擎**：使用sql.js接入真实SQLite引擎，支持完整SQL语法
- **游戏化设计**：关卡制学习，任务明确，反馈及时
- **低门槛操作**：支持"语法按钮拼接"，减少记忆负担
- **自由闯关**：关卡独立，支持按顺序学习或跳关挑战
- **进度保存**：自动保存关卡完成状态
- **丰富的SQL语法支持**：包括基础查询、条件查询、排序、分组、聚合函数、JOIN连接、子查询、窗口函数、LIKE模糊查询、IN条件查询、CASE语句、HAVING过滤等
- **一键复制答案**：查看提示时可直接复制正确的SQL语句
- **真实数据表**：查看表结构时显示真实的数据内容
- **序章学习**：新增序章页，专门用于SQL语法函数的学习，包含详细的语法讲解和示例
- **语法提示**：语法按钮hover1秒后显示详细的语法结构和示例
- **标签功能**：右键点击关卡可以标记/取消标记，方便重点题目管理
- **快捷按钮**：新增SELECT *快捷按钮，一键填充常用SQL片段
- **完整函数支持**：包含HAVING、CASE等高级SQL函数的详细讲解和示例
- **移动端适配**：响应式布局，支持手机和平板访问
- **侧边栏切换**：支持展开/收起侧边栏，优化小屏幕体验

## 关卡系统

- **序章**：SQL语法学习，包括基础语法和常用函数的详细介绍
- **基础篇**：SELECT、FROM、简单查询、指定字段查询、去重查询
- **进阶篇**：WHERE条件查询、ORDER BY排序、LIMIT限制
- **高级篇**：GROUP BY分组、聚合函数、JOIN连接、HAVING过滤
- **挑战篇**：子查询、窗口函数、LIKE模糊查询、IN条件查询、多条件查询、别名使用、多表JOIN、CASE语句、日期函数、综合挑战

### 关卡详情

| 关卡 | 名称 | 内容 |
|------|------|------|
| 0 | 序章：SQL语法学习 | 学习SQL基础语法和常用函数 |
| 1 | 简单查询 | 查询学生表中所有学生的信息 |
| 2 | 指定字段查询 | 查询学生表中所有学生的姓名和年龄 |
| 3 | 去重查询 | 查询学生表中所有不同的班级ID |
| 4 | WHERE条件查询 | 查询年龄大于18的学生信息 |
| 5 | ORDER BY排序 | 查询学生表，按年龄降序排列 |
| 6 | LIMIT限制 | 查询学生表中前5名学生的信息 |
| 7 | GROUP BY分组 | 按班级ID分组，统计每个班级的学生人数 |
| 8 | 聚合函数 | 计算学生表中所有学生的平均年龄 |
| 9 | JOIN连接 | 查询学生姓名及其所在班级名称 |
| 10 | 子查询 | 查询成绩大于平均分的学生ID |
| 11 | 窗口函数 | 查询每个学生的成绩排名 |
| 12 | LIKE模糊查询 | 查询姓名中包含'张'的学生信息 |
| 13 | IN条件查询 | 查询班级ID为1或2的学生信息 |
| 14 | 多条件查询 | 查询年龄大于18且班级ID为1的学生信息 |
| 15 | 别名使用 | 查询学生姓名和年龄，使用别名显示 |
| 16 | 多表JOIN | 查询学生姓名、课程名称和成绩 |
| 17 | HAVING过滤 | 查询学生人数大于3的班级ID |
| 18 | CASE语句 | 查询学生姓名和成绩等级 |
| 19 | 日期函数 | 查询学生信息，计算出生年份 |
| 20 | 综合挑战 | 查询每个班级的平均成绩，并按平均成绩降序排列

## 内置数据库

包含4张核心表：

- **student**（学生表）：id, name, age, class_id
- **class**（班级表）：id, class_name, teacher
- **course**（课程表）：id, course_name, credit
- **score**（成绩表）：student_id, course_id, score

## 快速开始

### 方式一：直接下载使用（推荐）

1. **下载项目文件**
   - 点击GitHub页面右上角的 "Code" 按钮
   - 选择 "Download ZIP" 下载压缩包
   - 解压到本地文件夹

2. **启动本地服务器**
   ```bash
   cd SqlGame
   python3 -m http.server 8000
   ```
   或者使用其他方式启动本地服务器：
   ```bash
   # 使用Node.js的http-server
   npx http-server -p 8000
   
   # 使用PHP
   php -S localhost:8000
   
   # 使用VS Code的Live Server插件
   # 右键点击index.html，选择"Open with Live Server"
   ```

3. **在浏览器中访问**
   ```
   http://localhost:8000
   ```

### 方式二：Git克隆（需要Git环境）

```bash
git clone https://github.com/wenbo030509/SqlGame.git
cd SqlGame
python3 -m http.server 8000
```

### 方式三：VS Code Live Server（最简单）

1. 在VS Code中安装 "Live Server" 插件
2. 打开项目文件夹
3. 右键点击 `index.html` 文件
4. 选择 "Open with Live Server"

## 技术实现

- 纯HTML、CSS和JavaScript
- 响应式布局，支持桌面端和移动端
- 模块化代码结构
- 真实SQL执行引擎：使用sql.js接入SQLite数据库
- 本地存储：使用localStorage保存学习进度
- WebAssembly：使用sql.js的WASM版本提高性能

## 项目结构

```
SqlGame/
├── index.html          # 主页面
├── sql-wasm.js         # SQL.js JavaScript接口
├── sql-wasm.wasm       # SQL.js WebAssembly模块
├── README.md           # 项目说明
├── android-app/        # Android应用（可选）
│   └── ...
├── ios-app/            # iOS应用（可选）
│   └── ...
└── .gitignore          # Git忽略文件
```

## 浏览器支持

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 移动端支持

- iOS 13+
- Android 7.0+

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

MIT License
