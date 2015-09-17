#!/usr/bin/python

class readFile():
    
    def __init__(self, fname):
        self.fname = fname
        
        self.read()


    def read(self):
        print "Read file: " + self.fname
        with open(self.fname, 'r') as f:
            content = f.readlines()

        #for line in content:
        #    print line
        print content[0]


if __name__ == '__main__':
    readFile("cax/2.cax")

