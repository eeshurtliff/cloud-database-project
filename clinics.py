import firebase_admin
from firebase_admin import credentials, firestore


# https://console.firebase.google.com/u/0/project/tennis-clinics/firestore/databases/-default-/data/~2FClinics~2FAges%2011-13



def update_document(db, collection_ref, document_name, changed_attribute, value):
    

    results = collection_ref.document(document_name).get()
    
    current_values = results.to_dict()
    # print(current_values)

    if changed_attribute in current_values:
        try:
            value = int(value)
        except:
            pass
        # if type(current_values[changed_attribute]) not in (int, list, str, float, dict):
            
            # print(f'value = {student_attributes[key]}')
            # if update_total_students(db, value, 'add'):
            #     update_total_students(db, current_values[changed_attribute], 'subtract')
            #     new_value = {changed_attribute: value}
            #     collection_ref.document(document_name).set(new_value, merge=True)
            #     return True
            # else:
            #     return False

            # if update_total_students(db, current_values[changed_attribute], )
                
        if type(value) == type(current_values[changed_attribute]):
            # print(value)
            new_value = {changed_attribute: value}
            collection_ref.document(document_name).set(new_value, merge=True)
            return True
        
        else:
            print('This is the wrong value type for this attribute.')
            print(current_values[changed_attribute])
            return False
        
    else:
        confirm = input('This attribute does not exist in this document. Are you sure you want to add it? (y/n)')
        if confirm.lower() == 'y':
            new_value = {changed_attribute: value}
            collection_ref.document(document_name).set(new_value, merge=True)
            return True
        else:
            return False

def add_document(db, collection_name, attributes_list):
    
    
    print('Please provide the details below: ')
    doc_details = {}

    for attribute in attributes_list:
        while True:
            if type(attributes_list[attribute]) == list:
                if attributes_list[attribute][0] == 'reference':
                    while True:
                        print('Please select an option below:')
                        options = db.collection(attributes_list[attribute][1]).get()
                        if attributes_list[attribute][1] == 'Clinics':
                            display_clinics(db.collection('Clinics'))
                        elif attributes_list[attribute][1] == 'Students':
                            
                            display_students(db.collection('Students'))
                        else:
                            pass
                        index = get_choice_index(len(options))

                        choice = options[index].id
                        reference = db.collection(attributes_list[attribute][1]).document(choice)
                        allowed = update_total_students(db, choice, 'add')
                        if allowed == True:
                            break

                        
                    doc_details[attribute] = reference
                    break
            
            else:
                answer = input(f"{attribute}: ")
                if type(answer) == attributes_list[attribute]:
                    doc_details[attribute] = answer
                    break
                    
                else:
                    print(f'This is the wrong value type for this attribute. it should be a {attributes_list[attribute]}')

    db.collection(collection_name).add(doc_details)

def update_total_students(db, document_name, action):
    record = db.collection('Clinics').document(document_name).get()
    data = record.to_dict()
    current = data['Total Students']
    total_allowed = data['Student Limit']
    if action == 'add':
        if current + 1 <= total_allowed:
            current += 1
            update_document(db, db.collection('Clinics'), document_name, 'Total Students', current)
            return True
        else:
            print('Error: The clinic is already full. Choose another clinic or contact the coach. ')
            return False
    else:
        if current - 1 >= 0:
            current -= 1
            update_document(db, db.collection('Clinics'), document_name, 'Total Students', current)
            return True
        else:
            print('Error: The clinic is already full. Choose another clinic or contact the coach. ')
            return False


    
def admin_pass():
    password = 'JkLmO'
    num_attempts = 0
    while True:
        attempt = input('What is the administration password?')
        if attempt == password:
            return True
        else:
            num_attempts += 1
            print(f'Incorrect. {3 - num_attempts} attempts left. ')
            if num_attempts == 3:
                return False
        


def get_choice_index(number_of_options):
    while True:
        try:
            choice = int(input("Select the number of your choice: "))


            if choice <= 0 or choice > number_of_options + 1:
                print('That number is not one of the options above. Please try again.')
            else:
                return choice - 1
                
        except:
            print('Please select one of the numbers in the menu above. ')

def choose_attribute_to_update(db, collection_ref, collection_record):
    display_list(collection_ref)
        
    index = get_choice_index(len(collection_record))
    choice = collection_record[index].id
    record = collection_ref.document(choice).get()
    data = record.to_dict()
    keys = list(data.keys())
    
    number = 1
    print()
    print('Which attribute would you like to update? ')
    for key in keys:
        print(f'{number}. {key}')
        number += 1
    attribute_index = get_choice_index(len(keys))
    attribute = keys[attribute_index]
    while True:
        if type(data[attribute]) not in (int, list, str, float, dict):
                # print(f'value = {student_attributes[key]}')
                # attribute_record = data[attribute].get()
                # print(f'This student is currently in {attribute_record.id}')
                # path = data[attribute].path
                # split_path = path.split('/')
                # collection_name = split_path[0]
                # options = db.collection(collection_name).get()
                # display_list(db.collection(collection_name))
                # index = get_choice_index(len(options))
                # choice = options[index]
                # value = db.collection(collection_name).document(choice)

                # accepted = update_document(db, collection_ref, choice, attribute, value)
                # if accepted == True:
                #     break
                print('This attribute cannot be updated currently. ')
                break
                
        else:
            
            value = input(f'What would you like to change \'{attribute}\' to?(write stop to leave.) ')
            if value == 'stop':
                break
            
            accepted = update_document(db, collection_ref, choice, attribute, value)
            if accepted == True:
                break
        

def create_attribute_list(db, collection_name, reference_collection):
    this_collection = db.collection(collection_name).get()
    first_in_collection = this_collection[0].to_dict()
    keys = list(first_in_collection.keys())
    
    attributes = {}
    for key in keys:
        attributes[key] = type(first_in_collection[key])

        if type(first_in_collection[key]) not in (int, list, str, float, dict):
            
            attributes[key] = ['reference' , reference_collection]

    return attributes

def display_list(collection_ref):
    path = collection_ref.id
    
    if path == 'Clinics':
        display_clinics(collection_ref)
    else:
        display_students(collection_ref)



def display_clinics(all_clinics):
    print()
    print(f'---------------Available Classes------------------')
    records = all_clinics.get()
    if records == None:
        print('There are no current Clinics')
    else:
        number_of_records = 0
        for record in records:
            number_of_records += 1
            print(f'{number_of_records}. {record.id}')

    

def display_students(all_students):
    print()
    records = all_students.get()
    if records == None:
        print('There are no current Students')
    else:
        number_of_records = 0
        print(f'--------------------Students----------------------')
        for record in records:
            data = record.to_dict()
            number_of_records += 1
            print(f"{number_of_records}. {data['First Name']} {data['Last Name']}")


def menu():
    print('----------------- Main Menu -----------------')
    print('1. View all Clinics')
    print('2. View all Students')
    print('3. Add a student to the Clinic')
    print('4. Delete a student from a Clinic')
    print('5. Update details')
    print('6. Done!')
    return get_choice_index(6)
    

def main():


    cred = credentials.Certificate("tennis_clinic_key.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()




    while True:
        clinic_attributes = create_attribute_list(db, 'Clinics', None)
        student_attributes = create_attribute_list(db, 'Students', 'Clinics')
        all_clinics = db.collection('Clinics')
        all_students = db.collection('Students')
        clinic_options = all_clinics.get()
        student_options = all_students.get()
        number = menu()
        number += 1
        if number == 1:
            display_clinics(all_clinics)

        elif number == 2:
            display_students(all_students)

        elif number == 3:
            add_document(db, 'Students', student_attributes)
            
        elif number == 4:
            print('Notice: You must be the coach to access this event. ')
            if admin_pass():
                display_students(all_students)
                index = get_choice_index(len(student_options))
                print(len(student_options))
                print(index)
                choice = student_options[index].id
                student = all_students.document(choice).get()
                print(student.id)
                data = student.to_dict()
                
                document_name = data['Clinic'].path.split('/')[1]
                update_total_students(db, document_name, 'remove')
                all_students.document(choice).delete()
            else:
                print('You do not have access to this event. ')
            
            
        elif number == 5:
            print('1. Update a Student')
            print('2. Update a Clinic')
            choice = get_choice_index(2)
            choice += 1
            if choice == 1:

                choose_attribute_to_update(db, all_students, student_options)
            if choice == 2:
                print('Notice: You must be the coach to access this event. ')
                if admin_pass():
                    choose_attribute_to_update(db, all_clinics, clinic_options)
                    # display_clinics(all_clinics)
                    # index = get_choice_index(len(clinic_options))
                    # choice = clinic_options[index].id
                    # record = all_clinics.document(choice).get()
                    # data = record.to_dict()
                    # keys = data.keys()
                    # number = 1
                    # print()
                    # for key in keys:
                    #     print(f'{number}. {key}')
                    #     number += 1
                    # print('Which attribute would you like to update?')
                    # attribute_index = get_choice_index(len(keys))
                    # attribute = keys[attribute_index]
                    # while True:
                    #     value = input(f'What would you like to change \'{attribute}\' to?(write stop to leave.)')
                    #     if value == 'stop':
                    #         break
                        
                    #     accepted = update_document(db, 'Clinics', choice, attribute, value)
                    #     if accepted == True:
                    #         break
                else:
                    print('You do not have access to this event. ')
        else:
            break


    
    

    



    # chosen_clinic = db.collection("Clinics").document(choice).get()
    # data = chosen_clinic.to_dict()
    # print('Data: ')
    # print(data)

    # db.collection("Clinics").document(choice).set
        
        




    # result = db.collection("Clinics").get()
    # total = 0
    # for record in result:
    #     data = record.to_dict()
    #     print(record.id)

    # choice = input("Select a clinic: ")
    # result = db.collection("Clinics").document(choice).get()
    # data = result.to_dict()
    # if data is None:
    #     print("Invalid class")
    # else:
    #     print(f" {data['Total Students']} / {data['Student Limit']}")


    # choice = input("Select a clinic: ")
    # new_limit = int(input("What is the new size limit for this class: "))
    # db.collection("Clinics").document(choice).set({"Total Students" : 1, "Time" : "3:30pm", "Day" : "MWF", "Student Limit" : new_limit})


    # db.collection("Clinics").document("Ages 11-13").set({"Total Students" : 3, "Time" : "3:30pm", "Day" : "TRS", "Student Limit" : 6})


    # results = db.collection("Students").get()
    # for result in results:
    #     data = result.to_dict()
    #     print(f"name = {data['First Name']}")

if __name__ == "__main__":
    main()