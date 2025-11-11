# 贡献指南

感谢您有兴趣为 ABN-MEQN 项目做出贡献！

## 如何贡献

### 报告问题
- 使用 [问题模板](ISSUE_TEMPLATES/bug_report.md)
- 提供详细的重现步骤
- 包括系统环境和版本信息

### 功能请求
- 使用 [功能请求模板](ISSUE_TEMPLATES/feature_request.md)  
- 描述使用场景和预期行为
- 讨论可能的实现方案

### 代码贡献
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 开发环境设置

```bash
# 1. Fork 并克隆仓库
git clone https://github.com/your-username/ABN-MEQN-Public.git
cd ABN-MEQN-Public

# 2. 安装开发依赖
pip install -r requirements-dev.txt

# 3. 安装预提交钩子
pre-commit install

# 4. 运行测试
pytest tests/ -v
```

代码规范

Python 代码风格

· 遵循 PEP 8 规范
· 使用 Black 进行代码格式化
· 使用 flake8 进行代码检查

文档标准

· 所有函数和类都需要文档字符串
· 使用 Google 风格的文档字符串格式
· 更新相关文档当代码变更时

测试要求

· 新功能需要包含单元测试
· 保持测试覆盖率在 80% 以上
· 使用 pytest 框架

提交消息规范

使用约定式提交格式：

```
类型(范围): 描述

正文...

脚注...
```

类型包括:

· feat: 新功能
· fix: 错误修复
· docs: 文档更新
· style: 代码格式调整
· refactor: 代码重构
· test: 测试相关
· chore: 构建过程或辅助工具变动

评审流程

1. 提交 Pull Request
2. 自动运行 CI/CD 流水线
3. 核心维护者代码审查
4. 解决评审意见
5. 合并到主分支

社区行为准则

请阅读并遵守我们的 行为准则。

联系方式

· 问题讨论: GitHub Discussions
· 实时交流: [Discord/Slack 频道] (即将推出)

感谢您的贡献！🎉
