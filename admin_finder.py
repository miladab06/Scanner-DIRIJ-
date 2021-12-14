#!/usr/bin/python
# This Python file uses the following encoding: utf-8
from colorama import init
init()
from colorama import Fore, Back, Style
import requests, time, sys, os, httplib, socket, threading
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import multi_thread_port_scan
h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
txt = {'user_login' , 'password' , 'username' , 'type="password"'}
TTL = {'TTL=126' , 'TTL=62' , 'TTL=255','TTL=32','TTL=128','TTL=254','TTL=200','TTL=60'}
php = {'admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
   'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
   'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
   'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
   'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','adminpanel.html','webadmin.html',
   'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
   'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
   'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
   'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
   'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
   'admin/adminLogin.html','adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
   'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
   'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
   'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
   'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
   'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
   'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
   'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
   'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php'}

asp = {'account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
   'admin_area/admin.asp','admin_area/login.asp',
   'admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
   'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
   'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
   'moderator/admin.asp','controlpanel.asp','user.asp','admincp/index.asp','admincp/login.asp','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
   'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
   'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp',
   'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
   'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
   'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp'}

cfm = {'admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
   'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm',
   'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm',
   'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp',
   'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
   'administrator/account.cfm','administrator.cfm','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
   'moderator/admin.cfm','account.cfm','controlpanel.cfm','admincontrol.cfm','acceso.cfm','rcjakar/admin/login.cfm',
   'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','adminpanel.cfm','user.cfm',
   'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
   'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
   'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
   'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm'}

js = {'admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
   'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js',
   'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js',
   'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp',
   'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
   'administrator/account.js','administrator.js','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
   'moderator/admin.js','account.js','controlpanel.js','admincontrol.js','rcjakar/admin/login.js',
   'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','adminpanel.js','user.js',
   'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
   'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
   'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
   'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js'}

cgi = {'admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi',
   'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi',
   'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi',
   'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp',
   'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
   'administrator/account.cgi','administrator.cgi','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
   'moderator/admin.cgi','account.cgi','controlpanel.cgi','admincontrol.cgi','rcjakar/admin/login.cgi',
   'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','adminpanel.cgi','user.cgi',
   'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
   'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
   'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
   'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi'}

brf = {'admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
   'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf',
   'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf',
   'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp',
   'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
   'administrator/account.brf','administrator.brf','acceso.brf','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
   'moderator/admin.brf','account.brf','controlpanel.brf','admincontrol.brf','rcjakar/admin/login.brf',
   'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','adminpanel.brf','user.brf',
   'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
   'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
   'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
   'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf'}
exitFlag = 0
class myThread (threading.Thread):
   def __init__(self, threadID, name, delay, pages, url):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.pages = pages
      self.url = url
      
   def run(self):
      # print "Starting " + self.name
      admin_finder(self.name, 1, self.delay, self.pages, self.url)
      # print "Exiting " + self.name

def admin_finder(threadName, counter, delay, pages, url):
   # print "%s: %s" % (threadName, time.ctime(time.time()))
   if exitFlag:
         threadName.exit()
         time.sleep(delay)
   counter -= 1
   var1 = 0
   var2 = 0
   url2 = url
   # urls = []
   # print url2     
   for admin in pages:
      admin = admin.replace('\n','')
      host = url2 + admin
      #print host
      # print (Fore.RED+'\n\t [#] Checking ' + host + '...')
      # print (Style.RESET_ALL)
      response = requests.get(host,headers=h)
      var2 = var2 + 1
      if response.status_code == 200:
         # urls[admin] = host
         # urls [var2] = urls [var2] + host
         print (Fore.GREEN+ '%s %s' % ( '\n\n\t>>>' + '\t' + host,''+Style.RESET_ALL+Fore.RED+ 'Admin page found!'))
         #raw_input('Press enter to continue scanning.\n')
         # print response.text
         # print response.content
         page_content = response.content.splitlines()
         found = False
         found = any(txt1 in line for txt1 in txt for line in page_content)
         print any(txt1 in line for txt1 in txt for line in page_content)
         for line in page_content:
            line = line.strip()
            line = line.replace(' ','')
            # print line
            # blabla = 'div'
            # if blabla in line:
               # found = True
               # break
               # print 'div'
         print (Style.RESET_ALL)
         continue
         if found == True:
            print (Fore.GREEN+ '%s %s' % ( '\n\n\t>>>' + '\t' + host,''+Style.RESET_ALL+Fore.RED+ 'Admin page found!'))
      elif response.status_code == 404:
         var2 = var2
      elif response.status_code == 302:
         print (Fore.RED+ '%s %s' % ('\n>>>' + host, 'Possible admin page (302 - Redirect)'))
         print (Style.RESET_ALL)
      else:
         print (Fore.RED+'%s %s %s' % (host, ' Interesting response:', response.status_code))
         print (Style.RESET_ALL)
      # print(Fore.GREEN+'\n\nCompleted \n')
      # print (Style.RESET_ALL)
      # print var1, ' Admin pages found'
      # print urls
      # print var2, ' total pages scanned'
      # raw_input('The Game Over; Press Enter to Exit')

def os_detection(url):
   try:
      response = os.popen('ping -n 1 ' + url )
      for line in response.readlines():
         if TTL in line:
            print 'OKK'
      # found = any(TTLT in line for TTLT in TTL for line in response.readlines())
      # print found
         print line
   except Exception as e:
      print 'Error:' , e
def main(url):
   try:
      print "Before port scan"
#      multi_thread_port_scan.scan_ports('127.0.0.1',1)
      print (Style.BRIGHT+Back.WHITE)
      print (Style.DIM+Fore.BLACK+'Admin Finder v1.0')
      print (Style.RESET_ALL)
      url = url.strip()
      url = url.replace('http://','')
      os_detection(url)
      if (not url.endswith('/')):
         url += '/'
      if (not url.endswith('http://', 1, 8)):
         url2 =  'http://' + url
      elif (url.endswith('http://', 1, 10)):
          print url2
         # Create new threads
      thread1 = myThread(1, "Thread-1", 1, php, url2)
      thread2 = myThread(2, "Thread-2", 1, asp, url2)
      thread3 = myThread(3, "Thread-3", 1, cfm, url2)
      thread4 = myThread(4, "Thread-4", 1, js, url2)
      thread5 = myThread(5, "Thread-5", 1, cgi, url2)
      thread6 = myThread(6, "Thread-6", 1, brf, url2)
      
      # Start new Threads
      thread1.start()
      thread2.start()
      thread3.start()
      thread4.start()
      thread5.start()
      thread6.start()

   except Exception as e:
      print e

def usage():
   try:
      print 'python FILE.py url'
   except Exception as e:
      print e

def clear_screen():
    '''
    Clears the terminal screen.
    '''
    # Clear command as function of OS
    command = 'cls' if system_name().lower()=='windows' else 'clear'

    # Action
    system_call(command)

try:
   clear_screen()
   print (Style.DIM+Fore.GREEN+'\t#########################################################################################################')
   print (Style.DIM+Fore.GREEN+'\t#                                              Scanner                                                  #')
   print (Style.DIM+Fore.GREEN+'\t#                                                                                                       #')
   print (Style.DIM+Fore.GREEN+'\t#           ###############   #######    #######       #######    #######                               #')
   print (Style.DIM+Fore.GREEN+'\t#           #             ##    # #      # ######        # #       # #                                  #')
   print (Style.DIM+Fore.GREEN+'\t#           #     #####    ##   # #      # #   # #       # #       # #                                  #')
   print (Style.DIM+Fore.GREEN+'\t#           #     #   #     ##  # #      # #    # #      # #       # #                                  #')
   print (Style.DIM+Fore.GREEN+'\t#           #     #   #     ##  # #      # #   # #       # #       # #                                  #')
   print (Style.DIM+Fore.GREEN+'\t#           #     #   #    ##   # #      # ##### #       # #       # #  ###                             #')
   print (Style.DIM+Fore.GREEN+'\t#           #     #####   ##    # #      # # #  # #      # #       # #  # #                             #')
   print (Style.DIM+Fore.GREEN+'\t#           #            ##     # #      # #     # #     # #       # #### #                             #')
   print (Style.DIM+Fore.GREEN+'\t#           ##############     #####    #####     ####  #####      ########                             #')
   print (Style.DIM+Fore.GREEN+'\t#                                                                                                       #')
   print (Style.DIM+Fore.GREEN+'\t#                                                                                               Finder  #')
   print (Style.DIM+Fore.GREEN+'\t#                                                                                       Coded by MiLAD  #')
   print (Style.DIM+Fore.GREEN+'\t#                                                                                                       #')
   print (Style.DIM+Fore.GREEN+'\t#########################################################################################################')
   if len(sys.argv) == 2:
      main(sys.argv[1])
   else:
      usage()
except (KeyboardInterrupt, SystemExit):
      pass 



  
