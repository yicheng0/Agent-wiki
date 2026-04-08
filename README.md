<div align="center">

# 🤖 Agent Wiki

### 大模型开发完整学习路线

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

*从零开始，系统掌握大模型开发技术栈*

[开始学习](#-学习路线) • [贡献指南](#-贡献) • [资源推荐](#-相关资源)

</div>

---

## 📚 学习路线

### ✅ 第一周：大模型必备基础速通

<details>
<summary>点击展开详细内容</summary>

- 📖 [Python 核心基础](./01-第一周：大模型必备基础速通/01-Python核心基础.md)
  - 数据类型与结构、函数式编程、面向对象
  - NumPy 数组操作、Pandas 数据处理
  - 文件操作、异常处理、装饰器

- 🧠 [神经网络核心概念](./01-第一周：大模型必备基础速通/02-神经网络核心概念.md)
  - 前向传播、反向传播、链式法则
  - 损失函数：交叉熵、MSE、Huber Loss
  - 激活函数：ReLU、Sigmoid、Tanh、GELU
  - 梯度下降：BGD、SGD、Mini-batch GD
  - 优化器：Momentum、Adam

- ⚡ [PyTorch 框架速通](./01-第一周：大模型必备基础速通/03-PyTorch框架速通.md)
  - Tensor 操作、自动求导机制
  - nn.Module 模型构建、常用层
  - 数据加载：Dataset、DataLoader
  - GPU 加速、混合精度训练

- 🎯 [模型推理和训练](./01-第一周：大模型必备基础速通/04-模型推理和训练.md)
  - 完整训练流程、学习率调度
  - 早停机制、梯度累积
  - 模型评估指标、调试技巧

</details>

### 🚧 第二周：手撕Transformer & MOE

> 即将更新...

**学习内容**：
- Self-Attention 机制
- Multi-Head Attention
- Position Encoding
- Transformer 完整实现
- Mixture of Experts (MOE)

### 🚧 第三周：手撕 Llama

> 即将更新...

**学习内容**：
- RoPE 位置编码
- RMSNorm 归一化
- SwiGLU 激活函数
- KV Cache 优化
- Llama 完整实现

### 📝 第四周：大模型部署、压测、应用开发

> 即将更新...

### 📝 第五周：RAG (Part 1)：检索增强生成

> 即将更新...

### 📝 第六周：RAG (Part 2)：RAG工业级应用

> 即将更新...

### 📝 第七周：Agent 智能体：让 LLM 自主决策

> 即将更新...

### 📝 第八周：大模型预训练实战

> 即将更新...

### 📝 第九周：大模型微调实战

> 即将更新...

### 📝 第十周：RLHF 实战 - PPO/DPO/GRPO

> 即将更新...

### 📝 第十一周：多模态大模型实战—— 模态对齐

> 即将更新...

### 📝 第十二周：手撕分布式训练实战

> 即将更新...

**学习内容**：
- 数据并行 (Data Parallelism)
- 张量并行 (Tensor Parallelism)
- 流水线并行 (Pipeline Parallelism)
- 混合并行策略

### 📝 第十三周：推理加速实战

> 即将更新...

**学习内容**：
- 模型量化 (Quantization)
- 模型剪枝 (Pruning)
- 知识蒸馏 (Distillation)

---

## 🎯 学习目标

通过这个学习路线，你将掌握：

| 技能领域 | 具体内容 |
|:---|:---|
| 🐍 **Python 基础** | 核心语法、NumPy、Pandas、面向对象编程 |
| 🧠 **深度学习** | 神经网络原理、PyTorch 框架、模型训练与调优 |
| 🤖 **大模型架构** | Transformer、Llama、MOE 等主流架构 |
| 🚀 **模型部署** | 推理优化、量化加速、分布式部署 |
| 📚 **RAG 应用** | 检索增强生成、向量数据库、工业级应用 |
| 🎭 **Agent 开发** | 智能体设计、工具调用、自主决策 |
| ⚡ **性能优化** | 分布式训练、推理加速、资源优化 |

## 💡 如何使用

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/agent-wiki.git
cd agent-wiki

# 2. 按周次学习
# 建议从第一周开始，循序渐进

# 3. 动手实践
# 每个章节都有完整代码示例，务必动手运行
```

> 💡 **学习建议**：
> - 每周投入 10-15 小时学习时间
> - 完成所有代码示例和实战练习
> - 建议组队学习，互相讨论交流

## 🔗 相关资源

### 官方文档
- [PyTorch 官方文档](https://pytorch.org/docs/stable/index.html)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [OpenAI API 文档](https://platform.openai.com/docs)

### 论文阅读
- [Papers with Code](https://paperswithcode.com/)
- [arXiv.org](https://arxiv.org/)

### 开源项目
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Llama 推理引擎
- [vLLM](https://github.com/vllm-project/vllm) - 高性能推理框架
- [LangChain](https://github.com/langchain-ai/langchain) - LLM 应用开发框架

## 🤝 贡献

欢迎贡献！如果你发现错误或有改进建议：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📄 License

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

<div align="center">

**⭐ 如果这个项目对你有帮助，欢迎 Star！**

Made with ❤️ by AI Learners

</div>
