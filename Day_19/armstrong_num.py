#num=1634
num=int(input("Enter a number to check Armstrong : "))

len_num=(len(str(num)))
temp=num
sum=0

while temp>0:
    last_num=temp%10
    sum += last_num **len_num
    temp //= 10

if num==sum:
    print(f'{num} is an Armstrong numbers')
else:
    print(f'{num} is not an Armstrong numbers')
