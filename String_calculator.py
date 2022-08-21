from audioop import add
from logging import raiseExceptions
from posixpath import split
import string
import re
from tokenize import String
from unittest.case import _AssertRaisesContext
class String_calculator:
    def add(strings):
        if strings == '':
            return 0
        elif len(strings) == 1:
            return int(strings)
        else:
            list_of_comaseperated_string = re.split(',|\n',strings)
            sum=0
            negativeNumbers=""
            for i in list_of_comaseperated_string:
                #print(i)
                if i[0] =='-':
                    negativeNumbers = negativeNumbers + i + ","

                elif i.isdigit() == True:
                    if int(i) <= 1000:
                        i = int(i)
                        sum = sum+i

                    elif int(i) > 1000:
                        continue
                elif i.isalpha()==True:
                    i = i.lower()
                    i = ord(i) - 96
                    sum = sum + i
            #print("Negatives: ",negativeNumbers)
            if(len(negativeNumbers) > 0):
                raise Exception('negatives not allowed: ' + negativeNumbers)
            return sum
