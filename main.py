import threading, requests

link = input("Vinted link: ")
lock = threading.Lock()
threads = int(input("Threads: "))
ctr = 0

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global ctr
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
    r = requests.get(link, headers = headers)
    if r.status_code == 200:
        ctr += 1
        safe_print("Views  +1 (Total: {}".format(ctr) + ")")
    else:
        safe_print("Error")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
        except:
            pass