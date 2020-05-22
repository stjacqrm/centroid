#!/usr/bin/env python3

#Author: Rich Stanton
#Author email: njr5@cdc.gov
#super incredibly minor modifications by: Rachael St. Jacques
#simm email: rachael.stjacques@dgs.virginia.gov
#description: selects optimal reference genome given a set of fasta files
#Requires: mash
#Usage: python centroid.py /path/to/assemblies/

import sys
import glob
import numpy
import operator
import os
from operator import itemgetter
import subprocess

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

import fileparser

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
            if files == files2:
                continue
            String1 = subprocess.check_output('mash dist ' + files + ' ' + files2, shell=True)
            Output.append(String1)
    Output.sort()
    return Output

def Mash_Sketch_Maker(input_read_dir):
    """Sketches read data"""
    Output = []
    print(input_read_dir)
    runfiles = fileparser.ProcessFastqs(input_read_dir, output_dir=input_read_dir)
    reads_dict = runfiles.id_dict()
    sketch_dir = os.path.join(os.getcwd(), "mash_sketches")
    if not os.path.exists(sketch_dir):
        os.mkdir(sketch_dir)
    for id in reads_dict:
        # capture read file and path names
        fwd_read = reads_dict[id].fwd
        rev_read = reads_dict[id].rev
        String1 = subprocess.check_output(f"mash sketch -r -m 2 -o {sketch_dir}/{id} {fwd_read} {rev_read}", shell=True)
        Output.append(f"{sketch_dir}/{id}.msh")
    return(Output)

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
ref_genome = Centroid.decode().rsplit('/',1)[1]
print(ref_genome, file=open("centroid_out.txt", "w"))
