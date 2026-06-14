#6.project

from datetime import datetime

class journal():
   
    def add(self):

        try:
            a=input("Enter your file name with extantion:")
            
            entry=input("Enter your journal entery:\n")

            time=datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")
            with open (a,"a") as file:
                file.write(f"[{time}]")
                file.write(entry+"\n\n")

            print("Entery added successfuly")

        except Exception as e:
            print("Error :",e)

    def view(self):

        try:
             with open(a,"r") as file:
                 content=file.read()
                 print(content)

        except FileNotFoundError:
            print("File Not Found.")

     def delete(self):

        try:
            b=input("Enter your file name in extantion:")
            c=input("Are you sure you want to delete(yes/no):")
            c.lower()

            if c=="yes":
                with open(b,"w") as file:
                 content=file.write()
                 print(content)
                 print("File deleted successfuly.")

            elif c=="no":
                print("contant is not deleted.")

            else:
                print("Enter correct file.")
                

        except FileNotFoundError:
            print("File Not Found.")

     def main(self):
         while True:
             print("\n=======Let's go========")
             print("1.add entery")
             print("2.Delete all entery")

             d=int(input(Enter your choice:))
             
            if d == "1":
                self.add()

            elif d == "2":
                self.delete()

            elif d == "3":

                self.view()

            elif d == "4":

                print("Program over")
                break

            else:

                print("Enyter a valid choice")

       
                 

        

        

            
            
        
    
