class ChooseDietPlan:
    diet_plans = ["1.Salt less","2.Fruit Diet","3.Keto Diet"]
    saltLess = ["Rasam","Idli","Dosa"]
    fruit_diet = ["Papaya","Watermelon","Cantalope"]
    keto_diet = ["ChickPea curry","Brocolie","Bellpeppers"]
    def __int__(self):
        pass

    def chooseDietPlan(self):
        fname = input("Enter your first name.")
        age = int( input("Enter your age."))
        weight = float(input("Enter your weight."))
        height = float(input("Enter your height."))
        fat = float(input("Enter your fat."))

        if weight> 80 and fat > 4:
            self.overWeight()
        else:
            self.normalWeight()

    def normalWeight(self):
        for a in range(0,len(self.diet_plans)):
            print(self.diet_plans[a])
        planNumber = int(input("Choose plan number to proceed."))
        self.choose_specific_dietPlan(planNumber)
        return  self.diet_plans

    def overWeight(self):
        for a in range(0,len(self.diet_plans)):
            print(self.diet_plans[a])
        planNumber = int(input("Choose plan number to proceed."))
        self.choose_specific_dietPlan(planNumber)
        return  self.diet_plans

    def choose_specific_dietPlan(self, planNumber):

        if planNumber == 1:
            for a in range(0, len(self.saltLess)):
                print(self.saltLess[a])
        elif planNumber == 2:
            for a in range(0, len(self.fruit_diet)):
                print(self.fruit_diet[a])
        elif planNumber == 3:
            for a in range(0, len(self.keto_diet)):
                print(self.keto_diet[a])
        else:
            print("No diet plan found in the system.")




