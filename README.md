# Virtual Coffee Shop

This is a simple web application that allows users to register, log in, create posts about coffee they have had, view all posts by themselves and others, and log out. The application is built using Flask, a Python web framework, and incorporates user authentication and post management features.


## Features

1. **User Registration:**
   - Users can register for an account by providing a unique username, email, and password.
   - Registration ensures that usernames and emails are unique to each user.

2. **User Login:**
   - Registered users can log in using their credentials.
   - The application securely manages user sessions.

3. **Post Creation:**
   - Authenticated users can create posts by entering text content.
   - Each post is associated with the user who created it.

4. **Viewing Posts:**
   - Users can view a feed of posts, displaying the most recent posts at the top.
   - The posts include the username of the creator, the post content, and the timestamp of creation.

5. **User Logout:**
   - Authenticated users can log out to end their session securely.

## Technologies Used

- **Flask:** A lightweight and flexible web framework for Python.
- **Flask-Bcrypt:** A Flask extension that provides Bcrypt hashing utilities for password hashing.
- **SQLAlchemy:** ORM (Object-Relational Mapping) library for working with databases.
- **MySQL on AWS RDS:** The application uses MySQL as the database hosted on Amazon RDS.
- **HTML AND CSS:** Basic webpage markup languages

## Setup

1. Install Python and create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Create a '**config.py**' file that will contain your app secret key, db credentials and any other secret the app uses. Be sure to create the database and all necessary credentials prior and test connectivity.
Schema is defined in the schema.sql file. Once you have set this up, you can import it into the 
    ```flaskr/__init__.py and use it.```

5. Run the application:

    ```bash
    flask run
    ```

   The application will be accessible at `http://127.0.0.1:5000/` in your web browser.



## Usage

1. Open the application in your web browser.

2. Register for a new account using a unique username and email.

3. Log in using your registered credentials.

4. Create a new post by entering text content.

5. View posts on the main feed, including your own posts and those of other users.

6. Log out when you are done.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
