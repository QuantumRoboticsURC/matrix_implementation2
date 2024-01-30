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


class MatrixSignalReciever(Node):
    def __init__(self):
        super().__init__('matrix_signal_receiver')
        # ________ ros atributes initialization ______

        self.subscription = self.create_subscription(Int8, '/matrix_signal', self.matrix_signal_callback, 1)
        #rospy.init_node("matrix_signal_reciever")
        #rospy.Subscriber("/matrix_signal", Int8, self.matrix_signal_callback, queue_size=1)

        # ________ Jetson TX2 initialization ______
        self.pin_1 = 15
        self.pin_2 = 22
        self.pin_3 = 37
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_1, GPIO.OUT)
        GPIO.setup(self.pin_2, GPIO.OUT)
        GPIO.setup(self.pin_3, GPIO.OUT)
        # ________ logic attributes initialization ______
        self.matrix_signal_to_color_dict = {0: "matrix_off", 1: "blue", 2: "red", 3: "green", 4:"quantum"}
        self.matrix_color = self.matrix_signal_to_color_dict[0]

    def matrix_signal_callback(self, data):
        self.matrix_color = self.matrix_signal_to_color_dict[data.data]
        #rospy.loginfo("new signal recieved, signal is: {s}".format(s = data.data))

    def main(self):
        while rclpy.ok():
            if self.matrix_color == "matrix_off":                
                GPIO.output(self.pin_3, GPIO.LOW)
                GPIO.output(self.pin_2, GPIO.LOW)
                GPIO.output(self.pin_1, GPIO.LOW)                 
            elif self.matrix_color == "blue":     
                GPIO.output(self.pin_3, GPIO.LOW)
                GPIO.output(self.pin_2, GPIO.LOW)           
                GPIO.output(self.pin_1, GPIO.HIGH)                
            elif self.matrix_color == "red":     
                GPIO.output(self.pin_3, GPIO.LOW)
                GPIO.output(self.pin_2, GPIO.HIGH)           
                GPIO.output(self.pin_1, GPIO.LOW)                
            elif self.matrix_color == "green":    
                GPIO.output(self.pin_3, GPIO.LOW)
                GPIO.output(self.pin_2, GPIO.HIGH)            
                GPIO.output(self.pin_1, GPIO.HIGH)                
            elif self.matrix_color == "quantum":
                GPIO.output(self.pin_3, GPIO.HIGH)
                GPIO.output(self.pin_2, GPIO.LOW)
                GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_3, GPIO.LOW)
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.LOW)
        GPIO.cleanup()

def main (args = None):
    rclpy.init(args=args)
    matrix_signal_reciever = MatrixSignalReciever()
    matrix_signal_reciever.main()
    rclpy.shutdown()

if __name__ == "__main__":
    main()