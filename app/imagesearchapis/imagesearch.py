import numpy as np
from bag_of_word import *
from Queue import PriorityQueue

def search_image(filepath,tfidf_txt,codebook_txt):
    codebook = np.loadtxt(codebook_txt)
    k,_ = codebook.shape
    bow = get_bow(filepath,codebook)
    tfidf = np.loadtxt(tfidf_txt)
    idi = np.zeros((1,l))
    for i in range(k):
        if bow[i] != 0 :
            idi = np.add(idi,tfidf[i])
    rank = [(i,j) for (i,j) in zip([i for i in range(l)],idi.tolist()[0])]
    q = PriorityQueue(50)
    for (x,y) in rank:
        print q.queue
        if not q.full():
            q.put((y,x))
        else:
            if i[1] > q.queue[0]:
                if q.full():
                    q.get()
                q.put((y,x))
    result = []
    while not q.empty():
        result.append(q.get())
    return result[::-1]


if __name__ == "__main__":
    filepath = "/Users/minhuigu/Downloads/ayahoo_test_images/bag_5.jpg"
    codebook_txt = "/Users/minhuigu/Desktop/codebook.txt" 
    tfidf_txt = "../outputs/img_representations/tfidf.txt"
    
    search_image(filepath,tfidf_txt,codebook_txt)