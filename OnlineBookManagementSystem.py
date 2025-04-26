class User:
    def __init__(self, username, email):
        self.username = username
        self.email =  email

    def display_user_info(self):
        print(f"User: {self.username}, Email: {self.email}")


class Customer(User):
    def __init__(self, username, email, shipping_address):
        super().__init__(username, email)
        self.shipping_address =  shipping_address
        self.cart =  []

    def add_to_cart(self, book):
        self.cart.append(book)
        print(f"{book.title} added to cart")

    def display_user_info(self):
        print(f"Customer: {self.username}, Address: {self.shipping_address}")


class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def display_user_info(self):
        print(f"Admin: {self.username}")

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id =  book_id
        self.title = title
        self.author =  author
        self.price = price
        
    def display_book(self):
        print(f"[{self.book_id}] {self.title} by {self.author} ${self.price: .2f}")


class Order:
    def __init__(self, customer, books):
        self.customer = customer
        self.books = books
        self.total_price = sum(book.price for book in books)

    def display_order_summary(self):
        print(f"\nOrder Summary for {self.customer.username}")
        for book in self.books:
            print(f"- {book.title} (${book.price:.2f})")
        print(f"Total: ${self.total_price:.2f}")

if __name__ == "__main__":
    book1 = Book(101, "Python Crash Course", "Eric Matthes", 30.00)
    book2 = Book(102, "Fluent Python", "Luciano Ramalho", 45.00)
    book3 = Book(103, "Automate the boring stuff", "Al Sweigart", 25.00)

    customer1 =  Customer("John Doe", "john@gmai.com", "Dhaka")
    admin1 = Admin("admin_user", "admin@store.com")

    admin1.display_user_info()
    customer1.display_user_info()

    print("\nAvailable Books: ")
    for book in [book1, book2,book3]:
        book.display_book()


    customer1.add_to_cart(book1)
    customer1.add_to_cart(book3)

    order1 =  Order(customer1, customer1.cart)
    order1.display_order_summary()
