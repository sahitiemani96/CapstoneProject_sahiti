import random
from Modals import FoodChoices as FoodChoices
import ChooseDietPlan as ChooseDietPlan
class Diet_Plan_main:



    def __init__(self):
        self.healthy_food = ["carrots","fruits","nuts"]
        self.unhealthy_food = ["chips","pizza","popcorn"]
        self.choose_diet_plan = ChooseDietPlan.ChooseDietPlan()

    def welcome_message(self):
        print("Welcome to vFIT Healthy Eating Diet Plan")

    def user_input(self):
        food_intrest= input("what is your favourite food?")
        self.food_choices(food_intrest)

    def food_choices(self, food_intrest):

        if food_intrest in self.healthy_food :
            print("Well done!!!! your eating healthy!!!!! Let's celebrate with "+random.choice(self.healthy_food))
            diet_plan = self.choose_diet_plan.chooseDietPlan()


        elif food_intrest in self.unhealthy_food:
            random.shuffle(self.healthy_food)
            print("You change the diet plan accordingly......to healthy version eating")
            for i in range(3):
                print(self.healthy_food[i]+"\n")
            diet_plan = self.choose_diet_plan.chooseDietPlan()


        else:
            print("Your food choices are not in our database,but we guess that is an unhealthy eating so here we have few alternatives")
            print(random.shuffle(self.healthy_food))
            food_interest2= input("what is your favourite food?")
            self.food_choices(food_interest2)
            diet_plan = self.choose_diet_plan.chooseDietPlan()

    def seedUnHealthyFood(self):
        f = FoodChoices.FoodChoices("chips")
        self.unhealthy_food.append(f)
        f = FoodChoices.FoodChoices("popcorn")
        self.unhealthy_food.append(f)

    def seedHealthyFood(self):
        f = FoodChoices.FoodChoices("carrots")

        self.healthy_food.append(f)

        f = FoodChoices.FoodChoices("fruits")
        self.healthy_food.append(f)
