#!/usr/bin/env python3

#MongoExport produces a file with each JSON document on a separate line (see ../tweets_09_23.json). This format is meant to be read line-by-line and will produce errors for tools/import utilities that intend to read each document as a single file. This script will convert the MongoExport result to a JSON array for those tools. 
import os
print(os.getcwd())

oldF = open('tweets_09_23.json', 'r') #Replace with correct path if not executing from project root
oldStr = oldF.read()
oldF.close()

import re
newStr = re.sub('\n',',',oldStr)
newStr = '[' + newStr + ']'
newF = open('sample_tweets.json','w+') #Replace with correct path if not executing from project root
newF.write(newStr)
newF.close()
