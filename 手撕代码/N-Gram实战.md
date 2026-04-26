## 什么是词元  
词元（token）是自然语言处理中的一个基本单位，通常包括单词、标点符号、标点符号、空格等。  
  
英文中可以是一个单词、一个字母、一个标点符号、一个字词（subword，unhappy -> un和happy）  
  
中文中可以是一个字、一个词语，一个成语

## 常见的分词
### jieba分词  
  
jieba是一个基于结巴分词的分词器，可以进行中文分词。![[Pasted image 20260425182756.png]]

### bert-base-chinese的分词器  
==bert自带的分词器是针对英文的，bert-base-chinese有单独的针对中文的分词器（按字来的）==
![[Pasted image 20260425185418.png]]
![[Pasted image 20260426173038.png]]
