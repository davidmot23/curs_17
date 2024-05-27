#5 Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string
def lungimestr():
    try:
        string=str(input("Introduceti un string: "))
        print(len(string))
    except ValueError:
        print('Trebuie sa introduceti string')

#lungimestr()


#6 Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea

def dictionar():
    dict={
        "a":1,
        "b":2,
        "c":3
        }
    n=input("Alegeti dintre a,b sau c")
    key=dict[n]
    print(key)

dictionar()