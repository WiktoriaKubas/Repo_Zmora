class PROG():

    def __init__(self):
        pass

    def funkcja(self,name):
	"""
	:name file
	:return dictionary 
	"""
        source=open(name+".txt").read()
        IN=source.split(" ")
        dic={}
        for i in IN:
            if len(i) in dic:
                dic[len(i)]=dic[len(i)]+1
            else:
                dic[len(i)]=1
        return dic
                    
P=PROG()
