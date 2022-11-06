from zoo.my_zoo import Zoo

my_zoo = Zoo()
stop_date = 14

while my_zoo.date <= stop_date:
    my_zoo.run(duration=1)



