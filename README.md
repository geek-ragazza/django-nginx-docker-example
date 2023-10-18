# Local Setup

To run the entire service locally, follow these steps:

1. Clone the Repository
    ```bash
    git clone https://github.com/geek-ragazza/django-nginx-docker-example.git
    cd django-nginx-docker-example
    ```

2. Build and Run the Docker Containers
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images and start the services. The Django application will be available at http://localhost:8003.

3. Access the Application
    - Login Page: Navigate to http://localhost:8003 to access the login page.
    - Register: If you don't have an account, click on the "Sign Up" button in the navbar to create a new account.
    - Login: Use your registered username and password to log in.


4. Admin Access
    - Admin URL: http://localhost:8003/admin/
    - Username: admin
    - Password: Initium1022

    In the admin panel, you can manage users and employees. Users who are employees will display their employee status.

# Application Features

- User Registration/Login/Logout: 
    - Users can register with a username, password, and confirm password. Optionally, they can provide their employee status and name for a more detailed registration process.
- Home Page: 
    - After logging in, the home page displays the user's name and, if the user is an employee, their employee status.
- Navbar: 
    - The navbar provides options to log out and, on the login page, a "Sign Up" button to create a new account.
- Admin Panel: 
    - Accessible at /admin, it allows the admin to manage users and employees, including setting the employee status.

# Example Screenshots
1. Login
    ![login-screenshot](example/login.png)
2. Register
    ![register-screenshot](example/register.png)
3. Home Page:
    ![login-screenshot](example/home-page-employee-status.png)
4. Admin Employee
    ![admin-employee](example/admin-employee.png)
5. Admin show employee status if the user is an employee
    ![admin-employee-status-screenshot](example/admin-employee-status.png)

