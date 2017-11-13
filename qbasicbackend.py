#!/usr/bin/env python
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('masterAccountFile')
    p.add_argument('transactionFiles',type=file, nargs='+')
    args = p.parse_args()
    master = args.masterAccountFile
    merged = open("merged.txt", "w")
    for tFile in args.transactionFiles:
        line = tFile.readline()
        while line:
            if line != "EOS 0000000 000 0000000 ***"+"\n":
                merged.write(line)
            line = tFile.readline()
    merged.close()

    mergeTransactions(merged)
    '''
    print("\n")
    print(master)
    print("\n")
    print(transactions)
    print("\n")
    print(vars(args))
    '''
    #mergeTransactions(transactions)
    #newMaster = backend(t, masterAcc)
    #createAccListFile(newMaster)

def mergeTransactions(file):
    #takes a long transaction file and makes it a list





main()