import sys
import os
import numpy as np
import pytest

# 添加父目录到路径，以便导入学生代码
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from solution.series_sum_solution import sum_S1, sum_S2, sum_S3
from series_sum import sum_S1, sum_S2, sum_S3
def test_sum_S1_basic():
    """测试sum_S1基本功能"""
    assert abs(sum_S1(1) - 0.166666666666667) < 1e-10, "N=1时计算错误"
    assert abs(sum_S1(2) - 0.216666666666667) < 1e-10, "N=2时计算错误"
    assert abs(sum_S1(4) - 0.254365079365079) < 1e-10, "N=4时计算错误"

def test_sum_S2_basic():
    """测试sum_S2基本功能"""
    assert abs(sum_S2(1) - 0.166666666666667) < 1e-10, "N=1时计算错误"
    assert abs(sum_S2(2) - 0.216666666666667) < 1e-10, "N=2时计算错误"
    assert abs(sum_S2(4) - 0.254365079365079) < 1e-10, "N=4时计算错误"

def test_sum_S3_basic():
    """测试sum_S3基本功能"""
    assert abs(sum_S3(1) - 0.166666666666667) < 1e-10, "N=1时计算错误"
    assert abs(sum_S3(2) - 0.216666666666667) < 1e-10, "N=2时计算错误"
    assert abs(sum_S3(4) - 0.254365079365079) < 1e-10, "N=4时计算错误"

def test_consistency_small_N():
    """测试小N值时三种方法结果一致"""
    N = 10
    assert abs(sum_S1(N) - sum_S3(N)) < 1e-10, "S1和S3在N=10时结果应该几乎相同"
    assert abs(sum_S2(N) - sum_S3(N)) < 1e-10, "S2和S3在N=10时结果应该几乎相同"

def test_monotonicity():
    """测试和的单调性"""
    N_values = [10, 100]
    sums_1 = [sum_S1(N) for N in N_values]
    sums_2 = [sum_S2(N) for N in N_values]
    sums_3 = [sum_S3(N) for N in N_values]
    
    # 验证和随N增大而增大
    assert sums_1[1] > sums_1[0], "S1结果应随N增大而增大"
    assert sums_2[1] > sums_2[0], "S2结果应随N增大而增大"
    assert sums_3[1] > sums_3[0], "S3结果应随N增大而增大"

def test_relative_difference():
    """测试大N值时的相对差异"""
    N = 1000
    s1 = sum_S1(N)
    s2 = sum_S2(N)
    s3 = sum_S3(N)
    
    # 验证S2的误差应该大于S1的误差
    err1 = abs((s1 - s3) / s3)
    err2 = abs((s2 - s3) / s3)
    assert err2 > err1, "S2的误差应该大于S1的误差"

if __name__ == "__main__":
    pytest.main(["-v", __file__])
    import numpy as np
import matplotlib.pyplot as plt

def sum_S1(N):
    """计算第一种形式的级数和：交错级数
    S_N^(1) = sum_{n=1}^{2N} (-1)^n * n/(n+1)
    """
    result = 0.0
    for n in range(1, 2*N + 1):
        result += (-1)**n * n / (n + 1)
    return result

def sum_S2(N):
    """计算第二种形式的级数和：两项求和相减
    S_N^(2) = -sum_{n=1}^N (2n-1)/(2n) + sum_{n=1}^N (2n)/(2n+1)
    """
    sum1 = sum2 = 0.0
    for n in range(1, N + 1):
        sum1 += (2*n - 1) / (2*n)
        sum2 += (2*n) / (2*n + 1)
    return -sum1 + sum2

def sum_S3(N):
    """计算第三种形式的级数和：直接求和
    S_N^(3) = sum_{n=1}^N 1/(2n(2n+1))
    """
    result = 0.0
    for n in range(1, N + 1):
        result += 1.0 / (2*n * (2*n + 1))
    return result

def calculate_relative_errors(N_values):
    """计算相对误差"""
    err1 = []
    err2 = []
    
    for N in N_values:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        
        err1.append(abs((s1 - s3) / s3))
        err2.append(abs((s2 - s3) / s3))
    
    return err1, err2

def plot_errors(N_values, err1, err2):
    """绘制误差分析图"""
    plt.figure(figsize=(10, 6))
    plt.loglog(N_values, err1, 'o-', label='S1 Error', alpha=0.7)
    plt.loglog(N_values, err2, 's--', label='S2 Error', alpha=0.7)
    
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.xlabel('N')
    plt.ylabel('Relative Error')
    plt.title('Relative Errors vs N')
    plt.legend()
    
    plt.savefig('series_sum_errors.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_results():
    """打印典型N值的计算结果"""
    N_values = [10, 100, 1000, 10000]
    
    print("\n计算结果:")
    print("N\tS1\t\tS2\t\tS3\t\tErr1\t\tErr2")
    print("-" * 80)
    
    for N in N_values:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs((s1 - s3) / s3)
        err2 = abs((s2 - s3) / s3)
        print(f"{N}\t{s1:.8f}\t{s2:.8f}\t{s3:.8f}\t{err1:.2e}\t{err2:.2e}")

def main():
    """主函数"""
    # 生成N值序列
    N_values = np.logspace(0, 4, 50, dtype=int)
    
    # 计算误差
    err1, err2 = calculate_relative_errors(N_values)
    
    # 打印结果
    print_results()
    
    # 绘制误差图
    plot_errors(N_values, err1, err2)

if __name__ == "__main__":
    main()
