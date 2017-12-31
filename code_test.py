'''
Filename: code_test.py
Author: Tyler Phillips

Test program for the code module
'''

import unit_testing as ut
from code import *

def test_get_methods():
    
    print()
    print('get_methods test:')
    print()
    for item in get_methods(str):
        print(item)
    print()

def main():
    
    test_get_methods()

if __name__ == '__main__':
    
    main()