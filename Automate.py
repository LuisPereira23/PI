import bpy
import os
from easybpy import *

def render(number):
    output_dir = r'C:\Users\Krow\Documents\Uni\PI\renders\test'
    output_file_pattern_string = 'test%d.jpg'
    
    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % number))
    bpy.ops.render.render(write_still = True)
    
def turn_off_lights():
      lights = get_objects_from_collection("Lights")
      for light in lights:
          hide_in_render(light)

def loop_light():
    lights = get_objects_from_collection("Lights")
    number = 0
    for light in lights:
        show_in_render(light)
        render(number)
        number = number + 1
        hide_in_render(light)
        
turn_off_lights()
loop_light()