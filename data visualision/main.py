import matplotlib.pyplot as plt

years = [1, 1000, 1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1980, 1990, 1995, 2000, 2005, 2010, 2015]


pops = [200, 400, 450, 500, 682, 791, 1000, 1262, 1658, 2525, 2758,
        3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735, 6125, 6520]


deaths = [50, 100, 200, 250, 300, 350, 400, 450, 500, 550, 600,
        650, 700, 750, 800, 850, 900, 950, 1000, 1500, 2000]

#linear graph
#plt.plot(years, pops, '----',color = (255/255, 100/255, 100/255))
#plt.plot(years, deaths, color = (200/255, 180/255, 100/255))


lines = plt.plot(years, pops, years, deaths)
plt.grid(True)

plt.setp(lines, color = 'r', marker="o")
plt.ylabel("Population in billion")
plt.xlabel("Population growth by year")

plt.title("Population Growth")

plt.show()
