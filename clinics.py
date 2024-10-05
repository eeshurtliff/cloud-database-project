import firebase_admin
from firebase_admin import credentials, firestore


def alter_dictionary(db, collection_name, document_name, attributes_list, changed_attribute, value):
    
    results = db.collection(collection_name).document(document_name).get()
    current_values = results.to_dict()
    print(current_values)
    if changed_attribute in attributes_list:
        if type(value) == attributes_list[changed_attribute]:

            print(current_values[changed_attribute])
            current_values[changed_attribute] = value
            print(current_values)
            return current_values
        else:
            print('This is the wrong value type fr this attribute.')
            return None
    else:
        print('This attribute does not exist in this document')
        return None



def main():


    cred = credentials.Certificate("tennis_clinic_key.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    clinic_attributes = {'total students': int, 'student limit' : int, 'Day' : list}

    new_values = alter_dictionary(db, 'Clinics', 'Ages 11-13',clinic_attributes, 'Day', ['Monday', 'Wednesday', 'Friday'] )
    db.collection("Clinics").document("Ages 11-13").set(new_values)



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