#!/usr/bin/python3
import sys
from datetime import datetime

date = datetime(2015, 10, 19)


def main():
    sys.stderr.write('and that piece of art is useful - Dora Korpar, {:%Y-%m-%d}\n'.format(date))
    exit(1)
  

if __name__=="__main__":
    main()
