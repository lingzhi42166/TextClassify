from importlib.resources import path
from pywt import wavedec
import numpy as np
import os
""" 读取数据 """
# 遍历指定目录的文本

def listdir_(data_dir):
    txt_arr = []
    for corpus in os.listdir(data_dir):
        txt_arr.append(corpus)
    return txt_arr
# 读取指定文本
def read_txt(path):
    txt_ = []
    with open(path,'r',encoding='utf-8') as f:
        txt = f.read()
        txt = txt.replace('[','')
        txt = txt.replace(']','')
        arr = txt.split(',')
        for i in arr:
            txt_.append(i.strip())
        
    return txt_


""" 数据持久化 """
def saveFile(path,data):
  f = open(path,'w+',encoding='utf-8')
  # for i in data:
  #   f.write(i + ':' + str(data[i]) + '\n')
  f.write(data)
  f.close()


""" 离散小波分解 """
def wavedec_(txt):
    coeffs_ = wavedec(txt, 'sym2', level=12) # return : [cA_n, cD_n, cD_n-1, ..., cD2, cD1]

    # [ca_1,cd_12,cd_11,cd_10,cd_9,cd_8,cd_7,cd_6,cd_5,cd_4,cd_3,cd_2,cd_1] = coeffs
    # [p_ca_1,p_cd_12,p_cd_11,p_cd_10,p_cd_9,p_cd_8,p_cd_7,p_cd_6,p_cd_5,p_cd_4,p_cd_3,p_cd_2,p_cd_1] = p_coeffs
    # print(coeffs[2])
    return (coeffs_[2])



""" 相关系数计算 """
def corr_(data1,data2):
    correlation = np.corrcoef(data1, data2)
    return correlation

""" 遍历所有的文本与词典进行相关系数计算 """
def corrcoef_():
    global txt_arr,base_path
    corr_dict = {}
    cidian_txt = read_txt('词典TF-IDF降序.txt')
    
    cdian_cd_11 = wavedec_(cidian_txt)
    for i in txt_arr:
        path = base_path + '/' + i
        data = read_txt(path)
        # print(data)
        txt_cd_11 = wavedec_(data)
        corr_num = corr_(cdian_cd_11,txt_cd_11)
        corr_dict[i] = corr_num[0][1]
    # saveFile('政治相关系数2.txt',corr_dict)
    saveFile('经济相关系数2.txt',corr_dict)

    # saveFile('词典cd_11.txt',str(cdian_cd_11))
    # saveFile('经济cd_11.txt',str(txt_cd_11))

    # print(cdian_cd_11)

# """ 读取数据 """
# base_path = 'corps/政治/归一化TF-idf'
base_path = 'corps/经济/归一化TF-idf'
# base_path = 'corps/环境/归一化TF-idf'


txt_arr = listdir_(base_path)
corrcoef_()




# print(txt_arr) # ['environment文本0的归一化TF-IDF.txt',......]

# cidian_txt = read_txt('词典TF-IDF降序.txt')
# p0_txt = read_txt('p文本0的归一化TF-IDF.txt')

# """ 小波分解 """
# [cd_11_1,cd_11_2] = wavedec_(cidian_txt,p0_txt)

# """ 相关系数计算 """
# corr_num = corr_(cd_11_1,cd_11_2)
# print(corr_num)