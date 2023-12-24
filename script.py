import module

choice = int(input("Please, choose the task 1-3 (0-EXIT): "))
while choice:
    if choice==1:
        module.find_min_max();
    elif choice==2:
        module.points_in_yellow_region();
    elif choice==3:
        result = module.check_convergence()
        print(f"The series converges up to n = {result}")
    else:
        print("Wrong task number!")
    choice = int(input("Please, choose the task again (0-EXIT): "))
print("Good by!") 