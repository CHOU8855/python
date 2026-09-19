class Books:
    def __init__(self, title,author, isborrow):
        self.title = title
        self.author = author
        self.science = isborrow

    def borrow(self):
        print('You have borrowed this book')

    def giveback(self):
        print('You have returned this book')

obj_novel = Books()
obj_comic = Books()
obj_science = Books()

for Books in (obj_novel,obj_science,obj_comic):
    Books.borrow
    Books.giveback



    

    