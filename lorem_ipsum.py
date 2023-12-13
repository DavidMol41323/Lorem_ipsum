import random

#Seznam náhodných slov v klingonštině.
slova = ['tlhIngan', 'chen', 'vavwI', 'targh', 'DavIqun', 'ghom', 'HIq', 'latlh', 'botlh', 'SoH', 'ghItlhon', 'ghItar', 'tach', 'QIS', 'HIq', 'qa', 'ngeH', 'yIn', 'be', 'chaj', 'qI', 'bIQ', 'qet', 'yotlh', 'Qugh', 'vItlhutlh', 'Do', 'tIn', 'Duj', 'pohtlh', 'ghItlhon', 'bagh', 'qIb', 'QImroq', 'Hoch', 'map', 'ISja', 'HuD', 'ngech', 'chen', 'yuch', 'HIv', 'qum', 'mIyon', 'qel', 'luch', 'pagh', 'netlh', 'pevIl', 'Hergh']
i = 1

#Zadání Počtu řádků a maximálního počtu slov ve větě.
pocet_radku = int(input("Zadejte počet řádků: "))
max_delka_vety = int(input("Zadejte maximální počet slov ve větě: "))

#Cyklus while, který vypíše náhodné věty.
while pocet_radku >= i:
    #Určení náhodné délky věty.
    nahodny_pocet = random.randint(3, min(max_delka_vety, len(slova)))
    #Určení náhodných slov.
    nahodna_slova = random.sample(slova, nahodny_pocet)
    #Přiřazení slov do věty.
    veta = " ".join(nahodna_slova)
    #Přepsání prvního písmene věty na velké písmeno.
    veta = veta.capitalize()
    #Vytisknutí věty
    print(f"{veta}.")
    i += 1