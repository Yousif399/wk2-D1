#exercies-1
number = 0
while True:
    cube = number ** 3
    if cube > 1000:
        break
    print(cube)
    number +=1

#exercies-2
for i in range(2,100):
    prime = True
    for n in range(2,i):
        if i % n == 0:
            prime = False
            break
    if prime:
        print(i, ' is prime')

#exercies-3
age = int(input("Please enter your age:"))
if age < 18:
	print('your a kid')
elif age >= 18 and age <= 65:
	print('your an adult')
else:
	print('senior')