class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан открыт")

    def reit(self, reit):
        self.reit=reit
        print(self.reit)


newRestaurant1=Restaurant("Рест", "чудесная кухня")
newRestaurant1.reit(10)
newRestaurant1.describe_restaurant()
newRestaurant1.open_restaurant()

newRestaurant2=Restaurant("Пицца", "норм кухня")
newRestaurant2.describe_restaurant()
newRestaurant2.open_restaurant()

newRestaurant3=Restaurant("Большепиццы!!!", "чудесная кухня")
newRestaurant3.describe_restaurant()
newRestaurant3.open_restaurant()
