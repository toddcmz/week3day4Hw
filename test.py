import unittest
from demoLibrary import demo_dict
from main import My_Media_Library

# takeaways from implementing this: I need to research whether there's a way to pass
# in pre-programmed user input responses in the cases I have below, otherwise it's
# not that convenient a testing script. Interesting.

class Test_Library(unittest.TestCase):

    # test deleting a book
    def delete_book_test(self):
        test_this_library = My_Media_Library(demo_dict)
        test_this_library.remove_entry("books", "Ender's Game")
        self.assertNotIn("Ender's Game", test_this_library["books"])
    
    # can I run a test on something that asks for input? turns out, yes! great.
    # of course, you have to actually change the rating here in the input call...else
    # I suppose this test would fail. 
    def test_edit_existing_tv_rating(self):
        test_this_library = My_Media_Library(demo_dict)
        test_this_library.edit_tv_show("shows", "Severance")
        self.assertNotEqual(test_this_library.my_library["shows"]["Severance"]["rating"],5)

    # like the test above which requires user input, you have to input the correct thing.
    # I'm not sure how you'd do this otherwise...you'd have to completely restructure
    # the method to accept previously defined input, perhaps? I don't want to do that.
    # So testers must add a game titled "testGame" in this case for this test to work.
    # this probably isn't so much in the spirit of this sort of testing. Meh.
    def test_add_new_game(self):
        test_this_library = My_Media_Library(demo_dict)
        test_this_library.add_game()
        self.assertIsInstance(test_this_library.my_library["games"]["testGame"], dict)

if __name__ == '__main__':
    unittest.main()