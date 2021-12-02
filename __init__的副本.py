# -*- coding:utf-8 -*-



nanhang = [40, 60, 22]
chuanhang = [35, 50, 8]
xiahang = [45, 40]

v = [0,0,0]
max_v = [0,0,0]

restrict = 300
max_value = 300


for a in range(3):
  for b in range(3):
    for c in range(3):
      for d in range(3):
        for e in range(3):
          for f in range(3):
            for g in range(3):
              for h in range(3):
                
                v[a]+=40
                v[b]+=60
                v[c]+=22
                v[d]+=35
                v[e]+=50
                v[f]+=8
                v[g]+=45
                v[h]+=40
                
                if v[0]<= restrict and v[1]<=restrict and v[2]<=restrict:
                  if max(v[0], v[1], v[2])<max_value:
                    max_value = max(v[0], v[1], v[2])
                    max_v[0]=v[0]
                    max_v[1]=v[1]
                    max_v[2]=v[2]
                    
                    print str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)
                    
                v[0]=0
                v[1]=0
                v[2]=0

print max_value
print max_v