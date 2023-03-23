import numpy as np
import matplotlib.pyplot as plt

class Plot():

    def __init__(self) -> None:
        self.graph = plt
        self.graph.ylabel('slots')
        self.graph.xlabel('tags')
    
    def add(self, x,y):
        #Cast to np arrays
        x = np.array(x)
        y = np.array(y)

        #Get line of best fit
        a, b = np.polyfit(x, y, 1)

        # add points to plot
        self.graph.scatter(x, y, color='purple')

        #add line of best fit to plot
        self.graph.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)

        #add fitted regression equation to plot
        # self.graph.text(1, 17, 'y = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'x', size=14)

    def show(self):
        self.graph.show()

    # def test():
    #     #define data
    #     x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    #     y = np.array([2, 5, 6, 7, 9, 12, 16, 19])

    #     #find line of best fit
    #     a, b = np.polyfit(x, y, 1)

    #     #add points to plot
    #     plt.scatter(x, y, color='purple')

    #     #add line of best fit to plot
    #     plt.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)

    #     #add fitted regression equation to plot
    #     plt.text(1, 17, 'y = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'x', size=14)
    #     plt.show()