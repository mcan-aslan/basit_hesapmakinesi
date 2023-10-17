sayi1 = int(input("Sayİ Giriniz: "))
sayi2 = int(input("Sayİ Giriniz: "))
islem = input("İşlem Seçiniz  + , - , * , / : ")
toplama= sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bölme = sayi1 / sayi2

if islem == "+" :
    print("Toplama Sonucunuz: " + str(toplama))

elif islem == "*":
    print("Çarpma Sonucu: " + str(carpma))

elif islem == "/":
    print("Bölme Sonucu: " + str(bölme))

else:
    print("Çarpma Sonucu: " + str(cikarma))