import psutil
import time
import subprocess
from os import system
import platform
from datetime import datetime
import slack_integration   # imported slack integration code 



def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def cpu_Monitor():
	print("="*40, "CPU Monitoring", "="*40)
	print("CPU Usage: "+str(psutil.cpu_percent()))
	if psutil.cpu_percent() > 80:
		print("Reached CPU threashold ! sending notification..........")
		slack_integration.post_message_to_slack("CPU reached maximum threashold","CPU_ALERT","https://cdn1.iconfinder.com/data/icons/tech-multimedia-2/64/CPU-hot_proc_PC_wet_burn-512.png")
	
	"""
	Per CPU
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
		print(f"	Core {i}: {percentage}%")
		print(f"	Total CPU Usage: {psutil.cpu_percent()}%")
		if psutil.cpu_percent() > 80:
			slack_integration.post_message_to_slack("CPU reached maximum threashold","CPU_ALERT")
	"""
def memory_Monitor():
	print("="*40, "Memory Information", "="*40)
	# get the memory details
	svmem = psutil.virtual_memory()
	print(f"	Total: {get_size(svmem.total)}")
	print(f"	Available: {get_size(svmem.available)}")
	print(f"	Used: {get_size(svmem.used)}")
	print(f"	Percentage: {svmem.percent}%")
	if svmem.percent > 50:
		print("Reached RAM threashold ! sending notification..........")
		slack_integration.post_message_to_slack("RAM reached maximum threashold ","RAM_ALERT","https://www.freeiconspng.com/uploads/ram-icon-png-11.png")

def disk_Monitor():
	# Disk Information
	print("="*40, "Disk Information -root (/) ", "="*40)
	partition_usage = psutil.disk_usage("/")
	print(f"	Total Size: {get_size(partition_usage.total)}")
	print(f"	Used: {get_size(partition_usage.used)}")
	print(f"  	Free: {get_size(partition_usage.free)}")
	print(f"  	Percentage: {partition_usage.percent}%")
	if partition_usage.percent > 90:
		print("Reached DISK threashold ! sending notification..........")
		slack_integration.post_message_to_slack("Disk reached maximum threashold ","Disk_ALERT","https://cdn1.iconfinder.com/data/icons/storage-data-6/24/storage_drive_disk_compact_alert_1-512.png")

def network_Monitor(url):
	print("="*40, "Network Latency for : "+ url + "="*40)
	
	network_lags= subprocess.getoutput('ping ' + url + ' -i 1  -c 5 | tail -1| cut -d"=" -f2').split('/')
	# i= interval  c= count  first tail -1 last line , cut= last output. cut
	print(f"	Min={network_lags[0]} ms")
	print(f"	Avg={network_lags[1]} ms")
	print(f"	Max={network_lags[2]} ms")


while(1):
	cpu_Monitor()
	memory_Monitor()
	disk_Monitor()
	network_Monitor('talentica-all.com')
	
	#slack_integration.post_message_to_slack("CPU reached maximum threashold Rohit_test")
	
