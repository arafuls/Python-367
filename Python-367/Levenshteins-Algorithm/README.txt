Description:
My take on Levenshtein's algorithm, a well known algorithm used in
bioinformatics research to study the similarity between genes from
different organisms.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

How to use the program:
cmd_prompt >>> lev_dist.py string1.txt string2.txt
	Assuming contents of textfiles are as follows:
		string1.txt:
		GGAAGGGGCGATCGGAGGGC
		
		string2.txt:
		GGTAAGGGGCCTGATCGAAGGGCAA
		
	Then the output should be as follows:
	GG-AAGGGG-C-GATCGGAGGGC--
	GGTAAGGGGCCTGATCGAAGGGCAA
	
	The minimum edit distance is 6
	Completed in 0.000234 seconds. (varies depending on machine)