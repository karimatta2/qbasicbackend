#!/usr/bin/env python
import argparse
def main():
    t = mergeTransactions()
    newMaster = backend(t, masterAcc)
    createAccListFile(newMaster)

main()
