class Player:
	def __init__(self,money,properties,icon): #should be form (int,list of properties, name of image file)
		self.money = money
		self.properties = properties
		self.icon = icon

	def gainMoney(moneygained): #method for when you get money 
		self.money += moneygained

	def loseMoney(moneylost): #method for when you spend/ lose money
		self.money -= moneylost



