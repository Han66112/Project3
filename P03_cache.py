# coding=UTF-8
# import math
import numpy as np

Byteaddress = ['C64E5', 'C64C5', 'C74EA', 'C64E8', 'C64CF', 'F64E6', 'F74EA', 'F84E6', 'C74CF', 'C64E6', 'C64C9',
               'C74E8']
# Lineaddress = ['C64E','C64C','C74E','C64E','C64C','F64E','F74E','F84E','C74C','C64E','C64C','C74E']
Lineaddress = ['', '', '', '', '', '', '', '', '', '', '', '']
# Tag = ['C6','C6','C7','C6','C6','F6','F7','F8','C7','C6','C6','C7']
Tag = ['', '', '', '', '', '', '', '', '', '', '', '']
# Index = ['4E','4C','4E','4E','4C','4E','4E','4E','4C','4E','4C','4E']
Index = ['', '', '', '', '', '', '', '', '', '', '', '']

Cache_1 = ['', '', '', '']
Cache1_Flag = ''
Cache_2 = ['', '', '', '']
Cache2_Flag = ''
FIFO_1 = ['', '', '', '']
FIFO_2 = ['', '', '', '']

Cache_Hit_Miss = ['', '', '', '', '', '', '', '', '', '', '', '']

# Cache_Index4C_FIFO_Counter = 0
# Cache_Index4E_FIFO_Counter = 0

Index_bits = 0


# Lecture11 (上課驗收日：1212) & Project 3 ,

# --------------------------------------------------------------------------
# 字串轉數值, 除數值, 再轉字串,
# --------------------------------------------------------------------------
def Str16_div(string_n1, W1):
    C1 = (int)(string_n1.upper(), 16)
    C2 = (int)(C1 / W1)
    str16_n1 = str(hex(C2).upper())
    str16_n2 = str16_n1[2:]
    # print('cc=' ,str16_n2)
    return str16_n2


# --------------------------------------------------------------------------
# 填值到 FIFO ,
# --------------------------------------------------------------------------
def Set_FIFO(fifo_c, fifo_ss):
    if fifo_c == 1:
        if fifo_ss == FIFO_1[0]:
            return
        elif fifo_ss == FIFO_1[1]:
            return
        elif fifo_ss == FIFO_1[2]:
            return
        elif fifo_ss == FIFO_1[3]:
            return

        if FIFO_1[0] == "":
            FIFO_1[0] = fifo_ss
        elif FIFO_1[1] == "":
            FIFO_1[1] = fifo_ss
        elif FIFO_1[2] == "":
            FIFO_1[2] = fifo_ss
        elif FIFO_1[3] == "":
            FIFO_1[3] = fifo_ss

    elif fifo_c == 2:
        if fifo_ss == FIFO_2[0]:
            return
        elif fifo_ss == FIFO_2[1]:
            return
        elif fifo_ss == FIFO_2[2]:
            return
        elif fifo_ss == FIFO_2[3]:
            return

        if FIFO_2[0] == "":
            FIFO_2[0] = fifo_ss
        elif FIFO_2[1] == "":
            FIFO_2[1] = fifo_ss
        elif FIFO_2[2] == "":
            FIFO_2[2] = fifo_ss
        elif FIFO_2[3] == "":
            FIFO_2[3] = fifo_ss


# --------------------------------------------------------------------------
# 將 FIFO 值往前移動,
# --------------------------------------------------------------------------
def Mov_FIFO(fifo_m):
    if fifo_m == 1:
        FIFO_1[0] = FIFO_1[1]
        FIFO_1[1] = FIFO_1[2]
        FIFO_1[2] = FIFO_1[3]
        FIFO_1[3] = ""
    elif fifo_m == 2:
        FIFO_2[0] = FIFO_2[1]
        FIFO_2[1] = FIFO_2[2]
        FIFO_2[2] = FIFO_2[3]
        FIFO_2[3] = ""


# --------------------------------------------------------------------------
# 填輸入值到 cache ,如 cache 已滿, 以 FIFO 取代, 根據 rerurn 值判斷 Hit 或 Miss,
# --------------------------------------------------------------------------
def Search_CacheEmpty(cache, str_c, i):
    if cache == 1:
        # --------------------------------------------------------------------------
        # Hit ,
        # --------------------------------------------------------------------------
        if Lineaddress[i] == Cache_1[0]:
            return 10
        elif Lineaddress[i] == Cache_1[1]:
            return 11
        elif Lineaddress[i] == Cache_1[2]:
            return 12
        elif Lineaddress[i] == Cache_1[3]:
            return 13

        if FIFO_1[3] != "":
            # --------------------------------------------------------------------------
            # Clear 1 Cache/FIFO ,
            # --------------------------------------------------------------------------
            if FIFO_1[0] == Cache_1[0]:
                Cache_1[0] = ""
            elif FIFO_1[0] == Cache_1[1]:
                Cache_1[1] = ""
            elif FIFO_1[0] == Cache_1[2]:
                Cache_1[2] = ""
            elif FIFO_1[0] == Cache_1[3]:
                Cache_1[3] = ""
            Mov_FIFO(1)

        # --------------------------------------------------------------------------
        # Miss ,
        # --------------------------------------------------------------------------
        if Cache_1[0] == "":
            return 0
        elif Cache_1[1] == "":
            return 1
        elif Cache_1[2] == "":
            return 2
        elif Cache_1[3] == "":
            return 3
        else:
            return 55
    elif cache == 2:
        # --------------------------------------------------------------------------
        # Hit ,
        # --------------------------------------------------------------------------
        if Lineaddress[i] == Cache_2[0]:
            return 10
        elif Lineaddress[i] == Cache_2[1]:
            return 11
        elif Lineaddress[i] == Cache_2[2]:
            return 12
        elif Lineaddress[i] == Cache_2[3]:
            return 13

        if FIFO_2[3] != "":
            # --------------------------------------------------------------------------
            # Clear 1 Cache/FIFO ,
            # --------------------------------------------------------------------------
            if FIFO_2[0] == Cache_2[0]:
                Cache_2[0] = ""
            elif FIFO_2[0] == Cache_2[1]:
                Cache_2[1] = ""
            elif FIFO_2[0] == Cache_2[2]:
                Cache_2[2] = ""
            elif FIFO_2[0] == Cache_2[3]:
                Cache_2[3] = ""
            Mov_FIFO(2)

        # --------------------------------------------------------------------------
        # Miss ,
        # --------------------------------------------------------------------------
        if Cache_2[0] == "":
            return 0
        elif Cache_2[1] == "":
            return 1
        elif Cache_2[2] == "":
            return 2
        elif Cache_2[3] == "":
            return 3
        else:
            return 55


if __name__ == "__main__":

    # f = open('./P03_cache.in', 'r')
    # lines = f.readlines()
    # for line in lines:
    #    num_list = line.split(' ')
    # Write your code here

    print('Byte address = %s ' % Byteaddress[0] + '%s ' % Byteaddress[1] + '%s ' % Byteaddress[2] + '%s ' % Byteaddress[
        3] + \
          '%s ' % Byteaddress[4] + '%s ' % Byteaddress[5] + '%s ' % Byteaddress[6] + '%s ' % Byteaddress[7] + \
          '%s ' % Byteaddress[8] + '%s ' % Byteaddress[9] + '%s ' % Byteaddress[10] + '%s ' % Byteaddress[11])

    # --------------------------------------------------------------------------
    # 計算 lines 數 ,
    # --------------------------------------------------------------------------
    Line_Number = (int)((16 * 1024) / 16)
    Len_Byteaddress = len(Byteaddress)
    for i in range(Len_Byteaddress):
        Lineaddress[i] = Str16_div(Byteaddress[i], 16)

    print('Line address = %s ' % Lineaddress[0] + '%s ' % Lineaddress[1] + '%s ' % Lineaddress[2] + '%s ' % Lineaddress[
        3] + \
          '%s ' % Lineaddress[4] + '%s ' % Lineaddress[5] + '%s ' % Lineaddress[6] + '%s ' % Lineaddress[7] + \
          '%s ' % Lineaddress[8] + '%s ' % Lineaddress[9] + '%s ' % Lineaddress[10] + '%s ' % Lineaddress[11])

    # --------------------------------------------------------------------------
    # 計算 Sets 數 , 需要的 bits 數 (Index_bits) ,
    # --------------------------------------------------------------------------
    Set_Number = (int)(Line_Number / 4)
    Counter = Set_Number
    while Counter > 1:
        Counter = (Counter / 2)
        Index_bits += 1

    print('ByteIn = ', Len_Byteaddress)
    print('Data = 16 KB')
    print('Bloxk = 16 Bytes')
    print('lines Num = %i' % Line_Number + ' (16 KB / 16 B)')
    print('Sets Num = %i' % Set_Number + ' (1024 Lines / 4 Way)')
    print('Index bits = %i' % Index_bits + ' (256 Sets)')

    # --------------------------------------------------------------------------
    # 計算 Index (Set 需 8 bits) , 計算 Tag ,
    # --------------------------------------------------------------------------
    for i in range(Len_Byteaddress):
        str_nn = Lineaddress[i]
        Tag[i] = str_nn[0:2]
        Index[i] = str_nn[2:]

    print('Tag = %s ' % Tag[0] + '%s ' % Tag[1] + '%s ' % Tag[2] + '%s ' % Tag[3] + \
          '%s ' % Tag[4] + '%s ' % Tag[5] + '%s ' % Tag[6] + '%s ' % Tag[7] + \
          '%s ' % Tag[8] + '%s ' % Tag[9] + '%s ' % Tag[10] + '%s ' % Tag[11])

    print('Index = %s ' % Index[0] + '%s ' % Index[1] + '%s ' % Index[2] + '%s ' % Index[3] + \
          '%s ' % Index[4] + '%s ' % Index[5] + '%s ' % Index[6] + '%s ' % Index[7] + \
          '%s ' % Index[8] + '%s ' % Index[9] + '%s ' % Index[10] + '%s ' % Index[11])

    print('==================================================================')
    # --------------------------------------------------------------------------
    # 計算 Cache1=>"4E", Cache2=>"4C", 的 Hit, Miss,; 使用 FIFO ,
    # --------------------------------------------------------------------------
    for i in range(Len_Byteaddress):
        print('i = %d ' % i)

        if Index[i] == Cache1_Flag:
            pos_1 = Search_CacheEmpty(1, Index[i], i)
            # print('pos1= %s ' % pos_1)
            if pos_1 >= 0 and pos_1 <= 3:
                Cache_1[pos_1] = Lineaddress[i]
                Cache_Hit_Miss[i] = 'Miss'
                Set_FIFO(1, Lineaddress[i])
            elif pos_1 >= 10 and pos_1 <= 13:
                Cache_Hit_Miss[i] = 'Hit'

        elif Index[i] == Cache2_Flag:
            pos_2 = Search_CacheEmpty(2, Index[i], i)
            # print('pos2= %s ' % pos_2)
            if pos_2 >= 0 and pos_2 <= 3:
                Cache_2[pos_2] = Lineaddress[i]
                Cache_Hit_Miss[i] = 'Miss'
                Set_FIFO(2, Lineaddress[i])
            elif pos_2 >= 10 and pos_2 <= 13:
                Cache_Hit_Miss[i] = 'Hit'

        else:
            if Cache1_Flag == '':
                Cache1_Flag = Index[i]
                pos_1 = Search_CacheEmpty(1, Index[i], i)
                # print('pos11= %s ' % pos_1)
                if pos_1 >= 0 and pos_1 <= 3:
                    Cache_1[pos_1] = Lineaddress[i]
                    Cache_Hit_Miss[i] = 'Miss'
                    Set_FIFO(1, Lineaddress[i])
                elif pos_1 >= 10 and pos_1 <= 13:
                    Cache_Hit_Miss[i] = 'Hit'
            elif Cache2_Flag == '':
                Cache2_Flag = Index[i]
                pos_2 = Search_CacheEmpty(2, Index[i], i)
                # print('pos22= %s ' % pos_2)
                if pos_2 >= 0 and pos_2 <= 3:
                    Cache_2[pos_2] = Lineaddress[i]
                    Cache_Hit_Miss[i] = 'Miss'
                    Set_FIFO(2, Lineaddress[i])
                elif pos_2 >= 10 and pos_2 <= 13:
                    Cache_Hit_Miss[i] = 'Hit'
            else:
                print('* ')

        print('Byteaddress= %s ' % Byteaddress[i])
        print('index= %s ' % Index[i])
        print('Cache1_Flag = %s ' % Cache1_Flag)
        print('Cache2_Flag = %s ' % Cache2_Flag)
        print('Cache_1 = %s ' % Cache_1)
        print('Cache_2 = %s ' % Cache_2)
        print('Cache_Hit_Miss = %s ' % Cache_Hit_Miss)
        print('FIFO_1 = %s ' % FIFO_1)
        print('FIFO_2 = %s ' % FIFO_2)
        print('-----------------------------')
    print('End')
    print('==================================================================')

# 2020
