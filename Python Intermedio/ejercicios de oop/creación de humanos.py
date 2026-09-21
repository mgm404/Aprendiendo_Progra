class Torso:
	def __init__(self, right_arm, left_arm, right_leg, left_leg, head):
		self.left_arm = left_arm
		self.right_arm = right_arm
		self.right_leg = right_leg
		self.left_leg = left_leg
		self.head = head

class Hand:
	def __init__(self):
	    pass

class Arm:
	def __init__(self, hand):
		self.hand = hand

class Foot():
	def __init__(self):
            pass

class Leg():
	def __init__(self, foot):
		self.foot = foot

class Head():
	def __init__(self):
            pass

class Human():
	def __init__(self, torso):
            self.body = torso

#right
right_hand = Hand()
right_arm = Arm(right_hand)
right_foot = Foot()
right_leg = Leg(right_foot)

#left
left_hand = Hand()
left_arm = Arm(left_hand)
left_foot = Foot()
left_leg = Leg(left_foot)

head = Head()

torso = Torso(right_arm, left_arm, right_leg, left_leg, head)

human = Human()