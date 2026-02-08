import os
import logging as log

log.basicConfig(level=log.INFO) # Set the threshold to INFO


def double(input1: int) -> int:
    return input1*input1

if __name__== "__main__":
    #log.info(f"double(56)")
    print(double(56))


#log.info(f"double(56)")