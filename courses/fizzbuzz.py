def fizzbuzz(x:int) :
    for numbers in x :
        if numbers % 3 == 0 :
            print('Fizz')
        elif numbers % 5 == 0 :
            print('Buzz')
        else : 
            print(x)

fizzbuzz(16)
    