#!/usr/bin/env python3

#Author: Rich Stanton
#Author email: njr5@cdc.gov
#super incredibly minor modifications by: Rachael St. Jacques
#simm email: rachael.stjacques@dgs.virginia.gov
#description: selects optimal reference genome given a set of fasta files
#Requires: mash
#Usage: python centroid.py Path_to_assemblies

import sys
import glob
import numpy
import operator
from operator import itemgetter
import subprocess

def Mash_List(Mash_Index):
    """Takes in an index of Mash files and makes a list of the info from each"""
    List1 = glob.glob(Mash_Index)
    Combined = []
    for files in List1:
        f = open(files, 'r')
        String1 = f.readline()
        Combined.append(String1)
        f.close()
    Combined.sort()
    return Combined

def Average_Mash(input_mash_list):
    """Takes in a Mash_List (made using Mash_List) and then makes a list with the average value for each entry"""
    Average_List = []
    List1 = input_mash_list[0].split('\t'.encode())
    Entry = List1[0]
    values = []
    for entries in input_mash_list:
        List1 = entries.split('\t'.encode())
        if List1[0] != Entry:
            average = numpy.mean(values)
            Total = []
            Total.append(Entry)
            Total.append(average)
            Average_List.append(Total)
            Entry = List1[0]
            values = []
            values.append(float(List1[2]))
        else:
            values.append(float(List1[2]))
    average = numpy.mean(values)
    Total = []
    Total.append(Entry)
    Total.append(average)
    Average_List.append(Total)
    Average_List.sort(key=operator.itemgetter(1))
    return Average_List

def Mash_List_Maker(input_assembly_list):
    """Makes a list of the all x all mash outputs"""
    Output = []
    for files in input_assembly_list:
        for files2 in input_assembly_list:
            String1 = subprocess.check_output('mash dist ' + files + ' ' + files2, shell=True)
            Output.append(String1)
    Output.sort()
    return Output

def Mash_Centroid(input_assembly_list):
    """Returns the name of the fasta with the lowest average mash index"""
    List1 = Mash_List_Maker(input_assembly_list)
    Averages = Average_Mash(List1)
    Best = Averages[0][0]
    return Best

Folder = sys.argv[1]
Assembly_List = glob.glob(Folder + '/*.fasta')
Centroid = Mash_Centroid(Assembly_List)
print(Centroid)
print(Centroid, file=open("centroid_out.txt", "w"))
