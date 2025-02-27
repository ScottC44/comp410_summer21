import unittest
from demo import show_aggie_pride


# https://docs.python.org/3/library/unittest.html
class MyTestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        df = show_aggie_pride()

        self.assertEqual(df.loc[0, 'Text'], 'Aggie Pride')
        self.assertEqual(df.loc[1, 'Text'], 'Worldwide')
        self.assertEqual(df.loc[2, 'Text'], 'Hard Work Yields Results')
        self.assertEqual(df.loc[3, 'Text'], 'Work today for what you want to achieve tomorrow')
        self.assertEqual(df.loc[4, 'Text'], 'Aggies DO!')
        self.assertEqual(df.loc[5, 'Text'], 'Giving Back Every Day, the Aggie Way')
        self.assertEqual(df.loc[6, 'Text'], 'Aggies Rule')
        self.assertEqual(df.loc[7, 'Text'], 'When One Door Closes Another One Opens')
        self.assertEqual(df.loc[8, 'Text'], 'Aggie Pride')
        self.assertEqual(df.loc[9, 'Text'], 'Aggies on fire')




if __name__ == '__main__':
    unittest.main()
