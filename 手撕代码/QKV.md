```python
import torch  
import torch.nn as nn  
  
  
class SelfAttention(nn.Module):  
  
    def __init__(self, embed_dim: int, attn_dim: int, output_dim: int):  
        super().__init__()  
  
        self.embed_dim = embed_dim  
        self.attn_dim = attn_dim  
        self.output_dim = output_dim  
  
        # QKV投影层：从输入维度映射到内部维度  
        # projection  
        self.q_proj = nn.Linear(embed_dim, self.attn_dim, bias=False) # y=wx  
        self.k_proj = nn.Linear(embed_dim, self.attn_dim, bias=False)  
        self.v_proj = nn.Linear(embed_dim, self.attn_dim, bias=False)  
  
        # 输出投影层：从内部维度映射到输出维度  
        self.out_proj = nn.Linear(self.attn_dim, self.output_dim, bias=False)  
  
    def forward(self, x):  
        """  
        输入: [batch_size, seq_len, embed_dim]  
        返回: [batch_size, seq_len, output_dim]  
        """        batch_size, seq_len, embed_dim = x.shape  
  
        # 投影到QKV空间  
        #  (batch_size, seq_len, embed_dim) * (embed_dim, attn_dim)  
        q = self.q_proj(x)  # [batch_size, seq_len, attn_dim]  
        k = self.k_proj(x)  # [batch_size, seq_len, attn_dim]  
        v = self.v_proj(x)  # [batch_size, seq_len, attn_dim]  
  
        # 计算注意力分数  
        # q [batch_size, seq_len, attn_dim]  
        # k.T [batch_size, attn_dim, seq_len]        # q @ k.T 形状: [batch_size, seq_len, seq_len]  
        attn_scores = torch.matmul(q, k.transpose(-2, -1))  
  
        # 缩放因子：防止乘积过大  
        d_k = k.size(-1)  
        attn_scores = attn_scores / torch.sqrt(torch.tensor(d_k))  
  
        # 计算注意力权重  
        attn_weights = torch.softmax(attn_scores, dim=-1)  
  
        # 计算注意力输出  
        # attn_weights: [batch_size, seq_len, seq_len]  
        # v: [batch_size, seq_len, attn_dim]        # [batch_size, seq_len, attn_dim]        attn_out = torch.matmul(attn_weights, v)  
  
        # 投影到输出空间  
        return self.out_proj(attn_out)
```