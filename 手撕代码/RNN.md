``` python
import torch  
import torch.nn as nn  
  
  
  
# seq 50个字 --> 5个词向量---->RNN--->结果  
  
class ZhouyuRNN(nn.Module):  
    def __init__(self, input_size, hidden_size):  
        super().__init__()  
  
        self.hidden_size = hidden_size  
  
        # 初始化权重参数  
        # input_size表示单词的词向量维度  
        # hidden_size表示隐藏层的维度  
        self.W_xh = nn.Parameter(torch.randn(input_size, hidden_size))  
        self.W_hh = nn.Parameter(torch.randn(hidden_size, hidden_size))  
        self.b_h = nn.Parameter(torch.zeros(hidden_size))  
  
        self.hidden = None  
  
    def init_hidden(self, batch_size):  
        # 初始化隐藏状态为全零  
        return torch.zeros(batch_size, self.hidden_size)  
  
    def forward(self, x):  
        # x的形状: (batch_size, seq_len, input_size)  
        batch_size, seq_len, input_size = x.shape  
  
        # 修改x的形状为：(seq_len, batch_size, input_size)  
        x = torch.transpose(x, 0, 1)  
  
        self.hidden = self.init_hidden(batch_size)  
  
        # 存储所有时间步的隐藏状态  
        hidden_states = []  
  
        # seq_len表示当前输入的序列长度，比如有多少个词  
        # 从第一个单词开始，到最后一个单词结束  
        for t in range(seq_len):  
            # 获取当前时间步的输入  
            # 也就是获取当前的单词，单词需要用词向量来表示  
            x_t = x[t]  
  
            # 计算隐藏状态  
            self.hidden = torch.tanh(  
                torch.mm(x_t, self.W_xh) +  
                torch.mm(self.hidden, self.W_hh) +  
                self.b_h  
            )  
  
            # 当前时间步的隐藏状态  
            hidden_states.append(self.hidden)  
  
        return torch.stack(hidden_states, dim=0), self.hidden  
        # return hidden_states, self.hidden  
  
  
# 超参数  
input_size = 3  # 表示输入的单词对应的词向量的维度  
hidden_size = 2  # 隐藏层维度，比如2个神经元，也就是一句话要分别输入给这两个神经元，所谓隐藏层状态，就是这两个神经元对应的状态  
seq_len = 4  # 表示1句话的长度，比如4个单词  
batch_size = 2  # 表示每次输入给模型的只有1句话  
  
rnn = ZhouyuRNN(input_size, hidden_size)  
  
# 创建随机输入数据  
x = torch.randn(batch_size, seq_len, input_size)  
print(x)  
print(x.shape)
```

``` python
  
# 超参数设置  
SEQ_LENGTH = 5  # 输入序列长度  
BATCH_SIZE = 1  
HIDDEN_SIZE = 128  
INPUT_SIZE = 128  
  
  
# 创建训练数据  
class TextDataset(Dataset):  
    def __init__(self, text, seq_length):  
        self.text = text  
        self.seq_length = seq_length  
  
        # 转换为索引序列  
        self.data = [word_to_idx[ch] for ch in text]  
  
    def __len__(self):  
        return len(self.data) - self.seq_length  
  
    def __getitem__(self, idx):  
        # 文本里的某个序列 X        input_seq = self.data[idx:idx + self.seq_length]  
  
        # 目标序列 Y        target_seq = self.data[idx + 1:idx + self.seq_length + 1]  
  
        # 相当于，假如语料为abcdefg, input_seq=abc, target_seq=bcd  
  
        return torch.LongTensor(input_seq), torch.LongTensor(target_seq)  
  
  
dataset = TextDataset(text, SEQ_LENGTH)  
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False)  
  
for input_seq, target_seq in dataloader:  
    print(input_seq)  
    print(target_seq)  
    break
```

```python
class ZhouyuModel(nn.Module):  
    def __init__(self, vocab_size, input_size, hidden_size):  
        super().__init__()  
  
        self.hidden_size = hidden_size  
  
        # 嵌入层，输入词索引，输出词向量  
        self.embedding = nn.Embedding(vocab_size, input_size)  
  
        # RNN参数  
        self.W_xh = nn.Parameter(torch.randn(input_size, hidden_size))  
        self.W_hh = nn.Parameter(torch.randn(hidden_size, hidden_size))  
        self.b_h = nn.Parameter(torch.zeros(hidden_size))  
  
        # 输出层  
        self.out_linear = nn.Linear(hidden_size, vocab_size)  
  
    def forward(self, x, hidden=None):  
  
        embedded = self.embedding(x)  
  
        batch_size, seq_len, input_size = embedded.shape  
        embedded = torch.transpose(embedded, 0, 1)  
  
        # 初始化隐藏状态，每个seq都创建一个初始隐藏状态  
        if hidden is None:  
            hidden = torch.zeros(batch_size, self.hidden_size)  
  
        outputs = []  
        for t in range(seq_len):  
            # 取第t个时间步对应字的向量  
            x_t = embedded[t]  # (batch_size, hidden_size)  
  
            hidden = torch.tanh(  
                torch.mm(x_t, self.W_xh) +  
                torch.mm(hidden, self.W_hh) +  
                self.b_h  
            )  
  
            # 隐藏状态输入到线性输出层，得到t时刻的输出  
            # 这里的隐藏状态，相当于记忆了前t-1个字的信息，然后结合t时刻的输入x，要预测t时刻对应的y  
            outputs.append(self.out_linear(hidden))  
  
        # outputs保存了所有时间步的输出，输入的是一个序列，每个时间步的输出就组合成了输出序列，然后再和目标序列进行误差计算  
        outputs = torch.stack(outputs, dim=1)  # (batch_size, seq_length, vocab_size)  
  
        return outputs, hidden  
  
  
# 初始化模型  
model = ZhouyuModel(vocab_size, INPUT_SIZE, HIDDEN_SIZE)  
criterion = nn.CrossEntropyLoss()  
optimizer = torch.optim.SGD(model.parameters(), lr=0.005)
```

``` python
  
    words = [word for word in content]  
  
    hidden = None  
    for _ in range(steps):  
        inputs = [word_to_idx[word] for word in words[-SEQ_LENGTH:]] # 取输入的最后SEQ_LENGTH个词的索引  
        # inputs = [word_to_idx[word] for word in words[-1:]] # 取输入的最后SEQ_LENGTH个词的索引  
        inputs = torch.LongTensor(inputs)  
  
        # 输入形状调整  
        inputs = inputs.view(1, -1)  # (1, seq_len)  
  
        # 前向传播  
        with torch.no_grad():  
            # output中包含了每个时间步的输出，推理预测时，只需要取最后一个时间步的输出即可，比如输入“鹰击”，相当于有两个时间步，但是我们只需要第2个时间步的输出，而输出是词汇表中各个词的概率  
            # 而hidden表示隐藏层，在推理预测时，因为我们会连续预测，外层有一个for循环，所以hidden需要保存，以便下一次循环使用  
            outputs, hidden = model(inputs, hidden)  
            last_output = outputs[0, -1, :]  # 取最后一个时间步的输出  
  
        # 应用温度采样  
        # last_output / temperature，相当于将last_output缩小，比如[8,2,2] / 2 = [4,1,1]，使得三个选项对应的数字之间的差别变小了  
        # 当然如果temperature<1，那么就是放大差别，比如[8,2,2] / 0.5 = [16,4,4]  
        # probs为做了softmax之后的概率  
        probs = torch.softmax(last_output / temperature, dim=-1)  
  
        # 多项式采样，probs是一个概率，比如是[0.3,0.2,0.5]，那么就是从0,1,2中随机选一个，那么2被选中的概率就是50%  
        # 谁的概率大，随被采样的概率就大  
        result_idx = torch.multinomial(probs, 1).item()  
  
        #  取概率最大的索引  
        # result_idx = torch.argmax(probs).item()  
  
  
        # 更新输入序列  
        words.append(idx_to_word[result_idx])  
  
    return ''.join(words)  
  
  
# 20表示预测20次, temperature越大，越随机
```

```python
class ZhouyuModel(nn.Module):  
    def __init__(self, vocab_size, input_size, hidden_size):  
        super().__init__()  
  
        self.hidden_size = hidden_size  
  
        # 嵌入层，输入词索引，输出词向量  
        self.embedding = nn.Embedding(vocab_size, input_size)  
  
        # RNN层  
        # Deep RNN  
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True, num_layers=2)  
  
        # 输出层  
        self.out_linear = nn.Linear(hidden_size, vocab_size)  
  
    def forward(self, x, hidden=None):  
        embedded = self.embedding(x)  
        outputs, hidden = self.rnn(embedded, hidden)  
        outputs = self.out_linear(outputs)  
        return outputs, hidden  
  
  
# 初始化模型  
model = ZhouyuModel(vocab_size, INPUT_SIZE, HIDDEN_SIZE)  
criterion = nn.CrossEntropyLoss()  
optimizer = torch.optim.SGD(model.parameters(), lr=0.005)
```
