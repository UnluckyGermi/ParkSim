import random
import utils
import numpy as np

class Person:

    def __init__(self, name, age, sex, height, weight, brave, vip):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.vip = vip
        self.brave = brave
        self.location = None
        
    def getAge(n):
        if n < 1887689: return random.randint(0, 4)
        elif n < 4163467: return random.randint(5, 9)
        elif n < 6689607: return random.randint(10, 14)
        elif n < 9107525: return random.randint(15, 19)
        elif n < 11489973: return random.randint(20, 24)
        elif n < 14038709: return random.randint(25, 29)
        elif n < 16825023: return random.randint(30, 34)
        elif n < 20075561: return random.randint(35, 39)
        elif n < 23999268: return random.randint(40, 44)
        elif n < 27945113: return random.randint(44, 49)
        elif n < 31644388: return random.randint(50, 54)
        elif n < 35067043: return random.randint(55, 59)
        elif n < 38074279: return random.randint(60, 64)
        elif n < 40555151: return random.randint(65, 69)
        elif n < 42755144: return random.randint(70, 74)
        elif n < 44522290: return random.randint(75, 79)
        elif n < 45816543: return random.randint(80, 84)
        elif n < 46807642: return random.randint(85, 89)
        elif n < 47254388: return random.randint(90, 94)
        elif n < 47367087: return random.randint(95, 99)
        else: return random.randint(100, 104)
    
    def getHeight(age):
        if age <= 1: return utils.getDiscreteNormalDistribution(68, 78)
        elif age == 2: return utils.getDiscreteNormalDistribution(80, 91)
        elif age == 3: return utils.getDiscreteNormalDistribution(87, 101)
        elif age == 4: return utils.getDiscreteNormalDistribution(94, 108)
        elif age <= 6: return utils.getDiscreteNormalDistribution(106, 124)
        elif age <= 8: return utils.getDiscreteNormalDistribution(119, 137)
        elif age <= 10: return utils.getDiscreteNormalDistribution(127, 150)
        elif age <= 12: return utils.getDiscreteNormalDistribution(139, 162)
        elif age <= 14: return utils.getDiscreteNormalDistribution(150, 171)
        elif age <= 16: return utils.getDiscreteNormalDistribution(152, 172)
        else: return utils.getDiscreteNormalDistribution(155, 185)
    
    def getImc(age):

        if age < 18:
            (x, y) = (16, 20)
            center = 16
        else:
            (x, y) = (15, 35)
            if age < 24: center = 22
            elif age < 34: center = 24
            elif age < 44: center = 25
            elif age < 54: center = 27
            elif age < 64: center = 28
            elif age < 74: center = 29
            elif age < 84: center = 30
            else: center = 28
        
        return utils.getDiscreteNormalDistribution(x, y, center)

    def getWeight(age, height):
        imc = Person.getImc(age)
        return round(imc * (height / 100) ** 2)

    def getVip():
        n = random.randint(0, 20)
        return n == 0

    def getRandomPerson():
        n = random.randint(0, 47385107)
        age = Person.getAge(n)
        height = Person.getHeight(age)
        weight = Person.getWeight(age, height)
        vip = Person.getVip()
        brave = random.randint(1, 3)
        sex = ['H', 'M'].__getitem__(random.randint(0,1))
        name = "Jose"

        return Person(name, age, sex, height, weight, brave, vip)

    def getRandomFullName(sex):
        return Person.getRandomName(sex) + " " + Person.getRandomSurname1() + " " + Person.getRandomSurname2()    
    
    def getRandomName(sex):
        if sex == 'H':
            prob = np.array(utils.freqnh) / sum(utils.freqnh)
            return np.random.choice(utils.namesh, p=prob)
        else:
            prob = np.array(utils.freqnm) / sum(utils.freqnm)
            return np.random.choice(utils.namesm, p=prob)
    
    def getRandomSurname1():
        prob = np.array(utils.freqsur1) / sum(utils.freqsur1)
        return np.random.choice(utils.surnames, p=prob)
    
    def getRandomSurname2():
        prob = np.array(utils.freqsur2) / sum(utils.freqsur2)
        return np.random.choice(utils.surnames, p=prob)