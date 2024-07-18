# TicketEase

## Description
TicketEase is a ticketing management system, that I built for the Alx Webstack Portfolio Project. This project marks the end of my backend specialization, in the 12-month Software Engineering Programn.

It provides a seamless and efficient way to manage tickets, allowing users to create, update, and track tickets for various projects.

 With TicketEase, you can easily stay organized and ensure smooth ticketing operations. 

## Technologies used
TicketEase is built using `Python` with `Django` framework for the backend and `HTML` and `CSS` for the frontend.

### Third-party Packages used
- `Django-allauth` - for the authentication system
- `python-dotenv` - to secure my environmental variables within the `.env` file
- `Pillow` - to handle images during production

## Getting Started
### Prerequisites
To test TicketEase locally, you will need to have `Python` installed on your machine. You can download it [here](https://www.python.org/downloads/).

### Installation
1. Clone the repo: `git clone https://github.com/TKaburu/TicketEase.git`
2. Navigate to the project directory: `cd TicketEase`
3. Create a virtual environment `python -m venv <environment_name> `. Replace `<environment_name>` with the actual name of your environment.
4. Activate your virtual environment: `.<environment_name\Scripts\activate` for windows and `source <environment_name>/bin/activate ` for macOs/linux
5. Install dependencies: `pip install -r requirements.txt`

### Run the application
You will need to do a couple of things before spinning up the server:

- create a `.env` file which will be used to host the `SECRETE KEY`

- Generate a `SECRETE KEY` using python shell. You can use `secrets` for this. 


  - Using Python shell import secrets then `print(secrets.token_hex(24))`
  - Copy the key and place it in the `.env` file like this
  `SECRET_KEY=copied_key`. Replace `copied_key` with the actual key
- Run migrations using `python manage.py migrate`
- Run the inbuilt django server using `python manage.py runserver`
- You can now access the application on `http://127.0.0.1:8000/`

### Django Admin
Django comes with an inbuilt admin panel that can be accessed on `http://127.0.0.1:8000/admin`, but first you will need a superuser.
#### Creating a Superuser
To create a superuser, on your terminal, run `python manage.py createsuperuser` and follow the prompts given.

_Note :  The password fields will appear blank as you are typing them in. Don't panic, it's to protect your password from prying eyes_ 👀

## Contributing
Want to help me make TicketEase better? 
1. Fork the Project
2. Create a new Branch to work on `git checkout -b <branch_name>`
3. Create some magic, using code ofcourse 🪄🪄
4. Commit your changes
5. Push to the Branch: `git push origin <branch_name>`
6. Open a pull request

## Contact
Have a question or you want to talk code, get in touch! 🫱🏾‍🫲🏻

Project Link: [TicketEase](https://github.com/TKaburu/TicketEase)

Twitter - [@kaburu_tracey](https://github.com/TKaburu/TicketEase)

Email - [traceymwendwa@gmail.com](mailto:traceymwendwa@gmail.com)
