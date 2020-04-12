from colorama import Fore, init;import threading, os, platform;from queue import Queue;import tkinter;from tkinter import filedialog;from tkinter import messagebox;import time, string, subprocess, requests, random, ctypes, webbrowser;import pypresence;from pypresence import Presence
now = time.time()
init()
root = tkinter.Tk()
root.withdraw()
views = 0
errors = 0
version = '1.0'
RED = Fore.LIGHTRED_EX
WHITE = Fore.LIGHTWHITE_EX
logo = f"""

{WHITE}  ____    ____  ______    __    __ {RED} .___________. __    __  .______    _______ 
{WHITE}  \   \  /   / /  __  \  |  |  |  |{RED} |           ||  |  |  | |   _  \  |   ____|
{WHITE}   \   \/   / |  |  |  | |  |  |  |{RED} `---|  |----`|  |  |  | |  |_)  | |  |__   
{WHITE}    \_    _/  |  |  |  | |  |  |  |{RED}     |  |     |  |  |  | |   _  <  |   __|  
{WHITE}      |  |    |  `--'  | |  `--'  |{RED}     |  |     |  `--'  | |  |_)  | |  |____ 
{WHITE}      |__|     \______/   \______/ {RED}     |__|      \______/  |______/  |_______|
                                                                              
                                           {WHITE} Made by 0x72 (version: {version})

"""

def logo_print():
    print(f"{logo}")
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')
def update_title(new_title):
    ctypes.windll.kernel32.SetConsoleTitleW(f'{new_title}')

err = False
client_id = '696453816609931385'
RPC = Presence(client_id=client_id)
try:
    RPC.connect()
    RPC.update(large_image='logo', large_text='Made by 0x72',details='Main Menu', start=now)
except (pypresence.InvalidPipe, pypresence.InvalidID, pypresence.PyPresenceException):
    err = True
clear()
update_title('Youtube Livestream View Bot | Made by 0x72')
logo_print()
print(f"{RED} [{WHITE}YOUTUBE{RED}]{WHITE} https://github.com/robert169/\n")
print(f"{RED} [{WHITE}1{RED}]{WHITE} Livestream View Bot")
print(f"{RED} [{WHITE}2{RED}]{WHITE} Download Proxies")
print(f"{RED} [{WHITE}3{RED}]{WHITE} Discord")
try:menu_choose = int(input(f"{RED}\n [{WHITE}?{RED}]{WHITE} "))
except:os._exit(0)


def get_Session(proxies):
    api_sender = requests.session()
    prxi = proxies.split(":")
    if len(prxi) == 2:
        api_sender.proxies = {"https": proxies}
        
        return api_sender
    elif len(prxi) == 4:
        api_sender.proxies = {"https": f"http://{prxi[2]}:{prxi[3]}@{prxi[0]}:{prxi[1]}"}
        return api_sender
    else:
        api_sender = "broken"
        return api_sender
def GetProxies():
    
    file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file (http/s)',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if file is not None:
        try:
            loadedFile = open(file.name).readlines()
            arrange = [lines.replace("\n", "") for lines in loadedFile]
        except ValueError:
            try:
                loadedFilee = open(file.name, encoding="utf-8", errors='ignore').readlines()
                arrange1 = [lines.replace("\n", "") for lines in loadedFilee]
            except ValueError:
                print(WHITE + "Cannot open file, Unsupported encoding.")
            else:
                return arrange1
        else:
            return arrange
    else:
        os._exit(0)
if menu_choose == 3:discord_link = requests.get('https://robert832.me/discord').text;os.system(f'start {discord_link}');os._exit(0)
elif menu_choose == 2:proxy_link1 = "https://proxyscrape.com/free-proxy-list";proxy_link2 = "https://advanced.name/freeproxy";os.system(f'start {proxy_link1} | start {proxy_link2}');os._exit(0)
elif menu_choose == 1:
    clear();logo_print()
    try:
        RPC.update(large_image='logo', large_text='Made by 0x72',details='Selecting Stream ID', start=now)
    except:
        pass
    update_title('Youtube Livestream View Bot | Select Stream ID | Made by 0x72')
    print(f"{RED}\n [?]{WHITE} Stream ID:", end=' ')
    id_stream = str(input('')).replace('\n', '').replace(' ', '').strip()
    if len(id_stream) < 5:print('Invalid Stream ID');time.sleep(2);os._exit(0)
    else:pass
    try:
        RPC.update(large_image='logo', large_text='Made by 0x72',details='Selecting Threads', start=now)
    except:
        pass
    update_title('Youtube Livestream View Bot | Select Threads | Made by 0x72')
    print(f"{RED}\n [?]{WHITE} Threads:", end=' ')
    try:treduri = int(input(''))
    except:print('Threads must be only int!');time.sleep(2);os._exit(0)
    try:
        RPC.update(large_image='logo',large_text='Made by 0x72', details='Selecting Proxy File', start=now)
    except:
        pass
    update_title('Youtube Livestream View Bot | Select Proxy File | Made by 0x72')
    print(f"{RED}\n [?]{WHITE} Select proxy file (http/s only)")
    proxies = GetProxies()
    try:
        RPC.update(large_image='logo', large_text='Made by 0x72',details='Sending Views', start=now)
    except:
        pass
    update_title('Youtube Livestream View Bot | Sending Views | Made by 0x72')
    print(f"{RED}\n [*]{WHITE} Sending views (wait a few minutes to load proxies)")
    time.sleep(2)
else:os._exit(0)


def discord_rich():
    if err == False:
        try:
            RPC.update(large_image='logo', large_text='Made by 0x72', details=f"Views: {views}", start=now)
        except:
            pass
 
        time.sleep(1)
        threading.Thread(target=discord_rich, args=()).start()

def ecran():
    while 1:
        update_title(f'YouTube Livestream View Bot | Views: {views} | Errors: {errors} | Made by 0x72')
        time.sleep(3)
def send_views():
    global views, errors
    while 1:
        try:
            sess = get_Session(random.choice(proxies))
            headers={'Host':'m.youtube.com',  'Proxy-Connection':'keep-alive',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',  'Accept-Encoding':'gzip, deflate'}
            resp = sess.get(f'https://m.youtube.com/watch?v={id_stream}', headers=headers)
            raspuns = resp.text.split('videostatsWatchtimeUrl\\":{\\"baseUrl\\":\\"')[1].split('\\"}')[0].replace('\\\\u0026', '&').replace('%2C', ',').replace('\\/', '/')
            cl = raspuns.split('cl=')[1].split('&')[0];ei = raspuns.split('ei=')[1].split('&')[0];of = raspuns.split('of=')[1].split('&')[0];vm = raspuns.split('vm=')[1].split('&')[0]
            headers={'Host':'s.youtube.com',  'Proxy-Connection':'keep-alive',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',  'Accept':'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',  'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',  'Referer':f'https://m.youtube.com/watch?v={id_stream}'}
            sess.get(f'https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid={id_stream}&ver=2&cmt=7334&ei={ei}&fmt=133&fs=0&rt=1003&of={of}&euri&lact=4418&live=dvr&cl={cl}&state=playing&vm={vm}&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634', headers=headers)
            views += 1;time.sleep(15)
        except:errors+=1
try:
    discord_rich()
    threading.Thread(target=(ecran), args=[]).start()
except KeyboardInterrupt:
    print('\nBye');time.sleep(2);os._exit(0)
except Exception as e:
    input(f'Something went wrong: {e}')
    os._exit(0)
if __name__ == "__main__":
    num = 0
    while 1:
        time.sleep(15)
        if num < treduri:
            num += 1
            try:threading.Thread(target=send_views).start()
            except KeyboardInterrupt:print('\nBye');time.sleep(2);os._exit(0)
            except: pass
