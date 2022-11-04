
"""
To ensure that PyTorch was installed correctly, we can verify the installation by running sample PyTorch code. Here we will construct a randomly initialized tensor.
"""
import torch
x = torch.rand(5, 3)
print(x)


"""
Additionally, to check if your GPU driver and CUDA/ROCm is enabled and accessible by PyTorch, run the following commands to return whether or not the GPU driver is enabled
"""
print(torch.cuda.is_available())
