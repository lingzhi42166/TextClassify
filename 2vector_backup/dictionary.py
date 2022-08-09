from gensim.models.tfidfmodel import TfidfModel
from gensim import corpora
from collections import defaultdict
import math
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

""" 创建词典 """
type = 'politics'
InputPath = '2vector/Good/politics/politics_分词并去停用词.txt'
DF_Path = '2vector/Good/'+ type +'/_DF.txt'
IDF_Path = '2vector/Good/'+ type +'/_IDF.txt'
TF_IDF_Path = '2vector/Good/'+ type +'/TF_IDF.txt'
Fe_Path = '2vector/Good/'+ type +'/词频.txt'
t2id_Path = '2vector/Good/'+ type +'/id.txt'
#导入语料（分好词的） 并做去空行处理

text_list = [] #每一行为一个文本
def read_txt1():
  txt = open(InputPath,'r',encoding='utf-8')

  for line in txt:
    #如果字符串中只包含空格，则返回 True，否则返回 False。
    if line.isspace():
        continue
    else:
      text = [word for word in line.split() ]
      # gensim中需要语料库是这种格式，与sklearn也不一样 ['词1','词2','']，所以通过split以空格为间隔符 分
      
      text_list.append(text)
  txt.close()

read_txt1() #读取分词后的AllIn文本


# 2、计算词频
frequency = defaultdict(int)  # 构建一个字典对象
# 遍历分词后的结果集，计算每个词出现的频率
for text in text_list:
    for token in text:
        frequency[token] += 1
# print(frequency)



# 选择频率大于1的词  => 在原文中 只保留出现过>=2的词

text_list = [[token for token in text if frequency[token] > 1] for text in text_list]

#3.创建字典（单词与编号之间的映射）
dictionary = corpora.Dictionary(text_list)
# print(len(dictionary)) # 34373

# print(dictionary.token2id)  # 单词到ID的映射
# print(dictionary.dfs)       #  查看多少文档包含这个token id


# # 将每一篇文档转换为向量
# corpus = [dictionary.doc2bow(text) for text in text_list]

# #初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
# tfidf = models.TfidfModel(corpus)






def save_2id():
  newF = open(t2id_Path,'w+',encoding='utf-8')
  t2id = dictionary.token2id
  print(t2id)
  for i in t2id:
    id = t2id[i]
    newF.write(i + ':' + str(id) + '\n')
  newF.close()

save_2id()



""" 读取单词的df 文档频率  查看多少文档包含这个token id"""
def re_df():
  newF = open(DF_Path,'w+',encoding='utf-8')
  token_2id = dictionary.token2id
  id_dfs = dictionary.dfs
  for i in token_2id:
    id = token_2id[i]
    num = id_dfs[id]
    newF.write(i + ':' + str(num) + '\n')
  newF.close()
re_df()  #获取构建后的词典的词项文档频率



""" 计算idf方法 """
totaldocs = dictionary.num_docs
# print(totaldocs)

def df2idf(docfreq, log_base=2.0, add=0.0):
  """使用文档频率去计算，逆文档频率   以log_base 2为底数"""
  return add + math.log(1.0 * totaldocs / docfreq, log_base)

""" 计算单词的idf 逆文档频率 """
def re_idf():
  newF = open(IDF_Path,'w+',encoding='utf-8')
  token_2id = dictionary.token2id
  id_dfs = dictionary.dfs
  for i in token_2id:
    id = token_2id[i]
    num = id_dfs[id]
    idf_num = df2idf(num)
    newF.write(i + ':' + str(idf_num) + '\n')
  newF.close()

re_idf()  #计算词项的idf


""" 计算单词的tf-idf  """
def re_tf_idf():
  newF = open(TF_IDF_Path,'w+',encoding='utf-8')
  token_2id = dictionary.token2id
  id_dfs = dictionary.dfs
  for i in token_2id:
    id = token_2id[i]
    num = id_dfs[id]
    idf_num = df2idf(num)
    tf_idf_num = frequency[i] * idf_num
    newF.write(i + ':' + str(tf_idf_num) + '\n')

  newF.close()

re_tf_idf()  #计算词项的TF-idf





""" 把语料库词频保存出去   Python中没有分号,用严格的缩进来表示上下级从属关系 冒号后面是要写上一定的内容的 所以不能注释函数内容"""
def re_ciPin():
  newF = open(Fe_Path,'w+',encoding='utf-8')
  for i in frequency:
    newF.write(i + ':' + str(frequency[i]) + '\n') 
  newF.close()








re_ciPin()   #词频
