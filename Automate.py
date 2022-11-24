import bpy
import os
from easybpy import *
import mathutils

colors = {
    "Black":(0,0,0,1)
    ,"White":(1,1,1,1)
    ,"LightSalmon":(1,0.63,0.48,1)
    ,"Gold":(1,0.843,0,1)
    }

number = 0


def render(number, camera):
    output_dir = r'C:\Users\Krow\Documents\Uni\PI\renders\test'
    output_file_pattern_string = 'test%d.jpg'
    
    bpy.context.scene.camera = camera
    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % number))
    bpy.ops.render.render(write_still = True)
    
def turn_off_lights():
      lights = get_objects_from_collection("Lights")
      for light in lights:
          hide_in_render(light)

def loop_light(camera):
    global number
    lights = get_objects_from_collection("Lights")
    for light in lights:
        show_in_render(light)
        render(number, camera)
        number = number + 1
        hide_in_render(light)

def change_color(color):
    obj = bpy.context.object
    bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = color
    
  
def main_loop():
    turn_off_lights()
    cameras = get_objects_from_collection("Cameras")
    for color in colors:
        for camera in cameras:
            change_color(colors[color])
            loop_light(camera)
    

main_loop()