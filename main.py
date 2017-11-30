import itertools


def merge_intervals(intervals):
    # handle if inputs is None
    if intervals is None:
        return []

    after_sorted = sorted(intervals, key=lambda interval: interval[0])

    merged = []

    for higher in after_sorted:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # in after_sorted, lower[0] <= higher[0] always
            if higher[0] > lower[1]:
                merged.append(higher)
            else:
                upper_bound = max(lower[1], higher[1])
                # merge current higher and current lower intervals
                merged[-1] = (lower[0], upper_bound)

    return merged


def interval_sub(include, exclude):
    down_include = include[0]
    upper_include = include[1]
    down_exclude = exclude[0] - 1
    upper_exclude = exclude[1] + 1

    after_sorted = sorted((down_include, down_exclude, upper_include, upper_exclude))
    result = []

    if after_sorted[0] == down_include:
        result.append((after_sorted[0], after_sorted[1]))
    if after_sorted[-1] == upper_include:
        result.append((after_sorted[2], after_sorted[-1]))

    return result


def intervals_sub(includes, excludes):
    for exclude in excludes:
        includes = list(itertools.chain(*[interval_sub(include, exclude) for include in includes]))
        
    return includes


if __name__ == '__main__':

    #includes = [(10, 100), (200, 300), (400, 500)]
    #excludes = [(95, 205), (410, 420)]
    #includes = [(10, 100), (200, 300), (400, 500), (600,800)]
    #excludes = [(95, 205), (265, 295), (280, 290)]
    #includes = [(1,200), (400,500), (600,700)]
    #excludes = [(10,20), (30,40), (50,60)]
    #includes = [(1,200), (300,400), (500,600)]
    #excludes = [(1,5), (10,20), (30,400)]
    #includes = [(1,200), (300,400), (500,600)]
    #excludes = [(320,330), (340,350)]
    includes = [(1,200), (300,400), (500,600), (700,800), (900,1000)]
    excludes = [(120,330), (340,350), (920,930)]

    merged_includes = merge_intervals(includes)
    merged_excludes = merge_intervals(excludes)
    after_sub = intervals_sub(merged_includes, merged_excludes)

    # expect result is [(1, 119), (331, 339), (351, 400), (500, 600), (700, 800), (900, 919), (931, 1000)]
    print(after_sub)
