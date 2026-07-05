#in this file i will discuss logical operators like add,sub,mul,truediv
#boolean operators like greaterthan,lessthan,ge,le,

class product:
    def __init__(self,price,quantity):
        self.price=price
        self.quantity=quantity
        
    def __add__(self,other):
        new_price=self.price+other.price
        new_quantity=self.quantity+other.quantity
        return product(new_price,new_quantity)
    
    def __sub__(self,other):
        if self.price < other.price or self.quantity < other.quantity:
            raise ValueError("Cannot subtract resulting in negative price or quantity!")
        new_price = self.price - other.price
        new_quantity = self.quantity - other.quantity
        return product(new_price, new_quantity)
    
    def __mul__(self,other):
        new_price=self.price*other.price
        new_quantity=self.quantity*other.quantity
        return product(new_price,new_quantity)
    
    def __truediv__(self, other):
        if other.price == 0 or other.quantity == 0:
            raise ZeroDivisionError("Cannot divide by a product with zero price or quantity!")
            
        new_price = self.price / other.price
        new_quantity = self.quantity / other.quantity
        return product(new_price, new_quantity)
    
    def __eq__(self, other):
        if self.price==other.price and self.quantity==other.quantity:
            return True
        else:
            return False
    
    #less than
    def __lt__(self, other):
        if self.price<other.price and self.quantity<other.quantity:
            return True
        else:
            return False
    
    #greater than
    def __gt__(self, other):
        if self.price>other.price and self.quantity>other.quantity:
            return True
        else:
            return False
    
    #less than or equals
    def __le__(self, other):
        if self.price<=other.price and self.quantity<=other.quantity:
            return True
        else:
            return False
    
    #less than or equals
    def __ge__(self, other):
        if self.price>=other.price and self.quantity>=other.quantity:
            return True
        else:
            return False



#creating two products
p1=product(300,10)
p2=product(670,13)

#adding two objects using add function
print('===================adding p1 and p2 ===============')
p3=p1+p2      #no need to call the function just place + operator between them
print(f"after adding p1 and p2!\nthe new product is p3 \np3 price is: {p3.price}\nP3 quantity is: {p3.quantity}")


# #subtacting p2 from p3 it will give us new object equal to p1
print('===================Subtracting p2 from p3 ===============')
p4=p3-p2
print(f"after subtracting p2 from p3!\nthe new product is p4 \np4 price is: {p4.price}\nP4 quantity is: {p4.quantity}")

# multiplying p1 and p2 
print('=================== multiplying p1 and p2  ===============')
p5=p1*p2
print(f"after multiplying p1 and p2!\nthe new product is p5 \np5 price is: {p5.price}\nP5 quantity is: {p5.quantity}")


# Dividing p5 by p2 
print('===================Dividing p5 by p2  ===============')
p6=p5/p2
print(f"after Dividing p5 by p2!\nthe new product is p6 \np6 price is: {p6.price}\nP6 quantity is: {p6.quantity}")

# checking equality
print("==================== Checking equaltity===============")
print(f"p1 = p2 : {p1==p2}")
print(f"p1 = p4 : {p1==p4}")
print(f"p5 = p2 : {p5==p2}")

#checking less than
print('==================== Checking less than===============')
print(f"p1 < p2 : {p1<p2}")
print(f"p1 < p4 : {p1<p4}")
print(f"p5 < p2 : {p5<p2}")
#checking greater than
print('==================== Checking greater than===============')
print(f"p1 > p2 : {p1>p2}")
print(f"p1 > p4 : {p1>p4}")
print(f"p5 > p2 : {p5>p2}")
#checking less than equals to
print('==================== Checking less than equals to===============')
print(f"p1 <= p2 : {p1<=p2}")
print(f"p1 <= p4 : {p1<=p4}")
print(f"p5 <= p2 : {p5<=p2}")
#checking greater than equals to
print('==================== Checking greater than equals to===============')
print(f"p1 >= p2 : {p1>=p2}")
print(f"p1 >= p4 : {p1>=p4}")
print(f"p5 >= p2 : {p5>=p2}")