# encoding: utf-8

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from operator import itemgetter, attrgetter, methodcaller
from fp_growth import find_frequent_itemsets
import numpy as np
import matplotlib.pyplot as plt

input_file = "./ebola.fasta"

def fetch_fasta_dict(file_path = input_file):
    print "begin to load fasta file"
    result = {}
    fasta_sequences = SeqIO.parse(open(file_path),'fasta')
    for fasta in fasta_sequences:
        name, sequence, describe = fasta.id, str(fasta.seq), fasta.description
        if "Crystal" not in describe:
            continue
        result[name] = sequence
    fasta_sequences.close()
    print "load file finis with len:", len(result)
    return result

def fetch_fasta_list(file_path = input_file):
    print "begin to load file"
    result = []
    fasta_sequences = SeqIO.parse(open(file_path),'fasta')
    for fasta in fasta_sequences:
        name, sequence, describe = fasta.id, str(fasta.seq), fasta.description
        if "Crystal" not in describe:
            continue
        result.append(sequence)
    fasta_sequences.close()
    print "load file finish"
    return result

def dynamic_programming_alignment(a, b):
    result = pairwise2.align.globalxx(a, b)
    #result = pairwise2.align.globalmx(a, b, 2, 1)
    result = sorted(result, key=itemgetter(2), reverse=True)
    result =  sorted(result, key=itemgetter(4), reverse=True)
    return result[0]

def common(a, b):
    return [i for i, j in zip(a, b) if i == j]

def clustering():
    dicts = fetch_fasta_dict()
    pivot = dicts.popitem()
    lengths = []
    scores = []
    for key, value in dicts.iteritems():
        length = len(value)
        lengths.append(length)
        score = (dynamic_programming_alignment(pivot[1], value)[2]);
        scores.append(score)
        print key, length, score
    
    cluster_pie_charts(scores)
    #cluster_bar_charts(scores)
    return lengths, scores

def cluster_pie_charts(scores):
    threshold = 50
    datas = {}
    for score in scores:
        label = int(score / 50)
        if label in datas:
            datas[label] = datas[label] + 1
        else:
            datas[label] = 1
    sizes = []
    labels = []
    for key, value in datas.iteritems():
        sizes.append(value)
        labels.append(key*50)
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', "green"]
    plt.pie(sizes,
            labels=labels, 
            colors=colors,
            autopct='%1.1f%%', 
            shadow=True, 
            startangle=90
            )
    plt.axis('equal')
    plt.show()
    
def cluster_bar_charts(scores):
    index = np.arange(len(scores))
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, scores, bar_width,
                 alpha=opacity,
                 color='g',
                 error_kw=error_config,
                 label='score')
    plt.xlabel('Index of sequence')
    plt.ylabel('Scores')
    plt.title('Scores of Sequence')
    plt.xticks(index + bar_width, range(0, len(scores)))
    plt.legend()
    plt.plot(scores, "r--")
    plt.show()

def show_alignment():
    data = fetch_fasta_list()
    result = dynamic_programming_alignment(data[0], data[1])
    #for x in result:
    #    print x
    print format_alignment(*result)
    comm = common(result[0], result[1])
    print "".join(comm)

show_alignment()
#clustering()
