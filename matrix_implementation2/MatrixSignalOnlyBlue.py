#!/usr/bin/env python3

"""Made by:
	José Ángel del Ángel
    joseangeldelangel10@gmail.com

Code description:
TODO - add description

Notes:

"""

import rclpy
from rclpy.node import Node 
import Jetson.GPIO as GPIO
from std_msgs.msg import String, Int8, Header



class MatrixSignalOnlyBlue:
    def __init__(self):
        # ________ ros atributes initialization ______
        rclpy.init()
        self.node = rclpy.create_node("matrix_signal_only_blue")  

        # ________ Jetson TX2 initialization ______
        self.pin_1 = 15
        self.pin_2 = 22
        self.pin_3 = 37
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_1, GPIO.OUT)
        GPIO.setup(self.pin_2, GPIO.OUT)
        GPIO.setup(self.pin_3, GPIO.OUT)
        # ________ logic attributes initialization ______
        self.matrix_signal_to_color_dict = {1: "blue"}
        self.matrix_color = self.matrix_signal_to_color_dict[1]

        self.matrix_signal_publisher = rclpy.Publisher('/matrix_signal', Int8, queue_size=1)
        self.matrix_signal_msg = Int8()

        self.matrix_signal_msg.data = 1
        self.r = rclpy.create_rate(10)

                    
                               

    def matrix_signal_callback(self, data):
        self.matrix_color = self.matrix_signal_to_color_dict[data.data]
        #rospy.loginfo("new signal recieved, signal is: {s}".format(s = data.data))*

    def main(self):
        while rclpy.ok():        
            if self.matrix_color == "blue":     
                GPIO.output(self.pin_3, GPIO.LOW)
                GPIO.output(self.pin_2, GPIO.LOW)           
                GPIO.output(self.pin_1, GPIO.HIGH)
                self.matrix_signal_publisher.publish(self.matrix_signal_msg)    
                self.r.sleep()

        GPIO.output(self.pin_3, GPIO.HIGH)
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.LOW)
             
        GPIO.cleanup()
   



if __name__ == "__main__":
    try:
        matrix_signal_only_blue = MatrixSignalOnlyBlue()
        matrix_signal_only_blue.main()
    except rclpy.exceptions.ROSInterruptException:   
        print("Exception")                           
