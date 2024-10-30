import torch
import sys

# 檢查 cuda,python,torch version
def cuda_version():
    # 檢查 Python 版本
    python_version = sys.version
    print(f"Python 版本: {python_version}")

    # 檢查 PyTorch 版本
    pytorch_version = torch.__version__
    print(f"PyTorch 版本: {pytorch_version}")

    # 檢查 CUDA 是否可用
    cuda_available = torch.cuda.is_available()
    print(f"CUDA 可用: {cuda_available}")

    if cuda_available:
        # 如果 CUDA 可用，檢查 CUDA 版本和 GPU 裝置
        print(f"CUDA 版本: {torch.version.cuda}")
        print(f"GPU 數量: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        # 取得目前使用中的 GPU 裝置
        current_device = torch.cuda.current_device()
        print(f"目前的 GPU 裝置：{torch.cuda.get_device_name(current_device)}")


"""
使用方式
from cuda_version import cuda_version
cuda_version()
"""