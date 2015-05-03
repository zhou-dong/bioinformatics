# Find Ebola Ancestor from fasta

## Description

Scientists tracking the Ebola outbreak in Guinea say the virus has mutated. More than 22,000 people have been infected with Ebola and 8,795 have died in Guinea, Sierra Leone and Liberia. Scientists are starting to analyse hundreds of blood samples from Ebola patients in Guinea. They are tracking how the virus is changing and trying to establish whether it's able to jump more easily from person to person. "We know the virus is changing quite a lot," said human geneticist Dr Anavaj Sakuntabhai. A virus can change itself to less deadly, but more contagious and that's something we are afraid of Dr Anavaj Sakuntabhai, Geneticist "That's important for diagnosing (new cases) and for treatment. We need to know how the virus (is changing) to keep up with our enemy."

Our project is going to  find the common ancestor from descendant to help scientists to conquer the wars between Humans Beening and Ebola.

## Steps:

1. Use FP-Growth to Find the Frequent Pattern

2. Use Dynamic Programming to find the different of sequence Alignment 

3. Check the result

## Data

Dataset: http://hgdownload.soe.ucsc.edu/goldenPath/eboVir3/ebolaAbSequences.fasta

Data Format: Fasta

```
    >gi|166007127|pdb|2QHR|H Chain H, Crystal Structure Of The 13f6-1-2 Fab Fragment Bound To Its Ebola Virus Glycoprotein Peptide Epitope.|pmid|18005986
    EVQVVESGGGLVKPGGSLKLSCAASGFAFSSYDMSWVRQTPEKRLEWVAYISRGGGYTYYPDTVKGRFTI
    SRDNAKNTLYLQMSSLKSEDTAMYYCSRHIYYGSSHYYAMDYWGQGTSVTVSSAKTTAPSVYPLAPVCGD
    TTGSSVTLGCLVKGYFPEPVTLTWNSGSLSSGVHTFPAVLQSDLYTLSSSVTVTSSTWPSQSITCNVAHP
    ASSTKVDKKIEP
```

## Development Information

Language

- python

Algorithm

- FP-Growth
- Dynamic programming

Python Package:

- Biopython
- python-fp-growth
- matplotlib

```
E-V--QLLES--GGGL-VKPGGSL--RLSCAASGFTLIN--------Y--RXN-----WVRQA-PG---KGL-E-WVS---S----I-S-SSSSYIHYADSVKGRFT--ISRDNAENSLYLQXNSLRAEDTAVYYCVREGPRATGY-SXA--DVFDIWGQG-TXV----TVSSASTKGPSVF--PLAPS--S-KSTSGGTAA-LGCL-V-KDYFP-EP-V-T-VSWNSGALTSG-----VHTFPAVLQ-S--SGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVD--K-KV---E--------P--K----
ELVXTQ---SPDS--LAV----SLGER----A---T-INCKSSQSVLYSSN-NKSYLAWY-QQKPGQPPK-LLIYWASTRESGVPDRFSGSG-S-G-T-D-----FTLTIS------SL--Q-----AEDVAVYYC-----Q-Q-YYS-APLT-F---G-GGTKVEIKRTV--A--A-PSVFIFP--PSDEQLKS--G-TASVV-CLLNNF-Y-PREAKVQWKVD-N--ALQSGNSQESV-T---E-QDSKDST-YSLSS--T-----L---T-------L-S--KADYEKHKVYACEVTHQGLRSPVTKSFNR
100.0
0
314
EVQSLVSLRATINYNWQPGKLWSSSSSDFTISSLQAEDAVYYCYSAFGGTVTVAPSVFPPSKSGTACLYPEVVNALSGVTQSSYSLSSTLTSKDKKVEPK
```

## Install Package

FP-growth:

    git clone https://github.com/enaeseth/python-fp-growth.git
    cd python-fp-growth
    python setup.py install
    sudo python setup.py install

Test FP-Growth

    python -m fp_growth -s 4 examples/tsk.csv

Install [Biopytho](http://biopython.org/wiki/Download)

    python setup.py build
    python setup.py test
    sudo python setup.py install
