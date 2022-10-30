def Tshirt(func):
	def wrapper():
		func()
		print('Tshirt')
	return wrapper

def sweater (func):
	def wrapper():
		func()
		print('sweater')
	return wrapper

def hat(deco):
	def wrapper():
		deco()
		print('hat')
	return wrapper

def cap(func):
	def wrapper():
		func()
		print('cap')
	return wrapper

def pants(func):
	def wrapper():
		func()
		print('pants')
	return wrapper

def glove(deco):
	def wrapper():
		deco()
		print('glove')
	return wrapper



@cap
@hat
@sweater
@pants
@glove
@Tshirt

def cap():
	print('This is cap')


def hat():
	print('This is hat')

def sweater ():
	print('This is sweater')


def pants():
	print('This is pants')

def glove():
	print('This is glove')


def Tshirt():
	print('This is Tshirt')

cap()
hat()
sweater()
pants()
glove()
Tshirt()
