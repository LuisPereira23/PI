import bpy
import os
from easybpy import *
import mathutils

colors = {
    "Black":(0,0,0,1)
    ,"White":(1,1,1,1)
    ,"LightSalmon":(1,0.63,0.48,1)
    ,"Gold":(1,0.843,0,1)
    ,"Olive":(0.375,0.852,0.137,1)
    }
    
lengths = [1, 0.95, 1.1, 1.13]

thickness = [1, 0.9, 1.1, 1.13]

bones = ["thumb.02.R", "thumb.03.R", "finger_index.01.R", "finger_index.02.R", "finger_index.03.R", "finger_ring.01.R", "finger_ring.02.R", "finger_ring.03.R", "finger_pinky.01.R", "finger_pinky.02.R", "finger_pinky.03.R", "finger_middle.01.R", "finger_middle.02.R", "finger_middle.03.R", "hand.R"]
    
number = 0


def render(number, camera):
    output_dir = r'C:\Users\Krow\Documents\Uni\PI\renders\B'
    output_file_pattern_string = 'B%d.jpg'
    
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
            for length in lengths: 
                print(length)
                for thick in thickness:
                    change_bone_scale(length, thick)
                    
                    change_color(colors[color])
                    loop_light(camera)
                    
                    change_bone_scale(1,1)

     
def change_bone_scale(length, thickness):
    armature = bpy.data.objects["Armature"]
    for bone in bones:
        pb = armature.pose.bones.get(bone)
        pb.scale = (thickness, length, 1)
        


main_loop()
#change_bone_scale(0.9,1)
