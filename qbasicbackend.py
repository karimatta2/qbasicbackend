#!/usr/bin/env python
import argparse
def main():
    p = argparse.ArgumentParser()
    p.add_argument('masterAccountFile')
    p.add_argument('transactionFiles', nargs='+')
    args = p.parse_args()
    t = mergeTransactions()
    newMaster = backend(t, masterAcc)
    createAccListFile(newMaster)

def backend(transL, oldM):

    #loops through transList
    for i in range(0,len(transL)):

        if transL[i][0:3] == "DEL":
            #print("deleting at iteration: " + str(i))
            for j in range(0, len(oldM)):
                if oldM[j][0:7] == transL[i][4:11] and oldM[j][13:] == transL[i][17:]:
                    del oldM[j]
                    print("deleted!!")
                    break
        if transL[i][0:3] == "NEW":
            #print("creating at iteration: " + str(i))
            out = transL[i][4:11]+ " 0000 " + transL[i][17:]
            oldM.append(out)
            print("created!!")


def mergeTransactions():
    return


main()

'''
#for backend NEW DEL testing
transList = ["NEW 1000004 0000 Name", "DEL 1000002 00000 Name"]
masterFile = ["1000003 10000 Name", "1000002 10000 Name", "1000001 10000 Name", "000000 0000 ****"]
print("\nOriginal transaction list:")
print(transList)   
print("\nOld master file:")
print(masterFile)   
backend(transList, masterFile)
print("\n\nNew transaction list:")
print(transList)   
print("\nNew master file:")
print(masterFile)
'''
