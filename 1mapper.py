import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 3) : 
    name,year,count = datalist

    # print intermediate key-value pairs to standard output
    print(name,"\t",count)