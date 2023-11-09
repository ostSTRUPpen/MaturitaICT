number = 0
while(number<100):
    number+=1
    text=""
    if(number%3==0):
        text+="Fizz"
    if(number%5==0):
        text+="Buzz"
    if(text==""):
        text=number
    print(text)