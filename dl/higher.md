## 影响网络准确率的的因素

### 模型部分
 - 模型的表示能力
 - 卷积的时候即使输入的H、W不和kernel_size stride匹配也会进行运算，只计算能够进行卷积的部分，剩余的不卷积
 - fine grained概念相关的论文

### 数据部分
 - 数据量，不平衡

### 参数部分
 - 初始化
 - 迁移学习、使用的是预训练之后的模型么
