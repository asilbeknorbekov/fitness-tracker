import json
import os
from datetime import datetime

#########################################################################################################################
####################################Classes############################################################################
#########################################################################################################################


class Workout(object):
    def __init__(self,duration, calories=None):
      self.duration = duration
      if calories==None:
          self.calories = self.calculate_calories()
      else:
          self.calories = calories

    def calculate_calories(self):
            return int(self.duration)*10

    def get_duration(self):
        return self.duration

    def get_calories(self):
        return self.calories

    def set_calories(self,calories):
        self.calories=calories

    def set_duration(self,new_duration):
        self.duration=new_duration

    def dict_record(self):
        now = str(datetime.now().replace(microsecond=0))
        list_record={"Type":"Exercising","Distance":0,
                     "Calories":self.calories,"Duration":self.duration,"Date&Time":now}
        return list_record
        

class Walking(Workout):
    def __init__(self,duration,distance=None,calories=None):
        super().__init__(duration,calories)
        if distance==None:
          self.distance = 0
        else:
          self.distance = distance

    def calculate_calories(self):
            return int(self.duration)*5
    def get_distance(self):
        return self.distance
    def set_distance(self,new_distance):
        self.distance= new_distance
    def dict_record(self):
        now = str(datetime.now().replace(microsecond=0))
        list_record={"Type":"Walking","Distance":self.distance,
                     "Calories":self.calories,"Duration":self.duration,"Date&Time":now}
        return list_record
    


class Running(Walking):
    def __init__(self,duration,distance=None,calories=None):
        super().__init__(duration,distance,calories)

    def calculate_calories(self):
            return int(self.duration)*10
    def dict_record(self):
        now = str(datetime.now().replace(microsecond=0))
        list_record={"Type":"Running","Distance":self.distance,
                     "Calories":self.calories,"Duration":self.duration,"Date&Time":now}
        return list_record

















#########################################################################################################################
####################################FUNCTIONS############################################################################
#########################################################################################################################

import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "workout.txt")


def load_file():
    """This function help to load file and move data into list
      return list"""
    if not os.path.exists(FILE_PATH):
        return []

    records = []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:  
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Skipping invalid line: {line}")
    return records


def save_to_file(record):
    """This function help to save data into file by using record list"""
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        json_line = json.dumps(record)
        file.write(json_line + "\n")
def clearing_file():
    """This function clearing file for rewrite list to file in order to save"""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(" ")




def add_workouts():
    """This function creates new activity records  and return it"""
    s="Which workout,do you want to choose?"
    s+="\n1.Exercising\n2.Walking\n3.Running"
    print(s)
    distance=None

    #WORKOUT--TYPE
    
    while True:
            num=input("Enter number:")
            if num=="1":
                Type="Exercising"
                break
            elif num=="2":
                Type="Walking"
                break
            elif num=="3":
                Type="Running"
                break
            else:
                print("Wrong input!! Try again!!")

    #Calories---input
        
    while True:
        
        calories=input("Enter calories (or leave empty): ")
        
        if calories == "":
            calories = None
            break
        
        elif calories.isdigit() and int(calories) >= 0:
            calories = int(calories)
            break

    #--Distance for walking and running

    if Type=="Running" or Type=="Walking":
       while True:
          distance=input("Enter Distance:")
          if distance.isdigit() :
              distance=int(distance)
              if distance>=0:
                 break
    #--Duration---
                
    while True:
        
        duration=input("Enter duration(minutes): ")
        if duration.isdigit():
            if int(duration)>=0:
                duration=int(duration)
                break
        print("Invalid Duration! Try again")

    if Type == "Exercising":
        a = Workout(duration,calories)
    elif Type == "Walking":
        a = Walking(duration, distance, calories)
    elif Type == "Running":
        a = Running(duration, distance, calories)

    return a.dict_record()


def view_workouts(records):
   """This function help to view records as a table"""
   i=1
   s="No"+2*" "
   s+=format("Type","<12")
   s+=format("Distance","<12")
   s+=format("Calories","<12")
   s+=format("Duration","<12")
   s+=format("Date","<12")
   
   print(s)
   for every_result in records:
       print(f"{i}."+2*" ",end=" ")
       i+=1

       for key,value in every_result.items():
          print(format(str(value),"<12"),end="")
       print()
       



def delete_workout(dict_file_list):
    """This function is used to help for deleting records"""
    
    while True:
        view_workouts(dict_file_list)
        while True:
         num=input("Choose id number OR 0 for back:")
         if num=="0":
            break
         if num.isdigit() and 1 <= int(num) <= len(dict_file_list):
            dict_file_list.pop(int(num)-1)
            view_workouts(dict_file_list)
            break
         else:
            print("Incorrect,please enter id number: ")
        print("Do you want to delete again?")
        ans=input("Enter Yes or No:").lower()
        if ans=="yes":
            pass
        else:
            break
    return dict_file_list




def analysis_records(dict_file_list):
    """This function help to show analysis"""
    if dict_file_list==[]:
        print("No records to analyze!")
        return
    #Analysis according to given choices
    

    while True:
        
        s="\n--- Analysis Menu ---"
        s+="\n1. Total calories burned"
        s+="\n2. Average workout duration"
        s+="\n3. Longest/shortest workout duration"
        s+="\n4. Total distance"
        s+="\n5. Sort records"
        s+="\n6. Filter by type"
        s+="\n0. Back to main menu"
        print(s)

        choice = input("Choose an option (0-6): ")

        if choice == "0":
            break

        elif choice == "1":
            total_calories = sum(r["Calories"] for r in dict_file_list)
            print(f"\nTotal calories burned: {total_calories} cal")

        elif choice == "2":
            avg_duration = sum(r["Duration"] for r in dict_file_list) / len(dict_file_list)
            print(f"\nAverage workout duration: {avg_duration:.2f} minutes")

        elif choice == "3":
            durations = [r["Duration"] for r in dict_file_list]
            print(f"\nLongest workout: {max(durations)} minutes")
            print(f"Shortest workout: {min(durations)} minutes")

        elif choice == "4":
            total_distance = sum(r["Distance"] for r in dict_file_list)
            print(f"\nTotal distance: {total_distance} KM")

        elif choice == "5":
            
            sorted_list = sorting_records(dict_file_list)

        elif choice == "6":
            types = set(r["Type"] for r in dict_file_list)
            print("\nAvailable workout types:", ", ".join(types))
            filter_type = input("Enter type to filter: ")
            filtered = [r for r in dict_file_list if r["Type"].lower() == filter_type.lower()]
            if filtered:
                print("\nFiltered Records:")
                view_workouts(filtered)
            else:
                print(f"No records found for type '{filter_type}'")

        else:
            print("Invalid choice! Please try again.")

    
def sorting_records(dict_file_list):
    """This function help to sort the given data according to the chosen field and return sorted list"""
    #IF THERE IS NO FILE
    if dict_file_list==[]:

        print("No records found!")

        return []

    #DISPLAY
    
    s="Which filed do you want to sort by?"
    s+="\n1. Type"
    s+="\n2. Calories"
    s+="\n3. Distance"
    s+="\n4. Duration"

    print(s)

    field_map = {"1": "Type","2": "Calories","3": "Distance",
                 "4": "Duration"}

    while True:
        choice = input("Enter number(1-5): ")
        if choice in field_map:
            field = field_map[choice]
            break
        print("Invalid choice! Try again.")
    #Sorting

    try:
        if field in ["Calories", "Distance", "Duration"]:
            sorted_list = sorted(dict_file_list, key=lambda x: int(x[field]))

        else:
            sorted_list = sorted(dict_file_list, key=lambda x: x[field])

    except KeyError:
        print(f"ERROR: File not found in records.")
        return dict_file_list

    print("\nSorted Records:")
    displaying(sorted_list)

    return sorted_list

def displaying(records):
   """This function help to display data in proper way"""
   i=1
   s="No"+2*" "
   s+=format("Type","<12")
   s+=format("Distance","<12")
   s+=format("Calories","<12")
   s+=format("Duration","<12")
   s+=format("Date","<12")
   
   print(s)
   for every_result in records:
       print(f"{i}."+2*" ",end=" ")
       i+=1

       for key,value in every_result.items():
          print(format(str(value),"<12"),end="")
       print()


#UPDATE---DATA
def update_workout(records):
    """This function is used to help for updating data in updating data in each record"""
    while True:
        view_workouts(records)
        while True:
         num=input("Choose id number OR 0 for back:")
         if num=="0":
            break
         if num.isdigit() and 1 <= int(num) <= len(records):
            record=records[int(num)-1]

            print("What do you want update?")
            
            while True:
                
              s=format("1.Distance\n")
              s+=format("2.Calories\n")
              s+=format("3.Duration\n")
              s+=format("0.back\n")
            
              print(s)
              a=input("Choose one(0-3)")
              if a=="0":
                  break
              elif a=="1":
                  new_distance=distance_set(record)
                  record["Distance"]=new_distance
                  print("New Distance is set!")
              elif a=="2":
                  new_calories=calories_set()
                  record["Calories"]=new_calories
                  print("New Calories is set!")
                  
              elif a=="3":
                  new_duration=duration_set()
                  record["Duration"]=new_duration
                  print("New Duration is set!")
                  
              else:
                 print("Wrong Input, Try again!")
        view_workouts(records)  
            
        print("Do you want to update again?")
        ans=input("Enter Yes or No:").lower()
        if ans=="yes":
            pass
        else:
            break   
def calories_set():
    """Calories Input take return integer number"""
        
    while True:
        
        calories=input("Enter calories (or leave empty): ")
        
        if calories == "":
            calories = 0
            break
        
        elif calories.isdigit() and int(calories) >= 0:
            calories = int(calories)
            break
        else:
            print("Try again!")
    return calories
def distance_set(record):
    """Distance Input take return integer number"""

    if record["Type"]=="Running" or record["Type"]=="Walking":
       while True:
          distance=input("Enter Distance:")
          if distance.isdigit() :
              distance=int(distance)
              if distance>=0:
                 break
              else:
                 print("Try again!")
          else:
            print("Try again!")
    else:
        print("You can't change this type's Distance")
        return 0
    return distance

def duration_set():
    """Duration Input take return integer number"""
    while True:
        
        duration=input("Enter duration(minutes): ")
        if duration.isdigit():
            if int(duration)>=0:
                duration=int(duration)
                break
        print("Invalid Duration! Try again")

    return duration
    

    

    
    

          
      


    
    

#########################################################################################################################
####################################MAIN AREA############################################################################
#########################################################################################################################



def main_menu():
    """
    MAIN MENU HELP TO DISPLAY PROCESS
    """
    records = load_file()
    

    
    while True:
        s="\n--- Fitness Tracker Main Menu ---"
        s+="\n1. Add Record"
        s+="\n2. View Records"
        s+="\n3. Update Record"
        s+="\n4. Delete Record"
        s+="\n5. Analysis Menu"
        s+="\n0. Save & Exit"
        print(s)
        
        choice = input("Choose an option (0-5): ")
        
        if choice == "0":
            print("Saving records and exiting...")
            # Save all records before exit
            clearing_file()
            for record in records:
                  save_to_file(record)
            print("Goodbye!")
            break
        
        elif choice == "1":
            # Add record
            new_record = add_workouts() 
            records.append(new_record)
            print("Record added successfully!")
        
        elif choice == "2":
            # View records
            if records:
                view_workouts(records)
            else:
                print("No records to display.")
        
        elif choice == "3":
            # Update record
            if records:
                update_workout(records)
            else:
                print("No records to update.")
        
        elif choice == "4":
            # Delete record
            if records:
                delete_workout(records)
            else:
                print("No records to delete.")
        
        elif choice == "5":
            # Analysis menu
            if records!=[]:
                analysis_records(records)
            else:
                print("No records for analysis.")
        
        else:
            print("Invalid choice. Please select a number between 0-5.")


if __name__ == "__main__":
    main_menu()

               
        


