
def good_day_flow(my_zoo):
    my_zoo.status()  
    my_zoo.work_manager.activate_workers()
    my_zoo.animal_cages.activate_animals()     
    my_zoo.status()  
    my_zoo.date +=1

def bad_day_flow(my_zoo):
    my_zoo.status()  
    # my_zoo.work_manager.activate_workers()
    my_zoo.animal_cages.activate_animals()     
    my_zoo.status()  
    my_zoo.date +=1
