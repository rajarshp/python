#!/usr/bin/python -tt

#########################################################################################################
#   Developer: Rajarshi Pain
#   Version: 1.0
#   Date:07/07/2016
#   Description: This will read XML file and print the details
#
#########################################################################################################

"""
XML File:
-<book id="bk101">
<author>Gambardella, Matthew</author>
<title>XML Developer's Guide</title>
<genre>Computer</genre>
<price>44.95</price>
<publish_date>2000-10-01</publish_date>
<description>An in-depth look at creating applications with XML.</description>
</book>

"""

############################################### MODULES #################################################

import xml.etree.ElementTree as ET
import datetime

############################################### VARIABLES ###############################################

xmlfile_name = 'book.xml'
xmlfile = ''
xmlcontent = ''

#########################################################################################################

def readxml():
    global xmlcontent, xmlfile

    xmlfile = ET.parse(xmlfile_name)
    xmlcontent = xmlfile.getroot()

    for item in xmlfile.findall('book'):
        id = item.get('id')
        author = item.find('author').text
        author = author.split(",")
        title = item.find('title').text

        print id, " - ",title," by ", author[0],author[1]




def main():

    start_time=datetime.datetime.now().replace(microsecond=0)
    readxml()
    end_time = datetime.datetime.now().replace(microsecond=0)

    print '\nTime taken for this operation :', (end_time-start_time)

if __name__=='__main__':
    main()