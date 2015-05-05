# Clustering Ebola virus fasta sequence with Dynamic Programming

## Description

Scientists tracking the Ebola outbreak in Guinea say the virus has mutated. More than 22,000 people have been infected with Ebola and 8,795 have died in Guinea, Sierra Leone and Liberia. Scientists are starting to analyse hundreds of blood samples from Ebola patients in Guinea. They are tracking how the virus is changing and trying to establish whether it's able to jump more easily from person to person. "We know the virus is changing quite a lot," said human geneticist Dr Anavaj Sakuntabhai. A virus can change itself to less deadly, but more contagious and that's something we are afraid of Dr Anavaj Sakuntabhai, Geneticist "That's important for diagnosing (new cases) and for treatment. We need to know how the virus (is changing) to keep up with our enemy."

Our project is going to use the dynamic programming method to calculte the similar of sequence and then clustring them to different groups.

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
>gi|193885309|pdb|3CSY|A Chain A, Crystal Structure Of The Trimeric Prefusion Ebola Virus Glycoprotein In Complex With A Neutralizing Antibody From A Human Survivor|pmid|18615077
EVQLLESGGGLVKPGGSLRLSCAASGFTLINYRXNWVRQAPGKGLEWVSSISSSSSYIHYADSVKGRFTI
SRDNAENSLYLQXNSLRAEDTAVYYCVREGPRATGYSXADVFDIWGQGTXVTVSSASTKGPSVFPLAPSS
KSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNV
NHKPSNTKVDKKVEPK
    
>gi|193885310|pdb|3CSY|B Chain B, Crystal Structure Of The Trimeric Prefusion Ebola Virus Glycoprotein In Complex With A Neutralizing Antibody From A Human Survivor|pmid|18615077
ELVXTQSPDSLAVSLGERATINCKSSQSVLYSSNNKSYLAWYQQKPGQPPKLLIYWASTRESGVPDRFSG
SGSGTDFTLTISSLQAEDVAVYYCQQYYSAPLTFGGGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVC
LLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLRSP
VTKSFNR
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


Calculate scores:

1. We choose one fasta sequcen to be pivot
2. Compare difference between pivot and other sequence.
3. Genereate the common sequence between them

<img alt="bar img" src="/img/score_sequence_bar.png"/>

Visualize differnt sequence use the score

1. Use the score to be wigth and length to represent the circle
2. random add circle into picture

<img alt="bar img" src="/img/ellipses.png"/>

- Use differnt score the cluster

1. We clustering the result use the scores
2. We divided scores into different levels
3. Calculte how many items in diffent levels

<img alt="bar img" src="/img/cluster_pie_charts.png"/>

Check the result

We think if position of the characters in sequence we could use K-means to clustering

After we use K-means to clustering the result is:

<img alt="bar img" src="/img/k-means-3.png"/>

<img alt="bar img" src="/img/k-means-4.png"/>

The result were terrible, so we do think the order of the characters in sequence.

And dynamic programming is better clustering method than some maching learning method.

## Install Package

Install [Biopytho](http://biopython.org/wiki/Download)

    python setup.py build
    python setup.py test
    sudo python setup.py install

Install scipy

    pip install scipy

Install sklearn

    pip install -U scikit-learn
