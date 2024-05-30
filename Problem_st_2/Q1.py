import os
import psutil
import logging

logging.basicConfig(filename='systemHealth.log',level=logging.WARNING)
 
 
# script will log alerts to a file named 'systemHealth.log'

THRESHOLD_CPU=80
THRESHOLD_MEMORY=80
THRESHOLD_DISK=80

def check_cpu_usage():
    cpu_usage=psutil.cpu_percent()
    if cpu_usage > THRESHOLD_CPU:
        logging.warning(f'CPU usage is high:{cpu_usage}%')
    else:
        print(f'CPU usage is normal: {cpu_usage}%')
        
def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > THRESHOLD_MEMORY:
        logging.warning(f'Memory usage is high: {memory_usage}%')
    else:
        print(f'Memory usage is normal: {memory_usage}%')

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > THRESHOLD_DISK:
        logging.warning(f'Disk usage is high: {disk_usage}%')
    else:
        print(f'Disk usage is normal: {disk_usage}%')

def check_processes():
    num_processes = len(psutil.pids())
    if num_processes > 50:  
        logging.warning(f'Number of running processes is high: {num_processes}')
    else:
        print(f'Number of running processes is normal: {num_processes}')

check_cpu_usage()
check_memory_usage()
check_disk_usage()
check_processes()

