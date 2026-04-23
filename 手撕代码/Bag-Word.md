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


