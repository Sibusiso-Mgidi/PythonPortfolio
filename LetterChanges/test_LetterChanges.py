'''
Unittests for LetterChanges from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import LetterChanges


class test_LetterChanges(unittest.TestCase):
    '''
    Class contains unittests for LetterChanges.py
    '''

    #region Unittests    
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = LetterChanges.LetterChanges("aaa bbb ccc")
        self.assertEqual(output, "bbb ccc ddd")

    def test_ProperOutputVowels(self):
        '''
        Checks if vowels became uppercase.
        '''
        output = LetterChanges.LetterChanges("bbb ccc ddd")
        self.assertEqual(output, "ccc ddd EEE")

    def test_UppercaseInInput(self):
        '''
        Checks if Uppercase letters in input, are convert lowercase in output as expected.
        '''
        output = LetterChanges.LetterChanges("aaa BBb ccc")
        self.assertEqual(output, "bbb ccc ddd")    

    def test_EmptyOutput(self):
        '''
        Checks if output is empty for empty input.
        '''
        output = LetterChanges.LetterChanges("")
        self.assertEqual(output, "")

    def test_NoLetters(self):
        '''
        Checks if input is without letters
        then output is equal to input.
        '''
        output = LetterChanges.LetterChanges("1234")
        self.assertEqual(output, "1234")

    def test_MixedLettersOtherSignsOutput(self):
        '''
        Checks if output is as expected for mixed characters.
        '''
        output = LetterChanges.LetterChanges("1234a?//")
        self.assertEqual(output, "1234b?//")

    def test_TypeAssertion(self):
        '''
        Checks if output is equal -1 for input type other than string.
        '''
        output = LetterChanges.LetterChanges(23)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()        