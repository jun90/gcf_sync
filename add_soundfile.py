ORGGCFPath = r"C:\Users\tianjun_Zhou\Documents\automationTest\smoke_test\ENG_analysis\origin\110365.gcf"
rstGCFPath = r"C:\Users\tianjun_Zhou\Documents\automationTest\smoke_test\ENG_analysis\result\110365.gcf"

orgGCF = open(ORGGCFPath)
orglines = orgGCF.readlines()

rstGCF = open(rstGCFPath)
rstlines = rstGCF.readlines()

tc = 1
tc_index_list = []
for line in orglines:
#    if ("PRINT TEST %04d" % tc) in line:
    if ("TEST %04d" % tc) in line:
        tc += 1
        print orglines.index(line)
        tc_index_list.append(orglines.index(line))

tc = 1
for line in rstlines:
    if ("PRINT TEST %04d" % tc) in line:
        line_idx = rstlines.index(line)
        a =  tc_index_list[tc - 1]
        orglines[21]
#        print orglines[tc_index_list[tc - 1] + 1]
        rstlines.insert(line_idx + 1, orglines[tc_index_list[tc - 1] + 1])

        rstlines.insert(line_idx + 2, orglines[tc_index_list[tc - 1] + 2])
        rstlines.insert(line_idx + 3, orglines[tc_index_list[tc - 1] + 3])

#write an output here
optGCFPath = r"C:\Users\tianjun_Zhou\Documents\automationTest\smoke_test\ENG_analysis\110365.gcf"
f = open(optGCFPath, 'w')
for line in rstlines:
    f.write(line)

f.close()

#help doc from google
#list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#print "%02d" % 5