n=int(input('in_1: '))
ochn=0
zaochn=0
for i in range(n):
    stroka=input(f'n_{i+2}: ')
    d=stroka.split()
    format=d[-1]
    if format=='True':
        ochn+=1
    elif format=='False':
        zaochn+=1
print(f'out: {ochn} {zaochn}')