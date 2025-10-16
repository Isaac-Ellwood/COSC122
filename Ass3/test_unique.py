""" Tests for the unique module """
import os
import shutil
from stats import IS_MARKING_MODE
import unittest
from stats import StatCounter, PLATE_COMPS
from unique import uniques_by_merge_opp
from classes3 import NumberPlate
from utilities import read_unique_test_data, plates_from_strings


DATA_DIR = './test_data/'
DEF_SEED = 'a'
FILE_TEMPLATE = 'unique-{len1}-{len2}-{n_expected}-{seed}.txt'


def real_comparisons(counter):
    """ calling real_comparisons will be
        equivalent to calling StatCounter.get_count
    """
    return StatCounter.get_count(counter)




class BaseTester(unittest.TestCase):

    def setUp(self, is_subtest=False):
        """Runs before every test case"""
        StatCounter.reset_counts()

    def check_file_result_list(
            self, len1, len2, n_expected, min_comps, max_comps, seed=DEF_SEED):
        base_filename = FILE_TEMPLATE.format(len1=len1, len2=len2,
                                             n_expected=n_expected, seed=seed)
        filename = DATA_DIR + base_filename
        list1, list2, expected_uniques = read_unique_test_data(filename)
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertGreaterEqual(comparisons, min_comps, 
            msg=self.make_expected_comps_message(comparisons, min_comps, operator="geq"))
        self.assertLessEqual(comparisons, max_comps, 
            msg=self.make_expected_comps_message(comparisons, max_comps, operator="leq"))
        return True

    def check_file_comps(self, len1, len2, n_expected,
                         min_comps, max_comps, seed=DEF_SEED):
        base_filename = FILE_TEMPLATE.format(len1=len1, len2=len2,
                                             n_expected=n_expected, seed=seed)
        filename = DATA_DIR + base_filename
        list1, list2, expected_uniques = read_unique_test_data(filename)
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertGreaterEqual(comparisons, min_comps, 
            msg=self.make_expected_comps_message(comparisons, min_comps, operator="geq"))
        self.assertLessEqual(comparisons, max_comps, 
            msg=self.make_expected_comps_message(comparisons, max_comps, operator="leq"))
        return True

    def check_file_real_comps(
            self, len1, len2, n_expected, min_comps, max_comps, seed=DEF_SEED):
        base_filename = FILE_TEMPLATE.format(len1=len1, len2=len2,
                                             n_expected=n_expected, seed=seed)
        filename = DATA_DIR + base_filename
        list1, list2, expected_uniques = read_unique_test_data(filename)
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))
        return True

    operators = {
        "eq": "",
        "leq": "less than or equal to ",
        "geq": "greater than or equal to ",
    }

    def make_expected_comps_message(self, comparisons, expected_comparisons, operator="eq"):
        message = f"Your code used {int(comparisons)} comparisons "
        message += f"but was expected to use {self.operators[operator]}{int(expected_comparisons)}."
        return message

    def make_actual_comps_message(self, comparisons, actual_comparisons):
        message = f"Your code reported using {int(comparisons)} comparisons "
        message += f"but it actually used {int(actual_comparisons)}. "
        message += "This means you are miscounting comparisons, eg, "
        message += "not counting comparisons when they are done or "
        message += "counting comparisons that weren't done."
        return message



class TestTiny(BaseTester):

    def test_001_two_item_lists1(self):
        list1 = plates_from_strings(['AAA111', 'BBB111'])
        list2 = plates_from_strings(['BBB111', 'BBB113'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(['BBB113'])
        expected_comparisons = 3
        self.assertEqual(student_uniques, expected_uniques)
        self.assertEqual(comparisons, expected_comparisons, 
            msg=self.make_expected_comps_message(comparisons, expected_comparisons))

    def test_002_two_word_lists1_real_comparisons(self):
        list1 = plates_from_strings(['AAA111', 'BBB111'])
        list2 = plates_from_strings(['AAA112', 'BBB111'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_005_two_item_lists2(self):
        list1 = plates_from_strings(['AAA112', 'BBB222'])
        list2 = plates_from_strings(['AAA111', 'BBB222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(['AAA111'])
        expected_comparisons = 5
        self.assertEqual(student_uniques, expected_uniques)
        self.assertEqual(comparisons, expected_comparisons, 
            msg=self.make_expected_comps_message(comparisons, expected_comparisons))

    def test_006_two_word_lists2_real_comparisons(self):
        list1 = plates_from_strings(['AAA111', 'BBB222'])
        list2 = plates_from_strings(['AAA111', 'DDD222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_010_two_item_lists3(self):
        list1 = plates_from_strings(['AAA111', 'DDD222'])
        list2 = plates_from_strings(['AAA111', 'BBB222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(['BBB222'])
        expected_comparisons = 3
        self.assertEqual(student_uniques, expected_uniques)
        self.assertEqual(comparisons, expected_comparisons, 
            msg=self.make_expected_comps_message(comparisons, expected_comparisons))

    def test_011_two_word_lists3_real_comparisons(self):
        list1 = plates_from_strings(['AAA111', 'BBB222'])
        list2 = plates_from_strings(['AAA111', 'DDD222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))


class TestSmall(BaseTester):

    def test_030_identical_lists(self):
        list1 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'DDD444', 'EEE555'])
        list2 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'DDD444', 'EEE555'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = []
        lower_limit, upper_limit = 5, 10
        self.assertEqual(student_uniques, student_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_040_identical_lists_real_comparisons(self):
        list1 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'DDD444', 'EEE555'])
        list2 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'DDD444', 'EEE555'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_050_unique_lists(self):
        list1 = plates_from_strings(
            ['AAA111', 'DDD222', 'EEE333', 'EEE444', 'FFF121'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'CCC234', 'FFF111', 'FFF123', 'JJJ234'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(
            ['BBB111', 'CCC222', 'CCC234', 'FFF111', 'FFF123', 'JJJ234'])
        lower_limit, upper_limit = 13, 18
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_060_unique_lists_real_comparisons(self):
        list1 = plates_from_strings(
            ['AAA111', 'DDD222', 'EEE333', 'EEE444', 'FFF121'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'CCC234', 'FFF111', 'FFF123', 'JJJ234'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))


class TestSmall2(BaseTester):

    def test_070_cross_over_lists(self):
        list1 = plates_from_strings(
            ['BBB111', 'BBB222', 'BBB333', 'EEE444', 'FFF121'])
        list2 = plates_from_strings(
            ['AAA121', 'AAA122', 'AAA123', 'BBB111', 'BBB222', 'BBB333'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(['AAA121', 'AAA122', 'AAA123'])
        lower_limit, upper_limit = 9, 12
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_080_cross_over_lists_real_comparisons(self):
        list1 = plates_from_strings(
            ['BBB111', 'BBB222', 'BBB333', 'EEE444', 'FFF121'])
        list2 = plates_from_strings(
            ['AAA121', 'AAA122', 'AAA123', 'BBB111', 'BBB222', 'BBB333'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_090_cross_over_lists_2(self):
        list1 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'GGG111', 'HHH222'])
        list2 = plates_from_strings(
            ['DDD121', 'EEE122', 'FFF123', 'GGG111', 'HHH222', 'III333', 'JJJ333'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(
            ['DDD121', 'EEE122', 'FFF123', 'III333', 'JJJ333'])
        lower_limit, upper_limit = 13, 14
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_100_cross_over_lists_2(self):
        list1 = plates_from_strings(
            ['AAA111', 'BBB222', 'CCC333', 'GGG111', 'HHH222'])
        list2 = plates_from_strings(
            ['DDD121', 'EEE122', 'FFF123', 'GGG111', 'HHH222', 'III333', 'JJJ333'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))


class TestSmall3(BaseTester):

    def test_110_zig_zag_lists(self):
        list1 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        list2 = plates_from_strings(
            ['AAA121', 'DDD122', 'FFF123', 'HHH111', 'JJJJ222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(
            ['AAA121', 'DDD122', 'FFF123', 'HHH111', 'JJJJ222'])
        lower_limit, upper_limit = 13, 18
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_120_zig_zag_lists_real_comparisons(self):
        list1 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        list2 = plates_from_strings(
            ['AAA121', 'DDD122', 'FFF123', 'HHH111', 'JJJJ222'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_130_zig_zag_lists2(self):
        list1 = plates_from_strings(
            ['AAA121', 'DDD122', 'FFF123', 'HHH111', 'JJJJ222'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        lower_limit, upper_limit = 13, 18
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_140_zig_zag_lists2_real_comparisons(self):
        list1 = plates_from_strings(
            ['AAA121', 'DDD122', 'FFF123', 'HHH111', 'JJJJ222'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))

    def test_150_zig_zag_lists3(self):
        list1 = plates_from_strings(['AAA121', 'DDD122', 'FFF123', 'HHH111'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        expected_uniques = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        lower_limit, upper_limit = 12, 16
        self.assertEqual(student_uniques, expected_uniques)
        self.assertGreaterEqual(comparisons, lower_limit, 
            msg=self.make_expected_comps_message(comparisons, lower_limit, operator="geq"))
        self.assertLessEqual(comparisons, upper_limit, 
            msg=self.make_expected_comps_message(comparisons, upper_limit, operator="leq"))

    def test_160_zig_zag_lists2_real_comparisons(self):
        list1 = plates_from_strings(['AAA121', 'DDD122', 'FFF123', 'HHH111'])
        list2 = plates_from_strings(
            ['BBB111', 'CCC222', 'EEE333', 'GGG444', 'III121'])
        student_uniques, comparisons = uniques_by_merge_opp(list1, list2)
        self.assertEqual(comparisons, real_comparisons(PLATE_COMPS), 
            msg=self.make_actual_comps_message(comparisons, real_comparisons(PLATE_COMPS)))




class TestMediumFiles(BaseTester):

    test_list = [(200, 200, 9, 227, 409),
                 (200, 200, 10, 230, 410),
                 (1000, 1000, 90, 1270, 2090),
                 (1000, 1000, 999, 2997, 3995), ]

    def test_500_medium_files(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure

    def test_510_medium_files_real_comparisons(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_real_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure


class TestLargeFiles(BaseTester):

    test_list = [(100, 10000, 9999, 10088, 19975),
                 (10000, 1000, 5, 10992, 19979),
                 (10000, 1000, 900, 11898, 21698),
                 (10000, 10000, 200, 10600, 20200),
                 (10000, 10000, 1000, 13000, 21000),
                 (10000, 10000, 9999, 29997, 39995), ]

    def test_600_large_files(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure

    def test_610_large_files_real_comparisons(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_real_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure


class TestVeryLargeFiles(BaseTester):

    test_list = [(50000, 1000, 9, 51008, 100007),
                 (50000, 50000, 9, 50027, 100009),
                 (50000, 50000, 1000, 53000, 101000),
                 (50000, 50000, 9999, 79997, 109999),
                 (50000, 50000, 25000, 125000, 125000)]

    def test_540_very_large_files(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure

    def test_550_very_large_files_real_comparisons(self):
        for n1, n2, n_expected, min_comps, max_comps in self.test_list:
            self.setUp(is_subtest=True)  # needed as subTest doesn't call it...
            passed = False
            with self.subTest(len1=n1, len2=n2, len_exp=n_expected):
                passed = self.check_file_real_comps(
                    n1, n2, n_expected, min_comps, max_comps)
            if not passed:
                break  # stop subtests after first failure




def all_tests_suite():
    suite = unittest.TestSuite()
    test_loader = unittest.defaultTestLoader.loadTestsFromTestCase

    suite.addTest(test_loader(TestTiny))

    # uncomment the following when you are ready to rumble
    # suite.addTest(test_loader(TestSmall))
    # suite.addTest(test_loader(TestSmall2))
    # suite.addTest(test_loader(TestSmall3))

    # suite.addTest(test_loader(TestMediumFiles))
    # suite.addTest(test_loader(TestLargeFiles))
    # suite.addTest(test_loader(TestVeryLargeFiles))
    return suite




def main():
    """ Makes a test suite and runs it. Will your code pass? """
    test_runner = unittest.TextTestRunner(verbosity=2)
    all_tests = all_tests_suite()
    test_runner.run(all_tests)



if __name__ == '__main__':
    main()
