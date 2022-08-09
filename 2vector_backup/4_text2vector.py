# from calendar import c
from array import array
import io
import sys
import os
import math
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

""" 文本向量化 """


type = 'Economy'
base_path = '2vector/Good/'+ type +'/'

input_path = base_path + '_分词并去停用词.txt'

ciDian_path = '2vector/政治降序归一化词典.txt'
idf_path = '2vector/_IDF.txt'


out_frequency_path = base_path + 'frequency/'
out_tf_idf_path = base_path + 'Tf-idf/'
out_norm_tf_idf_path = base_path + '归一化TF-idf/'

ciDianArr = [];


""" 读取词典 并只提取词 """
def read_ciDian():
  global ciDianArr
  f = open(ciDian_path,'r',encoding='utf-8')
  str = f.read()
  str = str.replace('[','')
  str = str.replace(']','')
  str = str.split(',')
  
  f.close()
  for i in str:
    i = i.replace("\'",'')
    i = i.lstrip()
    ciDianArr.append(i)
read_ciDian()
# print(ciDianArr)
""" 读取词典的IDF  变成dict格式 """

def read_ciDianIdf():
  ciDianIdf_dict = {}
  f = open(idf_path,'r',encoding='utf-8')
  for i in f:
    str = i.split(':')
    idf_str = str[1].replace('\n','')
    ciDianIdf_dict[str[0]] = idf_str
  f.close()
  return ciDianIdf_dict

# read_ciDianIdf()
# print(ciDianIdfArr)

""" 保存到文件 """
def saveFile(path,data):

  f = open(path,'w+',encoding='utf-8')
  f.write(data)
  f.close()

""" 读取测试文本，进行文本向量化 
1、统计本文的词频  将文本以空格为间隔 ['','','']

"""
# 统计词频方法
def txt_Frequency(text_list):
  frequency = defaultdict(int)  # 构建一个字典对象
  # 遍历分词后的结果集，计算每个词出现的频率
  for text in text_list:
    frequency[text] += 1
  return frequency

# 计算TF-IDF  输入都是dict类型的   frequency {词：词频}   idf{词：idf}
def tf_IDF(frequency,idf):
  tf_idf_arr = []
  for ci_str in ciDianArr:
    if ci_str in frequency:
      tf_idf = float(idf[ci_str]) * float(frequency[ci_str])
    else:
      tf_idf = 0
    tf_idf_arr.append(tf_idf)
  
  return tf_idf_arr

tf_idf_arr = [] # 把所有文档的
def read_txt_calculate():
  global tf_idf_arr 
  num = 1;
  f = open(input_path,'r',encoding='utf-8')
  for line in f:
    if(line.isspace()):continue; #空行不要统计 不然就为空了
    text = [word for word in line.split() ] # return [[词1，词2],[词1，词2],[词1，词2]]

    frequency_dict = txt_Frequency(text)
    idf_dict = read_ciDianIdf() #返回的是 列表
    tf_idf = tf_IDF(frequency_dict,idf_dict) #计算TF-IDF
    tf_idf_arr.append(tf_idf)

    saveFile(out_frequency_path + '文本' + str(num) +'的词频.txt',str(frequency_dict))
    saveFile(out_tf_idf_path + '文本' + str(num) + '的TF-IDF.txt',str(tf_idf))
    num+=1
  print(len(tf_idf_arr))
  f.close()

read_txt_calculate()



""" TF-IDF归一化处理 """
def tf_IDF_norm(): 
  num = 0;
  all_norm_sqrt_arr = []
  sqrt_arr = []
  tf_idf_add = 0;
  # print(tf_idf_arr)
  for i in tf_idf_arr:
    for j in i:
      if j == 0 : 
        continue
      tf_idf_add += j**2 
    sqrt_ = math.sqrt(tf_idf_add)#归一化 的分母只是求和自己这一篇文章的tf-idf^2
    sqrt_arr.append(sqrt_)

  # print(sqrt_arr[0])
  all_norm_sqrt_arr.append(sqrt_arr)
  saveFile(base_path + '文本的归一化分母数组.txt',str(all_norm_sqrt_arr))

  for k in tf_idf_arr:
    norm_TF_IDF_arr = [] #每一次新的循环 也就是进入新的文章时 归一化数组要清零，不然就重叠了
    for l in k:
      if l == 0 : 
        norm_TF_IDF = 0
      else:
        norm_TF_IDF = l / sqrt_arr[num] #第几篇就除以第几篇的 分母
      norm_TF_IDF_arr.append(norm_TF_IDF)
    
      
    saveFile(out_norm_tf_idf_path + '文本' + str(num) + '的归一化TF-IDF.txt',str(norm_TF_IDF_arr))
    
    num+=1

tf_IDF_norm()






