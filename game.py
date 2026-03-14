import random

while True:
    try: 
        n=int(input("Level: "))
        if n<=0:
            continue
        else:
             rand_int=random.randint(1,n)
             break
    except ValueError:
            continue

while True:
     try:
        guess_num=int(input("Guess: "))
        if guess_num < rand_int:
            print("Too small")
        elif guess_num > rand_int:
            print("Too Big")
        else:
            print("Just right")
            break
     except ValueError:
          continue

     

