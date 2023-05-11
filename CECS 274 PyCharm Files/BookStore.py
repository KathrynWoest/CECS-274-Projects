import Book
import ArrayList
# import ArrayQueue
# import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import time
import MaxQueue


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                # self.bookIndices.add(key, self.bookCatalog.size() - 1)
                # self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
            return s

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        printed = 0
        for book in self.bookCatalog:
            if infix in book.title and printed < cnt:
                print(book)
                printed += 1
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        start_time = time.time()
        top_book = self.shoppingCart.max()
        elapsed_time = time.time() - start_time
        print("getCartBestSeller returned")
        print(top_book.title)
        print(f"Completed in {elapsed_time} seconds")

    def addBookByKey(self, key):
        start_time = time.time()
        x = self.bookIndices.find(key)
        if x != None:
            s = self.bookCatalog.get(x)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"addBookByKey Completed in {elapsed_time} seconds")
            return s.title
        return x

    def addBookByPrefix(self, prefix):
        if prefix == "":
            return None
        book = self.sortedTitleIndices.smallest_key(prefix)
        n = len(prefix)
        if book.k == None or book.k[0:n] != prefix:
            return None
        else:
            s = self.bookCatalog.get(book.v)
            self.shoppingCart.add(s)
            return s.title

    def bestsellers_with(self, infix, structure, w=0):
        n = int(w)
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")

        if best_sellers != None:
            if infix == "":
                print("Invalid infix.")
            elif n < 0:
                print("Invalid number of titles.")
            else:
                start_time = time.time()
                for i in self.bookCatalog:
                    if infix in i.title:
                        if structure == 1:
                            best_sellers.add(i.rank, i)
                        elif structure == 2:
                            i.rank *= -1
                            best_sellers.add(i)
                if structure == 1:
                    if n == 0:
                        book_list = best_sellers.in_order()
                        book_list.reverse()
                        for i in range(len(book_list)):
                            print(book_list[i].v)
                    else:
                        books = best_sellers.in_order()
                        books.reverse()
                        book_list = books[0:n]
                        for i in range(len(book_list)):
                            print(book_list[i].v)
                elif structure == 2:
                    if n == 0:
                        for i in range(best_sellers.n):
                            x = best_sellers.remove()
                            if x.rank < 0:
                                x.rank *= -1
                            print(x)
                    else:
                        for i in range(n):
                            x = best_sellers.remove()
                            if x.rank < 0:
                                x.rank *= -1
                            print(x)

                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
