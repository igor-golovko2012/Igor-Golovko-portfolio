# Программа создает список потенциальных сотрудников из списка и сохраняет его в отдельный файл
# Потом программа рандомно назначает сотрудников на разные позиции и сохраняет эту информацию в другой файл.
# так же в отдельные файлы сохраняется информация о руководителе и о зароботном фонде


import random

#  это вызов функции, которая отвечает за правильные множественные окончания при выводе списков
#  функция сохранена как отдельный файл в папке с программой
from choose_plural import choose_plural

import csv

class Person(object):   #object это универсальный класс родитель(можно не указывать)
        
    P_AGE0 = 70     # верхняя возрастная планка для мужчин (0)
    P_AGE1 = 65     # верхняя возрастная планка для женщин (1)
    
    def __init__(self, n, g, a):
        
        self.name = n           #name - это ФИО
        self.gender = int(g)         #gender - это пол 
        self.age = int(a)            #age - это кол-во полных лет
 #       a и g  передаются из csv файла, как строки, поэтому я явно привожу их к int.
     
  
    def __str__(self):    # перегружаем метод строки для более комфортного вывода на печать
        
        return f"ФИО: {self.name:30}  Возраст:\t{self.age:3} " + choose_plural(self.age, ['год', 'года', 'лет'])
# в возвращаемой строке в зависимости от возраста будет выводиться 'лет', 'год' или 'года'

 # эта функция для возврата срока от 18 до 65 или 70 в зависимости от пола    
    def appoint(self):
                
        res1 = self.age >= 18   # результат 1 - больше или равно 18 (для всех)
        
        if self.gender == 0:
            curr_p_age = Person.P_AGE0    # если пол мужской (0), то верхняя планка 70 (стр 5)
        else:
            curr_p_age = Person.P_AGE1    # в противном случае верхняя планка 65 (стр 6)
        res2 = self.age < curr_p_age     # результат 2 - меньше верхней планки
        
        res = res1 and res2
        
        return res
        
 # более короткий вариант   return 18 <= self.age < Person.P_AGE0 if self.gender == 0 else 18 <= self.age < Person.P_AGE1
    
  # эта функция нужна при формировании класса Employee (будет передавать свойства класса Person)
    def get_attrs(self):
        return self.name, self.gender, self.age

 # это переименование необходимо, чтобы можно было вывести список кандидатов в алфавитном порядке   
    def __gt__(self, other):
        return self.name > other.name
     
class Employee(Person):    # наследник класса Person
    counter = 1    # счетчик сотрудников компании
    
    POSITIONS = ['Шеф', 'Заместитель', 'Руководитель подразделения', 'Полевой сотрудник']    
    SALARY0 = 45_000.00     #базовый уровень зарплаты
    SALARY = [100,10,5,1]    # коэффициенты повышения зар.платы (в соответствии с позициями в 45 строке)
    DEPTS = ['Штаб квартира', 'Новосибирск', 'Хабаровск']
    
    def __init__(self, n, g, a, p, d):     # к трем свойствам добавляем еще два  
         
               
        super().__init__(n, g, a)     #обозначаем наследованные свойства Можно написать Person.__init__(n, a)

        self.position = p     
        self.department = d   
        self.salary = Employee.SALARY0*Employee.SALARY[self.position]  
 # в последней строке расчет зарплаты в зависимоти от позиции сотрудника      
    
        self.counter = Employee.counter
        Employee.counter += 1   # здесь производится подсчет количества всех сотрудников компании (вместе с шефом)

# это переименование необходимо, чтобы можно было вывести сотрудников по отделам  
    def __gt__(self, other):
        return self.position > other.position
    
    def __str__(self):    # здесь использовал тройные кавычки, чтобы строка читалась более комфортно
    
        return f'''
ФИО: {self.name:28} ({self.age} {choose_plural(self.age, ['год', 'года', 'лет'])})
  Отдел: {Employee.DEPTS[self.department]:15}
    Должность: {Employee.POSITIONS[self.position]:20}
      Зарплата: {self.salary}''' + choose_plural(self.salary, [' рубль', ' рубля', ' рублей'])

    #  эта функция для случайного выбора сотрудников, она определена как статичный метод (@staticmethod)

    @staticmethod
    def rand_pick(seq):
        return seq.pop(random.randint(0,len(seq)-1)), seq 
    #   еще один статичный метод для расчета зароботного фонда 

    @staticmethod
    def get_salary_fund(c):
        fund = 0
        for e in c:
            fund += e.salary
        return fund

class Boss(Employee):     
    
    def __init__(self, n, g, a, p, d, b, u):
        
        super().__init__(n, g, a, p, d)
        
        self.bonus = b    
        self.under = u      # количество подчиненных
        
    def __str__(self):    # здесь использовал тройные кавычки, чтобы строка читалась более комфортно
    
        return f'''
ФИО: {self.name:28} ({self.age} {choose_plural(self.age, ['год', 'года', 'лет'])})
  Отдел: {Employee.DEPTS[self.department]:15}
    Должность: {Employee.POSITIONS[self.position]:20}
    Количество подчиненных: {(Employee.counter - 1):25}
      Зарплата: {self.salary}''' + choose_plural(self.salary, [' рубль', ' рубля', ' рублей'])    

#  # в строке выше я использовал функцию "choose_plural(x, words):" дважды - один раз внутри и в конце путем сложения.
       
def main():
     
# формируем объекты класса Person - потенциальные кандидаты на работу. 
    people = []
    
# берем список людей из csv файла 'peoples', который лежит в папке с основной программой.    
    with open('peoples.csv', 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            people.append(Person(*i))
       
 # Определяем пригодных к найму по возрасту
    candidates = []
    for i in people:
        if i.appoint():    # функция appoint прописана в классе Person (стр 23)
            candidates.append(i)
    with open('Candidates list.txt', 'w', encoding='utf-8') as output:
        print("Список потенциальных кандидатов\n", file=output)            
        print(*sorted(candidates), sep='\n', file=output)

    # Сформируем объекты класса Employee
 
    company = []
    boss = []
    
    # Назначаем Шефа
    c, candidates = Employee.rand_pick(candidates)
    company.append(Employee(*c.get_attrs(), 0, 0))
    #  три атрибута присваиваются при помощи функции get_attrs, потом должность (0) и отделение (0).
    boss.append(Boss(*c.get_attrs(), 0, 0, 0, 3))
    
    # Назначаем Заместителя
    c, candidates = Employee.rand_pick(candidates)
    company.append(Employee(*c.get_attrs(), 1, 0))
    boss.append(Boss(*c.get_attrs(),1, 0, 0, 2))
    
    # Назначаем остальных в случайные подразделения
    for i in range(len(candidates)):
        c, candidates = Employee.rand_pick(candidates)
        d = random.randint(1, 2)
        company.append(Employee(*c.get_attrs(), 3, d))
        
    # Сортируем компанию по подразделению
    company.sort(key=lambda x:x.department)
    
    # Назначаем руководителей подразделений
    
    # Распределяем объекты по подразделениям
    dworkers = {0:[],1:[],2:[]}
    for i in company:
        dworkers[i.department].append(i)
    
    # Ищем самого старого
    for d in [1,2]:
        oldest = 0
        for i in range(len(dworkers[d])):
            if dworkers[d][i].age > dworkers[d][oldest].age:
                oldest = i
        rand_bonus = random.randint(10,25)*1000
        boss.append(Boss(*dworkers[d][oldest].get_attrs(), 2,
             d,rand_bonus,len(dworkers[d])-1))
        dworkers[d][oldest].position = 2
        dworkers[d][oldest].salary = Employee.SALARY0*Employee.SALARY[2]+rand_bonus
   
    with open('Company_list.txt', 'w', encoding='utf-8') as output:  
        print("Список сотрудников компании\n", file=output)
        print(*sorted(company[1::]), sep='\n', file=output)

    with open('Head of company.txt', 'w', encoding='utf-8') as output:       
        print("Руководитель компании\n", file=output)
        for i in boss[0:1]:
            print(i, file=output)        
    
    with open('Salary Fund.txt', 'w', encoding='utf-8') as output:
        print("                 Общий зароботный фонд\n", file=output)
        sf = Employee.get_salary_fund(company) #вывод на печать общего зарплатного фонда.
        print(f"Общий зароботный фонд: {sf: 15} {choose_plural(sf, [' рубль', ' рубля', ' рублей'])}\n", file=output)
        
        sfBoss = Employee.get_salary_fund([company[0]])    # вывод на печать зарплаты 1 сотрудника(босса)
        print(f"Зарплата руководителя: {sfBoss: 15} {choose_plural(sfBoss, [' рубль', ' рубля', ' рублей'])}\n", file=output)
        print(f"Зарплата остальных сотрудников: {sf - sfBoss: 15} {choose_plural((sf - sfBoss), [' рубль', ' рубля', ' рублей'])}\n", file=output)
    
        
main()


