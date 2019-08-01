import commands
import psutil

f=open('Information_Server.txt','a+')

logical_cpu= psutil.cpu_count()
harddatat = commands.getoutput("system_profiler SPHardwareDataType | grep Processors")
physical_cpu=psutil.cpu_count(logical=False)
avaliable_cpu= psutil.cpu_times()
frequency_cpu = psutil.cpu_freq()

#use the later command to get the information of cpu
#CPU_specifications = commands.getoutput("sysctl -n machdep.cpu.brand_string")
CPU_specifications = commands.getoutput("cat /proc/cpuinfo")
f.write('\n'+'cpu_specification : '+str(CPU_specifications)+'\n')

f.write('\n'+'logical_cpu : '+str(logical_cpu)+'\n')
f.write('\n'+'harddatat : '+str(harddatat)+'\n')
f.write('\n'+'physical_cpu : '+str(physical_cpu)+'\n')
f.write('\n'+'avaliable_cpu : '+str(avaliable_cpu)+'\n')
f.write('\n'+'frequency_cpu : '+str(frequency_cpu)+'\n')

#SPMemoryDataType = commands.getoutput("system_profiler SPMemoryDataType")
SPMemoryDataType = commands.getoutput("cat /proc/meminfo")
f.write('\n'+'SPMemoryDataType : '+str(SPMemoryDataType)+'\n')



f.close()
