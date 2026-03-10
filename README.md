# SQL学习游戏客户端

一款本地运行、游戏化、交互式的SQL学习客户端，通过"语法按钮拼接+关卡闯关"的形式，降低学习门槛，提升学习趣味性。

## 功能特点

- **本地运行**：无需联网，无需安装数据库，开箱即用
- **游戏化设计**：关卡制学习，任务明确，反馈及时
- **低门槛操作**：支持"语法按钮拼接"，减少记忆负担
- **自由闯关**：关卡独立，支持按顺序学习或跳关挑战
- **进度保存**：自动保存关卡完成状态

## 关卡系统

- **基础篇**：SELECT、FROM、简单查询
- **进阶篇**：WHERE、ORDER BY、LIMIT
- **高级篇**：GROUP BY、聚合函数、JOIN
- **挑战篇**：子查询、窗口函数

## 内置数据库

包含4张核心表：

- **student**（学生表）：id, name, age, class_id
- **class**（班级表）：id, class_name, teacher
- **course**（课程表）：id, course_name, credit
- **score**（成绩表）：student_id, course_id, score

## 快速开始

1. 克隆仓库
   ```bash
   git clone https://github.com/wenbo030509/SqlGame.git
   ```

2. 启动本地服务器
   ```bash
   cd SqlGame
   python3 -m http.server 8000
   ```

3. 在浏览器中访问
   ```
   http://localhost:8000
   ```

## 技术实现

- 纯HTML、CSS和JavaScript
- 响应式布局
- 模块化代码结构
- 模拟SQL执行引擎

## 项目结构

```
SqlGame/
├── index.html          # 主页面
└── README.md           # 项目说明
```

## 浏览器支持

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

MIT License