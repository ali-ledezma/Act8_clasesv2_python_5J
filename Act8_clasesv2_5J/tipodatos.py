print("clases v2 Diego Ledezma")

class Datos:
    # el constructor funcion
    def __init__(self,estatura, peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, peso {self.peso} Kg ")
    def mi_lista(self):
        perfumes=["JPG","YSL","VALENTINO"]
        print(perfumes)
        for perf in perfumes:
            print(perf)
        conjuntoperfumes = {"parfum de marley", "tom ford", "coach", "badboy"}
        print("conjunto:")
        print(conjuntoperfumes)
        for perf1 in conjuntoperfumes:
            print(perf1)
        tuplaperfumes = ("kesto", "dior", "JPG", "invictus", "JPG")
        print("tuplas:")
        print(tuplaperfumes)
        for perf2 in tuplaperfumes:
            print(perf2)
        diccperfumes = {
        "marca": "paco rabanne",
        "modelo": "one million",
        "año": 1980
        }
        print("diccionario")
        print(diccperfumes)
        for perf3 in diccperfumes:
            print(perf3)
info=Datos(1.75,70.5)



info.mostrar_datos()
print(" Lista de perfumes Diego Ledezma")
info.mi_lista()
