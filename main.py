import arcade
import random

def main():
    shapes_data =["100,200,100",
                  "200,200,200",
                  "300,200,250",
                  "400,200,175",
                  "300,250,200"]
    our_colors =[arcade.color.REDWOOD,
                 arcade.color.DEEP_SKY_BLUE,
                 arcade.color.APPLE_GREEN,
                 arcade.color.BABY_PINK,
                 arcade.color.BRITISH_RACING_GREEN]
    arcade.open_window(700, 700, "string split demo")


    arcade.start_render()
    for line in shapes_data:
        data = line.split(",")
        current_color = random.choice(our_colors)
        bottom_y = int(data[1])
        height = int(data[2])
        center_y = bottom_y + height/2
        arcade.draw_rectangle_filled(int(data[0]),center_y ,
                                     50, int(data[2]), current_color)



    arcade.finish_render()


    arcade.run()


main()