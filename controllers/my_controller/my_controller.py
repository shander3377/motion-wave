"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motion, Keyboard
# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

motion_file = Motion("../../motions/wave.motion")
# - perform simulation steps until Webots is stopping the controller
timestep=32
keyboard.enable(timestep)
while robot.step(timestep) != -1:
    if(keyboard.getKey() == Keyboard.UP):
        motion_file.play()