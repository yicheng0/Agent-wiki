```python
import torch  
import torch.nn as nn  
  
  
class ZhouyuGRUCell(nn.Module):  
    def __init__(self, input_size, hidden_size):  
        super().__init__()  
        self.input_size = input_size  
        self.hidden_size = hidden_size  
  
        self.W_xz = nn.Parameter(torch.randn(input_size, hidden_size))  
        self.W_xr = nn.Parameter(torch.randn(input_size, hidden_size))  
        self.W_xh = nn.Parameter(torch.randn(input_size, hidden_size))  
  
        self.W_hz = nn.Parameter(torch.randn(hidden_size, hidden_size))  
        self.W_hr = nn.Parameter(torch.randn(hidden_size, hidden_size))  
        self.W_hh = nn.Parameter(torch.randn(hidden_size, hidden_size))  
  
        self.b_z = nn.Parameter(torch.zeros(hidden_size))  
        self.b_r = nn.Parameter(torch.zeros(hidden_size))  
        self.b_h = nn.Parameter(torch.zeros(hidden_size))  
  
    def forward(self, x, h_prev):  
        # 更新门  
        z_t = torch.sigmoid(torch.mm(x, self.W_xz) + torch.mm(h_prev, self.W_hz) + self.b_z)  
  
        ## 重置门  
        r_t = torch.sigmoid(torch.mm(x, self.W_xr) + torch.mm(h_prev, self.W_hr) + self.b_r)  
  
        # 候选隐状态  
        h_candidate = torch.tanh(torch.mm(x, self.W_xh) + torch.mm(h_prev * r_t, self.W_hh) + self.b_h)  
  
        # 最终隐状态  
        h_t = (1 - z_t) * h_prev + z_t * h_candidate  
  
        return h_t  
  
  
class ZhouyuGRU(nn.Module):  
    def __init__(self, input_size, hidden_size):  
        super().__init__()  
        self.hidden_size = hidden_size  
        self.cell = ZhouyuGRUCell(input_size, hidden_size)  
  
    def forward(self, x, hidden=None):  
        seq_len, batch_size, input_size = x.shape  
  
        # 初始化隐状态  
        if hidden is None:  
            hidden = torch.zeros(batch_size, self.hidden_size)  
  
        outputs = []  
        for t in range(seq_len):  
            # 输入给GRU，得到当前时间步的隐状态  
            hidden = self.cell(x[t], hidden)  
            outputs.append(hidden)  # 保持维度一致  
  
        return outputs, hidden  
  
  
input_size = 32  
hidden_size = 5  
batch_size = 1  
seq_len = 2  
  
yicheng_gru = YichengGRU(input_size, hidden_size)  
  
x = torch.randn(seq_len, batch_size, input_size)  
outputs, hidden = zhouyu_gru(x)  
  
outputs, hidden
```
