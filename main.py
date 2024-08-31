class Dog(object):
    number_of_foot = 4
    is_tail = True

    def go(self):
        for item in range (1, self.number_of_foot + 1):

            print(f'step{item}', end='')
            print()

    def say(self):
        print('wof-wof-wof!')

class Cat(object):
    number_of_foot = 4
    is_tail = True

    def go(self):
        for item in range(1, self.number_of_foot + 1):

            print(f'step{item}', end='')
            print()

    def say(self):
        print('meow!')

print("DjMarioMc asking to a dog:")
print("- mr.Doggy, after 3 steps, give your 'wof'")
print('the Dog')
a_1 = Dog()
a_1.number_of_foot = 3
a_1.go()
a_1.say()

print('-'*100)

print('It,s a cat')
a_2 = Cat()
a_2.number_of_foot = 1
a_2.go()
a_2.say()
