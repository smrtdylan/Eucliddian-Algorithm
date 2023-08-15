a = ''
b = ''

while a == '':
    a = int(input('First Number: '))
    if a<0:
        print("The Euclidian Algorithm doesn't work for negative numbers")
        to_restart = input('Type Yes To Restart or Anything To Stop: ')

        if to_restart.lower() == 'yes':
            a = ''

        else:
            quit()

while b == '':
    b = int(input('Second Number: '))

    if b<0:
        print("The Euclidian Algorithm doesn't work for negative numbers")
        to_restart = input('Type Yes To Restart or Anything To Stop: ')

        if to_restart.lower() == 'yes':
            b = ''

        else:
            quit()


if b>a:

    #assigning values to variables in the euclidian algorithm: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    int_value = int(b/a)
    remainder_value = float(b%a)

    #basic premice: resetting the value, etc. etc.

    while remainder_value > 0:
        b=int_value*a + remainder_value
        b=a
        a=a-a+remainder_value
        int_value = int(b/a)
        remainder_value = float(b%a)

    
    if remainder_value == 0:
        print(str(a) + ' is the greatest common divisor')
    
    else: 
        print('Something went wrong')


elif b<a:

    #just everything above
    int_value = int(a/b)
    remainder_value = float(a%b)

    while remainder_value > 0:
        a=int_value*b + remainder_value
        a=b
        b=b-b+remainder_value
        int_value = int(a/b)
        remainder_value = float(a%b)

    if remainder_value == 0:
        print(str(b) + ' is the greatest common divisor')
    
    else: 
        print('Something went wrong')

else:
    print('Both values are identical' + {a})

