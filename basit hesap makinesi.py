print("""

***************************

HESAP MAKİNESİ İŞLEMLERİ 

1. İŞLEM TOPLAMA

2. İŞLEM ÇIKARMA 

3. İŞLEM ÇARPMA

4. İŞLEM BÖLME

""")

a=int(input("ilk sayıyı giriniz : "))

b=int(input("ikinci sayıyı giriniz : "))

işlem = input("işlemi giriniz : ")

if (işlem == "1"):
    print("{} ile {} toplamı : {} .".format(a,b,a+b))

elif(işlem == "2"):
    print("{} ile {} farkı : {} ".format(a,b,a-b))

elif(işlem == "3"):
    print("{} ile {} çarpımı : {} ".format(a,b,a*b))

elif(işlem == "4"):
    print("{} ile {} bölümü : {} ".format(a,b,a/b))

else:
    print( "GEÇERSİZ İŞLEM SEÇTİNİZ")