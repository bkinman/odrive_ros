from __future__ import print_function

import rospy
import odrive.core
import odrive.util


def controller_for_uuid(uuid, channel_type='usb'):
    """ Returns a controller with a given id, if a channel can be created """

    channels = odrive.core.find_usb_channels(odrive.util.USB_VID_PID_PAIRS, print)

    for channel in channels:
        od = odrive.core.object_from_channel(channel)
        od_uuid = (od.UUID_2 << 2*4*8) + (od.UUID_1 << 1*4*8) + od.UUID_0
        rospy.loginfo('Found ODrive with UUID %d', od_uuid)
        if hex(od_uuid) == uuid:
            return od
    return None
