class Media:

    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating
    

class Book(Media):
    
    type = "books"

    def __init__(self, name, author, genre, rating, num_words):
        super().__init__(name, genre, rating)
        self.num_words = num_words
        self.author = author

class Game(Media):

    type = "games"

    def __init__(self, name, genre, rating, hours_played, console):
        super().__init__(name, genre, rating)
        self.hours_played = hours_played
        self.console = console

class Tv(Media):

    type = "shows"

    def __init__(self, name, genre, rating, stream_service, num_seasons):
            super().__init__(name, genre, rating)
            self.stream_service = stream_service
            self.num_seasons = num_seasons

class My_Media_Library:

    def __init__(self, my_library = {"books":{}, "games":{}, "shows": {}}):
        self.my_library = my_library

    def get_library(self):
        # yes, I know, don't say it: triple-nested for loop is big O complexity = outrageous
        # I'd find some other solution if performance mattered...but if performance
        # mattered, we'd be dealing with Large dictionaries, and you wouldn't
        # be asking us to print the entire thing in the first place. We'd just output to
        # a flat csv or something. Instead, here, we'd likely only
        # ever print subsets of the full thing based on more user queries. Could be implemented
        # later. That might be interesting: show me all books with genre "...", for example.
        for category, value in self.my_library.items():
            print(f'{category}:')
            for sub_category, sub_value in value.items():
                print(f'  {sub_category}:')
                for media_info, media_value in sub_value.items():
                    if media_info != "name":
                        print(f'    {media_info}: {media_value}')

    def new_library(self):
        self.my_library = {"books" : {}, "games" : {}, "shows" : {}}

    def check_library(self, media_to_check, title_to_check):
        if title_to_check in self.my_library[media_to_check]:
            print(f"{title_to_check} is in the library. Here's the entry:\n")
            print(self.my_library[media_to_check][title_to_check])
            user_edit = input("Do you want to edit this entry? (y/n): ").lower()
            if "y" in user_edit:
                if media_to_check == "books":
                    self.edit_book(media_to_check, title_to_check)
                elif media_to_check == "games":
                    self.edit_game(media_to_check, title_to_check)
                else:
                    self.edit_tv_show(media_to_check, title_to_check)
            else:
                print("Returning to main menu.")
        else:
            print(f'{title_to_check} has not yet been added. Make sure you typed the title correctly if you think it should be here. Returning to main menu.') 

    def add_book(self):
        new_book = Book(name = input("Enter the book's title: "),
                        author = input("Enter the book's author: "),
                        genre = input("Enter the book's genre: "),
                        rating = input("Enter your 1-5 rating of the book (1=worst 5=best): "),
                        num_words = input("Enter book's word count: "))
        
        title = new_book.name
        self.my_library["books"][title] = new_book.__dict__

    def add_game(self):
        new_game = Game(name = input("Enter the game's title: "),
                        genre = input("Enter the game's genre: "),
                        rating = input("Enter your 1-5 rating of the game (1=worst 5=best): "),
                        hours_played = input("Enter your hours played so far: "),
                        console = input("On which console do you play this game? "))
        
        title = new_game.name
        self.my_library["games"][title] = new_game.__dict__

    def add_tv_show(self):
        new_show = Tv(name = input("Enter the show's title: "),
                        genre = input("Enter the show's genre: "),
                        rating = input("Enter your 1-5 rating of the show (1=worst 5=best): "),
                        stream_service = input("Enter the streaming service used: "),
                        num_seasons= input("How many seasons are available? "))
        
        title = new_show.name
        self.my_library["shows"][title] = new_show.__dict__

    def remove_entry(self, media_to_remove, title_to_remove):
        del(self.my_library[media_to_remove][title_to_remove])

    def edit_book(self, media_to_edit, title_to_edit):
        this_edit = input("Which parameter would you like to edit? Note, you can't edit the title/name. Please type only 'genre', 'rating', 'author' or 'num_words':\n").lower()
        if this_edit == "genre" or this_edit == "author" or this_edit == "rating" or this_edit == "num_words":
            new_value = input(f"Please enter a new value for {this_edit}: ")
            self.my_library[media_to_edit][title_to_edit][this_edit] = new_value
        else:
            print("Sorry, that's not a parameter you can edit, returning to main menu.")

    def edit_tv_show(self, media_to_edit, title_to_edit):
        this_edit = input("Which parameter would you like to edit? Note, you can't edit the title/name. Please type only 'genre', 'rating', 'stream_service' or 'num_seasons':\n").lower()
        if this_edit == "genre" or this_edit == "rating" or this_edit == "stream_service" or this_edit == "num_seasons":
            new_value = input(f"Please enter a new value for {this_edit}: ")
            self.my_library[media_to_edit][title_to_edit][this_edit] = new_value
        else:
            print("Sorry, that's not a parameter you can edit, returning to main menu.")

    def edit_game(self, media_to_edit, title_to_edit):
        this_edit = input("Which parameter would you like to edit? Note, you can't edit the title/name. Please type only 'genre', 'rating', 'hours_played' or 'console':\n").lower()
        if this_edit == "genre" or this_edit == "rating" or this_edit == "hours_played" or this_edit == "console":
            new_value = input(f"Please enter a new value for {this_edit}: ")
            self.my_library[media_to_edit][title_to_edit][this_edit] = new_value
        else:
            print("Sorry, that's not a parameter you can edit, returning to main menu.")

    def view_subset(self):
        pass

    def main(self):
        while True:
            user_choice = input("What would you like to do?\nOptions include add entry, check/edit entry, remove entry, view library, or quit: ").lower()
            if "add" in user_choice:
                which_entry = input("Do you want to add a book, game, or tv show? ").lower()
                if "book" in which_entry:
                    self.add_book()
                elif "game" in which_entry:
                    self.add_game()
                elif "show" in which_entry:
                    self.add_tv_show()
                else:
                    print("Sorry, that wasn't a valid option as typed, returning to main menu.")
            elif "view" in user_choice:
                print("Displaying entire library:\n")
                self.get_library()
            elif "check" in user_choice or "edit" in user_choice:
                check_category = input("Do you want to check/edit books, games, or shows? (Please type only 'books', 'games', or 'shows'.) ").lower()
                if "books" == check_category or "games" == check_category or "shows" == check_category:
                    check_title = input("What's the exact, formatted title you want to check/edit? ")
                    self.check_library(check_category, check_title)
                else:
                    print("Sorry, that wasn't a valid option as typed, returning to main menu.")
            elif "remove" in user_choice:
                del_category = input("Do you want to delete books, games, or shows? (Please type only 'books', 'games', or 'shows'.) ").lower()
                if "books" == del_category or "games" == del_category or "shows" == del_category:
                    del_title = input("What's the exact, formatted title you want to delete? ")
                    if del_title in self.my_library[del_category]:
                        print(f"Deleting: {del_category}: {del_title}")
                        self.remove_entry(del_category, del_title)
                    else:
                        print("That title wasn't actually in the library, returning to main menu.")
                else:
                    print("Sorry, that wasn't a valid option as typed, returning to main menu.")
            elif user_choice == "quit" or user_choice=="q":
                return(self.my_library)
            else:
                print("Sorry, that wasn't a valid option as typed, returning to main menu.")

