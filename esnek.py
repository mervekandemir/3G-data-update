#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mervekandemir'

import csv
import itertools as it
import sys
komut_secenekleri=['get','lget']
def check_log():
    i=0
    while i!=1:
        name = raw_input("Log komutunu giriniz (get ya da lget): ")
        if name in komut_secenekleri:
            #print name
            i=1
            return name
            print "Check again!"


def logut(username):
    sfile = open("sahalar.txt","r")
    file1 = open("log_alRNC.txt","r+")
    file2 = open("log_alNODEB.txt","r+")
    file3 = open("log_alNODEB_sorted", "r+")
    for sline in sfile:
        pfile = open("parametreler.txt","r")
        for pline in pfile:
            splited = pline.strip().split(";")
            kfile = open("komutlar.txt","r")
            for kline in kfile:
                ksplited = kline.strip().split(";")
                if splited[0]==ksplited[1]:
                    if ksplited[0]=='Utrancell':
                        line = "%s %s=%s %s \n " % (name,ksplited[0],sline.strip(),ksplited[1])
                        print line
                        file1.write(line)
                    else:
                        line = "%s . %s \n " % (name,ksplited[1])
                        file2.write(line)
                        unique = set(file2.read().split("\n"))
                        file3.write("".join([line + "\n" for line in unique]))
                        print line


name=check_log()
logut(name)

komut_secenekleri=['rset','set']
def check():
    i=0
    while i!=1:
        name = raw_input("Parametre komutunu giriniz (set ya da rset) : ")
        if name in komut_secenekleri:
            return name
            print "Check again!"

def test(username):
    sfile = open("sahalar.txt","r")
    file1=open("RNC.txt","w")
    file2=open("NodeB.txt","r+")

    for sline in sfile:
        pfile = open("parametreler.txt","r")
        for pline in pfile:
            splited = pline.strip().split(";")
            kfile = open("komutlar.txt","r")

            for kline in kfile:
                ksplited = kline.strip().split(";")

                if splited[0]==ksplited[1]:
                    if ksplited[0]=='Utrancell':
                        line = "%s=%s %s %s %s \n " % (name,ksplited[0],sline.strip(),ksplited[1],splited[1])
                        print line
                        file1.write(line)
                    else:
                        line = "%s . %s %s \n " % (name,ksplited[1],splited[1])
                        file2.write(line)
                        print line


name=check()
test(name)


def tek(username):
    ufile = open("Unique.txt","r")
    for uline in ufile:
        pass




tek(name)