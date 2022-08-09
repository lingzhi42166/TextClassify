import io
import sys
import os
import math

import ast #提供了字符串字典转字典的方法

from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


""" 用于将词典TF-IDF降序以及词典IDF降序 """
cidian_path = '2vector\Good\politics\政治词典TF_IDF.txt'
type = 'politics'
base_path = '2vector/Good/'+ type +'/'

""" 保存文件 """
def saveFile(path,data):
  f = open(path,'w+',encoding='utf-8')
  f.write(str(data))
  f.close()


""" 对键值对词典进行归一化 """
tf_idf_arr = []
key_arr = []
def norm_dic():
  global tf_idf_arr,key_arr
  f = open(cidian_path,'r',encoding='utf-8')
  for i in f:
    i = i.split(':')
    key_arr.append(i[0])
    tf_idf_arr.append(i[1].replace('\n',''))
  f.close()




""" 归一化键值对词典 """
def norm():
  tf_idf = {}
  norm_TF_IDF_arr = []
  index = 0
  idf_add = 0
  for i in tf_idf_arr:
    idf_add += float(i)**2
  sqrt_ = math.sqrt(idf_add)

  for j in tf_idf_arr:
    norm_TF_IDF = float(j) / sqrt_
    norm_TF_IDF_arr.append(norm_TF_IDF)

  for k in norm_TF_IDF_arr:
    tf_idf[key_arr[index]] = k
    index+=1

  
  newF = open(base_path + '归一化词典键值对.txt','w+',encoding='utf-8')
  newF.write(str(tf_idf)) 
  newF.close()



""" 对键值对字典降序 返回的是列表元组 [(词,TF-IDF)]"""
def dec_dic():
  dic_ = open(base_path + '归一化词典键值对.txt','r',encoding='utf-8')
  dic_ = dic_.read()
  dic_ = ast.literal_eval(dic_)#字符串转字典
  res = sorted(dic_.items(), key=lambda dic_: dic_[1],reverse=True)
  # saveFile("desc/2022-7-25/降序归一化词典键值对.txt",str(res))
  return res




""" 导出降序后的词典 """
def re_cidian():
  arr = []
  arr1 = []
  for i in arr_dec_dic:
   arr.append(i[0])
   arr1.append(i[1])
  saveFile(base_path + '降序归一化词典.txt',str(arr))
  saveFile(base_path + '降序归一化词典TF-IDF.txt',str(arr1))

  


norm_dic()
norm()
arr_dec_dic = dec_dic()
re_cidian()