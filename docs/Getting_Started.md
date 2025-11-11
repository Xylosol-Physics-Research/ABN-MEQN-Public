# 快速开始指南

## 系统要求

- Python 3.8 或更高版本
- 4GB 以上内存
- 支持的操作系统: Windows 10+, macOS 10.14+, Ubuntu 18.04+

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/ABN-MEQN-Public.git
cd ABN-MEQN-Public
```

2. 创建虚拟环境（推荐）

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS  
source venv/bin/activate
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 验证安装

```python
python -c "from simulations.integrated_system import ABNMEQNSimulator; print('安装成功!')"
```

基础使用

量子系统模拟

```python
import numpy as np
from simulations.integrated_system import ABNMEQNSimulator

# 创建模拟器实例
simulator = ABNMEQNSimulator()

# 配置模拟参数
config = {
    "hardware_nodes": 81,
    "dimensions": 4,
    "use_magnetoelectric": True
}

# 运行量子材料模拟
material_params = {
    "name": "多铁性材料",
    "structure": "钙钛矿",
    "temperature": 300  # Kelvin
}

result = simulator.simulate_quantum_material(material_params, config)

# 查看结果
print(f"模拟状态: {result.status}")
print(f"收敛迭代: {result.iterations}")
print(f"最终能量: {result.final_energy}")

# 可视化
result.plot_energy_convergence()
result.plot_quantum_states()
```

量子加密演示

```python
from examples.crypto_demos import QuantumCryptographyDemo

# 初始化量子加密演示
crypto_demo = QuantumCryptographyDemo()

# 运行BB84协议演示
qkd_result = crypto_demo.demo_bb84_protocol(
    transmission_distance=50,  # km
    with_eavesdropper=False
)

print(f"安全密钥长度: {qkd_result['key_length']} 位")
print(f"量子比特错误率: {qkd_result['qber']:.4f}")

# 运行多维魔方加密演示
magic_crypto_result = crypto_demo.demo_multidimensional_magic_crypto()
```

进阶示例

分层加密网络

```python
from simulations.quantum_internet import TieredEncryptionNetwork

# 创建分层加密网络
encryption_net = TieredEncryptionNetwork()

# 模拟不同安全等级的数据传输
data_types = [
    {"sensitivity": "top_secret", "data": "核导弹发射指令"},
    {"sensitivity": "financial", "data": "银行交易记录"},
    {"sensitivity": "commercial", "data": "企业财务报表"},
    {"sensitivity": "consumer", "data": "社交媒体消息"}
]

for data in data_types:
    encrypted = encryption_net.encrypt_data(
        data["data"], 
        data["sensitivity"]
    )
    print(f"{data['sensitivity']} 数据加密完成")
    print(f"使用的加密等级: {encrypted['tier']}")
```

性能基准测试

```python
from benchmarks.performance_comparison import run_benchmarks

# 运行性能对比测试
results = run_benchmarks()

print("性能对比结果:")
print(f"ABN-MEQN vs 传统DFT: {results['speedup_vs_dft']:.1f}x 加速")
print(f"ABN-MEQN vs 经典神经网络: {results['speedup_vs_nn']:.1f}x 加速")
print(f"能效提升: {results['energy_efficiency']:.1f}x")

# 生成性能报告
results.generate_report()
```

故障排除

常见问题

Q: 导入错误 ModuleNotFoundError
A: 确保已安装所有依赖: pip install -r requirements.txt

Q: 内存不足错误
A: 尝试减少模拟规模或增加系统内存

Q: 可视化显示问题
A: 确保安装了matplotlib: pip install matplotlib

获取帮助

· 查看 问题追踪
· 加入 讨论区
· 阅读 API文档

下一步

· 探索 应用案例 了解实际应用
· 查看 技术白皮书 深入理解技术原理
· 参与 社区贡献 帮助项目发展
