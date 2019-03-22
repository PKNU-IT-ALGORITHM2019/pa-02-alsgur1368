#-*- coding: utf-8 -*-
import math

spot_list=[]
min_tour=0
tour=[]


class Spot:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def set_index(self,index):
		self.index=index





def input_tour():
	global tour
	tour=[spot_list[0].index]
	for i in range(1,len(spot_list)):
		tour.append(spot_list[i].index)
	print(tour)
	

def read_file(filename):
	
	fp=open(filename,"r")
	N=int(fp.readline().split('\n')[0])
	for i in range(0,N):
		xy=fp.readline().split('\n')[0]
		x=int(xy.split()[0])
		y=int(xy.split()[1])
		index=len(spot_list)
		spot_list.append(Spot(x,y))
		spot_list[i].set_index(index)
	fp.close()

def swap(k,i):
	tmp=spot_list[i]
	spot_list[i]=spot_list[k]
	spot_list[k]=tmp


def distance(x1,y1,x2,y2):
	return float(math.sqrt((x1-x2)**2+(y1-y2)**2))
	

def perm_spot(k,now_len):
	global min_tour

	if min_tour!=0 and min_tour<=now_len:
		return
	if k == len(spot_list):
		tmp=distance(spot_list[0].x,spot_list[0].y,spot_list[len(spot_list)-1].x,spot_list[len(spot_list)-1].y)
		now_len += float(tmp)
		if min_tour==0:
			min_tour=now_len
		if min_tour>now_len:
			min_tour=now_len
			print("최소 길이: ",min_tour)
			input_tour()
		now_len-=tmp
		return 
	for i in range(k,len(spot_list)):
		swap(k,i)
		if k==0:
			now_len=0
			perm_spot(k+1,now_len+distance(spot_list[k].x,spot_list[k].y,spot_list[k].x,spot_list[k].y))
		
		else :
			perm_spot(k+1,now_len+distance(spot_list[k].x,spot_list[k].y,spot_list[k-1].x,spot_list[k-1].y))
		swap(k,i)
	return 




def main():
	filename=input("filename: ")
	read_file(filename)
	for i in range(0,len(spot_list)):
		print(spot_list[i].x,spot_list[i].y,spot_list[i].index)
	
	perm_spot(0,0)
	print(min_tour)
	print(tour)
	

main()


