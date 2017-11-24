import unittest

from main import merge_intervals, intervals_sub


class TestMerge(unittest.TestCase):

    def test_case_1(self):
        includes = [(10, 100)]
        excludes = [(20, 30)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        result = intervals_sub(merged_includes, merged_excludes)
        self.assertEqual(result, [(10, 19), (31, 100)])

    def test_case_2(self):
        includes = [(50, 5000), (10, 100)]
        excludes = None
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        result = intervals_sub(merged_includes, merged_excludes)
        self.assertEqual(result, [(10, 5000)])

    def test_case_3(self):
        includes = [(10, 100), (200, 300)]
        excludes = [(95, 205)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        result = intervals_sub(merged_includes, merged_excludes)
        self.assertEqual(result, [(10, 94), (206, 300)])

    def test_case_4(self):
        includes = [(10, 100), (200, 300), (400, 500)]
        excludes = [(95, 205), (410, 420)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        result = intervals_sub(merged_includes, merged_excludes)
        self.assertEqual(result, [(10, 94), (206, 300), (400, 409), (421, 500)])

if __name__ == '__main__':
    unittest.main()