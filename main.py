# import json

# class PersonalLibrary:
#     def __init__(self):
#         # This will hold our library books
#         self.books = []

#     def add_book(self):
#         """Prompts the user to add a book to the library."""
#         title = input("Enter book title: ")
#         author = input("Enter book author: ")
#         publication_year = int(input("Enter publication year: "))
#         genre = input("Enter book genre: ")
#         read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
#         book = {
#             'title': title,
#             'author': author,
#             'publication_year': publication_year,
#             'genre': genre,
#             'read_status': read_status
#         }
        
#         self.books.append(book)
#         print(f"Book '{title}' added to your library.")

#     def remove_book(self):
#         """Prompts the user to remove a book from the library by title."""
#         title = input("Enter the title of the book to remove: ")
#         for book in self.books:
#             if book['title'].lower() == title.lower():
#                 self.books.remove(book)
#                 print(f"Book '{title}' removed from your library.")
#                 return
#         print(f"Book '{title}' not found.")

#     def search_book(self):
#         """Prompts the user to search for a book by title or author."""
#         search_term = input("Enter the title or author to search for: ").lower()
#         results = [book for book in self.books if search_term in book['title'].lower() or search_term in book['author'].lower()]
        
#         if results:
#             for book in results:
#                 print(f"Found: '{book['title']}' by {book['author']} ({book['publication_year']}) - Genre: {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")
#         else:
#             print(f"No books found matching '{search_term}'.")

#     def display_books(self):
#         """Displays all books in the library."""
#         if not self.books:
#             print("Your library is empty.")
#             return
        
#         print("\nBooks in your library:")
#         for book in self.books:
#             print(f"'{book['title']}' by {book['author']} ({book['publication_year']}) - Genre: {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")
    
#     def display_statistics(self):
#         """Displays statistics about the library (total books and percentage read)."""
#         total_books = len(self.books)
#         if total_books == 0:
#             print("Your library is empty.")
#             return
        
#         read_books = sum(1 for book in self.books if book['read_status'])
#         percentage_read = (read_books / total_books) * 100
        
#         print(f"\nTotal books: {total_books}")
#         print(f"Percentage read: {percentage_read:.2f}%")

#     def save_to_file(self, filename="library.json"):
#         """Saves the library to a file (JSON format)."""
#         with open(filename, 'w') as file:
#             json.dump(self.books, file)
#         print(f"Library saved to {filename}.")

#     def load_from_file(self, filename="library.json"):
#         """Loads the library from a file (JSON format)."""
#         try:
#             with open(filename, 'r') as file:
#                 self.books = json.load(file)
#             print(f"Library loaded from {filename}.")
#         except FileNotFoundError:
#             print(f"No existing library found at {filename}.")

# def print_menu():
#     """Prints the menu options for the user."""
#     print("\nPersonal Library Manager")
#     print("1. Add a book")
#     print("2. Remove a book")
#     print("3. Search for a book")
#     print("4. Display all books")
#     print("5. Display statistics")
#     print("6. Save library to file")
#     print("7. Load library from file")
#     print("8. Exit")

# def main():
#     library = PersonalLibrary()
#     library.load_from_file()  # Load library from file if available
    
#     while True:
#         print_menu()
#         choice = input("Choose an option: ")

#         if choice == '1':
#             library.add_book()
#         elif choice == '2':
#             library.remove_book()
#         elif choice == '3':
#             library.search_book()
#         elif choice == '4':
#             library.display_books()
#         elif choice == '5':
#             library.display_statistics()
#         elif choice == '6':
#             library.save_to_file()
#         elif choice == '7':
#             library.load_from_file()
#         elif choice == '8':
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

class PersonalLibrary:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
        read = input("Read? (yes/no): ").strip().lower() == 'yes'
        self.books.append({'title': title, 'author': author, 'year': year, 'genre': genre, 'read': read})
        print(f"Book '{title}' added.")

    def remove_book(self):
        title = input("Enter title of book to remove: ")
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]
        print(f"Book '{title}' removed.")

    def display_books(self):
        if not self.books:
            print("No books in your library.")
        else:
            for book in self.books:
                status = 'Read' if book['read'] else 'Unread'
                print(f"'{book['title']}' by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def print_menu():
    print("\n1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Exit")

def main():
    library = PersonalLibrary()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.remove_book()
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
