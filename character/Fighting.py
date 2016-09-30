import random

class NumGen():

    def _battle(self):
        hero = int (input("Please enter a number up to 10. "))
        monster = random.randint(1,10)
        """ x and z can both be used below without errors -- testing/learning"""

        randomNumber = random.randint(1,50)
        print ("hero attack does" , randomNumber ,"damg")
        if hero < monster:
            hero == ("winner")
            print("winner")
        elif hero > monster:
            hero == ("lose")
            print("lose")
        else:
            print("you lose")

        randomNumber = random.randint(1,50)
        print ("monster attack does" ,randomNumber,"damg")
        if monster < hero:
            monster == ("Winner")
            print("winner")
        elif monster > hero:
            monster == ("lose")
            print("lose")
        else:
            monster == ("monster defeated")
            print("monster defeated")

    def main(self):
        NumGen().mainloop()
        if __name__ == '__main__':()
