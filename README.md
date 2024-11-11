# cyberProjekt24

This Django-based web application, "CookBook," lets users create, edit, and delete recipes. However, it intentionally includes several cybersecurity vulnerabilities identified in the OWASP Top 10 2017 for educational purposes. Code comments offer potential fixes for these vulnerabilities. Please note that this application is not meant for production use and real-world applications.

Prerequisites:
•	Python: Ensure you have Python 3.5 or later. Check your version by running python3 --version in your terminal. If needed, install a newer version from the official Python website. https://www.python.org/downloads/
•	Django: If you don't have Django, install it using pip install Django.

Installation:
•	Clone the Project: Open your terminal, navigate to your desired project directory, and run git clone git@github.com:juuvuor/cyberProjekt24.git

Database Setup:
•	The database is preinstalled and should work normally.
•	If there are any database issues, run the following commands in the mysite/cookBook directory: 
    o	python3 manage.py makemigrations
    o	python3 manage.py migrate

Starting the Application:
•	Run the Server: Navigate to the mysite/cookBook directory and start the development server using python3 manage.py runserver.

Logging In:
•	Access the Application: Once the server is running, you can access the application in your web browser at the provided URL: http://127.0.0.1:8000/
•	Use Credentials: Log in with the provided username and password.
o	admin: admin
o	test: testi123
