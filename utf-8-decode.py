import colorama
from colorama import Fore, Back
import pyperclip as pc
from os import system

colorama.init()

inCmds = ["sudo apt-get install xsel"]

def colorPrint(color, text):
	print(color+text+Fore.RESET+Back.RESET)

colorPrint(Fore.GREEN ,"[+] Decode Began!")
code = input("Enter the code: ")
colorPrint(Fore.BLUE, f"[*] Your code: {code}")
colorPrint(Fore.BLUE, "[*] Splitting the code into pieces...")

count = 0
txts = []
txt = ""
for i in code:
	count += 1
	txt += i
	if count >= 2:
		txts.append(txt)
		txt = ""
		count = 0

colorPrint(Fore.YELLOW, f'[-] For debugging: {txts}')
newCode = b''.fromhex(code).decode('utf-8')
colorPrint(Fore.GREEN, f'[+] Your Code: {Fore.RED}{newCode}')
answer = input(Fore.YELLOW+"Do you want to copy to the clipboard?[Y/n] (default 'n'): "+Fore.RESET).lower()
if not answer in ["y", "n"]:
	answer = "n"
try:
	if answer == "y":
		pc.copy(newCode)
		colorPrint(Fore.GREEN,"[+] Successfully copied to the clipboard.")
except pc.PyperclipException:
	colorPrint(Fore.RED, "[Error] No clipboard mechanisme found on your machine!")
	colorPrint(Fore.BLUE, f"[*] You can try to download one for example via {Back.WHITE}{Fore.BLACK} apt-get install xsel ")
	colorPrint(Fore.GREEN, f'[+] Take a choice: ')
	for i in range(len(inCmds)):
		print(f'\t{i+1}) {inCmds[i]}')

	print(f'\t{len(inCmds)}) Not Now!')

	choice = int(input(Fore.BLUE+"So: "))

	if choice-1 in range(len(inCmds)):
		system(inCmds.choice)