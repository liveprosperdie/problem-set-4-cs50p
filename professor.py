import random

def main():
    level=get_level()
    a=0
    for _ in range (10):
        x,y=generate_integer(level),generate_integer(level)
        sum=x+y
        for i in range(3):
            try:
                ans=int(input (f"{x} + {y} = "))
                if ans == (x + y):
                    a+=1
                    break
                else:
                    print("EEE")
                if i==2:
                    print(f"{x} + {y} = {sum}")

            except ValueError:
                print ("EEE")
    print(f"Score: {a}")



def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if n not in [1,2,3]:
                continue
            else:
                break
        except ValueError:
            continue
    
    return n


def generate_integer(level):
    if level == 1:
        num=random.choice(range(0,10))
    elif level==2:
        num=random.choice(range(10,100))
    elif level==3 :
        num=random.choice(range(100,1000))
    else:
        raise ValueError
    return num


if __name__=="__main__":
    main()

