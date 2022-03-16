file_list1=['output.txt']
file_list2=['out.txt']
import re
for file1 in file_list1:
   for file2 in file_list2:
       file1=open(file1,'r')
       file2=open(file2,'w')
       for line in file1.readlines():
           x=re.findall("^#", line)
           if not x:
              if not "not counted" in line:
                file2.write(line)

file1.close()
file2.close()
import pandas as pd
data = pd.read_table('out.txt', sep='\s+', header=None, thousands=',', comment='#', names=['time','count','event'])
data=data.pivot(index=time, columns=event, values=count)
data.to_csv('output.csv',index=False)

