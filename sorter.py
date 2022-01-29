n = open("Thota_output.txt","r")  # open file, read-only
s = open("Thota_output2.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
