# Facebook: Aditya Putra Mahesa
# Github: AdityaTwinz

try: ##-> Import Modules
    import os, sys, time, rich, platform, random
    import requests, fake_useragent
except ModuleNotFoundError as e:
    os.system('clear') ; sys.exit(f''' \x1b[0m[\33[0;31mError\x1b[0m] {str(e).title()}\n \x1b[0m[\33[0;31mError\x1b[0m] Module \33[0;31m{str(e.name)} \x1b[0mBelum Terinstall\n \x1b[0m[\33[0;31mError\x1b[0m] Silahkan Install Manual Ketik, pip install \x1b[1;92m{e.name}''')

try: ##-> Modules Shelter
    from fake_useragent import UserAgent
    from rich.console import Console
    from rich import print as prints
    from rich.panel import Panel
    from time import sleep
    from os import system
except ImportError as e:
    os.system('clear') ; sys.exit(f''' \x1b[0m[\33[0;31mError\x1b[0m] {str(e).title()}\n \x1b[0m[\33[0;31mError\x1b[0m] Kesalahan Pada \33[0;31m{str(e.name)} \x1b[0mSilahkan Periksa Lagi''')

##-> Server Caller
class Server:
   
   ##-> Init Self
   def __init__(self):
       self.ses = requests.Session()
       self.coki = self.ses.get('https://pastebin.com/raw/0EhUuWCv').text
       self.check()
   
   ##-> Colors Tools
   def Colors(self):
       try:
           self.colors = random.choice(
               [
                 "[bold green1]",
                 "[green1]",
                 "[deep_pink4]",
                 "[yellow1]",
                 "[bold yellow]",
                 "[bold red]",
                 "[red1]",
                 "[cyan1]",
                 "[bold cyan]"
               ]
               )
           return self.colors
       except Exception as e : pass
       
   ##-> Terminal Cleaner
   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system('clear')
       elif "win" in sys.platform.lower():os.system('cls')
   
   ##-> Logo Tools
   def Logoo(self):
       prints(Panel(f'''{self.Colors()}.▄▄ · ▄▄▄ .▄▄▄   ▌ ▐·▄▄▄ .▄▄▄  
▐█ ▀. ▀▄.▀·▀▄ █·▪█·█▌▀▄.▀·▀▄ █·
▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█▄▄▌▐█•█▌ ███ ▐█▄▄▌▐█•█▌
 ▀▀▀▀  ▀▀▀ .▀  ▀. ▀   ▀▀▀ .▀  ▀''',width=80,padding=(0,17),style=f"bold grey100"))

   ##-> Checking Server
   def check(self):
       self.clearTerminal(platform) ; self.Logoo()
       try:
           headers = {'authority': 'pastebin.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'no-cache','pragma': 'no-cache','referer': 'https://pastebin.com/E2fK013P','sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': UserAgent().safari}
           response = self.ses.get('https://pastebin.com/raw/E2fK013P', headers = headers, cookies = {"cookie":self.coki})
           if "active" not in response.text:
              prints(Panel(f'[yellow1]Sorry, the server is not active, please wait',width=80,padding=(0,12),style=f"bold grey100")) ; sleep(3) ; sys.exit()
           else:prints(Panel(f'[green1]Congratulations, your server is active have fun',subtitle="╭───", subtitle_align="left",width=80,padding=(0,10),style=f"bold grey100")) ; Console().input(f'[bold grey100]   ╰─> [ Click Enter ]') ; prints(Panel(f'{self.Colors()}{self.coki}',width=80,padding=(1,4),style=f"bold grey100"))
       except Exception as e:
           sleep(3) ; prints(Panel(f'[yellow1]Sorry, there was an error on the server',width=80,padding=(0,14),style=f"bold grey100")) ; sleep(3) ; sys.exit()
           

Server()