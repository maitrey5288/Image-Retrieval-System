from jsonfunction import jsonread
import textfun
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
'''
In this code it calls ocr fun(line 17 )
then generated text is compared with keyword(line 18) 
if ratio is >65 image name is appended in list
then function returns list of matching images
'''


def search_keyword(keyword):
    data= jsonread()
    img_output_list = []
    
    for i in data:
        if i == 'pdf':
            d ={}
            for j in data[i]:  #j is pdf name
                l=[]
                for k in data[i][j]:   #k is each page in pdf
                    l =[]
                    s1 =data[i][j][k]
                    a =fuzz.partial_token_set_ratio(s1, keyword) 
                    print(a)
                    print(s1)

                    print('\n')
                    print('\n')
                    print('\n')
                    
                    if a>=65:
                          l.append(k)
                print("this is list hi hihihih",l)          
                d[j] = l
            img_output_list.append(d)              
        else:
            s1 = data[i]
            a =fuzz.partial_token_set_ratio(s1, keyword) 
            # s1 = s1.split()
            # word =''
            # for  j in s1:
            #     if(fuzz.partial_token_set_ratio(j, keyword) == a):
            #         word+= j
            #         word+= ' '


            # print(a)
            # print(s1)

            # print('\n')
            # print('\n')
            # print('\n')
            
            file = open('abc.txt', 'a')
            file.write("\n")
            file.write(f"{i}   ->    {a} ")
            file.close()

            if a>65:
                img_output_list.append(i)
    return img_output_list


# search_keyword('d','./static/images/')
# def search_keyword(keyword,path):
#     imgpath = path
#     img_list = imagelist.imagelist(imgpath)
#     img_output_list =[]
#     for i in img_list:
#         s1 =textfun.textfunwithkeyword(imgpath+i)

#         s1= s1.split()
#         print(s1)
#         match =False
#         num=0
#         num1= 0
#         for j in range(len(s1)):
#              a =fuzz.ratio(s1[j], keyword)
#              num1 = max(a,num1)
#              if a>65:
#                  match= True
        
#         if match:
#             img_output_list.append(i)
#     return img_output_list
# print(img_output_list)
    