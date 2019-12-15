import pandas as pd
import math
import os
import sys
"""
missing_values = ["n/a","","NaN"]


translation = pd.read_excel(r'translation.xlsx', na_values = missing_values)
X = translation.iloc[:]
print(X)
print("----------------")
print(X.columns)
for i in X.columns:
    print(i)
#print(X)
#translation = translation.loc[:, ~translation.columns.str.contains('^Unnamed')]

#print(translation)


#print(translation.columns)

#print(len(translation))
check 
#for i, j in X.iterrows(): 
  #  if not j.empty:
#        print(i, j)
 #       print() 
"""
        
class Helper:
        
    excelFile = pd.read_excel(r'translation.xlsx')
    
    def traverseExcelFile(self):
        for row in excel.itertuples(index=False): 
            for key, val in row._asdict().items():
                print(key, val)
    
    def isFileEmpty(self):
        return self.excelFile.empty
    
    def createDirectory(self, path, lang):
        directory = os.path.join(path + "-" +lang)
       # if n#ot checkDirectoryExist(directory):
        os.mkdir(directory)
        #createFile(directory, "strings.xml")
    
    def checkDirectoryExist(self, directory):
        return os.path.exists(directory)
    
    def createFile(self, directory, filename):
        f = open(directory+"/"+filename, "w+")
        f.close()


class Android():
    
    helper = Helper()
    
    def __init__(self):
        print("android initialze")
        #self.helper.createDirectory("abc", "ID")
    
    
    def initialize(self):
        if not self.helper.isFileEmpty():
            self.helper.traverseExcelFile()
        else:
            print("File is empty")
        

class Ios:
    pass    

class Main:
    
    os = sys.argv[1]
    if(os == "android"):
        print("passed param is android")
        android  = Android()
        android.initialize()
    elif(os == "ios"):
        print("passed param is ios")
    else:
        print("Please recheck the parameter's")
        

"""
class ios:

helper = Helper()
helper.createDirectory("valu", "")
helper.createFile("valu-", "string.xml")"""
