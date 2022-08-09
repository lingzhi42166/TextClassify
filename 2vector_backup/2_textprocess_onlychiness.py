import io
import sys
import os

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

""" 用于处理语料库 只保留中文，并导出文件 """ 
type = 'politics'
input_Path = '2vector/Good/'+ type +'/AllIn.txt'
out_path = '2vector/Good/'+ type +'/_只有中文.txt'

file_ = open(input_Path,'r',encoding='utf-8')
file_data = [] #文章列表


#只保留汉字
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str + i
    return content_str

# 参数传入的是每一句话
chinese_list = []
num = 0
for line in file_.readlines():
  if line.isspace(): #如果是空行 则不写入
    continue
  else:
    chinese_list.append(format_str(line))

# print(len(chinese_list)) 
file_.close()



def save_File(out_path,chinese_list):
  # if not os.path.exists(out_path):
  #   os.makedirs(out_path)
  #写入到新的文件中
  newF = open(out_path,'w+',encoding='utf-8')

  for each in chinese_list:
    # print(each)
    newF.write(each + '\r\n') #每篇文章\r\n分开
    
  newF.close()

save_File(out_path,chinese_list)
