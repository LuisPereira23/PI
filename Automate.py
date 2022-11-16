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
    
camera_locations = []

number = 0

def build_camera_locations(start_location=(0,-3.43,2),step=0.1):
    current = step
    max_step = 0.4
    camera_locations.append(start_location)
    while current < max_step:
        camera_locations.append((start_location[0] + current, start_location[1], start_location[2]))
        camera_locations.append((start_location[0] - current, start_location[1], start_location[2]))
        camera_locations.append((start_location[0], start_location[1], start_location[2] + current))
        camera_locations.append((start_location[0], start_location[1],start_location[2] - current))
        camera_locations.append((start_location[0] + current, start_location[1], start_location[2] + current))
        camera_locations.append((start_location[0] + current, start_location[1], start_location[2] - current))
        camera_locations.append((start_location[0] - current, start_location[1], start_location[2] - current))
        camera_locations.append((start_location[0] - current, start_location[1], start_location[2] + current))
        current = current + step 
     
    print(camera_locations)
    #print(len(camera_locations)) 25

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
    global number
    lights = get_objects_from_collection("Lights")
    for light in lights:
        show_in_render(light)
        render(number)
        number = number + 1
        hide_in_render(light)

def change_color(color):
    obj = bpy.context.object
    bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = color
    
def update_camera(camera, location):
    
    focus_point = point=bpy.data.objects["Armature"].location + mathutils.Vector((-0.1,0,1.5))
    
    camera.location = location
    bpy.context.view_layer.update()
    
    looking_direction = camera.location - focus_point
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    
  
def main_loop():
    turn_off_lights()
    build_camera_locations()
    for color in colors:
        for location in camera_locations:
            update_camera(bpy.data.objects['Camera'],location)
            change_color(colors[color])
            loop_light()
    

main_loop()