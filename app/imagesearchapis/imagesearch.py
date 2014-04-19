import numpy as np
from bag_of_word import *
from Queue import PriorityQueue

class Image(object):
    def __init__(self, priority, index):
        self.priority = priority
        self.index = index      
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
        
    def similarity(self):
        return float(self.priority)
        
    def id(self):
        return int(self.index)
        
def search_image(filepath,control="with_tfidf"):
    
    codebook_txt = "/Users/minhuigu/FoodAdvisor/app/outputs/codebook.txt"
    tfidf_txt = "/Users/minhuigu/FoodAdvisor/app/outputs/tfidf.txt"

    codebook = np.loadtxt(codebook_txt)
    k,_ = codebook.shape
    bow = get_bow(filepath,codebook)
    tfidf = np.loadtxt(tfidf_txt)
    _,l = tfidf.shape
    idi = np.zeros((1,l))
    
    for i in range(k):
        if bow[i] != 0 :
            idi = np.add(idi,tfidf[i])
    rank = [(i,j) for (i,j) in zip([i for i in range(l)],idi.tolist()[0])]
    
    q = PriorityQueue(50)
    for (x,y) in rank:
        if not q.full():
            q.put(Image(y,x))
        else:
            if y > q.queue[0].similarity():
                q.get()
                q.put(Image(y,x))

    result = []
    while not q.empty():
        result.append(q.get())
    # decreasing according to similarity
    return [i.id() for i in result][::-1]
