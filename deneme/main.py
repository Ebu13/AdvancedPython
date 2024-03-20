#sayi=15
#tür=type(sayi)
#print(type(tür))

#python -i hello.py şeklinde çalıştırırsan hello.py daki fonksiyonlara script in çalışması bitse bile yine erişebilirsin.
#python -c 'print("Hello, World")' ifadesi ile python dosyası oluşturulmasına gerek kalmadan komut çalışır.

#Böyle yazılırsa interface lerdeki method imzaları gibi davranır.
#def will_be_implemented_later():
#    pass

#c=147.e0
#print(c)

def carp(*args):
    sonuc = 1
    for arg in args:
        sonuc *= arg
    return sonuc

def fac(sayi):
    liste = {1}
    for i in range(1, sayi + 1):
        liste.add(i)
    return carp(*liste)

print(fac(5))


#print(carp(1,2,3,4,5,6))



