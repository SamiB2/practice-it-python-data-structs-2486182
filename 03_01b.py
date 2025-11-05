from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    john = Driver("John Wisley","BMW", 6)
    mickey = Driver("Mickey Trod", "Prius", 24)
    witty = Driver("Witty due", "Tesla", 72)
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(mickey, 554))
    return

if __name__ == "__main__":
    main()