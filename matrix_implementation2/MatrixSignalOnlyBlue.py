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
from std_msgs.msg import Int8



class MatrixSignalOnlyBlue(Node):
    def __init__(self):
        super().__init__("matrix_signal_only_blue")  

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

        self.matrix_signal_publisher = self.create_publisher(Int8, '/matrix_signal', 10)
        self.matrix_signal_msg = Int8()

        self.matrix_signal_msg.data = 1
        self.timer = self.create_timer(0.1, self.main)

    def matrix_signal_callback(self, msg):
        self.matrix_color = self.matrix_signal_to_color_dict[msg.data]
        #self.get_logger().info("new signal recieved, signal is: {s}".format(s = msg.data))

    def main(self):
        if self.matrix_color == "blue":     
            GPIO.output(self.pin_3, GPIO.LOW)
            GPIO.output(self.pin_2, GPIO.LOW)           
            GPIO.output(self.pin_1, GPIO.HIGH)
            self.matrix_signal_publisher.publish(self.matrix_signal_msg)    
        else:
            GPIO.output(self.pin_3, GPIO.HIGH)
            GPIO.output(self.pin_1, GPIO.LOW)
            GPIO.output(self.pin_2, GPIO.LOW)
             
        GPIO.cleanup()


def main(args=None):
    rclpy.init(args=args)
    matrix_signal_only_blue = MatrixSignalOnlyBlue()
    rclpy.spin(matrix_signal_only_blue)
    matrix_signal_only_blue.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
