import json
import numpy as np
from sklearn.cluster import DBSCAN


class Dbscan:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def get_result(self):
        locations = []
        with open(self.infile) as f:
            f.readline()
            line = f.readline()
            while line:
                location = line.strip().split(',')
                location[0] = float(location[0].strip())
                location[1] = float(location[1].strip())
                locations.append(location)
                line = f.readline()
        return locations

fileDirectory = "/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/"
if __name__ == '__main__':
    dbscan = Dbscan(fileDirectory + 'part3_neg.csv',fileDirectory + 'part4_neg.csv')
    results = dbscan.get_result()
    locations = results
    locations = np.array(locations)
    f = open(dbscan.outfile, 'w+')
    f.write('longitude,latitude\n')
    clustering = DBSCAN(eps=0.015, min_samples=50).fit(locations)

    label_cnt = {}
    for label in clustering.labels_:
        if label_cnt.get(label) is None:
            label_cnt[label] = 1
        else:
            current_cnt = label_cnt.get(label)
            label_cnt[label] = current_cnt + 1
    print(label_cnt)

    interested_labels = [0]
    cluster_coords = []
    for i in range(len(locations)):
        if clustering.labels_[i] in interested_labels:
            cluster_coords.append(locations[i])

    for i in range(len(cluster_coords)):
        txt = {'location': list(cluster_coords[i])}
        json_txt = json.dumps(txt)
        csv_txt = '%s,%s' % (cluster_coords[i][0],cluster_coords[i][1])
        f.write(csv_txt + '\n')