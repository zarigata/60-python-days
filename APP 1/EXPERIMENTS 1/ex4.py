filenames = ["1.rawdata.txt", "2.Reports.txt" , "3.Presentatios"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)