## 准备语料
```python
texts = [  
    "I love natural language processing.",  
    "I love machine learning.",  
    "I love coding in Python and Java.",  
    "I love Java.",  
    "I love Java, I don't love C++",  
    "I don't love Java."  
]
```

## 分词
``` python
words = [word for text in texts for word in text.split()]  
print(words)
```

## 构造词汇表

```python
vocabulary = {}  
for word in words:  
    if word not in vocabulary:  
        vocabulary[word] = len(vocabulary)  
  
vocabulary
```

## 转成bag-of-words向量
``` python
bows = []  
for text in texts:  
    bow = [0] * len(vocabulary)   # 词表长度的全零向量  
    for word in text.split():  
        bow[vocabulary[word]] += 1  
    bows.append(bow)  
  
bows
```
## 相似度  
  
两个句子的向量相似，就代表两个句子中的词相似，就代表两个句子的语义相似  
  
### 余弦相似度（Cosine Similarity）  
- **原理**：计算两个向量的夹角余弦值（忽略向量长度）。  
- **公式**：  
$$cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \cdot \|\mathbf{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \cdot \sqrt{\sum_{i=1}^{n} B_i^2}}$$  
- **应用**：文本相似度、推荐系统  
  
### 点积相似度（Dot Product Similarity）  
- **原理**：计算向量的内积（方向 + 长度均考虑）。  
- **公式**：  
$${sim}(\mathbf{A}, \mathbf{B}) = \mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} A_i B_i$$  
- **应用**：Transformer


Word2Vec分两种：  
* Continuous Skip-gram (CSG)：跳词模型，给定中心词，预测周围词  
* Continuous Bag-of-Words (CBoW)：连续的词袋模型，给定周围词，预测中心词  
  
通过Word2Vec的方式来训练模型，最终既能学到词向量，也能学到词之间的语义关系

![[Pasted image 20260423214723.png]]
![[Pasted image 20260423214746.png]]


``` python
# 生成训练数据  
def generate_training_data(sentences, window_size):  
    center_words = []  
    target_words = []  
  
    for sentence in sentences:  
        indices = [vocabulary[word] for word in sentence]  
        for center_pos in range(len(indices)):  
            # 确定上下文窗口范围  
            start = max(0, center_pos - window_size)  
            end = min(len(indices), center_pos + window_size + 1)  
  
            # 收集上下文词  
            for context_pos in range(start, end):  
                if context_pos != center_pos:  
                    center_words.append(indices[center_pos])  
                    target_words.append(indices[context_pos])  
  
    return torch.LongTensor(center_words), torch.LongTensor(target_words)  
  
  
WINDOW_SIZE = 2  
center_words, target_words = generate_training_data(sentences, WINDOW_SIZE)  
  
center_words, target_words
```
``` python
from torch import nn  
from torch import optim  
  
class SkipGram(nn.Module):  
    def __init__(self, vocab_size, embedding_dim):  
        super().__init__()  
  
        self.input_embed = nn.Linear(vocab_size, embedding_dim, bias=False)    # y=wx  13*100  
        self.output_embed = nn.Linear(embedding_dim, vocab_size, bias=False)   # y=wx  100*13  
  
    def forward(self, center_word):  
        center_word_one_hot = one_hot(center_word, vocab_size).view(1, -1)  
  
        hidden = self.input_embed(center_word_one_hot)  
        return self.output_embed(hidden)  
  
  
EMBEDDING_DIM = 10  


  
# 初始化模型、损失函数和优化器  
model = SkipGram(vocab_size, EMBEDDING_DIM)  
optimizer = optim.SGD(model.parameters(), lr=0.01)  
criterion = nn.CrossEntropyLoss()  
  
  
# 开始训练  
EPOCHS = 10  
  
for epoch in range(EPOCHS):  
    for center_batch, target_batch in dataloader:  
        predict = model(center_batch)  
        loss = criterion(predict, target_batch)  
  
        # 反向传播  
        optimizer.zero_grad()  
        loss.backward()  
        optimizer.step()  
  
        print(f"Epoch {epoch + 1}/{EPOCHS}, Loss: {loss:.4f}")
```
