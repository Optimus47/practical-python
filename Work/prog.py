#!/usr/bin/env python3
# prog.py

# Import statements (libraries)
#import modules

# Functions
def spam():
    pass #...

def blah():
    pass #...

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    print("HELLO...", argv)

if __name__ == '__main__':
    import sys
    main(sys.argv)
