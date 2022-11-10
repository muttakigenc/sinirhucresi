from sinirhucresi import sinirHucresi

sinirhucreleri=[
    [sinirHucresi(),sinirHucresi(),sinirHucresi()],
    [sinirHucresi(),sinirHucresi(),sinirHucresi(),sinirHucresi()],
    [sinirHucresi(),sinirHucresi()]
    ]

try:
    parametreler = []
    while True:
        parametreler.append(float("0." + str(int(input("parametre giriniz(0-100)(cikis Herhangi bir harf):")))))
except:
    pass

prms=parametreler;
sonprms=prms
for adim in sinirhucreleri:
    siradakiprms=[]
    for hucre in adim:
        siradakiprms.append(hucre.ağırlıkyap(prms).isle(prms))
    sonprms=prms=siradakiprms

for sonuc in sonprms:
    print(sonuc)