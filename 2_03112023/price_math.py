def getPrice(name, old_price, discount):
    new_price = old_price - (old_price*(discount/100))
    return [name, new_price]

while True:
    try:
        name = input("Název> ")
        old_price = int(input("Původní cena> "))
        discount = int(input("Procentuální sleva v procentech> "))
        data = getPrice(name, old_price, discount)
        print(f"Název produktu: {data[0]}, cena po slevě: {data[1]}Kč")
        print("--------")
    except Exception as error:
        print(f"Došlo k chybě: \n{error}")