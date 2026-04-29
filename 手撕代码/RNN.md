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
