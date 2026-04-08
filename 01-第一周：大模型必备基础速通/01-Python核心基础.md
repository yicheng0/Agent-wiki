# Python 核心基础 - 大模型开发必备

## 1. 数据类型与结构

### 1.1 基本数据类型

```python
# 字符串 - 处理文本数据（prompt、response）
text = "Hello, AI"
prompt = """多行文本
用于构建复杂的提示词"""

# 数字类型
learning_rate = 0.001  # float - 学习率
batch_size = 32        # int - 批次大小

# 布尔值 - 控制流程
is_training = True
use_cache = False
```

### 1.2 列表（List）- 最常用的序列类型

```python
# 存储批次数据
batch_texts = ["文本1", "文本2", "文本3"]
token_ids = [101, 2023, 2003, 102]

# 常用操作
batch_texts.append("文本4")      # 添加
first_text = batch_texts[0]      # 索引访问
sub_batch = batch_texts[1:3]     # 切片
batch_size = len(batch_texts)    # 长度

# 列表推导式 - 高效数据处理
lengths = [len(text) for text in batch_texts]
filtered = [x for x in token_ids if x > 100]
```

### 1.3 字典（Dict）- 存储配置和映射

```python
# 模型配置
config = {
    "model_name": "gpt-3.5",
    "temperature": 0.7,
    "max_tokens": 2048
}

# 访问和修改
model = config["model_name"]
config["temperature"] = 0.9

# 常用方法
keys = config.keys()
values = config.values()
items = config.items()
```

### 1.4 元组（Tuple）- 不可变序列

```python
# 固定的配置参数
model_shape = (768, 12, 12)  # (hidden_size, num_layers, num_heads)
version = (1, 0, 0)

# 解包
hidden_size, num_layers, num_heads = model_shape
```

## 2. 函数式编程

### 2.1 函数定义与参数

```python
# 基本函数
def tokenize(text, max_length=512):
    """文本分词函数"""
    tokens = text.split()
    return tokens[:max_length]

# 多返回值
def forward_pass(input_ids, attention_mask):
    logits = model(input_ids, attention_mask)
    loss = compute_loss(logits)
    return logits, loss

# 可变参数
def batch_process(*texts, **kwargs):
    max_length = kwargs.get('max_length', 512)
    return [tokenize(t, max_length) for t in texts]
```

### 2.2 Lambda 表达式

```python
# 简单的匿名函数
square = lambda x: x ** 2
add = lambda x, y: x + y

# 在数据处理中使用
sorted_texts = sorted(batch_texts, key=lambda x: len(x))
```

### 2.3 高阶函数

```python
# map - 批量转换
token_lengths = list(map(len, batch_texts))

# filter - 过滤数据
long_texts = list(filter(lambda x: len(x) > 100, batch_texts))

# reduce - 聚合操作
from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
```

## 3. 面向对象编程

### 3.1 类的定义

```python
class Tokenizer:
    """分词器类"""
    
    def __init__(self, vocab_size=50000, max_length=512):
        self.vocab_size = vocab_size
        self.max_length = max_length
        self.vocab = {}
    
    def encode(self, text):
        """编码文本为token ids"""
        tokens = text.split()
        return [self.vocab.get(t, 0) for t in tokens]
    
    def decode(self, token_ids):
        """解码token ids为文本"""
        inv_vocab = {v: k for k, v in self.vocab.items()}
        return ' '.join([inv_vocab.get(id, '[UNK]') for id in token_ids])
```

### 3.2 继承与多态

```python
class BaseModel:
    def __init__(self, config):
        self.config = config
    
    def forward(self, inputs):
        raise NotImplementedError

class GPTModel(BaseModel):
    def __init__(self, config):
        super().__init__(config)
        self.layers = self._build_layers()
    
    def forward(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer(x)
        return x
    
    def _build_layers(self):
        return [TransformerLayer() for _ in range(self.config['num_layers'])]
```

### 3.3 特殊方法

```python
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        """支持 len(dataset)"""
        return len(self.data)
    
    def __getitem__(self, idx):
        """支持 dataset[idx]"""
        return self.data[idx]
    
    def __iter__(self):
        """支持 for item in dataset"""
        return iter(self.data)
```

## 4. NumPy 基础

### 4.1 数组创建与操作

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
random = np.random.randn(3, 3)

# 数组形状
print(arr.shape)        # (4,)
print(zeros.shape)      # (3, 4)

# 重塑
reshaped = arr.reshape(2, 2)
flattened = reshaped.flatten()
```

### 4.2 数组运算

```python
# 元素级运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b               # [5, 7, 9]
d = a * b               # [4, 10, 18]
e = a ** 2              # [1, 4, 9]

# 矩阵运算
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)        # 矩阵乘法
C = A @ B               # 等价写法
```

### 4.3 索引与切片

```python
# 一维数组
arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[2])           # 2
print(arr[1:4])         # [1, 2, 3]
print(arr[::2])         # [0, 2, 4]

# 多维数组
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0, 1])     # 2
print(matrix[:, 1])     # [2, 5, 8]
print(matrix[1:, :2])   # [[4, 5], [7, 8]]

# 布尔索引
mask = arr > 2
filtered = arr[mask]    # [3, 4, 5]
```

### 4.4 广播机制

```python
# 不同形状的数组运算
a = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
b = np.array([10, 20, 30])             # (3,)

c = a + b  # b 自动广播为 [[10, 20, 30], [10, 20, 30]]
# 结果: [[11, 22, 33], [14, 25, 36]]
```

## 5. Pandas 基础

### 5.1 Series 和 DataFrame

```python
import pandas as pd

# Series - 一维数据
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s['a'])           # 1

# DataFrame - 二维表格
data = {
    'text': ['样本1', '样本2', '样本3'],
    'label': [0, 1, 0],
    'length': [50, 120, 80]
}
df = pd.DataFrame(data)
```

### 5.2 数据读取与保存

```python
# 读取数据
df = pd.read_csv('train.csv')
df = pd.read_json('data.json')
df = pd.read_excel('data.xlsx')

# 保存数据
df.to_csv('output.csv', index=False)
df.to_json('output.json')
```

### 5.3 数据选择与过滤

```python
# 列选择
texts = df['text']
subset = df[['text', 'label']]

# 行选择
first_row = df.iloc[0]
first_three = df.iloc[:3]
by_label = df.loc[df['label'] == 1]

# 条件过滤
long_texts = df[df['length'] > 100]
filtered = df[(df['label'] == 1) & (df['length'] > 50)]
```

### 5.4 数据处理

```python
# 统计信息
print(df.describe())
print(df['length'].mean())
print(df['label'].value_counts())

# 数据清洗
df = df.dropna()                    # 删除缺失值
df = df.drop_duplicates()           # 删除重复行
df['text'] = df['text'].fillna('')  # 填充缺失值

# 数据转换
df['length'] = df['text'].apply(len)
df['label_str'] = df['label'].map({0: 'negative', 1: 'positive'})
```

## 6. 文件操作

### 6.1 文本文件读写

```python
# 读取文件
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = f.readlines()

# 写入文件
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, AI\n')
    f.writelines(['line1\n', 'line2\n'])

# 追加模式
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('New log entry\n')
```

### 6.2 JSON 处理

```python
import json

# 读取 JSON
with open('config.json', 'r') as f:
    config = json.load(f)

# 写入 JSON
data = {'model': 'gpt-3.5', 'temperature': 0.7}
with open('config.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 字符串转换
json_str = json.dumps(data)
data = json.loads(json_str)
```

### 6.3 路径操作

```python
from pathlib import Path

# 路径操作
data_dir = Path('data')
model_path = data_dir / 'model.pt'

# 检查存在
if model_path.exists():
    print('Model found')

# 创建目录
output_dir = Path('output')
output_dir.mkdir(parents=True, exist_ok=True)

# 遍历文件
for file in data_dir.glob('*.txt'):
    print(file.name)
```

## 7. 异常处理

```python
# 基本异常处理
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Cleanup code")

# 自定义异常
class ModelLoadError(Exception):
    pass

def load_model(path):
    if not Path(path).exists():
        raise ModelLoadError(f"Model not found: {path}")
    return model

# 使用
try:
    model = load_model('model.pt')
except ModelLoadError as e:
    print(e)
```

## 8. 常用内置函数

```python
# 类型转换
int('123')              # 123
float('3.14')           # 3.14
str(123)                # '123'
list('abc')             # ['a', 'b', 'c']

# 序列操作
len([1, 2, 3])          # 3
sum([1, 2, 3])          # 6
max([1, 2, 3])          # 3
min([1, 2, 3])          # 1
sorted([3, 1, 2])       # [1, 2, 3]

# 迭代工具
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)      # 0 a, 1 b, 2 c

for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)         # 1 a, 2 b, 3 c

# 范围生成
range(5)                # 0, 1, 2, 3, 4
range(1, 5)             # 1, 2, 3, 4
range(0, 10, 2)         # 0, 2, 4, 6, 8
```

## 9. 装饰器

```python
import time
from functools import wraps

# 计时装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def train_model(epochs):
    # 训练代码
    time.sleep(1)
    return "Model trained"

# 缓存装饰器
def cache(func):
    cached_results = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    return wrapper

@cache
def expensive_computation(n):
    return sum(range(n))
```

## 10. 上下文管理器

```python
# 使用 with 语句
with open('file.txt', 'r') as f:
    content = f.read()
# 文件自动关闭

# 自定义上下文管理器
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.2f}s")

# 使用
with Timer():
    # 需要计时的代码
    time.sleep(1)
```

## 实战练习

### 练习1：数据预处理

```python
import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv('train.csv')

# 数据清洗
df = df.dropna()
df['text'] = df['text'].str.strip()

# 特征工程
df['length'] = df['text'].apply(len)
df['word_count'] = df['text'].apply(lambda x: len(x.split()))

# 数据分割
from sklearn.model_selection import train_test_split
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

print(f"Train: {len(train_df)}, Val: {len(val_df)}")
```

### 练习2：批次数据生成器

```python
class DataLoader:
    def __init__(self, data, batch_size=32, shuffle=True):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
    
    def __iter__(self):
        indices = np.arange(len(self.data))
        if self.shuffle:
            np.random.shuffle(indices)
        
        for i in range(0, len(indices), self.batch_size):
            batch_indices = indices[i:i + self.batch_size]
            yield [self.data[idx] for idx in batch_indices]
    
    def __len__(self):
        return (len(self.data) + self.batch_size - 1) // self.batch_size

# 使用
data = list(range(100))
loader = DataLoader(data, batch_size=10)

for batch in loader:
    print(f"Batch size: {len(batch)}")
```

### 练习3：配置管理

```python
import json
from pathlib import Path

class Config:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config = self.load()
    
    def load(self):
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}
    
    def save(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()

# 使用
config = Config('model_config.json')
config.set('learning_rate', 0.001)
config.set('batch_size', 32)
print(config.get('learning_rate'))
```