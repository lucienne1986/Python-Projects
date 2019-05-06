import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'names': ['Nick', 'Lucy', 'Panda'],
            
            'jan_ir': [124, 100, 200],
            'feb_ir': [100, 210, 210],
            'march_ir':[165, 35, 165]
            }

df = pd.DataFrame(raw_data, columns = ['names', 'jan_ir', 'feb_ir', 'march_ir'])
df['total_ir']=df['jan_ir']+df['feb_ir'] + df['march_ir']

color = [('r'),('b'),('g')]

plt.pie(df['total_ir'],
        labels=df['names'],
        colors=color,
        autopct='%1.1f%%')

plt.axis('equal')
        
plt.show()



