#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:11:51 2020

@author: nadia
"""
from nltk.corpus import framenet as fn
import json
FRAME_POLARITY = '../Data/Senti_Frames_mit_Framepolarity.txt'
#CONSTRAINTS = '../Data/Constraints/'
CONSTRAINTS = '../Data/Constraints/Frameconstraints_with_Polarity.json'
def get_annotation(annotation):
    #nice = []
    #good_examples = []
    #while len(good_examples)<number:
    #for annotation in annotations:
        #if annotation.frame.name not in senti_frames:
            #continue
        #if len(annotation.FE[0])>1:
            #print('ja')
    frame = annotation.frame.name
    text = annotation.text
    target = ''
    for el in annotation.Target:
        target += text[el[0]:el[1]]+' '
    fes = {}
    for el in annotation.FE[0]:
        fes[el[2]] = text[el[0]:el[1]]
    unexpr = annotation.FE[1]
    fes.update(unexpr)
    sent_info = {'text':text, 'Target':target, 'FE':fes, 'frame':frame}# 'FE_unexpr': unexpr,
    return sent_info
        #print(sent_info)
        #nice = sent_info
        #nice.append(sent_info)
        #good_examples.append(sent_info)
        #print(annotation.FE[0])
        #print(len(annotation.FE[0]))
    #return good_examples
    #print(type(good_examples))

def get_opinions(sentence):
    expressions = [sentence['text']]
    frame = sentence['frame']
    rules = constraints[frame]
    #for fe in sentence['FE'].items():
    for rule in rules:
        #print(frame+'.'+fe[0])
        rule_string = rule[0]+' '+rule[1]+' '+rule[2]
        #print(rule_string)
        for fe in sentence['FE'].items():
            #print(frame+'.'+fe[0])
            if frame+'.'+fe[0] in rule_string:
                #print('Yeeeeeeeeeeees')
                rule_string = rule_string.replace(frame+'.'+fe[0],fe[1])
        #print(rule_string)
        if rule_string.count('.') > 0:
            continue
        else: 
            expressions.append(rule_string)
            
        #elif rule_string.count('.') == 1:
        """ 
        if frame+'.'+fe[0] in rule:
            print(rule)
            if rule[0].split('.')[1] in sentence['FE']:
                rule[0] = sentence['FE'][rule[0].split('.')[1]]
            if rule[2].split('.')[1] in sentence['FE']:
                rule[2] = sentence['FE'][rule[2].split('.')[1]]
            check = True
            print(rule)
            for el in rule:
                if '.' in el: check = False
            if check == True:
                expressions.append(rule)
        """
    for el in expressions:
        print(el)
                
            

def get_frames(senti_frames):
    for senti_frame in senti_frames:
    #senti_frame = senti_frames[1]
        senti_frame = fn.frame(senti_frame)
    #print(senti_frame)
    #print(senti_frame.keys())
        lus = senti_frame.lexUnit
        for lu in lus:
            #print(lu)
            try:
                annotations = fn.annotations(lu)
                #annotations = filter_annotations(annotations)
                #print(annotations)
                ##annotation = annotations[0]
                """
                annotation.keys() =
                dict_keys(['cDate', 'status', 'ID', '_type', 'layer', '_ascii', 'Target', 'FE', 
                           'GF', 'PT', 'Other', 'Sent', 'Verb', 'sent', 'text', 'LU', 'frame'])
                """
                for annotation in annotations:
                    if annotation.frame.name not in senti_frames:
                        continue
                    sentence = get_annotation(annotation)
                    print(sentence)
                    opinions = get_opinions(sentence)
                #print(lu)
                #print(annotation.frame.name)
                #print(annotation.Target)
                #print(annotation.FE)
                #print(annotation.text)
                    print('#'*20)
            except:
                continue
    #print(senti_frame)
    #print(fn.annotations('alert.n'))

if __name__ == '__main__':
    with open(CONSTRAINTS,'r') as f:
        constraints = json.load(f)
    with open(FRAME_POLARITY,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    get_frames(senti_frames)