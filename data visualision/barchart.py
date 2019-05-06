import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .1

malta_scores = (554, 536, 538)
canada_scores = (310, 200, 500)
china_scores = (400, 350, 200)

index = np.arange(col_count)

def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width()/2.,height*1.05,
                 '%d' % int(height),
                 ha='center', va='bottom')


k1 = plt.bar(index, malta_scores, bar_width,
             alpha = .5,
             label="Malta")

ca1 = plt.bar(index+0.1, canada_scores, bar_width,
             alpha = .5,
             label="Canada")

ch1 = plt.bar(index+0.2, malta_scores, bar_width,
             alpha = .5,
             label="China")

CreateLabels(k1)
CreateLabels(ca1)
CreateLabels(ch1)

plt.ylabel("Mean Score in Pisa 2012")
plt.xlabel("Subjects")
plt.title("Subjects in Countries")

plt.xticks(index + .3/2, ("Math", "Science", "Programming"))
plt.legend(frameon=False, bbox_to_anchor=(1,1),loc=2)
plt.grid(True)



plt.show()
