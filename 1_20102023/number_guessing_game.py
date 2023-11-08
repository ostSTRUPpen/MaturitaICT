import random

random_number = -1
guess_count = 0

while True:
    try:
        if random_number == -1:
            random_number = random.randint(1, 100)
            guess_count = 0
            
        guess = int(input("Myslím si číslo od 1 do 100. Jaké?> "))
        guess_count+=1
        
        if guess == random_number:
            print(f"Správně, číslo bylo {random_number}.\n Uhádl jsi ho na {guess_count}. pokus.")
            print("------------------------------------")
            random_number = -1
        elif guess < random_number:
            print(f"Číslo {guess} je moc malé")
        elif guess > random_number:
            print(f"Číslo {guess} je moc velké")
    except Exception as error:
        print(f"You failed horribly {error}")       
            