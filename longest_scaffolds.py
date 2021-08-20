from Bio import SeqIO
import sys

genome = SeqIO.parse(sys.argv[1], "fasta")

for record in genome:
	
	print(record.description + " " + str(len(record.seq)) + "\n")
	
