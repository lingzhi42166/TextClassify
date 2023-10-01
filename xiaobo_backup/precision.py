import time
# 读取指定文本
def read_txt(path):
    txt_ = []
    with open(path,'r',encoding='utf-8') as f:
        for i in f:
          str = i.split(',')
          # str = i.split(':')

          str = str[1].replace('\n','')
          num = float(str)
          txt_.append(num)
        
    return txt_


# 准确率
def precision_(arr,num):
  count = 0
  for i in arr:
    if i >=num:
      count+=1
  pre_count = count/ len(arr) 
  return (count,pre_count)

# path = 'xiaobo\政治相关系数1.txt'


start_time = time.perf_counter()  
# 程序运行代码

path = 'xiaobo\经济相关系数1.txt'
txt_arr = read_txt(path)

[pre_06_count,pre_06] = precision_(txt_arr,0.6)
[pre_07_count,pre_07] = precision_(txt_arr,0.7)
[pre_08_count,pre_08] = precision_(txt_arr,0.8)
[pre_09_count,pre_09] = precision_(txt_arr,0.9)
print(pre_06,pre_07,pre_08,pre_09)
print(pre_06_count,pre_07_count,pre_08_count,pre_09_count)

end_time = time.perf_counter() 

print('程序运行时间: {} seconds'.format(end_time - start_time))


