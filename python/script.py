import sys
sys.path.insert(0, 'modules/')
import requests,os,time,i,ping,os.path

def check_if_file_exist():
    PATH = sys.argv[1]
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print 'File Name %s Found\t' % (PATH)
        i.print_number_of_lines(PATH,"Host")
        ping.ping_host()
    else:
        print "Invalid File  " +PATH  ## Checking if file name the True
def check_if_host_is_up():
    if len(sys.argv) not in [2]:
        print "Usage: ./script.py <hostlist>\n"
        exit()
    else:
        check_if_file_exist()


check_if_host_is_up()
