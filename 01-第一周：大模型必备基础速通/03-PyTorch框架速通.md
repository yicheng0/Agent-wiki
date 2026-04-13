# PyTorch 框架速通

## 1. Tensor 基础操作

### 1.1 创建 Tensor

```python
import torch

# 从数据创建
data = [[1, 2], [3, 4]]
tensor = torch.tensor(data)

# 从 NumPy 数组创建
import numpy as np
np_array = np.array([[1, 2], [3, 4]])
tensor = torch.from_numpy(np_array)

# 创建特殊 Tensor
zeros = torch.zeros(2, 3)           # 全0
ones = torch.ones(2, 3)             # 全1
empty = torch.empty(2, 3)           # 未初始化
rand = torch.rand(2, 3)             # [0, 1)均匀分布
randn = torch.randn(2, 3)           # 标准正态分布
arange = torch.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
linspace = torch.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# 创建与其他tensor相同形状的tensor
x = torch.ones(2, 3)
zeros_like = torch.zeros_like(x)
ones_like = torch.ones_like(x)
```

### 1.2 Tensor 属性

```python
tensor = torch.randn(3, 4)

print(tensor.shape)        # torch.Size([3, 4])
print(tensor.size())       # torch.Size([3, 4])
print(tensor.dtype)        # torch.float32
print(tensor.device)       # cpu 或 cuda:0
print(tensor.requires_grad) # False
print(tensor.ndim)         # 2
print(tensor.numel())      # 12 (总元素数)
```

### 1.3 Tensor 操作

```python
# 索引和切片
tensor = torch.randn(4, 5)
print(tensor[0])           # 第一行
print(tensor[:, 0])        # 第一列
print(tensor[1:3, 2:4])    # 切片

# 改变形状
x = torch.randn(4, 5)
y = x.view(2, 10)          # 改变形状（共享内存）
z = x.reshape(2, 10)       # 改变形状（可能复制）
w = x.flatten()            # 展平为一维
u = x.unsqueeze(0)         # 增加维度 (1, 4, 5)
v = u.squeeze(0)           # 删除维度 (4, 5)

# 转置和维度交换
x = torch.randn(2, 3, 4)
y = x.transpose(0, 1)      # 交换维度0和1
z = x.permute(2, 0, 1)     # 重排所有维度

# 拼接
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z1 = torch.cat([x, y], dim=0)  # 沿维度0拼接 (4, 3)
z2 = torch.cat([x, y], dim=1)  # 沿维度1拼接 (2, 6)
z3 = torch.stack([x, y], dim=0) # 新增维度拼接 (2, 2, 3)
```

### 1.4 数学运算

```python
# 元素级运算
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

z = x + y              # 加法
z = torch.add(x, y)    # 等价写法
z = x - y              # 减法
z = x * y              # 乘法
z = x / y              # 除法
z = x ** 2             # 幂运算

# 就地操作（in-place）
x.add_(y)              # x = x + y
x.mul_(2)              # x = x * 2

# 矩阵运算
A = torch.randn(3, 4)
B = torch.randn(4, 5)

C = torch.mm(A, B)     # 矩阵乘法 (3, 5)
C = A @ B              # 等价写法
C = torch.matmul(A, B) # 更通用的乘法

# 批量矩阵乘法
A = torch.randn(10, 3, 4)  # 10个3x4矩阵
B = torch.randn(10, 4, 5)  # 10个4x5矩阵
C = torch.bmm(A, B)        # (10, 3, 5)

# 其他运算
x = torch.randn(3, 4)
y = torch.sum(x)           # 求和
y = torch.mean(x)          # 平均值
y = torch.max(x)           # 最大值
y = torch.min(x)           # 最小值
y = torch.argmax(x)        # 最大值索引
y = torch.argmin(x)        # 最小值索引

# 沿指定维度运算
x = torch.randn(3, 4)
y = torch.sum(x, dim=0)    # 沿维度0求和 (4,)
y = torch.mean(x, dim=1)   # 沿维度1求平均 (3,)
values, indices = torch.max(x, dim=1)  # 返回值和索引
```

## 2. 自动求导（Autograd）

### 2.1 基本概念

```python
# 创建需要梯度的tensor
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# 前向传播
y = x ** 2
z = y.sum()

# 反向传播
z.backward()

# 查看梯度
print(x.grad)  # tensor([2., 4., 6.])

# 梯度清零
x.grad.zero_()
```

### 2.2 梯度计算示例

```python
# 简单函数的梯度
x = torch.tensor(2.0, requires_grad=True)
y = x ** 3 + 2 * x ** 2 + x + 1

y.backward()
print(x.grad)  # dy/dx = 3x^2 + 4x + 1 = 21.0

# 多变量函数
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = x ** 2 + y ** 2 + 2 * x * y

z.backward()
print(x.grad)  # dz/dx = 2x + 2y = 6.0
print(y.grad)  # dz/dy = 2y + 2x = 6.0
```

### 2.3 梯度控制

```python
# 禁用梯度计算
x = torch.randn(3, 4, requires_grad=True)

# 方法1：使用 torch.no_grad()
with torch.no_grad():
    y = x * 2
    print(y.requires_grad)  # False

# 方法2：使用 .detach()
y = x.detach()
print(y.requires_grad)  # False

# 方法3：使用 @torch.no_grad() 装饰器
@torch.no_grad()
def inference(model, x):
    return model(x)

# 累积梯度
x = torch.tensor([1.0, 2.0], requires_grad=True)

for i in range(3):
    y = (x ** 2).sum()
    y.backward()
    print(f"Step {i}: {x.grad}")  # 梯度会累积

# 清零梯度
x.grad.zero_()
```

## 3. 神经网络模块（nn.Module）

### 3.1 定义模型

```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型
model = SimpleNet(784, 256, 10)

# 查看模型结构
print(model)

# 查看参数
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}")

# 计算参数总数
total_params = sum(p.numel() for p in model.parameters())
print(f"Total parameters: {total_params}")
```

### 3.2 常用层

```python
# 全连接层
fc = nn.Linear(in_features=128, out_features=64)

# 卷积层
conv1d = nn.Conv1d(in_channels=3, out_channels=16, kernel_size=3)
conv2d = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)

# 池化层
maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
avgpool = nn.AvgPool2d(kernel_size=2)

# 归一化层
batchnorm = nn.BatchNorm1d(num_features=64)
layernorm = nn.LayerNorm(normalized_shape=64)

# Dropout
dropout = nn.Dropout(p=0.5)

# 激活函数
relu = nn.ReLU()
sigmoid = nn.Sigmoid()
tanh = nn.Tanh()
gelu = nn.GELU()

# Embedding层
embedding = nn.Embedding(num_embeddings=10000, embedding_dim=300)

# RNN层
rnn = nn.RNN(input_size=128, hidden_size=256, num_layers=2)
lstm = nn.LSTM(input_size=128, hidden_size=256, num_layers=2)
gru = nn.GRU(input_size=128, hidden_size=256, num_layers=2)

# Transformer层
transformer = nn.Transformer(d_model=512, nhead=8, num_encoder_layers=6)
```

### 3.3 Sequential 容器

```python
# 使用Sequential构建模型
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(128, 10)
)

# 使用OrderedDict命名层
from collections import OrderedDict

model = nn.Sequential(OrderedDict([
    ('fc1', nn.Linear(784, 256)),
    ('relu1', nn.ReLU()),
    ('dropout1', nn.Dropout(0.5)),
    ('fc2', nn.Linear(256, 10))
]))

# 访问特定层
print(model.fc1.weight.shape)
```

### 3.4 ModuleList 和 ModuleDict

```python
# ModuleList - 存储多个模块
class MyModel(nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.layers = nn.ModuleList([
            nn.Linear(128, 128) for _ in range(num_layers)
        ])
    
    def forward(self, x):
        for layer in self.layers:
            x = F.relu(layer(x))
        return x

# ModuleDict - 使用字典存储模块
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.ModuleDict({
            'encoder': nn.Linear(784, 256),
            'decoder': nn.Linear(256, 784)
        })
    
    def forward(self, x):
        x = self.layers['encoder'](x)
        x = self.layers['decoder'](x)
        return x
```

## 4. 损失函数

```python
# 交叉熵损失（分类）
criterion = nn.CrossEntropyLoss()
output = torch.randn(32, 10)  # (batch_size, num_classes)
target = torch.randint(0, 10, (32,))  # (batch_size,)
loss = criterion(output, target)

# 二分类交叉熵
criterion = nn.BCELoss()
output = torch.sigmoid(torch.randn(32, 1))
target = torch.randint(0, 2, (32, 1)).float()
loss = criterion(output, target)

# BCEWithLogitsLoss（更稳定）
criterion = nn.BCEWithLogitsLoss()
output = torch.randn(32, 1)  # 不需要sigmoid
target = torch.randint(0, 2, (32, 1)).float()
loss = criterion(output, target)

# 均方误差损失（回归）
criterion = nn.MSELoss()
output = torch.randn(32, 1)
target = torch.randn(32, 1)
loss = criterion(output, target)

# L1损失
criterion = nn.L1Loss()

# Smooth L1损失（Huber Loss）
criterion = nn.SmoothL1Loss()

# KL散度
criterion = nn.KLDivLoss()
```

## 5. 优化器

```python
import torch.optim as optim

# SGD
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Adam
optimizer = optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999))

# AdamW（带权重衰减的Adam）
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

# RMSprop
optimizer = optim.RMSprop(model.parameters(), lr=0.01)

# 不同参数组使用不同学习率
optimizer = optim.Adam([
    {'params': model.encoder.parameters(), 'lr': 1e-3},
    {'params': model.decoder.parameters(), 'lr': 1e-4}
])

# 学习率调度器
from torch.optim.lr_scheduler import StepLR, CosineAnnealingLR, ReduceLROnPlateau

# 每N个epoch降低学习率
scheduler = StepLR(optimizer, step_size=10, gamma=0.1)

# 余弦退火
scheduler = CosineAnnealingLR(optimizer, T_max=100)

# 根据指标自适应调整
scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10)
```

## 6. 数据加载

### 6.1 Dataset 和 DataLoader

```python
from torch.utils.data import Dataset, DataLoader

# 自定义Dataset
class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        x = self.data[idx]
        y = self.labels[idx]
        return x, y

# 创建数据集
data = torch.randn(1000, 784)
labels = torch.randint(0, 10, (1000,))
dataset = CustomDataset(data, labels)

# 创建DataLoader
dataloader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    pin_memory=True  # 加速GPU传输
)

# 使用DataLoader
for batch_idx, (data, target) in enumerate(dataloader):
    # 训练代码
    pass
```

### 6.2 数据增强

```python
from torchvision import transforms

# 图像变换
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                       std=[0.229, 0.224, 0.225])
])

# 应用到Dataset
class ImageDataset(Dataset):
    def __init__(self, images, labels, transform=None):
        self.images = images
        self.labels = labels
        self.transform = transform
    
    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        
        if self.transform:
            image = self.transform(image)
        
        return image, label
```

## 7. 完整训练流程

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 1. 准备数据
X_train = torch.randn(1000, 784)
y_train = torch.randint(0, 10, (1000,))
X_val = torch.randn(200, 784)
y_val = torch.randint(0, 10, (200,))

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

# 2. 定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x

model = Net()

# 3. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. 训练函数
def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for batch_idx, (data, target) in enumerate(dataloader):
        data, target = data.to(device), target.to(device)
        
        # 前向传播
        output = model(data)
        loss = criterion(output, target)
        
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # 统计
        total_loss += loss.item()
        pred = output.argmax(dim=1)
        correct += pred.eq(target).sum().item()
        total += target.size(0)
    
    avg_loss = total_loss / len(dataloader)
    accuracy = correct / total
    return avg_loss, accuracy

# 5. 验证函数
def validate(model, dataloader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data, target in dataloader:
            data, target = data.to(device), target.to(device)
            
            output = model(data)
            loss = criterion(output, target)
            
            total_loss += loss.item()
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()
            total += target.size(0)
    
    avg_loss = total_loss / len(dataloader)
    accuracy = correct / total
    return avg_loss, accuracy

# 6. 训练循环
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

num_epochs = 50
best_val_acc = 0

for epoch in range(num_epochs):
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    val_loss, val_acc = validate(model, val_loader, criterion, device)
    
    print(f'Epoch {epoch+1}/{num_epochs}')
    print(f'  Train Loss: {train_loss:.4f}, Acc: {train_acc:.4f}')
    print(f'  Val Loss: {val_loss:.4f}, Acc: {val_acc:.4f}')
    
    # 保存最佳模型
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_model.pth')

# 7. 加载模型
model.load_state_dict(torch.load('best_model.pth'))
```

## 8. 模型保存和加载

```python
# 保存整个模型
torch.save(model, 'model.pth')
model = torch.load('model.pth')

# 只保存参数（推荐）
torch.save(model.state_dict(), 'model_weights.pth')
model.load_state_dict(torch.load('model_weights.pth'))

# 保存训练状态
checkpoint = {
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}
torch.save(checkpoint, 'checkpoint.pth')

# 加载训练状态
checkpoint = torch.load('checkpoint.pth')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']
```

## 9. GPU 加速

```python
# 检查GPU可用性
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))

# 设置设备
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 将模型和数据移到GPU
model = model.to(device)
data = data.to(device)

# 多GPU训练
if torch.cuda.device_count() > 1:
    model = nn.DataParallel(model)

# 混合精度训练
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in train_loader:
    optimizer.zero_grad()
    
    # 自动混合精度
    with autocast():
        output = model(data)
        loss = criterion(output, target)
    
    # 缩放损失并反向传播
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## 实战练习

### 练习1：构建CNN图像分类器

```python
class CNN(nn.Module):
    def __init__(self, num_classes=10):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 4 * 4, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
```

### 练习2：实现自定义损失函数

```python
class FocalLoss(nn.Module):
    def __init__(self, alpha=1, gamma=2):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
    
    def forward(self, inputs, targets):
        ce_loss = F.cross_entropy(inputs, targets, reduction='none')
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha * (1 - pt) ** self.gamma * ce_loss
        return focal_loss.mean()
```
