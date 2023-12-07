from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn




# Create a dummy database (a list of books)
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    # ... other books
]


# Define a model for a book
from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# Initialize the FastAPI app
app = FastAPI()

# Endpoint 1: Retrieve All Books
@app.get("/api/books", response_model=List[Book])
async def get_all_books():
    return books_db

# Endpoint 2: Add a New Book
@app.post("/api/books", response_model=Book)
async def add_new_book(book: Book):
    # Check if the book already exists in the database
    for existing_book in books_db:
        if book.id == existing_book["id"]:
            raise HTTPException(status_code=400, detail="Book ID already exists")
        elif book.title == existing_book["title"] and book.author == existing_book["author"]:
            raise HTTPException(status_code=400, detail="Book already exists")
    books_db.append(book.dict())
    return book

# Endpoint 3: Update Book Details
@app.put("/api/books/", response_model=Book)
async def update_book_details(book: Book):
    # Find the book in the database
    for existing_book in books_db:
        if existing_book["id"] == book.id:
            existing_book.update(book.dict(exclude_unset=True))
            return existing_book
    raise HTTPException(status_code=404, detail="Book not found")

# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
