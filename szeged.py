import networkx as nx
import time
import string
class swhn:
   def create_2_level(self):
       self.g2.add_cycle([0,1,2,3,4])
       self.run_in_each_level();
       self.g2.add_cycle([4,5,6,7,8,0])
       self.g2.add_cycle([0,8,9,10,11,1])
       self.g2.add_cycle([1,11,12,13,14,2])
       self.g2.add_cycle([2,14,15,16,17,3])
       self.g2.add_cycle([3,17,18,19,5,4])
       self.run_in_each_level();
       self.g2.add_cycle([5,19,20,21,6])
       self.g2.add_cycle([6,21,22,23,24,7])
       self.g2.add_path([7,24,25,9])
       self.g2.add_path([25,26,27,28,10])
       self.g2.add_path([28,29,12])
       self.g2.add_path([29,30,31,32,13])
       self.g2.add_path([13,32,33,15])
       self.g2.add_path([33,34,35,36,16])
       self.g2.add_path([36,37,38,18])
       self.g2.add_path([38,39,40,20])
       self.run_in_each_level();
   def   create_fix_8_vertex(self,pre , n):
       self.g2.add_path([n-1 , n , n+1 , pre[0]])
       n+=2
       self.g2.add_path([n-1 , n , n+1 , n+2 , pre[1] ])
       pre[0]=n;
       pre[1]=n+1
       n+=3
       self.g2.add_path([ n-1 , n , pre[2]])
       n+=1
       pre[2]=n
       self.g2.add_path([ n-1 , n , n+1 , n+2 , pre[3] ])
       pre[3]=n+1
       n+=3
       self.g2.add_path([ n-1 , n , pre[4] ])
       n+=1
       self.g2.add_path([ n-1 , n , n+1 , n+2 , pre[5] ])
       pre[4]=n
       pre[5]=n+1
       n+=3
       self.g2.add_path([ n-1 , n , pre[6] ])
       n+=1
       pre[6]=n
       self.g2.add_path([ n-1 , n , n+1 , n+2 , pre[7] ])
       pre[7]=n+1
       n+=3
       return n
   def   create_latest_vertex(self,pre,number_of_hexagon , n):
       j=8
       for temp_iii in range(0,number_of_hexagon):
           self.g2.add_path([ n-1 , n , n+1 , pre[j] ])
           pre[j]=n
           n+=2
           j+=1
       pre.append(n)
       return n
   def create_next_levels(self,pre,nl , vertex_number):
       nv=3
       previous_vertex_number = vertex_number
       for temp_ii in range(nv,nl):
           previous_vertex_number = vertex_number
           vertex_number = self.create_fix_8_vertex(pre , vertex_number)
           vertex_number = self.create_latest_vertex(pre,nv, vertex_number)
           self.run_in_each_level()
           nv+=1
       return previous_vertex_number
   def __init__(self):
      self.llw=[]
      self.g2=nx.Graph()
      self.number_of_vertex=0;
      self.pre_number_of_vertex=0
      self.level_number=0;
   def run_in_each_level(self):
      self.level_number+=1;
      self.number_of_vertex=len(self.g2)
      ret1=self.calculation_work();
      self.llw.append(ret1)
      print(ret1);
      self.pre_number_of_vertex=self.number_of_vertex;
   def format_print(self,cal_name,sz):
      ret1 ="[level number: "
      ret1+=str(self.level_number)
      ret1+=" ]\t\t[number of vertex : "
      ret1+=str(self.number_of_vertex)
      ret1+=" ]\t\t["
      ret1+=cal_name
      ret1+=" : "
      ret1+=str(sz)
      ret1+="]\n";
      return ret1;
   def work_for_szeged_sum(self):
      sz=self.szeged_sum()
      ret1=self.format_print("szeged_sum index",sz);
      return ret1;
   def szeged(self):
       sum=0
       d1=nx.all_pairs_shortest_path_length(self.g2)
       for ed1 in self.g2.edges():
           n1_e_g=0
           n2_e_g=0
           for i in range(0,self.number_of_vertex):
               if i != ed1[0] and i != ed1[1] :
                   if d1[ed1[0]][i] > d1[ed1[1]][i] :
                       n1_e_g +=1
                   elif d1[ed1[0]][i] < d1[ed1[1]][i] :
                       n2_e_g +=1
           sum += n1_e_g * n2_e_g
       return sum
   def szeged_sum(self):
       sum=0
       d1=nx.all_pairs_shortest_path_length(self.g2)
       for ed1 in self.g2.edges():
           n1_e_g=0
           n2_e_g=0
           for i in range(0,self.number_of_vertex):
               if i != ed1[0] and i != ed1[1] :
                   if d1[ed1[0]][i] > d1[ed1[1]][i] :
                       n1_e_g +=1
                   elif d1[ed1[0]][i] < d1[ed1[1]][i] :
                       n2_e_g +=1
           sum += n1_e_g + n2_e_g
       return sum
   def save_graph(self,name):
       import os
       curPath=os.path.join(os.getcwd(),"out")
       if not os.path.isdir(curPath):
          os.mkdir(curPath)
       nx.write_adjlist(self.g2,os.path.join(curPath,name+'.adjlist'))
       nx.write_dot(self.g2,os.path.join(curPath , name+'.dot'))
       fwname = os.path.join(curPath,"szeged_sum_index"+name+ ".txt")
       f1=open(fwname , "w");
       i=0
       for lm in self.llw:
           f1.write(lm)
           i+=1
       f1.close()
   def common_calculation(self,nl):
      self.create_2_level()
      pre = [22 , 23 , 26 , 27 , 30 , 31 , 34 , 35 , 37 , 39 , 41 ]
      vertex_number = 41
      vertex_number=self.create_next_levels(pre,nl, vertex_number)
      name_of_file='nanohorn_'+str(nl+2)+'__time__'+str(time.time())+time.strftime("__%Y_%m_%d_%H_%M_%S_%A", time.localtime())
      self.save_graph(name_of_file)
   def calculate_szeged_sum(self,nl):
      self.calculation_work= self.work_for_szeged_sum
      self.common_calculation(nl);
nl=int(raw_input('Enter number of layer of SWHN: HN[n] = '));
swhn1=swhn()
swhn1.calculate_szeged_sum(nl);
