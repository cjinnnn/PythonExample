import os
def os_check():
    print(os.name)
    # Windows10,11 : nt
    # ubuntu 20.04 : posix

import sys
def sys_check():
    print(sys.platform)
    # Windows10,11 : win32
    # ubuntu 20.04 : linux

import platform
def platform_check():
    print(platform.system())
    # Windows10,11 : Windows
    # ubuntu 20.04 : Linux

    print(platform.uname())
    #Windows10,11 : uname_result(system='Windows', node='CJ-Gram', release='10', version='10.0.22621', machine='AMD64')
    #ubuntu20.04 : uname_result(system='Linux', node='CJ-Gram', release='5.15.0-52-generic', version='#58~20.04.1-Ubuntu SMP Thu Oct 13 13:09:46 UTC 2022', machine='x86_64', processor='x86_64')

    print(platform.uname().system)
    # Windows10,11 : Windows
    # ubuntu 20.04 : Linux

if __name__ == "__main__":
    print("===== os ====")
    os_check()

    print("===== sys ====")
    sys_check()

    print("===== platform ====")
    platform_check()