

import random
#fonksiyonlar
def LiveAndDeath(x):
    olumkalim = random.randint(1,100)
    if olumkalim<50:
        LivingBacterias.remove(x)

def Produce(x):
    urun= random.randint(1,100)
    if urun>= 75:
        if (isinstance(x.find("x"),int)):
            Vara = len(LivingBacterias)
            Varb = "xBac{}".format(Vara)
            LivingBacterias.append(Varb)
        else:
            Varb = "Bac{}".format(Vara)

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

z = int(input("Kaç Döngü Olsun:"))

i3 = 0 #Döngü Sayacı

while (i3 < z):
    for i in LivingBacterias:
        LiveAndDeath(i)
        Produce(i)
    i3+=1




print(LivingBacterias)






















