from sinirhucresi import sinirHucresi

sinirhucreleri=[
    [sinirHucresi([0.1,0.6,0.96,0.49,1.0,0.0],0.0),sinirHucresi([0.5,0.3,0.76,0.48,0.3,0.5],0.7),sinirHucresi([0.8,0.3,0.96,0.69,0.4,0.9],0.15)],
    [sinirHucresi([0.49,1.0,0.9],0.0),sinirHucresi([0.5,0.3,0.5],0.7),sinirHucresi([0.8,0.3,0.99],0.15),sinirHucresi([0.5,0.3,0.5],0.7)],
    [sinirHucresi([0.1,0.6,0.96,0.99],0.0),sinirHucresi([0.96,0.69,0.4,0.4],0.15)]
    ]

try:
    parametreler = []
    while True:
        parametreler.append(float(input("parametre giriniz(0.0-1.0)(cikis Herhangi bir harf):")))
except:
    pass

prms=parametreler;
sonprms=prms
for adim in sinirhucreleri:
    siradakiprms=[]
    for hucre in adim:
        siradakiprms.append(hucre.isle(prms))
    sonprms=prms=siradakiprms

for sonuc in sonprms:
    print(sonuc)