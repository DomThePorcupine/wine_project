import re
filer = open("data.js","w")
f = open('wine_data.csv','r')
# Write the beginning of the json file

first = True
airTemp = []
bb1Temp = []
bb2Temp = []
blueberryTemp = []
lbl = []

while True:
    ln = f.readline()
    ln = ln.rstrip()
    if not ln: break
    lbl.append(ln.split(",")[4])
    stf = re.findall( r'\d+\.*\d*', ln)

    airTemp.append(float(stf[0]))
    bb1Temp.append(float(stf[1]))
    bb2Temp.append(float(stf[2]))
    blueberryTemp.append(float(stf[3]))


filer.write("const dset = [\n")
filer.write("{\n")
filer.write("\tlabel: \"Air Temperature\",\n")
filer.write("\tborderColor: 'rgb(255, 99, 132)',\n")
filer.write("\tdata: " + str(airTemp) + ",\n")
filer.write("},\n")
filer.write("{\n")
filer.write("\tlabel: \"Blackberry 1\",\n")
filer.write("\tborderColor: 'rgb(0, 255, 0)',\n")
filer.write("\tdata: " + str(bb1Temp) + ",\n")
filer.write("},\n")
filer.write("{\n")
filer.write("\tlabel: \"Blackberry 2\",\n")
filer.write("\tborderColor: 'rgb(77, 0, 54)',\n")
filer.write("\tdata: " + str(bb2Temp) + ",\n")
filer.write("},\n")
filer.write("{\n")
filer.write("\tlabel: \"Blueberry\",\n")
filer.write("\tborderColor: 'rgb(0, 0, 255)',\n")
filer.write("\tdata: " + str(blueberryTemp) + ",\n")
filer.write("}\n")
filer.write("]\n")
filer.write("const lbls = " + str(lbl) + "\n")