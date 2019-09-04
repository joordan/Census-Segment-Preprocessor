# prompt user for file name

filename = raw_input("Enter file name: ")
if len(filename) < 1 : exit

# concatenate mod to file name
idx = filename.index(".")
outputname = filename[:idx] + "mod" + filename[idx:]

# open files for read/write
inputfile = open(filename)                    
outputfile = open(outputname,"w+")            

for line in inputfile:

	row = line.split(',')
	firstFour = []
	firstFour.append(row[0])
	firstFour.append(row[1])
	firstFour.append(row[2])
	firstFour.append(row[3])

	replaceThis = ",".join(firstFour)

	line = line.replace(replaceThis,"")
	outputfile.write(line)
