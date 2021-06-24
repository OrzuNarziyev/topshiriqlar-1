import math
# a = int(input("a = "))


# d = a % 2

# if (d == 0) :
#     print("juft")
# else:
#     print("toq")




# a = int(input("a = "))
# if a > 0 :
#     print('musbat')
# else :
#     print('manfiy')







# a<=b<=c

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# if (a>b):
#     print('b soni a dan katta bolsin!')

# if (a>c):
#     print('c soni a dan katta bolsin!')

# if (b>c):
#     print('c soni b dan katta bolsin!')

# if (a>b<c):
#     print('b soni a dan katta bolsin!')    

# if (a<b>c):
#     print('c soni b dan katta bolsin!')

# if (a>b>c):
#     print('c va b sonlari  dan katta bolsin!')

# if(a<=b<=c):
#     print("Ifoda to'g'ri bajarildi" , a ,"<=" ,b , "<=" ,c)







# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# x = max(a,b,c)

# print("\n" ,x)




# teng bo'lish qiymati
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# if (a==b!=c) is True:
#     print("2")
# elif (a!=b==c) is True: 
#     print("2")
# elif (a!=c==b) is True: 
#     print("2")
# if (a==b==c):
#     print("3")
# if (a!=b!=c) is True:
#     print("0")





# 5 ta sonning eng kattasi
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))

# x = max(a,b,c,d,e)
# print(x)




# a = int(input('Oy tartib raqamini kiriting: '))
# if (a==1):
#     print("Yanvarda 31 kun bor")
# elif (a==2):
#     print("Fevralda 28 kun bor")
# elif (a==3):
#     print("Martda 31 kun bor")
# elif (a==4):
#     print("Aprel 30 kun bor")
# elif (a==5):
#     print("Mayda 31 kun bor")
# elif (a==6):
#     print("Iyunda 30 kun bor")
# elif (a==7):
#     print("Iyulda 31 kun bor")
# elif (a==8):
#     print("Avgustda 31 kun bor")
# elif (a==9):
#     print("Sentabrda 30 kun bor")
# elif (a==10):
#     print("Oktabrda 31 kun bor")
# elif (a==11):
#     print("Noyabrda 30 kun bor")
# elif (a==12):
#     print("Dekabrda 31 kun bor")
# if (a>12):
#     print("Tanlangan son oy tartib raqamida mavjud emas")
    
# if (a<0):
#     print("Tanlangan son oy tartib raqamida mavjud emas")










# a = int(input("Ma'lumbir oyning tartib raqamini kiriting: "))
# b = int(input(f"{a}ning sanasini kiriting: "))
# # taqriban
# x = 365-(a*30+b)

# if (a>12):
#     print("Tanlangan son oy tartib raqamida mavjud emas")
  
# if (a<0):
#     print("Tanlangan son oy tartib raqamida mavjud emas")
# if x > 0:
#     print("Yangi yilgacha hali " ,x ,"kun bor")
# else:
#     print("Kiritilgan sana kutilganidan katta, qayta urinib ko'ring")







# a = int(input("Oy tartib raqamini kiriting: "))

# if (0 < a <= 2) or (a == 12):
#     print("QISH FASLI")
# elif (3 <= a <= 5):
#     print("BAHOR FASLI")
# elif (6 <= a <= 8):
#     print("YOZ FASLI")
# elif (9 <= a <= 11):
#     print("KUZ FASLI")
# if (a < 0) or (a > 12):
#    print("Tartib raqami 12 dan katta yoki manfiy son bo'lishi mumkin emas.")









# import time
# print("Yoshingiz korxona talablariga to'g'ri kelishi uchun yoshingiz tasdiqlang")
# time.sleep(2)
# nom = int(input("Yoshingizni tasdiqlangan: "))
# print(f"\t{nom} yosh")
# time.sleep(1)
# if (nom <= 25) or (nom >= 40):
#     print("Tasdiqlanmadi!")
# else:
#     print("Tasdiqlandi")











# yosh = int(input("\tYosh kiriting: "))

# if (0 <= yosh <= 5):
#     print("\tChaqaloq")
# elif(6 <= yosh <= 12):
#     print("\tBola")
# elif(13 <= yosh <= 19):
#     print("\tO'spirin")
# elif(20 <= yosh <= 50):
#     print("\tYoshroq")
# elif(50 <= yosh <= 100):
#     print("\tKeksa")
# elif(yosh >= 100):
#     print("\tAsr odami")
# if(yosh < 0):
#     print("\tManfiy son qabul qilinmaydi!")






# import time
# a = int(input("Dastlabki soat milini kiriting: "))
# b = int(input("Dastlabki daqiqani kiriting: "))

# if True:
#     time.sleep(1)
#     print("Dastlabki soat: " , a,":",b )
# a1 = int(input("O'tgan soat miqdorini kiriting: "))
# b1 = int(input("O'tgan minut miqdorini kiriting: "))

# if int(a+a1<=24):
#     time.sleep(1)
#     print("Hozirda soat: " , a+a1)
# if int(a+a1>=24):
#     print("Hozirda soat: " , (a + a1) - 24)

# if int(b+b1<=60):
#     time.sleep(1)
#     print("Hozirda soat: " , a+a1 , ":" ,b+b1)
# if int(b+b1>=60):
#     print("Hozirda soat: " , (a + a1) - 24 , ":" , b1+b-60)

