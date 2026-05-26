import random
def pobierz_dane_misji():
    print("=" * 40)
    print("  SYMULATOR ŁAZIKA MARSJAŃSKIEGO")
    print("=" * 40)
    nazwa = input("Podaj nazwę misji: ")
    pilot = input("Podaj imię pilota: ")
    return nazwa, pilot
def ruchy(x,y,energia):
    kierunek = input("\nPodaj kierunek (N/S/E/W): ")
    kierunek = kierunek.upper()
    print(f"Pozycja przed ruchem: x={x}, y={y}")
    print(f"Energia przed ruchem: {energia}") 
    if kierunek=="N":
        y=y+1
        print("Łazik jedzie na północ (N).")
    elif kierunek=="S":
        y=y-1
        print("Łazik jedzie na południe (S).")
    elif kierunek=="E":
        x=x+1
        print("Łazik jedzie na wschód (E).")
    elif kierunek=="W":
        x=x-1
        print("Łazik jedzie na zachód (W).")
    else:
        print("Nieznany kierunek! Wpisz N, S, E lub W.")
    if kierunek=="N" or kierunek=="S" or kierunek=="E" or kierunek=="W":
        energia=energia-10
    if energia<=0:
        print("Bateria rozładowana! Misja zakończona.")
    print(f"Nowa pozycja: x={x}, y={y}")
    print(f"Energia: {energia}")
    return x,y,energia
def sprawdz_granice(x,y):
    GRANICA=10
    if x>GRANICA:
        x=GRANICA
        print("Łazik dotarł do wschodniej granicy!")
    elif x<-GRANICA:
        x =-GRANICA
        print("Łazik dotarł do zachodniej granicy!")
    if y>GRANICA:
        y=GRANICA
        print("Łazik dotarł do północnej granicy!")
    elif y<-GRANICA:
        y=-GRANICA
        print("Łazik dotarł do południowej granicy!")
    return x,y
def losowe_zdarzenie(x, y, energia, historia):
    szansa=random.randint(1,3)
    if szansa==1:
        zdarzenie=random.randint(1,4)
        if zdarzenie==1:
            print("\n⚠ ZDARZENIE: Burza piaskowa! Łazik traci 20 energii.")
            energia=energia-20
            historia.append("Burza piaskowa (utrata energii)")
        elif zdarzenie==2:
            print("\n✓ ZDARZENIE: Panele słoneczne naładowane! +30 energii.")
            energia=energia+30
            historia.append("Naładowanie energii")
        elif zdarzenie==3:
            print("\n⚠ ZDARZENIE: Uszkodzenie koła! Łazik traci 15 energii.")
            energia=energia-15
            historia.append("Uszkodzenie koła")
        elif zdarzenie == 4:
            print("🌪 Anomalia grawitacyjna! Teleportacja!")
            x += random.randint(-3, 3)
            y += random.randint(-3, 3)
    else:
        print("\nBrak zdarzeń w tym kroku.")
    return x, y, energia
def main():
    nazwa_misji, imie_pilota = pobierz_dane_misji()

    while True:
        print(f"\nWitaj, {imie_pilota}! Misja '{nazwa_misji}' rozpoczęta.")

        try:
            x = int(input("Podaj startowe X: "))
        except:
            x = 0
        try:
            y = int(input("Podaj startowe Y: "))
        except:
            y = 0
        energia=100
        krok=0

        cel_x = random.randint(-5, 5)
        cel_y = random.randint(-5, 5)
        maks_krokow=20

        historia=[]

        wynik=""
        
        print(f"🎯 Cel misji: ({cel_x}, {cel_y})")
        print(f"Pozycja startowa: x={x}, y={y}")
        print(f"Energia: {energia}")
        print(f"Cel: {cel_x}, {cel_y}")

        while True:
            krok+=1
            print("\n" + "-"*30)
            print(f"Krok {krok}")
            x,y,energia=ruchy(x,y,energia)
            x,y=sprawdz_granice(x,y)
            x, y, energia = losowe_zdarzenie(x, y, energia, historia)
            if energia < 30 and energia > 0:
                print("⚠ NISKI POZIOM ENERGII")
            if x==2 and y==2:
                print("🔋 STACJA ŁADOWANIA +25 energii")
                energia+=25
                historia.append(f"Krok {krok}: stacja ładowania")
            elif x==-3 and y==1:
                print("🪨 POLE SKAŁ -15 energii")
                energia-=15
                historia.append(f"Krok {krok}: skały")
            elif x==4 and y==-2:
                print("🚀 WRAK STATKU +10 energii")
                energia+=10
                historia.append(f"Krok {krok}: wrak statku")
            if x==cel_x and y==cel_y:
                print("\n🎉 CEL MISJI OSIĄGNIĘTY!")
                wynik="SUKCES - dotarcie do celu"
                break
            if krok>=maks_krokow:
                print("\n⌛ Limit kroków!")
                wynik="PORAŻKA - limit kroków"
                break
            if energia<=0:
                print("\n💀 Brak energii!")
                wynik="PORAŻKA - brak energii"
                break
        print("\n" + "="*40)
        print("RAPORT KOŃCOWY")
        print("="*40)
        print(f"Misja: {nazwa_misji}")
        print(f"Pilot: {imie_pilota}")
        print(f"Pozycja: x={x}, y={y}")
        print(f"Kroki: {krok}")
        print(f"Energia: {energia}")
        print(f"Wynik: {wynik}")
        punkty = energia + (maks_krokow - krok) * 5
        if punkty < 0:
            punkty = 0
        print(f"Wynik punktowy: {punkty}")
        print("\nNajważniejsze zdarzenia misji:")
        for h in historia:
            print("-", h)
        start=input("\nCzy chcesz zagrać jeszcze raz? (t/n): ")
        if start.lower()!="t":
            print("Koniec programu.")
            break
main()
