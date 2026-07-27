import random 
try:

    n = random.randint(1, 100)

    a = -1 
    guesses = 1
    while(a!=n):
        a = int(input("Guess a number"))
        if(a>n):
            print("lower number please")
        elif(a<n): 
            print("Greater number please")
        guesses += 1 

    print(f"You guessed a number in {guesses} attempt.The number was {n}.")
except Exception as e:
    print(e)

