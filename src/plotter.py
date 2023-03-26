import numpy as np
import matplotlib.pyplot as plt

class Plot():

    def __init__(self, title, x_label, y_label) -> None:
        self.graph = plt
        self.graph.title(title)
        self.graph.ylabel(y_label)
        self.graph.xlabel(x_label)
        self.max_x = [0]
    
    def _plot_xlogx(self, x):
        x = np.linspace(np.min(x), np.max(x), 100)
        y = np.array(list(map(lambda v: v * np.log10(v), x)))
        self.graph.plot(x, y, color='red', linestyle='--', linewidth=2, label="xlogx")

    
    def add(self, x,y, c="purple", label=None):
        self.max_x = x if self.max_x[-1] < x[-1] else self.max_x

        #Cast to np arrays
        x = np.array(x)
        y = np.array(y)

        # add points to plot
        self.graph.scatter(x, y, color=c, label=label)

        #Get line of best fit
        # a, b = np.polyfit(x, y, 1)

        #add line of best fit to plot
        # self.graph.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)


    def show(self):
        # add xlog_10(x) as a baseline
        self._plot_xlogx(self.max_x)

        self.graph.legend()

        self.graph.show()
