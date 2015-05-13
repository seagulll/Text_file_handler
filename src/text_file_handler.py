'''
Created on Nov 18, 2013

@author: elingyu
'''

#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil

def parse_args():
    usage = """usage: %prog [options]
This is the txt file handler.
Run it like this:

    python text_file_handler.py -a "replace" -b "yes" -c "C:\simon\Temp\config_file\backup" -e "C:\simon\Temp\config_file\cfg" -f "*.cfg" -g hate -i "love"
    
"""
    parser = optparse.OptionParser(usage)
    parser.add_option("-a", "--do", dest="do", type="string", help="replace; insert; delete; insert_line; delete_line", default="replace")
    
    parser.add_option("-b", "--backup", dest="backup", type="string", help="yes; no", default="yes")
    parser.add_option("-c", "--backup directory", dest="backup_directory", type="string", help="backup directory", default="c:")
    
    parser.add_option("-e", "--origin directory", dest="origin_directory", type="string", help="origin directory", default="c:")
    parser.add_option("-f", "--origin files", dest="origin_files", type="string", help="origin files", default="*.cfg")
    parser.add_option("-g", "--origin characters", dest="origin_characters", type="string", help="origin characters", default="")
    
    parser.add_option("-i", "--target characters", dest="target_characters", type="string", help="target characters", default="")    
    
    parser.add_option("-j", "--target_characters_file", dest="target_characters_file", type="string", help="target_characters_file", default="")    
    parser.add_option("-k", "--del_line_number", dest="del_line_number", type="string", help="del_line_number", default="")    

    (options, _) = parser.parse_args()
    

    if options.origin_characters == "":
        parser.error("The origin character is null")
        parser.exit()
        
    if options.do == "replace":
        print "You are trying to replace the %s with %s !" %(options.origin_characters, options.target_characters)
    elif options.do == "insert":
        print "You are trying to insert the %s behind %s !" %(options.target_characters, options.origin_characters)
    elif options.do == "delete":
        print "You are trying to delete the %s !" %(options.origin_characters)
    elif options.do == "insert_line":
        print "You are trying to insert line !"
    elif options.do == "delete_line":
        print "You are trying to delete line !"
    else:
        print "The do %s is illegal!" %(options.do)
        parser.exit()

    print "The origin directory is %s" %(options.origin_directory)
    
    print "The origin files suffix is %s" %(options.origin_files)
    
    if options.backup == "yes":
        print "The backup directory is %s" %(options.backup_directory)
    elif options.backup == "no":
        print "The old files will not be backuped!"
    else:
        print "The backup number %s is illegal!" %(options.backup)
        parser.exit()
    
    return options.do, options.backup, options.backup_directory, options.origin_directory, options.origin_files, options.origin_characters, options.target_characters, options.target_characters_file, options.del_line_number


def backup_file(origin_directory, file_name, backup_directory):
    shutil.copyfile(origin_directory + "//" + file_name, backup_directory + "//" + file_name)

def replace_characters(origin_directory, file_name, origin_characters, target_characters):
    lines = open(origin_directory + "//" + file_name).readlines()
    fp = open(origin_directory + "//" + file_name, 'w')
    for s in lines:
        fp.write(s.replace(origin_characters, target_characters))
    fp.close()

def insert_characters(origin_directory, file_name, origin_characters, target_characters):
    lines = open(origin_directory + "//" + file_name).readlines()
    fp = open(origin_directory + "//" + file_name, 'w')
    for s in lines:
        fp.write(s.replace(origin_characters, origin_characters + target_characters))
    fp.close()

def delete_characters(origin_directory,file_name, origin_characters):
    lines = open(origin_directory + "//" + file_name).readlines()
    fp = open(origin_directory + "//" + file_name, 'w')
    for s in lines:
        fp.write(s.replace(origin_characters, ""))
    fp.close()
    
def insert_line(origin_directory, file_name, origin_characters, target_characters_file):
    fp_orig = open(origin_directory + "//" + file_name, 'r')    
    lines = fp_orig.readlines()
    fp_orig.close()
    
    fp_target =  open(origin_directory + "//" + target_characters_file, 'r') 
    target_lines = fp_target.readlines()
    fp_target.close()
    target_str = ''
    
    for tmp in target_lines:
        target_str += tmp
    
    all_text = ''
    for s in lines:
        if s.find(origin_characters) != -1:
            s += target_str
        all_text += s
        
    fp = open(origin_directory + "//" + file_name, 'w')
    fp.write(all_text)
    fp.close()

def delete_line(origin_directory, file_name, origin_characters, del_line_number):
    fp_orig = open(origin_directory + "//" + file_name, 'r')    
    lines = fp_orig.readlines()
    fp_orig.close()
    
    all_text = ''
    del_counter = 0
    for s in lines:
        if s.find(origin_characters) != -1:
            del_counter = int(del_line_number)-1
            continue
        
        if del_counter != 0:
            del_counter -= 1
            continue
        
        all_text += s
        
    fp = open(origin_directory + "//" + file_name, 'w')
    fp.write(all_text)
    fp.close()


def text_file_handler(do, backup, backup_directory, origin_directory, origin_files, origin_characters, target_characters, target_characters_file, del_line_number):
    file_list = os.listdir(origin_directory)
    file_number = len(file_list)
    org_file_list = []
    
    for i in range(0, file_number):
        if fnmatch.fnmatch(file_list[i], origin_files): 
            org_file_list.append(file_list[i])
    
    org_file_number = len(org_file_list)
    
    for i in range(0, org_file_number):
        if backup == "yes":
            backup_file(origin_directory, org_file_list[i], backup_directory)
        
        if do == "replace":
            replace_characters(origin_directory, org_file_list[i], origin_characters, target_characters)
        
        if do == "insert":
            insert_characters(origin_directory, org_file_list[i], origin_characters, target_characters)
            
        if do == "delete":
            delete_characters(origin_directory, org_file_list[i], origin_characters)
        
        if do == "insert_line":
            insert_line(origin_directory, org_file_list[i], origin_characters, target_characters_file)

        if do == "delete_line":
            delete_line(origin_directory, org_file_list[i], origin_characters, del_line_number)
        

if __name__ == '__main__':
    parameters = parse_args()
    text_file_handler(*parameters)
    
    print "Done!"


