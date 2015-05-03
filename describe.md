# Find Ebola Ancestor from fasta

## Description

Scientists tracking the Ebola outbreak in Guinea say the virus has mutated. More than 22,000 people have been infected with Ebola and 8,795 have died in Guinea, Sierra Leone and Liberia. Scientists are starting to analyse hundreds of blood samples from Ebola patients in Guinea. They are tracking how the virus is changing and trying to establish whether it's able to jump more easily from person to person. "We know the virus is changing quite a lot," said human geneticist Dr Anavaj Sakuntabhai. A virus can change itself to less deadly, but more contagious and that's something we are afraid of Dr Anavaj Sakuntabhai, Geneticist "That's important for diagnosing (new cases) and for treatment. We need to know how the virus (is changing) to keep up with our enemy."

Our project is going to  find the common ancestor from descendant to help scientists to conquer the wars between Humans Beening and Ebola.

## Abstract

Language

- python

Algorithm

- Dynamic programming

Python Package:

- Biopython
- matplotlib

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

## Steps

1. Use Dynamic Programming to find the different of sequence Alignment 

2. Find the common sequence

3. Use score to cluster the sequences to different group

## Example

- Use dynamic programming to compare two sequence

```
E-V--QLLES--GGGL-VKPGGSL--RLSCAASGFTLIN--------Y--RXN-----WVRQA-PG---KGL-E-WVS---S----I-S-SSSSYIHYADSVKGRFT--ISRDNAENSLYLQXNSLRAEDTAVYYCVREGPRATGY-SXA--DVFDIWGQG-TXV----TVSSASTKGPSVF--PLAPS--S-KSTSGGTAA-LGCL-V-KDYFP-EP-V-T-VSWNSGALTSG-----VHTFPAVLQ-S--SGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVD--K-KV---E--------P--K----
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
ELVXTQ---SPDS--LAV----SLGER----A---T-INCKSSQSVLYSSN-NKSYLAWY-QQKPGQPPK-LLIYWASTRESGVPDRFSGSG-S-G-T-D-----FTLTIS------SL--Q-----AEDVAVYYC-----Q-Q-YYS-APLT-F---G-GGTKVEIKRTV--A--A-PSVFIFP--PSDEQLKS--G-TASVV-CLLNNF-Y-PREAKVQWKVD-N--ALQSGNSQESV-T---E-QDSKDST-YSLSS--T-----L---T-------L-S--KADYEKHKVYACEVTHQGLRSPVTKSFNR
  Score=100
EVQSLVSLRATINYNWQPGKLWSSSSSDFTISSLQAEDAVYYCYSAFGGTVTVAPSVFPPSKSGTACLYPEVVNALSGVTQSSYSLSSTLTSKDKKVEPK

E--V--Q------L-----L-ESG---GGL--VKP--GGSLRLSCAASGF-T--LINYRXNWVRQAPGKGLEWVSSISSSSSYIHYADSVKG-RFTISRDNAE---NSLYLQXNSL--RAEDTAVYYCVREGPRATGYSXADVFDIWGQGTXVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHT-FPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNH---KPSN-T-KVD-----KKVEPK
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
EAIVNAQPKCNPNLHYWTTQDE-GAAIG-LAWI-PYFG-----P-AAEGIYTEGL-M-H-N---QD-G--L------------I-----C-GLRQ-L-A-N-ETTQA-L--Q---LFLRA--T-----T-EL-R-T-------F-------------------S-I-LN-R-K-------A----I-D-FLL-Q-R-W--G----G--TCH-I-L---G----------P---D-C-C-IE-P-HDWTK--NITDKIDQIIHDF-V--D
  Score=55
EVQLEGGLPGAAGTLNQGLIGRNELQLRATERTFSLKADFWGGTLGPIHKNTKDV
```

- Visualize differnt sequence use the score

<img alt="bar img" src="/img/ellipses.png"/>

- List the differnt scores

<img alt="bar img" src="/img/score_sequence_bar.png"/>

- Use differnt score the cluster

<img alt="bar img" src="/img/cluster_pie_charts.png"/>

## Install Package

<!--
FP-growth:

    git clone https://github.com/enaeseth/python-fp-growth.git
    cd python-fp-growth
    python setup.py install
    sudo python setup.py install

Test FP-Growth

    python -m fp_growth -s 4 examples/tsk.csv
-->
Install [Biopytho](http://biopython.org/wiki/Download)

    python setup.py build
    python setup.py test
    sudo python setup.py install
