import pytest
import numpy as np

class TestABNMEQNIntegration:
    """整合系统测试套件"""
    
    def test_initialization(self):
        """测试系统初始化"""
        simulator = ABNMEQNSimulator()
        assert simulator is not None
        assert simulator.hardware_simulator.initialized
        assert simulator.quantum_processor.initialized
    
    def test_convergence(self):
        """测试收敛性"""
        simulator = ABNMEQNSimulator()
        result = simulator.simulate_quantum_material(
            basic_material_params
        )
        assert result.converged
        assert result.iterations < 1000
    
    def test_performance_improvement(self):
        """测试性能提升"""
        baseline_time = measure_baseline_performance()
        our_time = measure_our_performance()
        
        improvement_ratio = baseline_time / our_time
        assert improvement_ratio > 10  # 至少10倍提升
