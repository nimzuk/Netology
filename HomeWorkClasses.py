class Animal:
    can_eat = True
    alive = True
    sound = None
    limbs = 4
    tail = True
    rus_alias = 'Животное'
    name = str()

    def voice(self):
        print(self.sound)

    def die(self):
        self.alive = False

    def check(self):
        if self.alive == False:
            state = "умер!"
        else:
            state = "жив!"
        print(self.rus_alias + " " + self.name + " " + state)


class Mammal(Animal):
    feed_chiled = "milk"
    rus_alias = 'Млекопитающее'


class Bird(Animal):
    wings = True
    rus_alias = 'Птица'


class Cow(Mammal):
    sound = "Mooooooo!"
    rus_alias = 'Корова'


class Goat(Mammal):
    sound = "Beh!"
    rus_alias = 'Коза'


class Sheep(Mammal):
    sound = "Meh!"
    rus_alias = 'Овца'


class Pig(Mammal):
    sound = "Hryuk!"
    rus_alias = 'Свиня'


class Duck(Bird):
    sound = "Cryak!"
    rus_alias = 'Утка'


class Chicken(Bird):
    sound = "Coco!"
    rus_alias = 'Курица'


class Goose(Bird):
    sound = "Gaga!"
    rus_alias = 'Гусь'


donald = Duck()
piggy = Pig()
donald.name = "Дональдь"

piggy.name = "Пигги"

print(piggy.name)

print(donald.name)
donald.die()
donald.check()
piggy.check()

# Необходимо реализовать классы животных на ферме:
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси. Duck, chicken, goose.
# Условия:
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.