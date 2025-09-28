from abc import abstractmethod
#车辆类

class Car:
    def __init__(self,brand,model,price,count):
        self.brand=brand
        self.model=model
        self.price=price
        self.count=count
#加购车辆
    def purchase(self,n):
        self.count+=n


    def showcount(self):
        print(f"{self.brand}{self.model}库存{self.count}辆")


#车辆子类奥迪
class Aodi(Car):
    def __init__(self,  model, price, count):
        super().__init__("奥迪", model, price, count)

#车辆子类问界
class Wenjie(Car):
    def __init__(self,  model, price, count):
        super().__init__("问界", model, price, count)



#车辆子类奔驰
class Benchi(Car):
    def __init__(self,  model, price, count):
        super().__init__("奔驰", model, price, count)


#车辆子类宝马
class Baoma(Car):
    def __init__(self,  model, price, count):
        super().__init__("宝马", model, price, count)

        
#车辆子类小米
class Xiaomi(Car):
    def __init__(self,  model, price, count):
        super().__init__("小米", model, price, count)


#顾客类
class Customer:
    def __init__(self,name="不愿意透露姓名的美男子"):
        self.name=name

    def buy(self,seller,car):
        seller.count+=1
        print(f"顾客{self.name}在销售{seller.name}处购买了一辆{car.brand}{car.model}花费了{car.price}元")
        print(f"销售{seller.name}现已销售{seller.count}单")
            

#销售类
class Seller:
    def __init__(self,name):
        self.name=name
        self.count=0

    def show(self):
        print(f"销售{self.name}（本月已售出{self.count}单）为您服务")
        print("本店销售有奔驰、奥迪、宝马、问界等多品牌的多种车型")


class User:
    @abstractmethod
    def __init__(self,name,age,sex) -> None:
        pass

    def run(self,l):
        pass

    def eat(self,w):

        pass
    def sleep(self,t):
        pass



if __name__=="__main__":
#创建4辆车
    car1=Aodi("A6",160000,50)
    car2=Xiaomi("yu7",250000,10)
    car3=Wenjie("m8",270000,60)
    car4=Benchi("E300L",500000,30)
    cars={car1,car2,car3,car4}
    
    customer=Customer("许文业")
    seller=Seller("王彧")
    seller.show()
    customer.buy(seller,car3)