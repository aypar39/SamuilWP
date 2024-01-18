import requests
import re
import os
from colorama import Fore, Style

banner = f"""
{Fore.RED}  .-')     ('-.     _   .-'){Style.RESET_ALL}                                  
{Fore.RED} ( OO ).  ( OO ).-.( '.( OO )_{Style.RESET_ALL}                                
{Fore.RED}(_)---\_) / . --. / ,--.   ,--.),--. ,--.    ,-.-'){Style.RESET_ALL}  ,--.      
{Fore.RED}/    _ |  | \-.  \\  |   `.'   | |  | |  |    |  |OO){Style.RESET_ALL} |  |.-')  
{Fore.RED}\\  :` `..-'-'  |  | |         | |  | | .-')  |  |  \\{Style.RESET_ALL} |  | OO ) 
{Fore.RED} '..`''.)\| |_.'  | |  |'.'|  | |  |_|( OO ) |  |(_/{Style.RESET_ALL} |  |`-' | 
{Fore.RED}.-._)   \\ |  .-.  | |  |   |  | |  | | `-' /,|  |.'{Style.RESET_ALL}(|  '---.' 
{Fore.RED}\\       / |  | |  | |  |   |  |('  '-'(_.-'(_|  |   {Style.RESET_ALL}|      |  
{Fore.RED} `-----'  `--' `--' `--'   `--'  `-----'     `--'{Style.RESET_ALL}    `------'  
   X-CLASS -> Warband
     [1]Warband IP addresses of All Servers(Active and Unactive)
     [2]Checker IP
     [0]Exit
"""
os.system("cls||clear")
print(Fore.LIGHTMAGENTA_EX+ banner)


def check_ip(ip_address, port):
    try:
        response = requests.get(f'http://{ip_address}:{port}', timeout=5)
        if response.status_code == 200:
            content = response.text
            # <Name> etiketleri içindeki metni bulma
            name_pattern = r'<Name>(.*?)</Name>'
            names = re.findall(name_pattern, content, re.DOTALL)
            module_pattern= r'<ModuleName>(.*?)</ModuleName>'
            modules = re.findall(module_pattern, content, re.DOTALL)
            
            
            for name in names:
                print(f'Server Name: {name}')
            for module in modules:
                print(f'Module Name: {module}')
            
            return True
        else:
            return False
    except requests.RequestException:
        return False

while True:
    ask = str(input(Fore.WHITE + "=>"))

    if ask == "1":
        print("Starting")
        url = 'https://warbandmain.taleworlds.com/handlerservers.ashx?type=list'
        response = requests.get(url)

        if response.status_code == 200:
            content = response.text
            ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b', content)
        
            for ip_port in ip_addresses:
                ip, port = ip_port.split(':') 
                if check_ip(ip, port):
                    print(f'{ip}:{port} Server Active')
                    with open('servers.txt', 'a') as file:
                        file.write(f'http://{ip}:{port} Active Info Saved -> Servers.txt\n')
                else:
                    print(f"{Fore.RED}{ip}:{port} not active {Style.RESET_ALL}")  
        else:
            print('Failed to Receive Data')
    elif ask == "2":
        c_ip = str(input("IP:"))
        c_port = str(input("PORT:"))
        if check_ip(c_ip, c_port):
            print(f"{Fore.GREEN}Live {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Dead {Style.RESET_ALL}")
    else:
        print("Invalid input")
