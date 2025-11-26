###############################################################################
#
#  Author:           Rykir Evans & Victoria Heredia
#  Email:            rjevans0408@my.msutexas.edu | vdheredia1128@my.msutexas.edu
#  Title:            Log Analyzer & Data Cleaner
#  Course:           CMPS 4143 Java and Python
#  Professor:        Dr. Tina Johnson
#  Semester:         Fall 2025
#
#  Description:
#         
#         
#  Usage:
#         
#
#  Files: 
#         main.py
#         log.txt
###############################################################################

import re

lineCount = 0
invalidCount = 0
errorCount = 0

users = [] 
statuses = {}

with open("temp.txt", encoding="utf-8") as fin:
    for line in fin:
        s = line.strip()
        lineCount += 1

        if "invalid" in s.lower():
            invalidCount += 1
        

        
        # Searches for all continuous instances containing an `@` symbol and a period `.`
        # This should grab any email address
        user = re.findall(r"\w+@.+\.\w+", s)

        # Append to list of users 
        if(user):
            # Since findall returns a list, we used `.extend()`
            users.extend(user)

            # Determine login status
            status = re.findall(r"login(?i)\S+", s)

            #
            if(user[0] not in statuses):
                statuses[user[0]] = status
            else:
                statuses[user[0]].extend(status)
                
            print(status)
            print(statuses)

        # Finds anywhere that might indicate an error by searching for ERR (not case-sensitive)
        err = re.findall(r"\w*[Ee][Rr]{2}\w*", s)
        
        if(err):
            # Specifically excludes occurences in a username/email address
            if((user and (err[0] in user[0]))):
                pass
            else:
                errorCount += 1
                # print(err)
               
        


    
    print(f"Invalid entries: {invalidCount}")
    print(f"Total errors: {errorCount}")
    print(users)