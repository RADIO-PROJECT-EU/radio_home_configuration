#!/usr/bin/env python
import rospkg

def init():
    rospack = rospkg.RosPack()
    yaml_file = rospack.get_path('radio_home_configuration') + '/config/current_configuration.yaml'
    raw_input('Welcome to RADIO Home configuration.\nThis is just a command line tool, but future version will include a GUI!\nPress ENTER to continue\n')
    s = ""
    while(True):
        ans = raw_input('Please enter the name of the room:\n')
        s += '\n-\n  name: "' + ans + '"'
        ans = raw_input('Please enter the x coordinate of the room:\n')
        s += '\n  x: ' + ans
        ans = raw_input('Please enter the y coordinate of the room:\n')
        s += '\n  y: ' + ans
        ans = raw_input('Please enter the z coordinate of the room:\n')
        s += '\n  z: ' + ans
        ans = raw_input('Please enter the w coordinate of the room:\n')
        s += '\n  w: ' + ans
        ans = raw_input('Please enter the name of the icon for the room: (Available image names: common_area2, doc, gym, kitchen, livingroom, my_room, spoon)\n')
        s += '\n  image: "' + ans + '"'
        while not (ans == 'y' or ans == 'n'):
            ans = raw_input("Do you want to add another room? (y/n)\n")
        if ans == 'n':
            break
    f = open(yaml_file, 'w')
    f.write(s)
    f.close()
    print 'Configuration saved!'

if __name__ == '__main__':
    init()