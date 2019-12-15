import pandas as pd
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
#       print(i, j)
#       print() 
"""
        
class Helper:
        
    ANDROID_VALUES_FOLDER = "values"
    ANDROID_SEPERATOR = "-"
    ANDROID_FILE_START = "<resources>"
    ANDROID_FILE_END = "</resources>"
    ANDROID_STRING_END = "</string>"
    ANDROID_STRING_START = "<string name="
    ANDROID_KEY_END = "\">"
    KEY = "key"
    storeKey = ""
    NEW_LINE = "\n"
    
    excelFile = pd.read_excel(r'translation.xlsx')
    
    def traverseExcelFile(self):
        for row in excel.itertuples(index=False): 
            for key, value in row._asdict().items():
                if key == self.KEY:
                    storeKey = key
                else:
                    writeTranslation(ANDROID_VALUES_FOLDER, ANDROID_SEPERATOR, key, value)           
    
    def isFileEmpty(self):
        return self.excelFile.empty
    
    def androidStringStart(self, key):
        return ANDROID_STRING_START + key + ANDROID_KEY_END 
    
    def writeTranslation(self, path, seperator, lang, value):
        directoryName = os.path.join(path + seperator + lang)
        if not checkDirectoryOrFileExist(directoryName):
            print("directory not exist", directoryName)
            os.mkdir(directory)
            createFile(directory, "strings.xml")
    
    def checkDirectoryOrFileExist(self, path):
        return os.path.exists(path)
    
    def createFile(self, directory, filename):
        fileName = s.path.join(directory, filename)
        #if not checkDirectoryOrFileExist(fileName)
        f = open(fileName, "w+")
        f.close()


class Android():
    
    helper = Helper()
    
    def __init__(self):
        print("android initialze")
    
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

helper = Helper()
helper.createDirectory("valu", "")
helper.createFile("valu-", "string.xml")"""
