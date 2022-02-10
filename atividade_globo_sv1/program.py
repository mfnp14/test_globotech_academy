import module1

if __name__ == '__main__':
    x = input('Enter an integer: ')
    result = module1.triple(module1.add_two(int(x)))
    print('x plus 2 times 3 yields \n {}'.format(result)
    
