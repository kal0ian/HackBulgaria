class Product(object):
	def __init__(self,name, stock_price,final_price):
		self.name=name
		self.stock_price=stock_price
		self.final_price=final_price
	def profit(self):
		return self.final_price-self.stock_price
class Laptop(Product):
	def __init__(self,name, stock_price,final_price,diskspace,RAM):
		self.name=name
		self.stock_price=stock_price
		self.final_price=final_price
		self.diskspace=diskspace
		self.RAM=RAM
class Smartphone(Product):
	def __init__(self,name, stock_price,final_price,display_size,mega_pixels):
		self.name=name
		self.stock_price=stock_price
		self.final_price=final_price
		self.display_size=display_size
		self.mega_pixels=mega_pixels
class Store(object):
	products_laptop={}
	products_smartphone={}
	money_earned=0
	def __init__(self,name):
		self.name=name

	def  load_new_products(self,product,count):
		if type(product) is Smartphone:
			self.products_smartphone[product]=[product.name,count]
		if type(product) is Laptop:
			self.products_laptop[product]=[product.name,count]


	def  list_products(self,product_class):
		if product_class is Smartphone:
			for i in self.products_smartphone:
				print self.products_smartphone[i]
		if product_class is Laptop:
			for i in self.products_laptop:
				print self.products_laptop[i]

	def sell_product(self,product):
		
		for i in self.products_laptop:	
			if i == product:
				if self.products_laptop[i][1]==0:
					return False
				else:
					self.money_earned +=product.profit()
					buf = self.products_laptop[i][1]
					self.load_new_products(product,buf-1)
					return True
			else: 
				return False
		for i in self.products_smartphone:
			if i == product:
				if self.products_smartphone[i][1]==0:
					return False
				else:
					self.money_earned +=product.profit()
					buf = self.products_smartphone[i][1]
					self.load_new_products(product,buf-1)
					
					return True
			else: 
				return False

	def  total_income(self):
		return self.money_earned

store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
print store.sell_product(smarthphone) # True
print store.sell_product(smarthphone) # True

print store.total_income() # 640

