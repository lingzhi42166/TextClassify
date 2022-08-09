import io
import sys
import jieba
sys.stdout = io.TextIOWrapper(
  sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
""" 用于分词，去停用词 """ 
type = 'politics'
input_Path = '2vector/Good/'+ type +'/_只有中文.txt'
out_path = '2vector/Good/'+ type +'/_分词并去停用词.txt'

#加载停用词表
def load_stopword():
  f_stop = open('hit_stopwords.txt', encoding='utf-8')  # 自己的中文停用词表
  sw = [line.strip() for line in f_stop]  # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
  f_stop.close()
  return sw

# 中文分词并且去停用词
def seg_word(sentence):
  sentence_seged = jieba.cut(sentence.strip())
  stopwords = load_stopword()
  outstr = ''
  for word in sentence_seged:
    if word not in stopwords:
      if word != '/t':
        outstr += word
        outstr += " "
  # print(outstr)
  return outstr

#读取文本后 去除停用词
textList = []
file = open(input_Path,'r',encoding='utf-8')
for sentence in file:
  textList.append(seg_word(sentence))
  

#输出处理后的文本
newF = open(out_path,'w+',encoding='utf-8')
for each in textList:
  newF.write(each + '\n') #每篇文章\r\n分开
  
newF.close()






