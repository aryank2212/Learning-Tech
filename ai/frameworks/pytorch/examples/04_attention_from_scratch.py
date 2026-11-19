# /// script
# requires-python = ">=3.11"
# dependencies = ["torch"]
# ///
"""Self-attention written by hand, then checked against PyTorch's built-in version.

Run:  uv run 04_attention_from_scratch.py
"""
import torch
import torch.nn.functional as F
from torch import nn

torch.manual_seed(0)


def attention(q, k, v, causal=True):
    """softmax(q k^T / sqrt(d)) v, with an optional mask so a position can't see the future."""
    d = q.size(-1)
    scores = q @ k.transpose(-2, -1) / d**0.5
    if causal:
        future = torch.triu(torch.ones(scores.shape[-2:], dtype=torch.bool), diagonal=1)
        scores = scores.masked_fill(future, float("-inf"))
    return torch.softmax(scores, dim=-1) @ v


class SelfAttention(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.qkv = nn.Linear(dim, 3 * dim, bias=False)
        self.out = nn.Linear(dim, dim, bias=False)

    def forward(self, x):                       # x: (batch, time, dim)
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        return self.out(attention(q, k, v))


q, k, v = (torch.randn(2, 5, 8) for _ in range(3))
mine = attention(q, k, v)
reference = F.scaled_dot_product_attention(q, k, v, is_causal=True)
print("matches F.scaled_dot_product_attention:", torch.allclose(mine, reference, atol=1e-5))

layer = SelfAttention(8)
x = torch.randn(2, 5, 8)
print("output shape:", tuple(layer(x).shape))

# The causal mask means changing a *later* token must not change an *earlier* output.
x2 = x.clone()
x2[:, -1] += 10.0
print("earlier positions unchanged by a later token:", torch.allclose(layer(x)[:, :-1], layer(x2)[:, :-1], atol=1e-5))
