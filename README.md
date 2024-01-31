# Flask App on AWS EC2

This project is a Flask web application deployed on an AWS EC2 instance. The application includes user authentication, user information retrieval, and updating user information.

Deployed on EC2 Instance: http://ec2-3-128-171-197.us-east-2.compute.amazonaws.com/

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- SQLite (for the database)
- AWS EC2 instance with necessary permissions

## Getting Started

1. Clone the repository:

   ```
   git clone <repository-url>
   cd flaskapp
   ```
   
2. Virtual Environment:
   Create and activate a virtual environment to isolate dependencies.
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the Flask App:
   - Start the Flask application.
     ```
     python flaskapp.py
     ```
   - The application should be running at `http://your-ec2-instance-ip:5000/`.

5. Install the apache webserver and mod_wsgi:

```
$ sudo apt-get install apache2 libapache2-mod-wsgi-py3
$ sudo apachectl restart
```
     


## Usage

- Access the application by navigating to `http://your-ec2-instance-ip:5000/` in your web browser.
- Use the login form to enter your username and password.
- If the username doesn't exist, a new user will be created, and you'll be prompted to provide additional information.
- Once logged in, you can view your user information, including first name, last name, and email.
- You can also update your user information by clicking on the "Save" button.

## Additional Notes

- **File Paths:**
  - Update file paths in the code as needed, especially if you move the application files to a different location.

- **EC2 Security Groups:**
  - Ensure that your EC2 instance's security group allows inbound traffic on port 5000.

- **Database Backups:**
  - Implement a regular backup strategy for the SQLite database, especially in a production environment.

## License

This project is licensed under the [MIT License](LICENSE).
