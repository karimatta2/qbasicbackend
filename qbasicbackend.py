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

main()

def mergeTransactions():

    return
