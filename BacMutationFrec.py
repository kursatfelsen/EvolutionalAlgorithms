import random
#fonksiyonlar
#BAKTERİ SAYISINA GÖRE ÖLÜM KALIM ORANINI DEĞİŞTİR
def LiveAndDeath(x):
    olumkalim = random.randint(1,100)

    if olumkalim<50:
        LivingBacterias.remove(x)

def Produce(x):
    urun= random.randint(1,100)
    Vara=0
    Varb=0
    if urun>= 75:
        if (x.find("x")!= -1):
            Vara = len(LivingBacterias)
            Varb = "xBac{}".format(Vara)
            LivingBacterias.append(Varb)
        else:
            Varb = "Bac{}".format(Vara)
            LivingBacterias.append(Varb)
#ESAS KISIM
x = int(input("Kaç Adet Bakteriyle Başlamak istiyorsunuz:"))

i1=0 #sayaç
LivingBacterias= []

while (i1 < x):
    LivingBacterias.append("Bac{}".format(i1))
    i1+=1

y = int(input("Kaç adet mutasyonlu birey olsun:"))

i2=0 #sayaç2

while (i2<y):
    LivingBacterias[i2]=("xBac{}".format(i2))
    i2+=1

#print(LivingBacterias)

#Döngüye Başlayalım artık

z = int(input("Kaç Jenerasyon Olsun:"))
print(LivingBacterias)
i3 = 0 #Jenerasyon Sayacı

Mutasyonlubakterisayisi = 0.
Mutasyonsuzbakterisayisi = 0.

while (i3 < z):
    for i in LivingBacterias:
        LiveAndDeath(i)
    for i in LivingBacterias:
        Produce(i)
    Mutasyonlubakterisayisi = 0
    Mutasyonsuzbakterisayisi = 0
    for i in LivingBacterias:
        if (i.find("x") == 0):
            Mutasyonlubakterisayisi += 1
        else:
            Mutasyonsuzbakterisayisi += 1
    print("****************************\n{}.jenerasyon\nMutasyonlu Bakteri sayısı:{}\nMutasyonu Olmayan Bakteri Sayısı:{}".format(i3,Mutasyonlubakterisayisi,Mutasyonsuzbakterisayisi))
    if Mutasyonlubakterisayisi!=0:
            if Mutasyonsuzbakterisayisi!=0:
                print("Oran:{}".format(Mutasyonlubakterisayisi/(Mutasyonsuzbakterisayisi+Mutasyonsuzbakterisayisi)))
            else:
                print("Oran:1.0")
    else:
        if Mutasyonsuzbakterisayisi!=0:
            print("Oran:0.0")
        else:
            print("Bakterilerin Nesli Tükendi")
            break
    i3+=1
