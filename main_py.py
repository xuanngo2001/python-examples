#!/bin/python3
# Description: 
#   Every Python script should have a main() function. It will be easier to read
#       your code this way. Besides, you can call your helper function before
#       definining it, as long as you keep calling the function main() at the end.

def main():
    print("main()")
    ahelper()

def ahelper(a):
    print("A helper")
    
if __name__ == '__main__':
    main()

