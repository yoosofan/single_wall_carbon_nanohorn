import networkx as nx
import time
import string
#import pylab as plt
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
   #
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
   #
   def   create_latest_vertex(self,pre,number_of_hexagon , n):
       j=8
       for temp_iii in range(0,number_of_hexagon):
           self.g2.add_path([ n-1 , n , n+1 , pre[j] ])
           pre[j]=n
           n+=2
           j+=1
       pre.append(n)
       return n
   #
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
#
   def __init__(self):
      self.llw=[]
      self.g2=nx.Graph()
      self.number_of_vertex=0;
      self.pre_number_of_vertex=0
      self.level_number=0;
      self.do_save_picture= False;
#
   def run_in_each_level(self):
      self.level_number+=1;
      self.number_of_vertex=len(self.g2)
      ret1=self.calculation_work();
      self.llw.append(ret1)
      print(ret1);
      self.pre_number_of_vertex=self.number_of_vertex;
#
   def format_print(self,cal_name,sz):
      '''
      work in python 3
      ret1="[level number: {0} ]\t\t[number of vertex : {1} ]\t\t [szeged_sum index : {2} ]\n";
      #ret1.format(self.level_number,self.number_of_vertex,sz);
      #"{{{0}}} {1} ;-}}".format("I'm in braces", "I'm not") ;
      '''
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
#
   def work_for_szeged_sum(self):
      sz=self.szeged_sum()
      ret1=self.format_print("szeged_sum index",sz);
      return ret1;
#
   def work_for_wiener_index(self):
      sz=self.wiener_high_speed_high_memory()
      ret1=ret1=self.format_print("wiener index",sz);
      return ret1;
#
   def work_for_save_picture(self):
      sz= self.number_of_vertex
      ret1=ret1=self.format_print("number of vertex",sz);
      return ret1;
#
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
#
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
#
   def wiener(self , last_previous_level_vertex_number , previous_level_wiener):
       sum=0
       n=self.level_number
       #print('last vertex in wiener ' , last_previous_level_vertex_number )
       for i in range(last_previous_level_vertex_number , n):
           path=nx.single_source_shortest_path(self.g2,i)
           for j in range(0,last_previous_level_vertex_number):
               sum+= (len(path[j]) -1)*(len(path[j]) -1)*(len(path[j]) - 1)
           for j in range(i+1,n):
               sum += (len(path[j]) - 1)*(len(path[j]) - 1)*(len(path[j]) - 1)
       #print path
       return sum+previous_level_wiener
#
   def wiener_low_memory(self):
       sum=0
       n=self.level_number
       for i in range(0,n):
           for j in range(i+1,n):
               sum += nx.shortest_path_length(self.g2 , i , j)
       return sum
#
   def wiener_high_speed_high_memory(self):
       sum=0
       n=self.number_of_vertex
       d1=nx.all_pairs_shortest_path_length(self.g2)
       for i in range(0,n):
           for j in range(i+1,n):
               sum+= d1[i][j]
       return sum
#
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
#
   def save_picture_of_graph(self, name):
      import os
      curPath=os.path.join(os.getcwd(),"out")
      if not os.path.isdir(curPath):
          os.mkdir(curPath)
      #g4=pgv.AGraph(os.path.join('out' , name+'.dot'))
      g4=nx.to_agraph(self.g2)  # g3=nx.from_agraph(g4); g3 will be in networkx graph type
      #g4.graph_attr['label']='nano horn '
      g4.node_attr['shape']='' # box circle diamond
      g4.edge_attr['color']='black'
      g4.draw(os.path.join(curPath , name+'.png'),prog="neato")
      g4.draw(os.path.join(curPath , name+'.svg'),prog="neato")
      g4.draw(os.path.join(curPath , name+'.jpg'),prog="neato")
      g4.draw(os.path.join(curPath , name+'.gif'),prog="neato")
      #nx.draw(g2)
      #plt.savefig(os.path.join('out' , name +'.png'))
#
   def verify_graph(self,previous_level_last_vertex):
       for i in range(0,previous_level_last_vertex+2):
           if self.g2.degree(i) != 3 :
               print("error degree of " , i , " is not 3 ")
       print('end of verify ')
#
   def comment4nextg(self):
       '''
       End of second level
       Node 20 (last one) belongs to the pentagon which is created first on second level
       self.g2.add_path([40,41,42,22])
       self.g2.add_path([42,43,44,45,23])
       n=45
       #print nx.connected_components(g2)
       #g1=self.g2.copy()
       #print self.g2.nodes()
       #print self.g2.edges()
       #print(self.g2.degree(1))
       '''
       temp_ii=12
#
   def common_calculation(self,nl):
      self.create_2_level()
      pre = [22 , 23 , 26 , 27 , 30 , 31 , 34 , 35 , 37 , 39 , 41 ]
      vertex_number = 41
      vertex_number=self.create_next_levels(pre,nl, vertex_number)
      name_of_file='nanohorn_'+str(nl+2)+'__time__'+str(time.time())+time.strftime("__%Y_%m_%d_%H_%M_%S_%A", time.localtime())
      self.save_graph(name_of_file)
      if self.do_save_picture == True :
         self.save_picture_of_graph(name_of_file)
      self.verify_graph(vertex_number)
#
   def calculate_szeged_sum(self,nl):
      self.calculation_work= self.work_for_szeged_sum
      self.common_calculation(nl);
#
   def calculate_wiener_index(self,nl):
      self.calculation_work= self.work_for_wiener_index;
      self.common_calculation(nl);
#
   def create_picture(self,nl):
      self.do_save_picture= True;
      self.calculation_work= self.work_for_save_picture;
      self.common_calculation(nl);
#
def run():
   nl=int(raw_input('Enter number of layer of SWHN: HN[n] = '));
   #print(type(nl),'  ' ,str(nl));
   swhn1=swhn()
   print('Enter calculation you need\n')
   which_calculation=raw_input('Wiener index [W] or Szeged_index [S] or Both [B] otherwise save picture of graph ')
   which_calculation=which_calculation.strip().lower()
   if which_calculation == 'w':
      swhn1.calculate_wiener_index(nl);
   elif  which_calculation == 's':
      swhn1.calculate_szeged_sum(nl);
   elif  which_calculation == 'b':
      swhn1.calculate_wiener_index(nl);
      swhn1.calculate_szeged_sum(nl);
   else:
      swhn1.create_picture(nl);
#
run();
