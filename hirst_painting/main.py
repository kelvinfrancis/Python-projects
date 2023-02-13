# import colorgram
#
# image = colorgram.extract('image_colors.jpg', 20) # Extract colors from the image
# rgb_colors = []
# for n in range(20):
#     color = image[n].rgb
#     rgb_colors.append(tuple(color))
#
# print(rgb_colors)
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
              (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
              (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50)]

tim.setheading(208)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
