from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import TextInput
from bokeh.plotting import figure

# Create a blue textbox
text_input = TextInput(value="Hello", title="Message:", background="blue", foreground="white")

# Create a layout for the textbox
layout = column(text_input)

# Add the layout to the current document
curdoc().add_root(layout)
