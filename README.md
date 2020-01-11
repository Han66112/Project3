# Project3 Cache

TeamWork-Cache
command:
使用 Python 3.6,pycharm 書寫,
執行主程式:
P03_cache.py
執行結果:

 
執行結果1.jpg

 
執行結果2.jpg

系統流程：
1.根據條件,計算 Tag Index 相關值,
2.根據每一個輸入,跟 cache 比對 Hit, Miss,
3.cache 使用 FIFO,
Function:
def Str16_div(string_n1,W1): # 字串轉數值, 除數值, 再轉字串,
def Set_FIFO(fifo_c, fifo_ss): # 填值到 FIFO ,
def Mov_FIFO(fifo_m): # 將 FIFO 值往前移動,
def Search_CacheEmpty(cache, str_c, i):
# 填輸入值到 cache ,如 cache 已滿, 以 FIFO 取代, 根據 rerurn 值判斷 Hit 或 Miss,


程式註解:
在主程式P03_cache.py中,以
#-----------------------------------------------------------
#-註解
#-----------------------------------------------------------
表示註解,
參考:
Lecture11 (上課驗收日：1212) & Project 3

