#!/usr/bin/ python
# Author: @Givemefivw
# Descri: 调用Xray basic爬虫批量扫描
import re
import argparse
import os
import subprocess
import sys
import hashlib


def banner():
    banner = '''    

    Coding:
            @Givemefivw
    '''
    print(banner)

def autoxray(file):
    target = open(file,'r',encoding='utf-8')
    lines = target.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                url = "http://" + line.strip()
            else:
                url = line.strip()

            outputfilename=hashlib.md5(url.encode("utf-8"))

            filename = outputfilename.hexdigest()

            cmd = ["./xray","webscan","--basic-crawler",url,"--html-output" ,"report_{}.html".format(filename)]

            rsp = subprocess.Popen(cmd)

            output, error = rsp.communicate()

            print(output)
        
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