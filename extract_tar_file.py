#!/usr/bin/python -tt

#########################################################################################################
#   Developer: Rajarshi Pain
#   Version: 1.0
#   Date:07/07/2016
#   Description: This will read and extract specific file from a TAR file from a list of components
#
#########################################################################################################

############################################### MODULES #################################################

import tarfile
import datetime
import sys
import re
import os

############################################### VARIABLES ###############################################

input_file = 'components.txt'
tar_file_name = ''
failed_files = ''
current_path=os.getcwd()

############################################### METHODS #################################################

def take_input():
    global tar_file_name

    tar_file_name = raw_input('Enter the source TAR file name: ')
    tar_file_name = tar_file_name.strip()
    while not tar_file_name:
        print '##########\nInvalid input\n##########'
        tar_file_name = raw_input('Enter the source TAR file name: ')
        tar_file_name = tar_file_name.strip()


def extracrTAR():
    global tar_file_name, failed_files

    print 'Extracting files from ',tar_file_name
    try:
        inputfile = open(input_file)
        tar_file = tarfile.open(tar_file_name)
        tar_list = tar_file.getmembers()

        for component in inputfile:
            is_extracted = 'false'

            component = component.strip()
            component = component.strip('\n')
            if component == '' or len(component) == 0: continue
            print 'Extracting ', component
            for item in tar_list:

                item1 = '"'+str(item)+'"'

                match = re.search(component, item1)
                if match:
                    tar_file.extract(item)
                    is_extracted = 'true'
                    break
            if is_extracted == 'false':
                failed_files = failed_files + '\nFailed to extract ' + component

    except Exception, e:
        print 'ERROR: ', e.message

############################################### MAIN METHOD #############################################

def main():
    take_input()
    start_time=datetime.datetime.now().replace(microsecond=0)
    extracrTAR()
    end_time = datetime.datetime.now().replace(microsecond=0)
    print failed_files
    print '\nTime taken for this operation :', (end_time-start_time)

if __name__=='__main__':
    main()
