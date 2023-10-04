books_in_library = int(input("The number of books in your library: "))
books_for_read = int(input("Books for read: "))
books_in_library_list = set()
books_for_read_list = set()
for i in range(books_in_library):
    book = input()
    books_in_library_list.add(book)
for i in range(books_for_read):
    book = input()
    books_for_read_list.add(book)
for book in books_for_read_list:
    if book in books_in_library_list:
        print("YES")
    else:
        print("NO")