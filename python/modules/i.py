import os
def print_error(a):
    print"\033[1;37m[\033[0m\033[0;31m!\033[0m\033[1;37m]\033[0m\033[0;31m %s \033[0m" % a
def print_good(a):
    print"\033[1;37m[\033[0m\033[0;34m+\033[0m\033[1;37m]\033[0m\033[0;34m %s \033[0m" % a
def print_warning(a):
    print"\033[1;37m[\033[0m\033[0;31m-\033[0m\033[1;37m]\033[0m\033[0;31m %s \033[0m"  % a
def print_heading(a):
    print '\033[2;36m %s \033[0m' % a

def clear():
  if os.name == 'nt':
	os.system('cls')
  else:
     os.system('sleep 5 && clear')

## count number of lines in file
def print_number_of_lines(a,b):
    fname = a
    num_lines = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
    print "Total %d Number of %s loded" % (num_lines,   b)
##use PATH = file and i.print_number_of_lines(PATH,"Host")
