import psutil
import time
import subprocess
from os import system
import platform
from datetime import datetime
import slack_integration   # imported slack integration code 



def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def cpu_Monitor():
	if psutil.cpu_percent() > 80:
		slack_integration.post_message_to_slack("CPU reached maximum threashold","CPU_ALERT","https://cdn1.iconfinder.com/data/icons/tech-multimedia-2/64/CPU-hot_proc_PC_wet_burn-512.png")
def memory_Monitor():
	svmem = psutil.virtual_memory()
	if svmem.percent > 50:
		slack_integration.post_message_to_slack("RAM reached maximum threashold ","RAM_ALERT","https://www.freeiconspng.com/uploads/ram-icon-png-11.png")

def disk_Monitor():
	# Disk Information
	partition_usage = psutil.disk_usage("/")
	if partition_usage.percent > 10:
		slack_integration.post_message_to_slack("Disk reached maximum threashold ","Disk_ALERT","https://cdn1.iconfinder.com/data/icons/storage-data-6/24/storage_drive_disk_compact_alert_1-512.png")

def network_Monitor(url):
	network_lags= subprocess.getoutput('ping ' + url + ' -i 1  -c 5 | tail -1| cut -d"=" -f2').split('/')
	# i= interval  c= count  first tail -1 last line , cut= last output. cut


while(1):
	cpu_Monitor()
	memory_Monitor()
	disk_Monitor()
	network_Monitor('facebook.com')
	
	
