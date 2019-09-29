# _*_ coding: utf-8 _*_
import sys
import csv


class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]
        index1 = args.index('-c')
        configfile1 = index[index1+1]
        index2 = args.index('-d')
        configfile2 = index[index2+1]
        index3 = args.index('-o')
        configfile3 = index[index3+1]
    try:



class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        _config = {}
        with open('comfigfile1','r') as f:
            for i in f:
                name,value = split(' = ')
                _config[name]=float(value)


