import random

class Trening:
    def __init__(self):
        self.zagrijavanje = ["- Trčanje (10-15 min)", 
                             "- Veslanje (10 - 15 min)", 
                             "- Bicikl (10 - 15 min)", 
                             "- Girije (10 - 15 min)"]
        self.noge = ["- Hodanje sa šipkom (4 serije)", 
                     "- Čučnjevi s utegom (radiš koliko možeš)", 
                     "- Listovi",
                     "- Čučanj",
                     "- Bugarski iskorak"]
        self.sipka = ["- Dead lift (4 serije)", 
                      "- Podizanje šipke u trbuh (3 serije)", 
                      "- Podizanje ramena šipkom (3 serije)", 
                      "- Bench"]
        self.beki_trening = [
            "- Bench\n-  Veslanje\n-  Dizanje ramena (stojecki)\n-  Kosi bench (svaka ruka)\n-  Biceps EW\n-  Prednji rameni potisak\n-  Bocni biceps",
            "- Potisak ramena (sjedeci)\n-  Lat\n-  Triceps\n-  Jednorucni biceps\n-  Chest fly\n-  Ramena dizanje sastrane\n-  Leđa na klupici"]
        self.ostale_vjezbe = ["- Propadanje (triceps)", 
                              "- Vježbe za trbuh na podu + plank", 
                              "- Trbušnjaci na spravi s utegom",
                              "- Dizanje utega leđima"]

    def generiraj_trening(self):
        zagrijavanje_trening = f"Zagrijavanje: \n {random.choice(self.zagrijavanje)}"
        noge_trening = f"Noge: \n {random.choice(self.noge)}"
        sipka_trening = f"Šipka: \n {random.choice(self.sipka)}"
        beki_trening = f"Trening:\n {random.choice(self.beki_trening)}"
        dodatne_vjezbe = f'Dodatno: \n {random.choice(self.ostale_vjezbe)}'
        return f"{zagrijavanje_trening}\n\n{noge_trening}\n\n{sipka_trening}\n\n{beki_trening}\n\n{dodatne_vjezbe}"

trening = Trening()
generirani_trening = trening.generiraj_trening()