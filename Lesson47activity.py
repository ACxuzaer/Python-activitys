# Create Class
class Employee:

    # Initializing
    def _init_(self):
        print('Employee created')

    #Calling destructor
    def _del_(self):
        print("Destructor called")


def create_obj():
    print('Making object...')
    obj = Employee()
    print('funtion end...')
    return obj


print('Calling create_obj() funtion...')
obj = create_obj()
print('Program End...')