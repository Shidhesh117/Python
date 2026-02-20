import plotly.graph_objects as go
import numpy as np

def create_3d_scatter_plot():
    x=np.random.rand(100)
    y=np.random.rand(100)
    z=np.random.rand(100)

    scatter_plot=go.Figure(data=[go.scatter(x=x,y=y,z=z,mode='markers')])
    scatter_plot.show()
    scatter_plot.write_html("3d_scatter_plot.html")
create_3d_scatter_plot()
