#README

The module SentiFrameNet combines FrameNet with Sentiment Analysis.

The required modules are:
				- framenet from nltk.corpus
				- sentiwordnet from nltk.corpus
				- networkx


The Code of the module divides in the following files:

- try_me.py

	This module gives an interactive access to the project.
	Best run it in a terminal via >> python try_me.py
	You can look up Opinion Mappings of a given word or frame.
	These will be chosen randomly from the data base.
	You can also get information about SentiFrames, FrameNet 
	and other things. For more information type help after running.


- search_for_senti_frames.py

	This module was written to find SentiFrames in FrameNet.
	It uses FrameNet's Frame Relations to expand the list of SentiFrames.
	This module also models a SentiGraph of the SentiFrames via networkx.
	It was writen for research and therefore edited a few times


- mk_constraints.py

	This module computes and writes Constraints for SentiFrames.
	Mappings are saved in: '../Data/Constraints/'

- mk_constraints_dict.py

	This module reshapes constraints of SentiFrames and stores them to a dictionary,
	'../Data/Constraints/Frameconstraints.json',
	like: {frame:['constraint1','constraint2',...],...}


- get_annotated_sentences_from_fn.py

	This module gets annotated sentences for SentiFrames from FrameNet,
	saves them in the file: '../Data/annotated_sents_from_FrameNet.txt',
	one dictionary a line
	dict like: {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes}


- SentiWordNet.py

	This module looks up a word (and optional it's POS-Tag) in SentiWordNet,
    	adds up positive and negative Scores of the found synsets
    	returns the sentiment with the highest score
    	returns neutral if both scores are equal
    	returns no_entry if no entry was found


- map_constraints_to_annotation.py

	This module mapps annotated sentences to their Opinion Constraints
	of the SentiFrame they evoke. 
	Mappings are saved in: '../Data/Opinion_mapping/'



