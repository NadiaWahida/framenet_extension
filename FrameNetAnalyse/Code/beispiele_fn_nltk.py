#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:08:07 2019

@author: nadia
"""

from nltk.corpus import framenet as fn

# Alle Frames in FrameNet
frames = fn.frames()
print(len(frames), ' Frames insgesamt in FrameNet 1.7\n\n')

# Einen Frame anzeigen
frame = frames[0]
#print(frame)

# Auf einzelne Attribute des Frames zugreifen
ID = frames[0].ID
name = frames[0].name
definition = frames[0].definition
lexicalUnits = frames[0].lexUnit
#print(ID)
print(name)
print(definition)
#print(lexicalUnits)

# Lexical Units 
lu_name = fn.lu(14839).name
#print(fn.lu(14839))

# Frames anzeigen zu denen ein Wort gehört
abandon_frames = fn.frames_by_lemma('abandon')
#print(abandon_frames)

# Annotationen eines Wortes anzeigen
abandon_annotations = fn.annotations('abandon')
#print(abandon_annotations)
#print(abandon_annotations[0])