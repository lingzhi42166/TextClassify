import io
import sys
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码



""" 
  1、处理语料库,把同一类的文本放在一个txt中,一行为一个文本
"""
def preProccess(style):
  outPath  = '2vector/Good/' + style
  data_dir = '2vector/test/' + style + '/copus'
  
  # 将文件夹中的语料提取到一个txt文件中，作为一个类
  temp_corpus_list = []  # 用来存放这一类的语料
  # 遍历data_dir文件夹下的每一条文件(语料),并保存到temp_corpus_list，一行为一个文本（语料）
  for corpus in os.listdir(data_dir):
    # print(corpus) 
    text = open(data_dir + '/' + corpus, 'rb').read().decode('UTF-8', 'ignore')

    # 去除一些奇怪的字符 
    text = text.replace('\r', ' ').replace('\n', ' ').replace(
        '\u3000', '').replace('             ', '')
    temp_corpus_list.append(text)
  print(len(temp_corpus_list))# 1026个文本 对应上了

  save_corpus(outPath,temp_corpus_list)


def save_corpus(outPath,temp_corpus_list):
  if not os.path.exists(outPath):
    os.makedirs(outPath)
  
  f = open(outPath + '/AllIn.txt', 'w', encoding='utf-8')
  for text in temp_corpus_list:
    f.write(text + '\r\n')
  f.close()


preProccess("politics") 