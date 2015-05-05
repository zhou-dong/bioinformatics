# -*- coding: utf-8 -*-

from time import time
from Bio import SeqIO

import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

input_file = "./ebola.fasta"

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
data = fetch_fasta_list()

def get_dimension(_input = data):
    result = []
    one_sequence = _input[0]
    for x in one_sequence:
        if x not in result:
            result.append(x)
    print "dimension length:", len(result)
    return result

def create_datas(_input = data):
    dimension = get_dimension()
    result = []
    for x in _input:
        tmp = []
        total_length = len(x)
        for y in dimension:
            tmp.append(x.count(y)/float(total_length))
        result.append(tmp)
    return result

kmeans_data = scale(create_datas())
n_samples, n_features = kmeans_data.shape
#n_digits = len(np.unique(kmeans_data))
n_digits = 3
labels = kmeans_data
sample_size = 30

print("n_digits: %d, \t n_samples %d, \t n_features %d"
              % (n_digits, n_samples, n_features))

def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    #print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
         # % (name, (time() - t0), estimator.inertia_,
           #  metrics.homogeneity_score(labels, estimator.labels_),
           #  metrics.completeness_score(labels, estimator.labels_),
           #  metrics.v_measure_score(labels, estimator.labels_),
           #  metrics.adjusted_rand_score(labels, estimator.labels_),
           #  metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
           #  metrics.silhouette_score(data, estimator.labels_,
           #                           metric='euclidean',
           #                           sample_size=sample_size)))

bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
              name="k-means++", data=kmeans_data)

bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
              name="random", data=kmeans_data)

# in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=n_digits).fit(kmeans_data)
bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
              name="PCA-based",
              data=kmeans_data)
print(79 * '_')


###############################################################################
# Visualize the results on PCA-reduced data

reduced_data = PCA(n_components=2).fit_transform(kmeans_data)
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() + 1, reduced_data[:, 0].max() - 1
y_min, y_max = reduced_data[:, 1].min() + 1, reduced_data[:, 1].max() - 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
