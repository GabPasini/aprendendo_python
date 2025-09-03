# number = int(input('digite um number'))



# while number != 0:
#     print('valor que vc digitou é', number) 
#     number = int(input('digite um number dnv vro: '))



# c = 0

# n1 = int(input('digite um numero pra fazer a tabuada'))
# for c in range(10):
#     c= c + 1
#     print (f'{n1} x {c} = {n1 * c}')



n1 = int(input('digite um numero pra fazer a tabuada'))
while n1 > 0:
    for c in range(1,11):
        print (f'{n1} x {c} = {n1 * c}')
    n1 = int(input('digite um numero pra fazer a tabuada'))