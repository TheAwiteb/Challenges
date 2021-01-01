#is parallelogram or no

def is_parallelogram(lst):
    def get_length_of(points1:tuple,points2:tuple):
        # 0 mean x and 1 mean y
        x1,x2 = points1[0],points2[0]
        y1,y2 = points1[1],points2[1]
        length= (x2-x1)**2 + (y2-y1)**2
        return length
    A,B,C,D = lst
    #If AB=DC, or, equivalently, AD=BC, then ABCD is a parallelogram, because this 
    #means that AB has same length and is parallel to DC (or, equivalently, same thing with AD and BC), which defines the parallelogram.
    if get_length_of(A,B) == get_length_of(C,D) or get_length_of(B,C) == get_length_of(D,A):
        return True
    else:
        return False 