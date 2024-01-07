Task 1:
Beckett Pizza Plaza Cashier - Chloe The Pizza Price Calculator
This Python script serves as Chloe, the Pizza Price Calculator, for Beckett Pizza Plaza. It helps calculate the total price for pizza orders based on various factors like quantity, delivery, discounts, and app usage.

Overview
The Chloe Pizza Price Calculator is a simple command-line interface tool that interacts with customers to determine the total price for their pizza orders. It factors in the number of pizzas ordered, delivery requirements, Tuesday discount offers, and app usage discounts to provide the grand total for the order.

Features
Takes input for the number of pizzas ordered.
Allows users to specify delivery requirements.
Considers Tuesday discount offers.
Calculates discounts for orders made through the BPP app.
Presents the total price breakdown and grand total for the order.

Usage
Run the Beckett_Pizza_Plaza_Cashier.py script in a Python environment.
Follow the on-screen prompts to input the necessary information:
Number of pizzas ordered
Delivery requirement (Yes/No)
Whether it's Tuesday (Yes/No)
App usage for the order (Yes/No)
Review the displayed breakdown of charges and the grand total for the order.
Ensure Python is installed on your system to run the script.

Completed: 26th December, 2023 AD 

Task 2
Cat Visitation Log Analysis
This Python script analyzes cat visitation log data to derive statistics such as the number of visits, total time spent by cats, average visit lengths, and more.

Overview
The Cat Visitation Log Analysis script reads a log file containing cat visitation data. It calculates various metrics related to cat visits, including total visits by our cat, the total time spent by all cats, the longest and shortest visit durations, and more.

Usage
Run the task2.py script in a Python environment, providing the log file as an argument.

Functionality
The script performs the following tasks:
Counts the number of visits by our cat and other neighbor cats.
Calculates the total time spent by all cats in the house.
Computes the total time spent specifically by our cat.
Determines the average visit length of our cat.
Identifies the longest and shortest visit durations by our cat.

Output
After analyzing the log file, the script displays the following statistics:
Total cat visits recorded.
Count of visits by neighbor cats.
Total time spent in the house by all cats.
Total time spent in the house by our cat.
Average visit length of our cat.
Longest visit duration by our cat.
Shortest visit duration by our cat.

Completed: 30th December, 2023AD


Task 3
User Account Management System
This Python script provides functionalities for managing user accounts, including adding users, deleting users, and changing passwords. It utilizes a text file, passwd.txt, to store user account information.

Functionality Overview
1. Add User Functionality
The add_user function allows adding new users to the passwd.txt file. It verifies if the entered username already exists, requires usernames to be in lowercase, encrypts passwords using ROT_13, and writes the new user information to the file.

2. Delete User Functionality
The del_user function enables deleting existing users from the passwd.txt file. It checks for the existence of the entered username and its password, encrypts the password using ROT_13 for comparison, and updates the file after removing the specified user.

3. Login Functionality
The login_user function manages user login by checking the provided username and password against the passwd.txt file. It encrypts the password using ROT_13 for comparison and grants or denies access based on matching credentials.

4. Change Password Functionality
The change_pass function allows changing passwords for existing users in the passwd.txt file. It verifies the current password, encrypts it using ROT_13 for comparison, replaces the old password with the new encrypted password, and updates the file accordingly.

Usage
Ensure Python is installed on your system.
Run each function separately by executing the corresponding script segment.
Example:
python add_user.py passwd.txt
Ensure to replace add_user.py with the respective script name for each function.

Follow the on-screen prompts for each function:
Add User: Enter a new username, real name, and password.
Delete User: Enter the username and its password for deletion.
Login: Enter the username and its password for login verification.
Change Password: Enter the username, current password, new password, and confirmation.

Completed: 5th January, 2023 AD



