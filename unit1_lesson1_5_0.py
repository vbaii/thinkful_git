def addition(a,b):
    x = a + b
    print(x)
    return x
# rememeber the .func_doc property will give you your function description.
def fib(nth):
    'returns the sequence of Fibonacci numbers up to the nth'
    if nth < 2:
        return nth
    else:
        return fib(nth-2)+fib(nth-1)

def FizzBuzz():
    
    for i in range(1,101):
        print {
            3 : "Fizz",
            5 : "Buzz",
            15 : "FizzBuzz"}.get(15*(not i%15) or
                                 5*(not i%5 ) or
                                 3*(not i%3 ), '{}'.format(i))
                                 
    '''
    for i in range(1,101):
        print {15:"FizzBuzz"}.get(15*
        '''


