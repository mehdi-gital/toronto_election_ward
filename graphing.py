#!/usr/bin/python3

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.embed import file_html

plot = figure()
plot.circle([1,2], [3,4])
plot.line([1,2], [3,4])
#script, div = components(plot)
html = file_html(plot, CDN, "my plot")

f = open('graph.html', 'w') 
f.write(html)
