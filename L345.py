import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "Акно"

# открывает код

arcade.open_window(WIDTH, HEIGHT, TITLE )

# фон
arcade.set_background_color(arcade.color.AQUA)
arcade.start_render()


point_triangle =  [ [500,30], [800,500], [1200,30] ]
arcade.draw_polygon_filled(point_triangle,arcade.color.GRAY)

text = "score"
arcade.draw_text(text,10,700, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )


text = "time"
arcade.draw_text(text,80,700, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )


text = "coins"
arcade.draw_text(text,130,700, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )



text = "200"
arcade.draw_text(text,10,670, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )


text = "369"
arcade.draw_text(text,80,670, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )


text = "16"
arcade.draw_text(text,130,670, arcade.color.WHITE, 15, True, align="right", font_name="arial", bold=True, italic=True, anchor_x="center", anchor_y="center",  )

x = 700
y = 90
width_rect = 100
height_rect = 200
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 650
y = 10
width_rect = 1300
height_rect = 40
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x =  300
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 370
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 450
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 900
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 970
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 1050
y = 600
width_rect = 80
height_rect = 80
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BROWN)

x = 1050
y = 690
width_rect = 400
height_rect = 10
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BLACK)

x = 880
y = 690
width_rect = 60
height_rect = 50
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.YELLOW)


x = 60
y = 110
width_rect = 30
height_rect = 170
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 60
y = 220
width_rect = 80
height_rect = 180
arcade.draw_ellipse_filled(x, y, width_rect, height_rect, arcade.color.GREEN)

x = 160
y = 110
width_rect = 30
height_rect = 170
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 160
y = 220
width_rect = 80
height_rect = 180
arcade.draw_ellipse_filled(x, y, width_rect, height_rect, arcade.color.GREEN)


x = 500
y = 110
width_rect = 30
height_rect = 170
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 500
y = 220
width_rect = 80
height_rect = 180
arcade.draw_ellipse_filled(x, y, width_rect, height_rect, arcade.color.GREEN)


x = 550
y = 110
width_rect = 30
height_rect = 170
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 550
y = 220
width_rect = 80
height_rect = 180
arcade.draw_ellipse_filled(x, y, width_rect, height_rect, arcade.color.GREEN)





x = 1000
y = 110
width_rect = 30
height_rect = 170
arcade.draw_rectangle_filled(x,y,width_rect,height_rect,arcade.color.BRONZE)

x = 1000
y = 220
width_rect = 80
height_rect = 180
arcade.draw_ellipse_filled(x, y, width_rect, height_rect, arcade.color.GREEN)

x = 300
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)



x = 380
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)



x = 460
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)

x = 900
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)

x = 980
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)

x = 1060
y = 660
width_rect = 10
height_rect = 30
arcade.draw_rectangle_filled(x, y, width_rect, height_rect, arcade.color.CADMIUM_YELLOW)



arcade.finish_render()
arcade.run()