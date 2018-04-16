def load_data():
    init_list = [
        "Deep Learning_2018",
        "Weapons of ... _2011",
        "Computer System_2018",
        "Bitcoin blah blah_2016",
        "Code Complete_2017"
    ]
    return init_list


def sort_books(books):
    for i in range(len(books)):
        for j in range(len(books) - 1 - i):
            if books[j] > books[j + 1]:
                temp = books[j]
                books[j] = books[j + 1]
                books[j + 1] = temp
    return books


def filter_books_by_pubdate(books, filter_date):
    result = []
    for b in books:
        book_date = b[-4:]
        if int(book_date) >= filter_date:
            result.append(b)
    return result


def print_books(books, caption):
    print("------", caption, "------")
    for index in range(0, len(books)):
        print(index + 1, books[index])


# main()
book_list = load_data()
print_books(book_list, "initial data")

aaa = sort_books(book_list)
print_books(aaa, "sorted data")

pubdate = 2017
bbb = filter_books_by_pubdate(book_list, pubdate)
print_books(bbb, "extracted data")
