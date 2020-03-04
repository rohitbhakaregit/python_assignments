import psutil
import time
from os import system
import platform
from datetime import datetime
def  menu():
	print("="*40, "System Monitoring", "="*40)
	print("1. CPU and System load")
	print("2. Memoy usage")
	print("3. Disk Usage")
	print("4. Network latency")
	print("0. exit")

menu()

def cpu_monitor():
	print("="*40, "CPU Monitoring", "="*40)
	while(1):
		print("CPU Usage Per Core:")
		for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
			print(f"Core {i}: {percentage}%")
		print(f"Total CPU Usage: {psutil.cpu_percent()}%")
		time.sleep(2.4)
		system('clear')

def memory_monitor():
	print("for RAM")




def SwitchExample(argument):  # as python do not have swithch case I have use the dictionary
    switcher = {
        1: cpu_monitor(),
        2: memory_monitor(),
        3: " This is Case 3 ",
        4: " This is Case 4 ",
        0:   exit()
               }
    return switcher.get(argument, "nothing")

x = input("Enter your choice:")
print(SwitchExample(int(x)))

