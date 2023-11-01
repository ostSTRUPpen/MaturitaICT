all_numbers = input("Vložte čísla (Oddělená \" \" (mezerou))>  ").split(" ")

even_numbers = []
odd_numbers = []
divisible_by_five_numbers = []

for number in all_numbers:
    number = int(number)
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 5 == 0:
        divisible_by_five_numbers.append(number)
    else:
        odd_numbers.append(number)
        
print(f"Sudá čísla: {even_numbers}")
print(f"Lichá čísla: {odd_numbers}")
print(f"Dělitelná pěti čísla: {divisible_by_five_numbers}")