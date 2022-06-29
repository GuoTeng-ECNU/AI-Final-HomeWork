### 执行环境
 - 本次实验训练主要在colab上执行，如需在本地执行，请安装相关依赖
 - pip3 install -r requirements.txt
 - 注意在执行时需修改路径，符合本地路径
 - 数据集需解压数据集, 数据集链接：https://drive.google.com/file/d/1M1H5TqSCrbjkVL46O_bN63DHBCm7kXwR/view?usp=sharing

### 项目目录
```
.
│  README.md
│  requirements.txt
│
├─model
│      ImageModel.py
│      TextModel.py
│
├─notebook
│      main.ipynb
│      save_text_jsonl.ipynb
│
└─output
        test_output.txt
```

### 执行代码
 - 检查数据集存在，如不存在，解压data.zip
 - 先执行save_text_jsonl.ipynb，将文本数据转为jsonl文件
 - 检查model文件夹里的两个分类器
 - 执行main.ipynb，训练模型，使用late fusion形成融合模型，并输出测试集上的结果