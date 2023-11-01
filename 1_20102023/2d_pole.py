#Input data
array_2D = [[1, 2, 3], [4, 5, 6], [7, 20, 9]]
number_distance = 3

#Starting values
number_count = 0
addition = 0
all_numbers = []
final_numbers = []

#Getting an average
for row in array_2D:
    for colum in row:
        number_count+=1
        addition+= colum
        all_numbers.append(colum)

average = addition/number_count

#Finding numbers in correct distance
for number in all_numbers:
    if abs(number-average) <= number_distance:
        final_numbers.append(number)

#Data printing
print("Vstupní údaje")
for row in array_2D:
    print(row)
print(f"Průměrná hodnota: {average}")        
print(f"Čísla ve vzdálenosti {number_distance} od průměrné hodnoty: {final_numbers}")

# Getting the cords
cords = ""
while True:
    if(len(final_numbers) == 0):
        break
    # first is a number, second is na array
    for row_cords, row in enumerate(array_2D):
        for colum_cords, colum in enumerate(row):
            if colum in final_numbers:
                final_numbers.remove(colum)
                cords += f"Číslo: {colum}, Souřadnice řádku {row_cords}, Souřadnice sloupce: {colum_cords}\n"
#Final output
print(cords)