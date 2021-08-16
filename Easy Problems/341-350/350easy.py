#https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/
import sys

#Finds the current book in a set of books
def find_cur_book(books, low):
    for item in books:
        if item[0] == low:
            return item

#Organizes shelves
def organize(shelves, books):
    #Sorts shelves to go with lowest, makes final list
    shelves = sorted(shelves)
    shelves_lst = []
    #Grabs a list of book width's, and the lowest one.
    b_lst = [int(b[0]) for b in books]
    lowest = str(min(b_lst))
    #Current shelf count
    shelf_count = 1

    #For every shelf
    for i in shelves:
        #If a book is higher than any possible shelf
        if max(b_lst) > max(shelves):
            print("impossible")
            return

        # If no more books
            if len(books) == 0:
                break

        #Stores all books for shelf, and current shelf amt
        cur_lst = []
        cur_i = i

        while i > int(lowest):
            # If no more books
            if len(books) == 0:
                break

            #grabs lowest
            b_lst = [int(b[0]) for b in books]
            lowest = str(min(b_lst))

            #grabs current book, appends to list
            cur_book = find_cur_book(books, lowest)
            cur_lst.append("{}: ({}w)".format(cur_book[1], cur_book[0]))

            #Takes the width and leftover from the book shelf
            i -= int(lowest)
            if int(lowest) > 0:
                i -= i % 10

            #Takes book off the book list
            books.remove(cur_book)


        #Add to final list, remove book shelf from book list, increment shelf count for final list
        if len(cur_lst) > 0:
            item = "Shelf {} ({} width): ".format(shelf_count, str(cur_i)) + ', '.join(cur_lst)
        else:
            item = "Shelf {} ({} width): ".format(shelf_count, str(cur_i)) + "Empty shelf"

        shelves_lst.append(item)
        shelves.remove(cur_i)
        shelf_count += 1

    #Print all items
    for s in shelves_lst:
        print(s)

#Grabs shelves; use enter to activate
shelves = list(map(int, sys.stdin.readline().split()))
shelves.sort(reverse=True)

#Grabs books; use "CTRL+D or "CTRL+Z" to activate
books = sys.stdin.readlines()
books = [(b.replace('\n', '').split(' ', 1)) for b in books]
organize(shelves, books)