#!/usr/bin/env python

# open file

with open("/tmp/foo.txt", "r") as f:
  lines = f.readlines()   //readlines will read all the lines of the file and all the lines will be stored in "lines"
  print lines
  #print f

