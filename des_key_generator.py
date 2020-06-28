import random as rd

#Function
#Key Initialization Function
def initial_key_input():
    initial_key=[]
    print("Enter 64 Bit Initial Key: ")
    num=1
    #Test purpose
    #for i in range(0,64):
       # initial_key.append(rd.randint(0,1))

    ## ACtual Function
    #############################################3
    for i in range(0,64):
        var_01=input("Enter bit no "+str(num)+" :")
        #if(not(var_01==1) or not(var_01==0)):
        initial_key.append(var_01)
        num=num+1
    #############################################3


    return initial_key

#Left Circular Shift
def left_cicular_shift(var_list):
    var_01=var_list[0]
    for i in range(0,len(var_list)-1):
        var_list[i]=var_list[i+1]
    var_list[len(var_list)-1]=var_01
    #print("List Lenght",len(var_list))

    return var_list

def permutation_ch_01_lhs(var_list):
    #Hardcode According To Methode
    list_01=[]
    list_01.append(var_list[56])
    list_01.append(var_list[48])
    list_01.append(var_list[40])
    list_01.append(var_list[32])
    list_01.append(var_list[24])
    list_01.append(var_list[16])
    list_01.append(var_list[8])
    list_01.append(var_list[0])
    list_01.append(var_list[57])
    list_01.append(var_list[49])
    list_01.append(var_list[41])
    list_01.append(var_list[33])
    list_01.append(var_list[25])
    list_01.append(var_list[17])
    list_01.append(var_list[11])
    list_01.append(var_list[1])
    list_01.append(var_list[58])
    list_01.append(var_list[50])
    list_01.append(var_list[42])
    list_01.append(var_list[34])
    list_01.append(var_list[26])
    list_01.append(var_list[18])
    list_01.append(var_list[10])
    list_01.append(var_list[2])
    list_01.append(var_list[59])
    list_01.append(var_list[51])
    list_01.append(var_list[43])
    list_01.append(var_list[35])

    return list_01

def permutation_ch_01_rhs(var_list):
    #Hardcode According To Methode
    list_01=[]
    list_01.append(var_list[62])
    list_01.append(var_list[54])
    list_01.append(var_list[46])
    list_01.append(var_list[38])
    list_01.append(var_list[30])
    list_01.append(var_list[22])
    list_01.append(var_list[14])
    list_01.append(var_list[6])
    list_01.append(var_list[61])
    list_01.append(var_list[53])
    list_01.append(var_list[45])
    list_01.append(var_list[37])
    list_01.append(var_list[29])
    list_01.append(var_list[21])
    list_01.append(var_list[13])
    list_01.append(var_list[5])
    list_01.append(var_list[60])
    list_01.append(var_list[52])
    list_01.append(var_list[44])
    list_01.append(var_list[36])
    list_01.append(var_list[28])
    list_01.append(var_list[20])
    list_01.append(var_list[12])
    list_01.append(var_list[4])
    list_01.append(var_list[27])
    list_01.append(var_list[19])
    list_01.append(var_list[11])
    list_01.append(var_list[3])

    return list_01

def permutation_ch_02(var_list_01):
    list_02=[]
    list_02.append(var_list_01[13])
    list_02.append(var_list_01[16])
    list_02.append(var_list_01[10])
    list_02.append(var_list_01[23])
    list_02.append(var_list_01[0])
    list_02.append(var_list_01[4])
    list_02.append(var_list_01[2])
    list_02.append(var_list_01[27])
    list_02.append(var_list_01[14])
    list_02.append(var_list_01[5])
    list_02.append(var_list_01[20])
    list_02.append(var_list_01[9])
    list_02.append(var_list_01[22])
    list_02.append(var_list_01[18])
    list_02.append(var_list_01[11])
    list_02.append(var_list_01[3])
    list_02.append(var_list_01[25])
    list_02.append(var_list_01[7])
    list_02.append(var_list_01[15])
    list_02.append(var_list_01[6])
    list_02.append(var_list_01[26])
    list_02.append(var_list_01[19])
    list_02.append(var_list_01[12])
    list_02.append(var_list_01[1])
    list_02.append(var_list_01[40])
    list_02.append(var_list_01[51])
    list_02.append(var_list_01[30])
    list_02.append(var_list_01[36])
    list_02.append(var_list_01[46])
    list_02.append(var_list_01[54])
    list_02.append(var_list_01[29])
    list_02.append(var_list_01[39])
    list_02.append(var_list_01[50])
    list_02.append(var_list_01[44])
    list_02.append(var_list_01[32])
    list_02.append(var_list_01[47])
    list_02.append(var_list_01[43])
    list_02.append(var_list_01[48])
    list_02.append(var_list_01[38])
    list_02.append(var_list_01[55])
    list_02.append(var_list_01[33])
    list_02.append(var_list_01[52])
    list_02.append(var_list_01[45])
    list_02.append(var_list_01[41])
    list_02.append(var_list_01[49])
    list_02.append(var_list_01[35])
    list_02.append(var_list_01[28])
    list_02.append(var_list_01[31])

    return list_02

#Function That May help full in Encryption and Decryption
'''
def pc_1_left_hand(initial_key):
    var_01=0
    list_01=[]
    for i in range(0,32):
        if(i==7 or i==15 or i==23 or i==31):
            continue
        else:
            list_01.append(initial_key[i])
    print("LHS Suceeded")
    print(list_01)
    print(len(list_01))
    return list_01

def pc_1_right_hand(initial_key):
    var_01=0
    list_02=[]
    for i in range(32,64):
        if(i==39 or i==47 or i==56 or i==63):
            continue
        else:
            list_02.append(initial_key[i])
    print("LHS Suceeded")
    print(list_02)
    print(len(list_02))
    return list_02

    print("Something")
    
def rem_parity_bit(initial_key):
    for i in range(0,64):
        if(i==8 or i==16 or i==24 or i==32 or i==40 or i==48 or i==56 or i==64):
            initial_key.remove(initial_key[i])
    return initial_key    
'''
#Test Key:
'''
initial_key=[1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,
             0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,
             1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1
             ]
'''



initial_key=initial_key_input()
print("Initial Key List: ")
print(initial_key,"\n")

## Variable_Declaration

process_list=[]
process_list_02=[]
lhs=[]
rhs=[]
round=0

lhs=permutation_ch_01_lhs(initial_key)
rhs=permutation_ch_01_rhs(initial_key)

key_num=-1
key_num=int(input("Enter Number You want To generate: "))
key_num=key_num-1

for i in range(-1,key_num):
    if(key_num<0 or key_num>15):
        print("Re Enter Key Number Between 1 - 16: \n")
        break

    if(round==0 or round==1 or round==8 or round==15):
        lhs=left_cicular_shift(lhs)
        rhs=left_cicular_shift(rhs)
    else:
        lhs=left_cicular_shift(lhs)
        lhs=left_cicular_shift(lhs)
        rhs=left_cicular_shift(rhs)
        rhs=left_cicular_shift(rhs)

    '''    
    #Uncomment this section to view Left Circular Shift
    
    print("Left Hand After Permutation C1")
    print(lhs,"\n")
    print("Right Hand After Permutation C1")
    print(rhs,"\n")
    print("Shift Total Length",(len(lhs)+len(rhs)))

'''

    process_list=lhs+rhs
    process_list=permutation_ch_02(process_list)


    round=round+1

print("\n48 bit Key is: \n")
print(process_list)



