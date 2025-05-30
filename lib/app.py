import argparse
from lib.models.operations import Operations

parser = argparse.ArgumentParser(description="Library Book Tracker System CLI")
subparsers = parser.add_subparsers(dest="command")

# Add user command
user_parser = subparsers.add_parser("add_user", help="Add a new user")
user_parser.add_argument("--name", type=str, required=True, help="Name of the user")

# Add book command
book_parser = subparsers.add_parser("add_book", help="Add a new book")
book_parser.add_argument("--title", type=str, required=True, help="Title of the book")
book_parser.add_argument("--author", type=str, required=True, help="Author of the book")

# Check out book command
checkout_parser = subparsers.add_parser("check_out_book", help="Check out a book for a user")
checkout_parser.add_argument("--user_id", type=int, required=True, help="ID of the user")
checkout_parser.add_argument("--book_title", type=str, required=True, help="Title of the book to check out")

# Return book command
return_parser = subparsers.add_parser("return_book", help="Return a book for a user")
return_parser.add_argument("--user_id", type=int, required=True, help="ID of the user")
return_parser.add_argument("--book_title", type=str, required=True, help="Title of the book to return")

# Search books by title command
search_parser = subparsers.add_parser("search_books_by_title", help="Search for books by title")
search_parser.add_argument("--title", type=str, required=True, help="Title of the book to search for")

# List all books command
list_parser = subparsers.add_parser("list_books", help="List all books in the library")

# List all users command
list_users_parser = subparsers.add_parser("list_users", help="List all users in the library")

# List all loans command
list_loans_parser = subparsers.add_parser("list_loans", help="List all loans in the library")

args = parser.parse_args()

# If no command is provided, print the help message
if not args.command:
    parser.print_help()
    exit(1)

if args.command == "add_user":
    Operations.add_user(args.name)
elif args.command == "add_book":
    Operations.add_book(args.title, args.author)
elif args.command == "check_out_book":
    Operations.check_out_book(args.user_id, args.book_title)
elif args.command == "return_book":
    Operations.return_book(args.user_id, args.book_title)
elif args.command == "search_books_by_title":
    Operations.search_books_by_title(args.title)
elif args.command == "list_books":
    Operations.list_books()
elif args.command == "list_users":
    Operations.list_users()
elif args.command == "list_loans":
    Operations.list_loans()



