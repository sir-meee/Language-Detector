#TextBlob is a python library for processing textual data.
#It provides a simple API for diving into common natural language
#processing (NLP) tasks such as part-of-speech tagging, noun phrase
#extraction, sentiment analysis, classification, translation, and more.
#The Language Detection and Translation of textblob module is powered 
#by Google Translate API

from textblob import TextBlob

#   ------------------ DETECT INPUT STRING LANGUAGE ----------------------

#Prompting the user to enter a string
inputSTR = input("\nENTER THE STRING :")

#Creating object of TextBlob() and passing the input-string to it
textblob_obj = TextBlob(inputSTR)

#Detecting the language of the input string using detect_language()
detectLanguage = textblob_obj.detect_language()

#Printing the detected language
print("\nDETECTED LANGUAGE :", detectLanguage)

#   ------------------ TRANSLATE INPUT STRING TO OTHER LANGUAGES ----------------------

#Prompting the user to enter a string
inputString = input("\nENTER THE STRING :")

#Creating object of TextBlob() and passing the input-string to it
textblob_obj1 = TextBlob(inputString)

#Translate the string to different languages using translate() with to argument
#set to '' and printing the translated result
arabicOUTPUT = textblob_obj1.translate(to='ar')
print("\nINPUT STRING IN ARABIC LANGUAGE : ", arabicOUTPUT)

chineseSimplified = textblob_obj1.translate(to='zh-CN')
print("\nINPUT STRING IN CHINESE SIMPLIFIED LANGUAGE : ", chineseSimplified)

frenchOUTPUT = textblob_obj1.translate(to='fr')
print("\nINPUT STRING IN FRENCH LANGUAGE : ", frenchOUTPUT)

greekOUTPUT = textblob_obj1.translate(to='el')
print("\nINPUT STRING IN GREEK LANGUAGE : ", greekOUTPUT)

hindiOUTPUT = textblob_obj1.translate(to='hi')
print("\nINPUT STRING IN HINDI LANGUAGE : ", hindiOUTPUT)        