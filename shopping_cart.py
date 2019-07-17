class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None,total=0,items=[]):
      self.employee_discount=employee_discount
      self.total=total
      self.items=items
    def add_item(self, name, price, quantity=1):
      item_list=[]
      for i in range(quantity):
        item_list.append({'item':name,'price':price})
      self.items=self.items+item_list
      self.total+=price*quantity
      return self.total
    def mean_item_price(self):
      return self.total/len(self.items)
    def median_item_price(self):
      price_list=[]
      for x in range(len(self.items)):
        price_list.append(self.items[x]['price'])
      price_list.sort()
      if len(price_list)%2==0:
        low_mid=int(len(price_list)/2-1)
        high_mid=int(len(price_list)/2)
        median=(price_list[low_mid]+price_list[high_mid])
      else:
        mid=int(len(price_list)/2-0.5)
        median=price_list[mid]
      return median
    def apply_discount(self):
      if self.employee_discount!=None:
        discounted_total=self.total*(100-self.employee_discount)/100
        return discounted_total
      else:
        return "Sorry, there is no discount to apply to your cart. :("
    def void_last_item(self):
      last_item=self.items.pop()
      self.total-=last_item['price']
      return self.items