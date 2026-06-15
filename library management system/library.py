class Library:
    def __init__(self):
        self.books=[]
    def add_book(self, book_name):
      self.books.append(book_name)
      print(f"{book_name} added successfully!")
    def show_books(self):
     print("\n---Available books---")
     for index,book in enumerate(self.books, 1):
            print(f"{index}.{book}")
def main():
    my_lib = Library()
    while True:  
        print("\n1.Add book 2.show books 3. Exit")
        choice=input("select option:")
        if choice=='1':
            name=input("Enter book Name:")
            my_lib.add_book(name)
        elif choice=='2':
            my_lib.show_books()
        elif choice=='3':
            break
        else:
            print("invalid choice!")
if __name__ == "__main__":
  main()
        
        