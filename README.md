
# Simple Quiz Application

A basic quiz application allowing users to create accounts and add quizzes.  This README details the application's functionality, usage, and technical aspects.

## 📝 Description

This Python application provides a simple command-line interface for managing user accounts and creating quizzes. Users can either create a new account or, if they already have one, add new quizzes to the system.  The quiz data and user accounts are stored in JSON files.

## 🚀 Features

* **User Account Creation:**  Allows new users to register with a name and mobile number.
* **Quiz Creation:** Enables users to add quizzes specifying the subject (currently limited to "science" or "maths"), the number of questions (up to 10), and the question details (question, four options, and the correct answer).
* **Data Persistence:** Stores user accounts and quiz data in JSON files (`ac.json` and `app.json` respectively) for future use.
* **Input Validation:** Performs basic input validation to ensure data integrity (e.g., checking subject selection, number of questions).

## ⚙️ Technical Details

* **Programming Language:** Python
* **Libraries:** `json` (for JSON file handling)
* **Data Storage:** JSON files (`ac.json` for accounts, `app.json` for quizzes)
* **Command-Line Interface:** The application runs entirely within the command line.


## 🏃 Running the Application

1.  **Prerequisites:** Ensure you have Python 3 installed on your system.
2.  **Clone the Repository:**  (If applicable, provide a GitHub link here)
3.  **Run `app.py`:** Execute the script using a Python interpreter:  `python app.py`
4.  **Follow Prompts:** The application will guide you through the process of creating an account or adding a quiz.

## 🗂️ File Structure

```
quiz_app/
├── app.py       # Main application script
└── ac.json      # User account data
└── app.json     # Quiz data
```

## ⚠️ Limitations

* **Error Handling:**  Error handling is basic. More robust error checks and handling of unexpected input could be implemented.
* **Security:**  The application does not include any security measures to protect data.  In a production environment, appropriate security measures would be necessary.
* **Scalability:**  The application's design is not optimized for large-scale use.


## 💡 Future Enhancements

* Implement more robust error handling.
* Add user authentication and authorization.
* Improve input validation to handle a wider range of input.
* Create a more user-friendly interface (e.g., a GUI).
* Allow users to view existing quizzes.
* Add features for quiz taking and score tracking.
* Implement data encryption for better security.


## 🤝 Contributing

Contributions are welcome! Please feel free to fork the repository, make improvements, and submit pull requests.

