#-*- coding: utf-8 -*-
import math


text=[]
spot=[]
dist_list=[]
dic={}
dist_spot={}
def distance(x1,y1,x2,y2):
    dist=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))    
    return float(dist)

def total_len(a,N):
    dist=distance(int(a[0][0]),int(a[0][1]),int(a[N-1][0]),int(a[N-1][1]))
    for i in range(0,N-1):
        dist+=distance(int(a[i][0]),int(a[i][1]),int(a[i+1][0]),int(a[i+1][1]))
    return float(dist)

def read_spot(filename):
    fp=open(filename,"r")
    N=int(fp.readline().split('\n')[0])
    for i in range(0,N):
        text.append(fp.readline().split('\n')[0])
        dic[text[i]]=i
    fp.close()
    

def make_spot():
    for i in text:
        spot.append(i.split())



def swap(List,k,i):
    tmp=List[k]
    List[k]=List[i]
    List[i]=tmp


def perm_spot(k):
    if k==len(text):
        dist=total_len(spot,len(text))
        dist_list.append(dist)
        dist_spot[dist]=text[:]
        return
    for i in range(k,len(text)):
        swap(spot,k,i)
        swap(text,k,i)
        perm_spot(k+1)
        swap(spot,k,i)
        swap(text,k,i)


def find_tour(min_len):
    find_list=dist_spot[min_len]
    print find_list
    print "[",
    for i in range(0,len(find_list)):
        print dic[find_list[i]],
        if i!=len(find_list)-1:
            print "->",
    print "]"


filename=raw_input("filename:")

read_spot(filename)
make_spot()
perm_spot(0)
min_len = min(dist_list)
print min_len
find_tour(min_len)
