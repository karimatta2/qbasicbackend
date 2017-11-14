#!/usr/bin/env python
import argparse

def main():
    #argument parsing so that the program can be run from the command line
    p = argparse.ArgumentParser()
    p.add_argument('masterAccountFile')
    p.add_argument('transactionFiles',type=file, nargs='+')
    args = p.parse_args()
    master = args.masterAccountFile
    masterAccList = masterList()
    
    #************************************************************
    #to merge all transaction files into one file
    merged = open("merged.txt", "w")
    for tFile in args.transactionFiles:
        line = tFile.readline()
        while line:
            if line != "EOS 0000000 000 0000000 ***"+"\n":
                merged.write(line)
            line = tFile.readline()
    merged.close()

    #function call to make the merged.txt file into a list to be easier to alter 
    transactionsList = mergeTransactions()
    #*************************************************************
    
    '''
    #for backend NEW DEL testing
    #transList = ["NEW 1000004 0000 Name", "DEL 1000002 00000 Name"]
    #masterFile = ["1000003 10000 Name", "1000002 10000 Name", "1000001 10000 Name", "000000 0000 ****"]
   
    print("\nOriginal transaction list:")
    print(transList)   
    print("\nOld master file:")
    print(masterFile)   
    backend(transactionsList, masterAccList)
    print("\n\nNew transaction list:")
    print(transList)   
    print("\nNew master file:")
    print(masterFile)
    '''
    #newMaster = backend(t, masterAcc)
    #createAccListFile(newMaster)

def masterList():
    lis = []
    with open("masterAccountFile.txt") as openfile:
        for line in openfile:
            line = line.rstrip("\n")
            lis.append(line)
        
    return lis

def mergeTransactions():
    #takes a long transaction file and makes it a list
    transactionsList = []
    with open("merged.txt", "r") as openfile:
        for line in openfile.readlines():
            line = line.rstrip('\n')
            transactionsList.append(line)
        
    return transactionsList





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

            
  def deposit(transaction, masterAcc):
    accNum = transaction.split(' ')[1]
    for i in range(0,len(masterAcc)-1):
        number = masterAcc[i].split(' ')[0]
        if accNum == number:
            balance = int(masterAcc[i].split(' ')[1])
            dep = int(transaction.split(' ')[2])
            balance += dep
            
            masterAcc[i] = masterAcc[i].replace(masterAcc[i].split(' ')[1], str(balance))
            return masterAcc
        else:
            continue
    return masterAcc



def withdraw(transaction, masterAcc):
    accNum = transaction.split(' ')[1]
    for i in range(0,len(masterAcc)-1):
        number = masterAcc[i].split(' ')[0]
        if accNum == number:
            balance = int(masterAcc[i].split(' ')[1])
            withD = int(transaction.split(' ')[2])
            balance -= withD

            masterAcc[i] = masterAcc[i].replace(masterAcc[i].split(' ')[1], str(balance))

            return masterAcc
    return masterAcc
        

def transfer(transaction, masterAcc):
    toAcc = transaction.split(' ')[1]
    fromAcc = transaction.split(' ')[3]
    for i in range(0,len(masterAcc)-1):
   
        number = masterAcc[i].split(' ')[0]
        if toAcc == number:
            balance = int(masterAcc[i].split(' ')[1])
            dep = int(transaction.split(' ')[2])
            balance += dep
            masterAcc[i]= masterAcc[i].replace(masterAcc[i].split(' ')[1], str(balance))
            
        
        elif fromAcc == number:
            balance = int(masterAcc[i].split(' ')[1])
            withD = int(transaction.split(' ')[2])
            balance -= withD
            masterAcc[i] = masterAcc[i].replace(masterAcc[i].split(' ')[1], str(balance))
            
        else:
            continue
    return masterAcc
            
            
def createAccountListFile():
    #takes a master accounts file and loops through it to find all valid account numbers to create a list of them (returns in file format)
    lineList = []
    masterAccounts = open('masteraccounts.txt','r')
    
    for line in masterAccounts:
        lineList.append(line.split()[0])

    with open('validaccountlist.txt','w') as accList:
        for line in lineList:
            accList.write(line + '\n')
    return


main()
