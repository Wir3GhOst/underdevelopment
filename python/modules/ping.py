import requests,os,time,i,sys
def ping_host():
     word = sys.argv[1]
     i.clear()
     i.print_heading('                    checking if host is up.......')
     f = open(word, 'r')
     for line in f:
        panel = line.strip('\n')
        urlx = ' '+str(panel)
        url = 'http://'+str(panel)
        try:
           response = requests.get(url,timeout=10)
        except Exception as e:
            i.print_error(urlx+'                             ==> Invalid Host')
        else:
            r = response.status_code
            if  (r) == 200 and r <300:
                i.print_good(urlx+'                      \033[2;37m==> Host is up')
                save_urlx = 'echo'+urlx+'>>target.txt'
                os.system(save_urlx)
            else:
                i.print_warning(urlx+'                      ==> Host is Down')
