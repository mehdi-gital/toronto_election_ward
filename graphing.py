#!/usr/bin/python3

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.embed import file_html

import numpy as np
import sklearn.datasets.samples_generator as samples_generator

X, y = samples_generator.make_blobs(n_samples=200, centers=[(3.5,5), (-3.5,5)], cluster_std=0.4)
c_X = np.arange(-5,5,0.1)
c_y = ((c_X ** 2) * 2 / 25) + np.random.normal(0,0.2, 100)

plot = figure()
plot.circle(X[:,0],X[:,1])
plot.circle(c_X, c_y)
#script, div = components(plot)
html = file_html(plot, CDN, "my plot")

f = open('graph.html', 'w') 
f.write(html)
