class CashDesk(object):
    money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def __init__(self):
        pass

    def take_money(self,taken_money):
        for i in taken_money:
        	self.money[i]=taken_money[i] 
    def total(self):
    	sum=0
    	for i in self.money:
    		sum+=i*self.money[i]
    	return sum
    def can_withdraw_money(self,amount_of_money):
    	if self.total()>=amount_of_money:
    		return True
    	return False
my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.total())
print(my_cash_desk.can_withdraw_money(30))
print(my_cash_desk.can_withdraw_money(80))