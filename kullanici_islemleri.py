import time

def girisYap():
    kullanici_adi=input("Kullanıcı adınızı girin  :  ")
    sifre=input("Şifrenizi girin  : ")

    dosya=open("kullanicilar.txt","r")
    satirlar=dosya.readlines()
    cevrimici=False
    for kullanici in satirlar:
       bolunmus=kullanici.split()
       bolunmus_k_adi=bolunmus[0]
       bolunmus_k_sifre=bolunmus[1]
       if kullanici_adi == bolunmus_k_adi and sifre==bolunmus_k_sifre:
           cevrimici=True
    if cevrimici:
        print("Hoşgeldiniz: ",kullanici_adi)
    else:
        print("Bilgilerinizi Kontrol ediniz ve Oturumu tekrar açmayı deneyiniz!!!")
    input()




def kayitOl():
    kullanici_adi=input("Kullanıcı adı girin : ")
    if not kontrol(kullanici_adi):
        #Kullanici Adi müsait değilse
        print("===========Kullanıcı Adı Zaten Mevcut============")
        time.sleep(1)
        return kayitOl()
    sifre=input("Şifrenizi girin : ")
    sifre_onay = input("Şifrenizi girin : ")

    if sifre!=sifre_onay:
        print("=============Şifreler eşleşmiyor!!!!!!!!!!!!")
        time.sleep(1)
        return kayitOl()

    dosya=open("kullanicilar.txt","w")
    dosya.write(kullanici_adi)
    dosya.write(" ")
    dosya.write(sifre)
    dosya.write("\n")
    dosya.close()
    print("Kullanıcı Kaydedildi..")
    input()



def kontrol(kullanici_adi):
    if kullanici_adi not in open("kullanicilar.txt","r").read():
        return True
    else:
        return False



while True:
    print("""
            [1] Kayıt Ol
            [2] Giriş Yap
         """)

    secim=int(input("Seçiminizi yapın : "))

    if secim==1:
        kayitOl()
    elif secim==2:
        girisYap()




