class Player:
	def __init__(self,money,properties,icon,pos): #should be form (self, int, list of properties, name of image file)
		self.money = money
		self.properties = properties
		self.icon = icon
                self.pos = pos #Current space the piece is on (0-39)

	def gainMoney(moneygained): #method for when you get money 
		self.money += moneygained

	def loseMoney(moneylost): #method for when you spend/ lose money
		self.money -= moneylost



