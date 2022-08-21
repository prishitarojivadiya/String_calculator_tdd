from posixpath import split
import re
class String_calculator:
    def add(strings):
        if strings == '':
            return 0
        elif len(strings) == 1:
            return int(strings)
        