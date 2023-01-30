from picarx import Picarx
import time

class Manuvering():
	def __init__(self):
		self.picar = Picarx()

	def delay_stop(self):
		time.sleep(0.5)
		self.picar.stop()
		self.picar.set_dir_servo_angle(0)

	def Moveit(self, order = "forward"):
		if order == "forward":
			self.picar.always_forward(75)
			self.delay_stop()
		elif order == "backward":
			self.picar.always_backward(75)
			self.delay_stop()
		elif order == "forward left":
			self.picar.set_dir_servo_angle(-30)
			self.picar.forward(75)
			self.delay_stop()
		elif order == "forward right":
			self.picar.set_dir_servo_angle(30)
			self.picar.forward(75)
			self.delay_stop()
		elif order == "backward left":
			self.picar.set_dir_servo_angle(-30)
			self.picar.backward(75)
			self.delay_stop()
		elif order == "backward right":
			self.picar.set_dir_servo_angle(30)
			self.picar.backward(75)
			self.delay_stop()
		elif order == 'stop':
			self.picar.stop()

	def estop(self):
		self.picar.stop()

	def parallel_park(self, order = "left"):
		if order == "left":
			self.picar.set_dir_servo_angle(0)
			self.picar.forward(75)
			self.picar.set_dir_servo_angle(-30)
			time.sleep(0.5)
			self.picar.set_dir_servo_angle(30)
			self.delay_stop()

		elif order == "right":
			self.picar.set_dir_servo_angle(0)
			self.picar.forward(75)
			self.picar.set_dir_servo_angle(30)
			time.sleep(0.5)
			self.picar.set_dir_servo_angle(-30)
			self.delay_stop()

	def kturning(self, order="left"):

		if order == "right":
			self.Moveit("forward right")

			self.picar.set_dir_servo_angle(-30)
			self.picar.backward(50)
			self.delay_stop()

			self.picar.set_dir_servo_angle(20)
			self.picar.forward(75)

			time.sleep(0.5)
			self.picar.set_dir_servo_angle(0)
			self.delay_stop()

		elif order == "left":
			self.Moveit("forward left")

			self.picar.set_dir_servo_angle(30)
			self.picar.backward(50)
			self.delay_stop()

			self.picar.set_dir_servo_angle(-20)
			self.picar.forward(75)
			time.sleep(0.5)
			self.picar.set_dir_servo_angle(0)
			self.delay_stop()


if __name__ == "__main__":
	manuvering = Manuvering()
	actions = ["forward right", "backward right", "forward left", "backward left","forward", "backward"]
	dirs = ["left", "right"]
	while True:
        
		usr_input = int(input("Choose maneuver: \n1] move in direction \n2] park in direction \n3] k-turn \n4] stop \n5] exit \n"))
		manuvering.estop()

		if usr_input == 1:
			print("choose: forward right, backward right, forward left, backward left, forward")
			ip = input("direction to move: ")
			if ip in actions:
				manuvering.Moveit(ip)
			else:
				continue

		elif usr_input == 2:
			ip = input("Parallel park left or right:")
			if ip in dirs:
				manuvering.parallel_park(ip)
			else:
				continue

		elif usr_input == 3:
			ip = input("k-turning left or right: ")
			if ip in dirs:
				manuvering.kturning(ip)
			else:
				continue

		elif usr_input == 4:
			manuvering.estop()

		elif usr_input == 5:
			manuvering.estop()
			break
		else:
			print("Choose Action => ")