import unittest

from main import merge_intervals, intervals_sub, remove_overlap


class TestMerge(unittest.TestCase):

    def test_case_1(self):
        includes = [(10, 100)]
        excludes = [(20, 30)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        after_sub = intervals_sub(merged_includes, merged_excludes)
        result = remove_overlap(after_sub)
        self.assertEqual(result, [(10, 19), (31, 100)])

    def test_case_2(self):
        includes = [(50, 5000), (10, 100)]
        excludes = None
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        after_sub = intervals_sub(merged_includes, merged_excludes)
        result = remove_overlap(after_sub)
        self.assertEqual(result, [(10, 5000)])

    def test_case_3(self):
        includes = [(10, 100), (200, 300)]
        excludes = [(95, 205)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        after_sub = intervals_sub(merged_includes, merged_excludes)
        result = remove_overlap(after_sub)
        self.assertEqual(result, [(10, 94), (206, 300)])

    def test_case_4(self):
        includes = [(10, 100), (200, 300), (400, 500)]
        excludes = [(95, 205), (410, 420)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        after_sub = intervals_sub(merged_includes, merged_excludes)
        result = remove_overlap(after_sub)
        self.assertEqual(result, [(10, 94), (206, 300), (400, 409), (421, 500)])

    def test_case_5(self):
        includes = [(90, 100), (50, 60), (20, 190), (400, 550), (700, 800), (230, 410)]
        excludes = [(500, 750), (150, 269)]
        merged_includes = merge_intervals(includes)
        merged_excludes = merge_intervals(excludes)
        after_sub = intervals_sub(merged_includes, merged_excludes)
        result = remove_overlap(after_sub)
        self.assertEqual(result, [(20, 149), (270, 499), (751, 800)])

if __name__ == '__main__':
    unittest.main()