import numpy as np
import math          
import json


def inv_file_index_with_tfidf(vq_txt,tfidf_txt,l,k):
    vq_matrix = np.loadtxt(vq_txt)
    row_sums = vq_matrix.sum(axis=1)
    tf_matrix = vq_matrix / row_sums[:, np.newaxis]
    idf = []
    for i in vq_matrix.T:
        if max(i) <= 0:
            idf.append(0)
        else:
            idf.append(math.log10( l/sum([1 for p in i if p>0])))     
    for i in range(l):
        tf_matrix[i] = tf_matrix[i]*idf    
             
    np.savetxt(tfidf_txt, tf_matrix.T) 
    
    
if __name__ == "__main__":
    imgs_txt = "../outputs/images_data.txt"
    vq_txt = "../outputs/img_representations/vq.txt"
    tfidf_txt = "../outputs/img_representations/tfidf.txt"
    
    images_data_path = "../outputs/images_data.txt"
    images_folder = "../static/"
    img_list = []
    json_content = open(images_data_path).read()
    for each in json.loads(json_content):
        img_list.append(images_folder + each['relpath'])
         
    l = len(img_list)
    k = 1000
    
    inv_file_index_with_tfidf(vq_txt,tfidf_txt,l,k)