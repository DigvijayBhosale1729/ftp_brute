# ftp_brute
A command line tool written in python that bruteforces FTP server according to password file and username
Usage 

      Usage: python3 ftp_brute [options] argument use -h for help

      Options:
        -h, --help   show this help message and exit
        -m MODE      Specify Mode you want to use. -m 1 for passsword file with
                     username and password separated by : and -m 2 for entering one
                     username and corresponding password file
        -H HOSTNAME  Specify hostname
        -f PASSWD    Specify dictionary file
        -u USERNAME  When using -m 2, use this option for username
        -s SEPCHAR   Optional argument - When using -m 1, use this option for
                     charachter separating username and password
                    
PS- The script was tested only on a local FTP server. It should work on an online server as well, but should a problem arise, i'll try to correct it as soon as possible
