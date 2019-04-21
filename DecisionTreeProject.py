"""Code to make prediction for 20 percent of new Facebook users on the basis of 80 percent of dataset having features of existing 
Facebook users extracted from Weka website which creates the Decision tree once dataset is uploaded 
@author: A.Gupta, S.Jeffcoat, J.Morrison, J.Jones"""

class Decision_Tree:
  """code to make prediction about new FB users' interest on the basis of given data"""
  def __init__(self, name):
    self.name = name
   
  
  def Get_User_features(self):
    self.Gender = input("Gender: M of F? ")
    self.Ethnicity = input("Ethnicity: Caucasian, Asian, Minority? ")
    self.Age = input("Age: 18-25, 26-35, 36-55? ")
    self.Relative = input("Relative to you: Yes, No? ")
    self.Post = input("Do you post frequently or non-frequently: FRE, NFRE? ")
    self.Relationship = input("Are you in a relationship: Yes, No?  ")

  def prediction(self):
    """check all the conditions to make close prediction about new users' interest"""
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Caucasian":
      print("the new user is interested in Atheletics")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Asian" and self.Post == "FRE" and self.Relationship == "Yes":
      print("the new user is interested in Cosmetics")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Asian" and self.Post == "FRE" and self.Relationship == "No":
      print("the user is interested in Cosmetics")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Asian" and self.Post == "NFRE":
      print("the new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Minority" and self.Post == "FRE" and self.Relationship == "Yes" and self.Gender == "M":
      print("the new user is interested in Cosmetics")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Minority" and self.Post == "FRE" and self.Relationship == "Yes" and self.Gender == "F":
      print("the new user is interested in Cosmetics")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Minority" and self.Post == "FRE" and self.Relationship == "No":
      print("the new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "18-25" and self.Ethnicity == "Minority" and self.Post == "NFRE" and self.Gender == "M" or self.Gender == "F":
      print("the new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "M" and self.Relationship == "Yes":
      print("The new user is interested in Atheletics")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "M" and self.Relationship == "No":
      print("The new user is interested in Cosmetics")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "F" and self.Relationship == "Yes":
      print("The new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "F" and self.Relationship == "No" and self.Ethnicity == "Caucasian":
      print("The new user is interested in Atheletics")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "F" and self.Relationship == "No" and self.Ethnicity == "Asian":
      print("The new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "FRE" and self.Gender == "F" and self.Relationship == "No" and self.Ethnicity == "Minority":
      print("The new user is interested in Atheletics")
    if self.Relative == "Yes" and self.Age == "26-35" and self.Post == "NFRE" and self.Relationship == "Yes" or self.Relationship == "No":
      print("the new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "36-55" and self.Gender == "M":
      print("the new user is interested in Outgoing")
    if self.Relative == "Yes" and self.Age == "36-55" and self.Gender == "F":
      print("the new user is interested in Cosmetics")
    if self.Relative == "No" and self.Post == "FRE" and self.Relationship == "Yes" and self.Gender == "M" and self.Ethnicity == "Caucasian":
      print("the new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "FRE" and self.Relationship == "Yes" and self.Gender == "M" and self.Ethnicity == "Asian":
      if  self.Age == "18-25":
        print("the new user is interested in Reading")
      if self.Age == "26-35":
        print("the new user is interested in Atheletics")
      if self.Age == "36-55":
        print("the new user is interested in Animals")
    if self.Relative == "No" and self.Post == "FRE" and self.Relationship == "Yes" and self.Gender == "F":
      if self.Ethnicity == "Caucasian":
        print("the new user is interested in Outgoing")
      if self.Ethnicity == "Asian":
        if self.Age == "18-25":
          print("the new user is interested in Cosmetics")
        if self.Age == "26-35":
          print("the new user is interested in Outgoing")
        if self.Age == "36-55":
          print("the new user is interested in Atheletics")
      if self.Ethnicity == "Minority":
        if self.Age == "18-25":
          print("the new user is interested in Outgoing")
        if self.Age == "26-35":
          print("the new user is interested in Outgoing")
        if self.Age == "36-55":
          print("the new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "FRE" and self.Relationship == "No":
      if self.Ethnicity == "Caucasian":
        print("the new user is interested in Outgoing")
      if self.Ethnicity == "Asian":
        if self.Gender == "M":
          print("the new user is interested in Atheletics")
        if self.Gender == "F":
          if self.Age == "18-25" and self.Age == "26-35":
            print("the new user is interested in Outgoing")
          if self.Age == "36-55":
            print("the new user is interested in Atheletics")
      if self.Ethnicity == "Minority":
        if self.Gender == "M":
          if self.Age == "18-25":
            print("the new user is interested in Atheletics")
          if self.Age == "26-35":
            print("the new user is interested in Atheletics")
          if self.Age == "36-55":
            print("the new user is interested in Cosmetics")
        if self.Gender == "F":
          if self.Age == "18-25":
            print("the new user is interested in Cosmetics")
          if self.Age == "26-35":
            print("the new user is interested in Atheletics")
          if self.Age == "36-55":
            print("the new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Caucasian" and self.Age == "18-25":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Caucasian" and self.Age == "26-35":
      print("The new user is interested in Cosmetics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Caucasian" and self.Age == "36-55":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Asian" and self.Age == "18-25" and self.Gender == "M":
      print("The new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Asian" and self.Age == "18-25" and self.Gender == "F":
      print("The new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Asian" and self.Age == "26-35":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Asian" and self.Age == "36-55":
      print("The new user is interested in Reading")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "18-25" and self.Relationship == "Yes" and self.Gender == "M":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "18-25" and self.Relationship == "Yes" and self.Gender == "F":
      print("The new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "18-25" and self.Relationship == "No" and self.Gender == "M":
      print("The new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "18-25" and self.Relationship == "No" and self.Gender == "F":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "26-35" and self.Gender == "M" and self.Relationship == "Yes":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "26-35" and self.Gender == "M" and self.Relationship == "No":
      print("The new user is interested in Outgoing")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "26-35" and self.Gender == "F":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "36-55" and self.Relationship == "Yes":
      print("The new user is interested in Atheletics")
    if self.Relative == "No" and self.Post == "NFRE" and self.Ethnicity == "Minority" and self.Age == "36-55" and self.Relationship == "No":
      print("The new user is interested in Outgoing")        

              

DT = Decision_Tree("Alleyah")
DT.Get_User_features()
DT.prediction()


        
        



