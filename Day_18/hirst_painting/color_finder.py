import colorgram

# Full file path to the image
image_path = r'C:\Without_Sync\Py\python-100-days\Day_18\hirst_painting\dots.jpeg'
rgb_colors=[]


# Extract the colors from the image
colors = colorgram.extract(image_path, 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# Print the colors
print(rgb_colors)