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
                if i.isdigit()==True:
                    i = int(i)
                    sum = sum+i
                elif i.isalpha()==True:
                    i = i.lower()
                    i = ord(i) - 96
                    sum = sum + i
            return sum
