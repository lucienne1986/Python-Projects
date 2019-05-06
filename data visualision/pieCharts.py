import matplotlib.pyplot as plt

labels= 'Python', 'PHP', 'Java', 'C++', 'Perl', 'C#'
pops = [20, 30, 45, 17, 90, 2]
separated = (.1, .3, 0, 0, .6, 0)

plt.pie(pops, labels=labels, autopct = '%1.1f%%')
plt.axis('equal')
plt.show()
