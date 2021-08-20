## Chromosome painting and macrosynteny analyses for Gila monster sex chromosome evolution ##

### Step 1: Gather your genome and annotation files ###

**If your species' genome files are available on EMBL or Genbank (.dat) they can be downloaded from ftp.ensembl.org for easy use. **

EMBL or Genbank genome files on Ensembl are easily converted for use in SynChro. However, if your species of interest does not have these files, in **steps 3–5 below** you can use genome FASTA and GFF3 annotation files for use in SynChro, which requires specific formatting.

### Step 2: Use write_fasta_from_gff.py to create protein FASTA records with info from GFF annotation ### 

to use genome FASTAs and GFF annotations in SynChro, protein FASTA records must be extracted from both files and supplemented with data on gene position and scaffold. this modified gff2fasta.pl script will perform this task.

write_fasta_from_gff.py takes three parameters:

- -i (input file) : GFF annotation for the genome of interest
- -f (FASTA file) : genome FASTA to pull sequences from
- -o (output file) : name of the output protein FASTA

```
write_fasta_from_gff.py -i Gila.gff -f Gila.fa -o Gila_proteins.fasta
```

### Step 3: Choose scaffolds to be used in chromosome painting ###

many new genome releases do not have full-length chromosomes assembled. instead, the genome is separated into a series of scaffolds and, potentially, assigned to certain chromosomes. with too many scaffolds, the chromosome painting figures become much harder to interpret. in this paper, we take the 50 longest scaffolds for Gila monster and 24 longest scaffolds for Komodo dragon alongside assigned sex chromosome scaffolds for each.

longest_scaffolds.py can determine the longest scaffolds from a genome FASTA:

```
longest_scaffolds.py Gila.fasta > Gila_lengths.txt
```



```
pull_id_match.py Gila_proteins.fasta Gila_scaffolds.txt Gila_protreduct.fasta
```

### Step 4: Convert files to SynChro format ###

```
ConvertFasta.py Gila HelodermaSuspectum HSUS 1 5 2 3 4 0
```

### Step 5: Run SynChro.py ### 

```
SynChro.py Gila 0 2
```

