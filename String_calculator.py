from logging import raiseExceptions
from posixpath import split
from unittest.case import _AssertRaisesContext
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
                    negative_numbers = int(i) < 0
                    if negative_numbers == True:
                        raise Exception('negatives not allowed ' )
                        return i
                        break
                    elif int(i) <= 1000:
                        i = int(i)
                        sum = sum+i
                    elif int(i) > 1000:
                        continue
                elif i.isalpha()==True:
                    i = i.lower()
                    i = ord(i) - 96
                    sum = sum + i
                
            return sum
