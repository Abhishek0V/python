import json
import os
import sys
import datetime as Dt

class Todo:
    
    def __init__(self):
        self.file = "tasks.json"
        self.status = ['Not Done','In Progress','Completed']
    
    def load(self):
        if os.path.exists(self.file):
            with open(self.file,"r") as files:
                try:
                    return json.load(files)
                except json.JSONDecodeError:
                    return []
        return []
    
    
    
    def save(self,test):
        with open(self.file,"w") as files:
            json.dump(test,files,indent = 2)
    
    
    
    # Add Task
    def add_task(self,task_description):
        tasks = self.load()
        task_id = tasks[-1]['id'] + 1 if tasks else  1
        
        task_info = {
            "id":task_id,
            "task":task_description,
            "status":self.status[0],
            "created_at":Dt.datetime.now().strftime("%Y-%m-%d | %H:%M"),
            "updated_at":""
        }
        tasks.append(task_info)
        self.save(tasks)
        
        print(f"Task Added successfully :(ID {task_id})")
    
    # 2) Delete the task - completed
    
    def Delete(self):
        content = self.load()
        id = sys.argv[2]
        for index,i in enumerate(content):
            if int(id) == i["id"]:
                del content[index]
                print(f"Task with ID {id} deleted successfully.")
                return
        print(f"Task with ID {id} not found.")         
    
    
    #Update Task
    def update(self,data,id):
        tasks = self.load()    
    
        for i in tasks:
            if id == str(i["id"]):
                i["task"] = data
                self.save(tasks)
                print(f"Task with ID {id} updated successfully.")
                return
            
        print(f"Task with ID {id} not found.")
        

    # Mark as Completed
    def markProgress(self,id):
        tasks = self.load()
        
        for index,i in enumerate(tasks):
            if i["id"] == id:
                if tasks[index]['status'] == self.status[2]:
                    print(f"Task with ID {id} already Done")
                    return
                tasks[index]["status"] = self.status[1]
                tasks[index]['updated_at'] = Dt.datetime.now().strftime("%Y-%m-%d | %H:%M")
                self.save(tasks)
                print(f"Task with ID {id} marked as Completed.")
                return
        print("Task with ID {id} not found.")
    
    
    
    def markDone(self,id):
        tasks = self.load()
        
        for index,i in enumerate(tasks):    
            if i["id"] == id:
                tasks[index]["status"] = self.status[2]
                tasks[index]['updated_at'] = Dt.datetime.now().strftime("%Y-%m-%d | %H:%M")
                self.save(tasks)
                print(f"Task with ID {id} marked as Completed.")
                return    
            
        print("Task with ID {id} not found.")
        
        
    def list(self):
        tasks = self.load()
        if not tasks:
            print("No tasks found.")
            return
        print("List of Tasks \n==============")
        for i in tasks:
            print(f"{i['id']} | {i['task']} | {i['status']} | {i['created_at']} | {i.get('updated_at', 'N/A')}")
    
    def listDone(self):
        tasks = self.load()
        print("List of Done-Tasks \n==============")
        if len([i for i in tasks if i['status'] == self.status[2]]) <1:
            print("Empty record")
            return
        for i in tasks:
            if i['status'] == self.status[2]:
                print(f"{i['id']} | {i['task']} | {i['status']} | {i['created_at']} | {i.get('updated_at', 'N/A')}")
        
    def listProgress(self):
        tasks = self.load()
        print("List of Progress-Tasks \n==============")
        
        if len([i for i in tasks if i['status'] == self.status[1]]) <1:
            print("Empty record")
            return
             
        for i in tasks:
            if i['status'] == self.status[1]:
                print(f"{i['id']} | {i['task']} | {i['status']} | {i['created_at']} | {i.get('updated_at', 'N/A')}")

    def main(self):
        if len(sys.argv) < 2:
            print("Usage: task-cli add \"your task here\"")
            return
        else:
            command = sys.argv[1]
            if command == "add":
                data = " ".join(sys.argv[2:])
                self.add_task(data)
                
            elif command == "del":
                self.Delete()
                
            elif command == "update":
                data = " ".join(sys.argv[3:])
                id = sys.argv[2]
                self.update(data,id)
                
            elif command == "mark-in-progress":
                id = int(sys.argv[2])
                self.markProgress(id)
                
            elif command == "mark-done":
                id = int(sys.argv[2])
                self.markDone(id)
                
            elif command == 'list':
                self.list()
            
            elif command == "list-Progress":
                self.listProgress()
                
            elif command == 'list-Done':
                self.listDone()
                
            else:
                print("Invalid command")
                           
                    
if __name__ == "__main__":
    Todo().main()