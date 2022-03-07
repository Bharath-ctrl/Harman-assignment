#prime number between 2 - 500
number=2
Prime=True
while number < 500:
    for i in range(2,number):
        if(number%i==0):
            Prime=False
            break
    if Prime:
        print(number)
    Prime=True
    number+=1