from posixpath import split
import re
class String_calculator:
    def add(strings):
        if strings == '':
            return 0
        elif len(strings) == 1:
            return int(strings)
        else:
            list_of_comaseperated_string = strings.split(",")
            sum=0
            for i in list_of_comaseperated_string:
                i = int(i)
                sum = sum+i
            return sum