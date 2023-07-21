<div align="center">
  <h1 align="center">CRUD API</h1>
</div>

### About
To Create, Read, Update, or Delete the tasks using API endpoints. Built using Django REST Framework

### Testcase
Passed all the test cases  
![Screenshot 2023-07-21 173723](https://github.com/Nandan26/task-api/assets/77192056/5b4f3c77-c406-4126-837e-edd5e8fd9981)

### Demo of API
#### 1. Create a new Task  
![1](https://github.com/Nandan26/task-api/assets/77192056/ae2d7e61-068c-4b7b-8fc3-ffca31327aa7)
#### 2. List all tasks created  
![2](https://github.com/Nandan26/task-api/assets/77192056/3f7dd2a8-611f-4577-994a-ee0accdf022d)  
#### 3. Get a specific task
![3](https://github.com/Nandan26/task-api/assets/77192056/34798b2c-8426-4445-863b-7efc2f8b76d7)  
If task not exist  
![3_1](https://github.com/Nandan26/task-api/assets/77192056/a2b1800b-8db3-4b85-abd7-bc9f6d4b4971)  
#### 4. Delete a task
![5](https://github.com/Nandan26/task-api/assets/77192056/5ed05775-32db-4bd1-b016-befad6006615)  
#### 5. Update a task  
![4](https://github.com/Nandan26/task-api/assets/77192056/91b0777e-0392-4cb6-81c3-e07687c86f77)
After update  
![4_2](https://github.com/Nandan26/task-api/assets/77192056/8ffb124f-c66c-49c9-9ba5-f382dbea94ca)
#### 6. Post multiple tasks  
![6](https://github.com/Nandan26/task-api/assets/77192056/ba043d61-7016-4bf3-b791-860af7ff2b68)  
#### 7. Delete multiple tasks
![7](https://github.com/Nandan26/task-api/assets/77192056/47581684-abd9-44d5-8443-880553a0c872)  
After delete perform get all task: Task 2,3 successfully deleted
![7_2](https://github.com/Nandan26/task-api/assets/77192056/3382ed29-b943-44fd-bf86-1e07a8f2cdcf)



### Installation
To set up the Referred project on your local machine, follow these steps:

1. Fork the project
2. Clone the repository:  
3. Navigate to the project directory
4. Create a virtual environment:  
   `python3 -m venv myenv`
5. Activate the virtual environment
6. Install the project dependencies:  
   `pip install -r requirements.txt`
7. Apply the database migrations:  
   `python manage.py migrate`
8. Run the development server:  
   `python manage.py runserver 5000`
