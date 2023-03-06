import os
def ping_os(hostname):
    ping_count = 1
    timeout = 3
    response = -1
    if os.name == "posix": #Linux
        response = os.system(f"ping -c {ping_count} -W {timeout} {hostname}")
    elif os.name == "nt": #Windows
        response = os.system(f"ping -n {ping_count} -w {timeout} {hostname}")

    if response == 0:
        print(f"{hostname} ping ok!")
    else:
        print(f"{hostname} ping error!")

import ping3 #설치필요: pip install ping3
def ping_ping3(hostname):
    timeout = 3
    response = ping3.ping(hostname, timeout=timeout)
    if response == None:
        print(f"{hostname} ping error!")
    else:
        print(f"{hostname} ping ok!")

if __name__ == "__main__":
    print("===== os ping ====")
    ping_os("google.com")

    print("===== ping3 ====")
    ping_ping3("google.com")