import eel

from datetime import datetime

#it will fetch the information about the host computer
import platform
import psutil

#initializing eel
#pass in the directory where all the html css and javascript files are stored
eel.init("front_end")

#getting system info using platform class in python
@eel.expose
def generate_system_data():
    #calculating bytes into MB GB and TB
    def storage_size_utility(size, initialis="B"):
        factor = 1024
        for memory_unit in ["", "k", "M", "G", "T"]:
            if size < factor:
                return (f"{size:.2f}{memory_unit}{initialis}")
            size/=factor
    sysname = platform.uname()
    data = {}
    data.update({"OS type :-":sysname.system})
    data.update({"System name :-": sysname.node})
    data.update({"OS release :-": sysname.release})
    data.update({"OS version :-": sysname.version})
    data.update({"Machine :-": sysname.machine})
    data.update({"Processor type :-": sysname.processor})
    #hard disk info
    partition_info = psutil.disk_partitions()
    mounted_drive_infoIfor_linux_only = partition_info[0]
    try:
        drive_size = psutil.disk_usage(mounted_drive_infoIfor_linux_only.mountpoint)
        print(drive_size)
    except:
        pass
    #getting the boot directory drive
    data.update({"Drive name:-":mounted_drive_infoIfor_linux_only.mountpoint})
    #getting the type of file system used by the os
    data.update({"File System Used By OS:-":str(mounted_drive_infoIfor_linux_only.fstype)})
    #total hdd size
    data.update({"Drive size:-": storage_size_utility(drive_size.total)})
    #free hdd space
    data.update({"Drive free space:-": storage_size_utility(drive_size.free)})
    #used hdd space
    data.update({"Drive used space:-": storage_size_utility(drive_size.used)})

    #used space in percentage
    data.update({"Drive Space used in percentage":str(drive_size.percent)+"%"})

    #ram usage info
    memory_info = psutil.virtual_memory()
    #total ram installed on the system
    data.update({"Total Ram installed:-": storage_size_utility(memory_info.total)})
    #amount of ram free in the system
    data.update({"Free Ram:-": storage_size_utility(memory_info.available)})

    #amount of ram used
    data.update({"Total Ram usage:-": storage_size_utility(memory_info.used)})

    #ram usage in percentage
    data.update({"Ram usage in percentage:-": str(memory_info.percent)+"%"})
    return data

#here pass the starter html file
#here we can pass the window size
eel.start("systeminfo.html",size=(800,600))