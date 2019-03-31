# This small program in Python is developed by Victor Mitra on 08-03-2019 to show the status of different components of the current system.

# Importing necessary modules

import psutil
import datetime
from psutil import disk_partitions
from psutil import net_io_counters
from os import system, name

# Definition of all the functions

# This is the main menu which offers 7 choices and is the main entry point to the program

def MainMenu():
    clear()
    print('\n\n      Main menu     \n\n\n')
    print('1. Disk partition info\n')
    print('2. Disk usage info\n')
    print('3. Disk I/O info\n')
    print('4. CPU info\n')
    print('5. Network info\n')
    print('6. Memory usage info\n')
    print('7. System and user info\n\n')
    x = input('Enter your choice: ')
    clear()
    if x == 1:
        diskinfo()
    if x == 2:
        duinfo()
    if x == 3:
        dcoinfo()
    if x == 4:
        cpuinfo()
    if x == 5:
        netwinfo()
    if x == 6:
        meminfo()
    if x == 7:
        sysinfo()
    if x>7 or x<1:
        print('Invalid choice.')
    
# This function clears the screen by issuing the correct command based on the OS

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


# This function shows the disc info

def diskinfo():
    print '\n\n########## Displaying disk partition information ###############\n\n'
    for i, disk in enumerate(disk_partitions()):
       print 'Details of Disk #{0:d} {1:s}:'.format(i, disk.device)
       print ' Mount Point: {0:s}'.format(disk.mountpoint)
       print ' File System: {0:s}\n'.format(disk.fstype)
       

# This function shows the disk usage info

def duinfo():
    print '\n\n########## Displaying disk usage information #############\n\n'
    dustat=psutil.disk_usage('/')
    print ('Total space: {} GB'.format(dustat[0]/1024/1024/1024))
    print ('Used space: {} GB'.format(dustat[1]/1024/1024/1024))
    print ('Free space: {} GB'.format(dustat[2]/1024/1024/1024))
    print ('Percentage: {}'.format(dustat[3]) + '%\n')


# This function shows the disk i/o counters

def dcoinfo():
    print '\n\n############ Displaying disk I/0 counters information ##############\n\n'
    dcostat=psutil.disk_io_counters(perdisk=False, nowrap=True)
    print ('Read count: {}'.format(dcostat[0]))
    print ('Write count: {}'.format(dcostat[1]))
    print ('Bytes read: {}'.format(dcostat[2]))
    print ('Bytes written: {}\n'.format(dcostat[3]))


# This function shows the CPU info

def cpuinfo():
    print '\n\n########## Displaying CPU information ###############\n\n'
    print ('CPU count: {}\n'.format(psutil.cpu_count()))
    cpu=psutil.cpu_stats()
    print ('Number of context switches: {}'.format(cpu[0]))
    print ('Number of interrupts since boot: {}'.format(cpu[1]))
    print ('Number of software interrupts since boot: {}'.format(cpu[2]))
    print ('Number of system calls since boot: {}\n'.format(cpu[3]))


# This function shows the network info

def netwinfo():
    print '\n\n######### Displaying network information ##############\n\n'
    netstat=psutil.net_io_counters(pernic=False, nowrap=True)
    print ('Bytes sent: {}'.format(netstat[0]))
    print ('Bytes received: {}'.format(netstat[1]))
    print ('Packets sent: {}'.format(netstat[2]))
    print ('Error-in: {}'.format(netstat[3]))
    print ('Error-out: {}'.format(netstat[4]))
    print ('Drop-in: {}'.format(netstat[5]))
    print ('Drop-out: {}\n'.format(netstat[6]))
    

# This function shows the memory info

def meminfo():
    print '\n\n########## Displaying Memory usage information ###############\n\n'
    memstat=psutil.virtual_memory()
    print ('Total memory: {} MB'.format(memstat[0]/1024/1024))
    print ('Available memory: {} MB'.format(memstat[1]/1024/1024))
    print ('Percentage: {}'.format(memstat[2]) + '%')
    print ('Used memory: {} MB'.format(memstat[3]/1024/1024))
    print ('Free memory: {} MB'.format(memstat[4]/1024/1024))
    print ('Active memory: {} MB'.format(memstat[5]/1024/1024))
    print ('Inactive memory: {} MB'.format(memstat[6]/1024/1024))
    print ('Wired memory: {} MB\n'.format(memstat[7]/1024/1024))       
   

# This function shows the system and user info

def sysinfo():
    print '\n\n######## Displaying system and user information #########\n\n'
    print ('System is running since: {}\n'.format(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")))
    a=1
    for x in psutil.users():
        print ('Displaying details of user {}\n'.format(a))
        print ('Terminal: {}'.format(x[1]))
        print ('Host: {}'.format(x[2]))
        print (datetime.datetime.fromtimestamp(x[3]).strftime("%Y-%m-%d %H:%M:%S"))
        print ('Process ID: {}'.format(x[4]))
        a+=1
        print ('\n')


# The main menu is called

MainMenu()
        
    





    


      
    







