##new_name=input("Enter name of the patient to store it")
##new_name=input("Enter a name to search")
##new_name=input("Enter a name to remove patient")

patient_map={1:"arun",2:"babu",3:"ajay",4:"akhil",5:"",6:"jerin"}
patients = [1,2,3,4,5,6]
curr_patients=len(patient_map.keys())

def add_patients(name):
    
    patient_map[curr_patients+1]=name
    patients.append(curr_patients)
    if(patient_map[curr_patients+1] is not "" ):
        return "patient added successfully"


def remove_patient(name):
    
    patient_list= patient_map.values()
    if (name in patient_list):
        for i in patients:
            
            if patient_map[i] == name:
                patient_map[i]=""
                if(patient_map[i]==""):
                    print("patient removed success")
    else:
        print("patient no found")

      

def search_patient_bed(name):
    
    for i in range(0,len(patients)):
        if (patient_map[i+1]==""):
            print("there are 200 beds numbered from 0-199")
            print("empty bed found at",i)
        elif (patient_map[i+1]==name):
            print("there are 200 beds numbered from 0-199 ")
            print(patient_map[i+1],"'s bed has been found at bed no ",i)
        else :
            print("patient no in hospital")

print(remove_patient(new_name))
