import torch
import numpy as np

# Example of generating random data
data = np.random.rand(100, 5)
random_data = torch.from_numpy(data).float()
print(random_data)
