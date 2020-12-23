import colorgram

colors = colorgram.extract('image.jpg',6)
color_list = []
for color in (colors):
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    color_list.append(new_color)

print(color_list)