# Base class representing a general County in Kenya
class County:
    def __init__(self, name, population_millions):
        # Attributes initialized via constructor
        self.name = name                  # County name
        self.population_millions = population_millions  # Population in millions

    # Method to print basic info - demonstrating encapsulation by controlling access 
    def info(self):
        print(f"{self.name} County has a population of {self.population_millions} million.")

    # Placeholder method for county-specific major activity (to be overridden)
    def major_activity(self):
        print(f"{self.name} County has diverse activities.")

# Child class inherits from County and specializes major_activity method (polymorphism)
class AgriculturalCounty(County):
    def __init__(self, name, population_millions, main_crop):
        super().__init__(name, population_millions)  # Inherit name and population
        self.main_crop = main_crop                    # Specific to AgriculturalCounty

    # Override major_activity with county-specific farming info
    def major_activity(self):
        print(f"{self.name} County primarily produces {self.main_crop}.")

# Child class inheriting County with a focus on tourism
class TourismCounty(County):
    def __init__(self, name, population_millions, main_attraction):
        super().__init__(name, population_millions)
        self.main_attraction = main_attraction        # Specific to TourismCounty

    # Overriding major_activity to show tourism
    def major_activity(self):
        print(f"{self.name} County is famous for {self.main_attraction}.")

# Creating instances for different counties
nairobi = TourismCounty("Nairobi", 4.9, "national parks and city life")
kisii = AgriculturalCounty("Kisii", 1.34, "tea and bananas")
mombasa = TourismCounty("Mombasa", 1.37, "beaches and historical sites")

# List of counties to demonstrate polymorphism
counties = [nairobi, kisii, mombasa]

# Loop to print info and major activity for each county
for county in counties:
    county.info()           # Calls base class method
    county.major_activity() # Calls overridden method based on actual object class
