import plotly.graph_objects as go
import numpy as np
from PIL import Image
import plotly.io as pio

pio.renderers.default = "browser"

# Load the Earth texture image
img = Image.open('Globe/earth.png')  # Use a 2:1 aspect ratio equirectangular projection
img = img.resize((360, 180))  # Resize for consistent mapping
img_data = np.array(img)

# Generate sphere coordinates
theta = np.linspace(0, 2 * np.pi, img_data.shape[1])
phi = np.linspace(0, np.pi, img_data.shape[0])
theta, phi = np.meshgrid(theta, phi)

# Sphere coordinates
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Normalize RGB image data for surfacecolors
surfacecolor = img_data / 255.0

# Create the surface plot
fig = go.Figure(data=[go.Surface(
    x=x,
    y=y,
    z=z,
    surfacecolor=surfacecolor[..., 0],  # Use R channel or grayscale; Plotly doesn't accept RGB directly
    cmin=0,
    cmax=1,
    showscale=False
)])

# Adjust layout for globe effect
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='data',
    ),
    margin=dict(t=0, b=0, l=0, r=0)
)

fig.show()
print(surfacecolor)