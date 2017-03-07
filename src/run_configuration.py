#!/usr/bin/env python
import os
import yaml
import rospy
import rospkg
from std_msgs.msg import String

def init():
    rospy.init_node('radio_home_configuration')
    publisher = rospy.Publisher('radio_home_rooms', String, queue_size=1, latch=True)
    rospack = rospkg.RosPack()
    yaml_file = rospack.get_path('radio_home_configuration') + '/config/current_configuration.yaml'
    if not os.path.isfile(yaml_file):
        print 'Please create a configuration first. Exiting...'
        return
    s_ = String()
    stream = open(yaml_file, 'r')
    home = yaml.load(stream)
    for room in home:
        if len(s_.data) > 0:
            s_.data += ','
        name = ''
        x = ''
        y = ''
        z = ''
        image = ''
        for n, v in room.items():
            if n == 'name':
                name = v
            elif n == 'x':
                x = str(v)
            elif n == 'y':
                y = str(v)
            elif n == 'z':
                z = str(v)
            elif n == 'image':
                image = v
        s_.data += name + ',' + x + ',' + y + ',' + z + ',' + image
    publisher.publish(s_)
    while not rospy.is_shutdown():
        rospy.spin()


if __name__ == '__main__':
    init()