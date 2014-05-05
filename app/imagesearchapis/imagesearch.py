import numpy as np
from bagofword import *
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

def search_image(filepath, codebook, tfidf, control="with_tfidf"):
    print_detail = True
    k,_ = codebook.shape
    if print_detail:
        print "-------------------------------------------------------------------------------"
    bow = get_bow(filepath,codebook)
    if print_detail:
        print "-------------------------------------------------------------------------------"
        print "tfidf matrix shape:"
        print tfidf.shape
        print "-------------------------------------------------------------------------------"
        print "Bag of Word of: ",filepath
        print bow
        print "-------------------------------------------------------------------------------"
    _,l = tfidf.shape
    control = "no_tfidf"
    if control == "with_tfidf":
        idi = np.zeros((1,l))
        for i in range(k):
            if bow[i] != 0 :
                idi = np.add(idi,tfidf[i])
        rank = [(i,j) for (i,j) in zip([i for i in range(l)],idi.tolist()[0])]
    else:
        bow = [ float(i)/sum(bow) for i in bow.tolist()]        
        rank =  np.dot(np.asarray(bow),tfidf)
        rank =  [(i,j) for (i,j) in zip([i for i in range(l)],rank.tolist())]
       
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
        
   
    # images_data_path = "/Users/minhuigu/FoodAdvisor/app/outputs/images_data.txt"
    # images_folder = "/Users/minhuigu/Desktop/"
    # img_list = []
    # json_content = open(images_data_path).read()
    # for each in json.loads(json_content):
    #     img_list.append(images_folder + each['relpath'])
    # 
    # for a in [i.id() for i in result][::]:
    #     print img_list[a]
    if print_detail:
        print "Best rank images: "
        print [i.id() for i in result][::]   
        print "-------------------------------------------------------------------------------"  
    # decreasing according to similarity    
    return [i.id() for i in result][::]
