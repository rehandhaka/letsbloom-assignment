# letsbloom-assignment
LetsBloom - Assignment

Introduction
This README provides guidelines for setting up and using the Library Management API. This API, built with FastAPI, offers a simple way to manage a library system, allowing for operations such as retrieving all books, adding new books, and updating book details.

Getting Started

Prerequisites
- Python 3.6+
- FastAPI
- Uvicorn

Installation

Install FastAPI: pip install fastapi

Install Uvicorn: pip install uvicorn

Running the Application

Start the Application:
Run the following command in your terminal: uvicorn main:app --reload


Access the Application:
The API will be available at http://localhost:8000.

Seeding the Database with Mock Data
The application uses an in-memory mock database initialized with some pre-defined books. To add more books for testing purposes, modify the books_db list in the script. Each book should be a dictionary with keys: id, title, author, and year. I have not integrated a separate database with this.

API Documentation

1. Retrieve All Books

- Endpoint: GET /api/books
- Description: Retrieves a list of all books in the library.
- Response Format: A JSON array of books. Each book is an object with id,  title, author, and year.

2. Add a New Book

- Endpoint: POST /api/books
- Description: Adds a new book to the library.
- Request Format: JSON object representing the new book, including id, title, author, and year.
- Response Format: JSON object of the added book.
- Error Handling: Returns an error if the book ID already exists or the book details are duplicated.

3. Update Book Details

- Endpoint: PUT /api/books/
- Description: Updates the details of a specific book in the library.
- Request Format: JSON object with the updated book details, including id, title, author, and year.
- Response Format: JSON object of the updated book.
- Error Handling: Returns an error if the book to update is not found.

Additional Information
The API uses a simple in-memory list to store the data, so all changes are lost when the application is restarted.

Visit http://localhost:8000/docs for interactive API documentation provided by FastAPI.

Conclusion

This Library Management API serves as a basic example of creating RESTful APIs using FastAPI. It is intended for educational purposes and not suited for production use without further enhancements such as database integration, authentication, and more robust error handling.

