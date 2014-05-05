import cv2
from scipy import cluster,histogram
import numpy as np
import math          
import json

def record_sift(des,f):
    np.savetxt(f,des,fmt='%1.0f')
    
def dect_SIFT(image):
    print "getting SIFT for: ", image
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, des = cv2.SIFT().detectAndCompute(gray, None)
    return des
    
def dect_dense_SIFT(image):
    print "getting dense SIFT for: ", image
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dense = cv2.FeatureDetector_create("Dense")
    kp = dense.detect(gray)
    _,des=cv2.SIFT().compute(img,kp)
    return des[100:2350:3]
       
def new_file(filename):
    f = open(filename,"w")
    f.write("")
    f.close()

def grab_and_save_SIFT(img_list,SIFT_txt):
    new_file(SIFT_txt)
    f = file(SIFT_txt,"a")
    for a_img in img_list:
        record_sift(dect_dense_SIFT(a_img),f)
    f.close()
    
    
# ---------------------------------------------------    
def load_SIFT(file):
    sift_pool = np.loadtxt(file)
    print sift_pool.shape
    return sift_pool


def clustering(txt,codebook_txt,K):
    sift_pool = load_SIFT(txt)
    print "clustering..for K: ", K
    nd, _ = cluster.vq.kmeans2(sift_pool, K)
    print "saving codebook"
    np.savetxt(codebook_txt, nd)
    return nd
        
def get_bow(imagepath,codebook):
    #print "dense vq for: ",imagepath
    #vecs, _ = cluster.vq.vq(dect_SIFT(imagepath), codebook)
    vecs, _ = cluster.vq.vq(dect_dense_SIFT(imagepath), codebook)
    counts, bins = histogram(vecs, len(codebook))
    return counts 
    
        
def quantization(img_list,bookfile,vq_txt,l,k):
    bow_matrix = np.zeros((l,k))
    codebook = np.loadtxt(bookfile)
    i = 0
    for a_img in img_list:
        bow_matrix[i] = get_bow(a_img,codebook)
        i += 1
    print "vq matrix shape", bow_matrix.shape
    np.savetxt(vq_txt, bow_matrix,fmt='%1.0f')
   
    
if __name__ == "__main__":

    SIFT_txt = "../outputs/img_representations/SIFT.txt"    
    codebook_txt = "../outputs/img_representations/codebook.txt"  
    vq_txt = "../outputs/img_representations/vq.txt"
    
    
    images_data_path = "../outputs/images_data.txt"
    images_folder = "../static/"
    img_list = []
    json_content = open(images_data_path).read()
    for each in json.loads(json_content):
        img_list.append(images_folder + each['relpath'])
          
    l = len(img_list)
    k = 1000
    
    grab_and_save_SIFT(img_list,SIFT_txt)
    
    clustering(SIFT_txt,codebook_txt,k)
    
    quantization(img_list,codebook_txt,vq_txt,l,k)
    
    
    