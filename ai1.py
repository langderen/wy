from calendar import c
from re import A
import time
from typing import Dict

class Num:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def sort(self):
        if self.a > self.b:
            self.a, self.b = self.b, self.a
        if self.b > self.c:
            self.b, self.c = self.c, self.b
        if self.a > self.b:
            self.a, self.b = self.b, self.a

    def print(self):
        print(f"排序后的数据为：{self.a},{self.b},{self.c}")


    # numbers = Num(3, 1, 2)
    # numbers.sort()
    # numbers.print()



class Animal:
    def __init__(self,id,name,age,weight):
        self.id=id
        self.name=name
        self.age=age
        self.weight=weight
        self.ishungry=False
        self.healthlever=10
        self.species='未知'

    def die(self,reason):
        print(f'动物{self.name}由于过度{reason}死亡。')

    def feed(self):
        if self.ishungry == False:
            self.die('进食')
        else:
            self.ishungry = False
        
    def run(self):
        self.ishungry=True
        self.healthlever-=1
        if self.healthlever==0:
            self.die('跑动')

    def heal(self):
        if(self.healthlever==10):print(f'{self.name}健康状态优秀，请继续保持')
        else:
            self.healthlever=10
            print(f'{self.name}已医治完成。')

class Tiger(Animal):
    def __init__(self, id, name, age, weight):
        super().__init__(id, name, age, weight)
        self.species = '老虎'


class Dog(Animal):
    def __init__(self, id, name, age, weight):
        super().__init__(id, name, age, weight)
        self.species = '狗'

class lion(Animal):
    def __init__(self, id, name, age, weight):
        super().__init__(id, name, age, weight)
        self.species = '狮子'

class elephant(Animal):
    def __init__(self, id, name, age, weight):
        super().__init__(id, name, age, weight)
        self.species = '大象'

class monkey(Animal):
    def __init__(self, id, name, age, weight):
        super().__init__(id, name, age, weight)
        self.species = '猴子'
class zoo:
    def __init__(self):
        self.animals: Dict[int, Animal] = {}

    def add_animal(self, animal: Animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal_id: int):
        if animal_id in self.animals:
            del self.animals[animal_id]
            return True
        return False

    def find_animal(self, search_term: str) :
        return [a for a in self.animals.values() 
               if search_term.lower() in a.name.lower() 
               ]





def display_menu():
    print("---------------")
    print("动物园管理系统")
    print("1. 添加动物")
    print("2. 删除动物")
    print("3. 查找动物")
    print("4. 显示所有动物")
    print("-1. 退出")
    print("---------------")
    

if __name__ == "__main__":

    manager=zoo()
    
    display_menu()
    choice = input("请选择操作: ")
    while choice!=-1:
        
        if choice == '1':
            
            id=len(manager.animals)+1
            species=input("物种(老虎/狗/狮子/大象/猴子): ")
            if species=='老虎':
                Animal=Tiger
            elif species=='狗':
                Animal=Dog
            elif species=='狮子':
                Animal=lion
            elif species=='大象':
                Animal=elephant
            elif species=='猴子':
                Animal=monkey
            else:
                print("不支持该物种，添加失败")
                display_menu()
                choice = input("请选择操作: ")
                continue
            name=input("名称: ")
            age=int(input("年龄: "))
            weight=input("体重: ")
            animal = Animal(id,name,age,weight)
            manager.add_animal(animal)
            print(f"{animal.species}{animal.name}添加成功!")
            
        elif choice == '2':
            animal_id = input("输入要删除的动物id: ")
            if manager.remove_animal(animal_id):
                print("动物删除成功")
            else:
                print("未找到该动物")
                
        elif choice == '3':
            term = input("输入搜索词(名称/物种): ")
            results = manager.find_animal(term)
            for animal in results:
                print(f"{animal.id}: {animal.name} ({animal.species})")
                
        elif choice == '4':
            if len(manager.animals)==0:
                print('动物园内还没有动物！')
            for animal in manager.animals.values():
                print(f"ID: {animal.id} | 名称: {animal.name}  | 年龄: {animal.age}")
                
        elif choice == '-1':
            print("感谢使用动物园管理系统!")
            break
            
        else:
            print("无效选择，请重试")

        display_menu()
        choice = input("请选择操作: ")
