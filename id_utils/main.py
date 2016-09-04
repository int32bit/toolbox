#!/usr/bin/python
#coding=utf-8

from id_util import *

if __name__ == "__main__":
    data = list()
    with open("test_id_number.txt", "r") as f:
        for line in f:
            data.append(line.split()[0].strip())
    print_info(data)
