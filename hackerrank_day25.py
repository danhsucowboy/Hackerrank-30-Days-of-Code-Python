def main(num):
    root = int(num ** 0.5)
    is_prime = True
    for i in range(2,root+1):
        if num%i==0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Not prime")

T = int(input())
for _ in range(T):
    num = int(input())
    if num > 1:
        main(num)
    else:
        print("Not prime")
    pass