import random

random_number = -1
# add count guess

while True:
    try:
        if random_number == -1:
            random_number = random.randint(1, 100)
        guess = int(input("Myslím si číslo od 1 do 100. Jaké?> "))
        if guess == random_number:
            print(f"Správně, číslo bylo {random_number}")
            print("------------------------------------")
            random_number = -1
        elif guess < random_number:
            print(f"Číslo {guess} je moc malé")
        elif guess > random_number:
            print(f"Číslo {guess} je moc velké")
    except Exception as error:
        print(f"You failed horribly {error}")       
            