import Calculator
import BookStore
import DLList
import algorithms


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "2":
            repeat = "Y"
            while repeat == "Y":
                var = input("Enter a variable: ")
                val = float(input("Enter its value: "))
                calculator.set_variable(var, val)
                repeat = input("Enter another variable? Y/N ")
        elif option == "3":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                calculator.print_expression(expression)
            else:
                print("Invalid expression")
        elif option == "4":
            try:
                exp = input("Enter the expression: ")
                result = calculator.evaluate(exp)
                print("Evaluating expression: ", end="")
                calculator.print_expression(exp)
                print("Result:", result)
            except ValueError:
                print("Result: Error - Not all variable values are defined.")

        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            book_key = input("Enter book key: ")
            result = bookStore.addBookByKey(book_key)
            if result != None:
                print("Added title:", result)
            else:
                print("Book not found.")
        elif option == "8":
            prefix = input("Introduce the prefix: ")
            book_result = bookStore.addBookByPrefix(prefix)
            if book_result == None:
                print("Error: Prefix was not found.")
            else:
                print("Added first matched title:", book_result)
        elif option == "9":
            infix = input("Enter infix: ")
            struct_int = int(input("Enter structure (1 or 2): "))
            max_num = input("Enter max number of titles: ")
            if max_num == "":
                max_num = 0
            bookStore.bestsellers_with(infix, struct_int, max_num)
        elif option == "10":
            print("Choose an algorithm:")
            print(" 1 - Merge Sort")
            print(" 2 - Quick Sort (first element pivot)")
            print(" 3 - Quick Sort (random element pivot")
            x = int(input("Your selection: "))
            if x == 1:
                algorithms.merge_sort(bookStore.bookCatalog)
            elif x == 2:
                algorithms.quick_sort(bookStore.bookCatalog, False)
            elif x == 3:
                algorithms.quick_sort(bookStore.bookCatalog, True)
            else:
                print("Invalid algorithm")
        elif option == "11":
            num_books = int(input("Enter the number of books to display: "))
            for i in range(num_books):
                print(bookStore.bookCatalog[i])


        ''' 
        Add the menu options when needed
        '''


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            y = input("Enter a word/phrase: ")
            palindrome = DLList.DLList()
            x = 0
            for i in y:
                if i.isalpha():
                    palindrome.add(x, i)
                    x += 1
            result = palindrome.isPalindrome()
            print("Result: ", end='')
            if result:
                print("Palindrome")
            else:
                print("Not a palindrome")


if __name__ == "__main__":
    main()
