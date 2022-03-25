menu={"sandwich":20, "parantha":25, "burger":25, "maggi":25, "fried rice":50}

def get_order():
	current_order=[]
	while True:
		print("--->What do you want to order?")
		order=input()
		if order in menu:
			current_order.append(order)
		else:
			print("--->Sorry we don't serve that")
			continue
		if is_order_complete():
			return current_order
			
def is_order_complete():
	choices=["yes", "no"]
	choice=""
	while choice not in choices:
		choice=input("--->Anything else? yes/no: ")
	if choice=="no":
		return True
	elif choice=="yes":
		return False
		
		
def output_order(order_list):
	print("--->So you want")
	sm=0
	for order in order_list:
		print(f"\t{order} {menu[order]}Rs")
		sm+=menu[order]
	print(f"\tTotal cost= {sm}Rs")
		
def main():
	print(menu)
	order=get_order()
	output_order(order)
	print("--->Please take your order from window no. 2<---")
	
if __name__=="__main__":
	while True:
		print("NEW ORDER")
		main()
		print("\n\n\n")
			
			
