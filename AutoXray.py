import re
import argparse
import os
import sys


def banner():
    banner = '''
  __   _  _  ____  __     _  _  ____   __   _  _ 
 / _\ / )( \(_  _)/  \   ( \/ )(  _ \ / _\ ( \/ )
/    \) \/ (  )( (  O )   )  (  )   //    \ )  / 
\_/\_/\____/ (__) \__/   (_/\_)(__\_)\_/\_/(__/  

                Author : Givemefivw
                Version: 0.1
    '''
    print(banner)

def autoxray(file):
    target = open(file,'r')
    lines = target.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                url = "http://" + line.strip()
            else:
                url = line.strip()
            time = '%date:~0,4%%date:~5,2%%date:~8,2%0%time:~1,1%%time:~3,2%%time:~6,2%'
            command = "xray.exe webscan --basic-crawler {} --html-output result-{}.html".format(url,time)
            os.system(command)
        except Exception as e:
            pass
        except KeyboardInterrupt:
            sys.exit
    target.close()


def main():
    parser = argparse.ArgumentParser(description='Auto Xray Help')
    parser.add_argument('-f','--file',help='urlfile',default='')
    args = parser.parse_args()

    if args.file:
        file = args.file
        autoxray(file)


if __name__ == '__main__':
    banner()
    main()