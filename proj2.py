from pyevolve import G1DList
from pyevolve import GSimpleGA
import math

width=int(raw_input("width"))
hight=int(raw_input("hight"))

if width>hight:
    z=width
else:
    z=hight
scale=float(80.00/z)

P_width=width*scale
P_hight=hight*scale
#print P_width , P_hight
#emtiazdehiamun bayad olaviataro dar nazar begire
def inrange_func(genome):
    inrange_score=0
    for i in range(0,len(genome),4):
        if genome[i]<P_width or genome[i+2]<genome[i]:
            inrange_score=inrange_score +5
        if genome[i+1]<P_hight or genome[i+3]>genome[i+1]:
            inrange_score=inrange_score +5
    return inrange_score

def light_func(genome):
    light_score=0
    for i in range(0,len(genome),4):
        light_score=light_score+0.05*genome[i]
        light_score=light_score+0.05*(P_hight-genome[i+1])
    return light_score
      
def unusedplace_func(genome):
    unused_score=0
    for i in range(0,len(genome)-4,4):#out of range nemide
        if P_width-genome[i]==0:
            unused_score=unused_score+5
        if P_hight-genome[i+3]==0:
            unused_score=unused_score+5
        if int(genome[i]-genome[i+4])==0:
            unused_score=unused_score+5
        if int(genome[i+2]-genome[i+6])==0:
            unused_score=unused_score+5
    return unused_score
            
def overlab_func(genome):
    overlab_score=0
    for i in range(0,len(genome)-4,4):
        for j in range(0,len(genome)-4,4):
            if not(genome[i+2]<genome[j]<genome[i]):#x ha
                overlab_score=overlab_score+1
            if not(genome[i+1]<genome[j+3]<genome[i+3]):#y ha
                overlab_score=overlab_score+1
    return overlab_score
	
	
def av_function(genome):
    av_score=0
    vul=0
    room_centers=[]
    center=[40,40]
    for i in range(0,len(genome),4):
        center_X=float((genome[i]+genome[i+2])/2)
        center_Y=float((genome[i+1]+genome[i+3])/2)
        room_centers.append(center_X)
        room_centers.append(center_Y)
    for j in range(0,len(genome),4):
        for t in range(0,len(room_centers),2):
            if 40<genome[j]<room_centers[t]:
                vul=vul+1
            if 40<genome[j+2]<room_centers[t]:
                vul=vul+1
            if room_centers[t]<genome[j]<40:
                vul=vul+1
            if room_centers[t]<genome[j+2]<40:
                vul=vul+1
            if 40<genome[j+1]<room_centers[t+1]:
                vul=vul+1
            if 40<genome[j+3]<room_centers[t+1]:
                vul=vul+1
            if room_centers[t+1]<genome[j+1]<40:
                vul=vul+1
            if room_centers[t+1]<genome[j+3]<40:
                vul=vul+1
    if vul==1:
        av_score=5
    return av_score
		
def eval_func(genome):
    return light_func(genome)+inrange_func(genome)+unusedplace_func(genome)+overlab_func(genome)+av_function(genome)


gen_len=4*int(raw_input("how many rooms?"))
'''def eval_func(chromosome):
   score = 0.0
   # iterate over the chromosome
   for value in chromosome:
      if value==2:
         score += 1
   return score'''

genome = G1DList.G1DList(gen_len)
genome.setParams(rangemin=0, rangemax=80)
genome.evaluator.set(eval_func)
#genetic algorithm
ga = GSimpleGA.GSimpleGA(genome)
ga.setMutationRate(0.05)
ga.evolve(freq_stats=10)
print ga.bestIndividual()
#print genome
print scale
