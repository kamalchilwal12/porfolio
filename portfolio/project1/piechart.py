import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])

mylabels = ["Apples","Banana","Orange","Dates"]

mycolors = ["red","yellow","orange","brown"]

plt.pie(y,labels=mylabels,colors=mycolors)

plt.show()