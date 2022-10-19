'''
Module for class BookLoverTestSuite, which tests the methods of a BookLover
'''

import unittest
from booklover import *

class BookLoverTestSuite(unittest.TestCase):
    '''
    Tests the methods of a BookLover

    Instance variables:
        none

    Public methods:
        test_1_init
    '''

    def setUp(self):
        '''
        Creates a instance variable with a value of a BookLover

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Creates an instance variable with a value of a BookLover

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        self.book_lover = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')

    def test_0_init(self):
        '''
        Tests BookLover.__init__

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Tests whether a BookLover's name, email, favorite genre, number of read books, and book list are equal to expected values

        Exceptions raised:
            AssertionError if a BookLover's name, email, favorite genre, number of read books, or book list is not equal to an expected value

        Restrictions on when this method can be called:
            none
        '''

        self.assertEqual(self.book_lover.name, 'Han Solo')
        self.assertEqual(self.book_lover.email, 'hsolo@millenniumfalcon.com')
        self.assertEqual(self.book_lover.fav_genre, 'scifi')
        self.assertEqual(self.book_lover.num_books, 0)
        self.assertTrue(self.book_lover.book_list.equals(pd.DataFrame({'book_name':[], 'book_rating':[]}).astype(dtype = {'book_name': 'str', 'book_rating': 'int'})))


    def test_1_add_book(self):
        '''
        Tests BookLover.add_book by confirming that a book was successfully added to a BookLover's read book list

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Adds a book to the read-book list of a BookLover and tests whether the book is in the BookLover's read-book list

        Exceptions raised:
            AssertionError if a book, including book name and rating, is not correctly added to the read-book list of a BookLover

        Restrictions on when this method can be called:
            none
        '''
        
        self.book_lover.add_book('Star Wars: A New Hope', 5)
        self.assertTrue(self.book_lover.book_list.equals(pd.DataFrame({'book_name':['Star Wars: A New Hope'], 'book_rating':[5]})))

    def test_2_add_book(self):
        '''
        Tests BookLover.add_book by running test_1_add_book twice

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Adds a book to the read-book list of a BookLover and tests whether the book is in the BookLover's read-book list

        Exceptions raised:
            AssertionError if a book, including book name and rating, is not correctly added to the read-book list of a BookLover

        Restrictions on when this method can be called:
            none
        '''
        
        self.book_lover.add_book('Star Wars: A New Hope', 5)
        self.assertTrue(self.book_lover.book_list.equals(pd.DataFrame({'book_name':['Star Wars: A New Hope'], 'book_rating':[5]})))

    def tearDown(self):
        '''
        Deletes an instance variable with a value of a BookLover

        Keyword arguments:
            none

        Return values:
            none

        Side effects:
            Deletes an instance variable with a value of a BookLover

        Exceptions raised:
            none

        Restrictions on when this method can be called:
            none
        '''

        del self.book_lover

if __name__ == '__main__':
    verbose = 3
    unittest.main(verbosity = verbose)