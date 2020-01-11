import pandas as pd
import os
import sys
        
class Helper:
        
    ANDROID_VALUES_FOLDER = "values"
    ANDROID_SEPERATOR = "-"
    ANDROID_FILE_START = "<resources>"
    ANDROID_FILE_END = "</resources>"
    ANDROID_STRING_END = "</string>"
    ANDROID_STRING_START = "<string name=\""
    ANDROID_KEY_END = "\">"
    KEY = "key"
    storeKey = ""
    stringFile = ""
    NEW_LINE = "\n"
    isFileExist = False
    isFolderExist = False
    
    excelFile = pd.read_excel(r'translation.xlsx')
    
    def traverseExcelFile(self):
        for row in self.excelFile.itertuples(index=False): 
            for key, value in row._asdict().items():
                if key == self.KEY:
                    self.storeKey = value
                else:
                    self.writeTranslation(self.ANDROID_VALUES_FOLDER, self.ANDROID_SEPERATOR, key, value)
    
    def isFileEmpty(self):
        return self.excelFile.empty
    
    def androidStringStart(self, key):
        return ANDROID_STRING_START + key + ANDROID_KEY_END 
    
    def writeTranslation(self, path, seperator, lang, value):
        directoryName = os.path.join(path + seperator + lang)
        if not self.checkDirectoryOrFileExist(directoryName):
            print("directory not exist", directoryName)
            os.mkdir(directoryName)
        self.createFile(directoryName, "strings.xml", lang, value)
    
    def checkDirectoryOrFileExist(self, path):
        return os.path.exists(path)
    
    def createFile(self, directory, fileName, lang, value):
        self.stringFile = os.path.join(directory, fileName)
        #if not checkDirectoryOrFileExist(fileName)
        if os.path.exists(self.stringFile):
            append_write = 'r+' # append if already exists
            isFileExist = True
            print("append string file:", self.stringFile)
            f = open(self.stringFile, append_write)
            fileData = f.readlines()
            secondLastLineNumber = len(fileData) - 2
            print(fileData)
            print("number:",secondLastLineNumber )
            f.truncate(0)
            f.close()
            f = open(self.stringFile, "a+")
            newTranslationLine = self.ANDROID_STRING_START + self.storeKey + self.ANDROID_KEY_END + value  + self.ANDROID_STRING_END + self.NEW_LINE
            fileData.insert(secondLastLineNumber, newTranslationLine)
            f.writelines(fileData)
            f.close()

        else:
            append_write = 'w+' # make a new file if not
            isFileExist = False
            print("write string file:", self.stringFile)
            f = open(self.stringFile, append_write)
            f.writelines(self.ANDROID_FILE_START + self.NEW_LINE)
            f.writelines(self.ANDROID_STRING_START + self.storeKey + self.ANDROID_KEY_END + value  + self.ANDROID_STRING_END + self.NEW_LINE)
            f.writelines(self.ANDROID_FILE_END)
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
