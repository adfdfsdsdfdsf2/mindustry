import arcade
WIDTH = 600
HEIGHT = 600
TITLE = 'Практическая часть'

arcade.open_window(WIDTH,HEIGHT,TITLE)
arcade.set_background_color(arcade.color.YALE_BLUE)
arcade.start_render()

# Вывод круга
x = 260; y = 475; rad = 85
arcade.draw_circle_filled(x,y,rad, arcade.color.ORANGE)

# Вывод треугольника слева
point_triangle = [ [ 100, 200], [ 100, 475], [250, 350 ] ] 
arcade.draw_polygon_filled(point_triangle, arcade.color.BLUE)

# Вывод треугольника СПРАВО
point_triangle = [ [ 275, 350], [ 425, 500], [425, 205] ] 
arcade.draw_polygon_filled(point_triangle, arcade.color.GREEN)
point_triangle = [ [ 50,100], [ 325, 225], [410, 50] ] 
arcade.draw_polygon_filled(point_triangle, arcade.color.RED)
arcade.finish_render()
arcade.run()