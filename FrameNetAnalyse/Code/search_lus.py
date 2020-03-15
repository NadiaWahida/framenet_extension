#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 16:29 2019

@author: sanaz

This Modul gives information about Name and ID of the LU, Frame Name and ID of the frame and SemanticTypes of the LU.
"""
from nltk.corpus import framenet as fn

INPUT = '../Data/example_words.txt'
OUTPUT = 'lexUnits.txt'

def open_file(filename):
	"""
	Read given filename. This file contains a list of words, each word per line.
	
	Args:
		filename (str): path to given input file
	
	Returns:
		list: list of given words
	"""
    with open(filename,'r') as f:
        words = [el.strip() for el in f.readlines()]
    return words

def write_file(filename, data):
	"""
	Write output data into file.
	
	Args:
		filename (str) : path to output file
		data (str): data to write
		
	"""
    if data != None:
        with open(filename,'a') as f:
                f.writelines(data)
                f.writelines('\n\n')

def get_frames(lu):
	"""
	Get a list of all frames that contain LUs
	
	Args:
		lu (str):
	
	Returns:
		list(AttrDict): a list of frame objects
	"""
    frames = fn.frames_by_lemma(lu)
    return frames

def get_lus(word):
	"""
	Get LU for a word.
	
	Args:
		word (str): given word
		
	Returns:
		dict(int:str): LU index(IDs) and Names
	"""
    return fn.lu_ids_and_names(word)

def get_lu_info(lu_id, sem_types_dict):
	"""
	Get information of the LU based on its ID.
	
	Args:
		lu_id (int): ID of the LU
		sem_types_dict (dict): nicht benutzt in dieser Funktion
		
	Returns:
		str: information of the LU
	"""
	# Get LU names by calling the lu() function and passing in an LU's 'ID' number 
    name = fn.lu(lu_id).name + '\t' + str(lu_id)
    # Get Frame names and frame ID
    frame = fn.lu(lu_id).frame.name + '\t' + str(fn.lu(lu_id).frame.ID)
    #Get Semantic type of lu_id
    semTypes = fn.lu(lu_id).semTypes
    #semTypes = '\n'.join(semTypes)
    semTypes = str(semTypes)
    info = "\t".join([name, frame, semTypes])
    return info

if __name__=='__main__':
    
    words = open_file(INPUT)

    sem_types_dict = {}
    for word in words:
        # print(word)
        lus = get_lus(word)
        for lu_id in lus.keys():
            # print(lu_id)
            info = get_lu_info(lu_id, sem_types_dict)
            # print(info)





