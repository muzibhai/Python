# with arguments
# wap find given number is prime or not

def isprime(num):
    
    count_fact =0
    for i in range(1,num+1):
        if(num % i ==0):
            count_fact+=1
    if(count_fact == 2):
        print "Given ",num," is prime"
    else:
        print "Given ",num," is not prime"
def main():
    num = input("enter any number")
    isprime(num)
if(__name__ =="__main__"):
    main()
