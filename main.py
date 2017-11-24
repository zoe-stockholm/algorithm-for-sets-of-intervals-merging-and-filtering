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
    result = []
    pointer = 0

    # handle if excludes is None/empty, than no need to do any substraction
    if len(excludes) == 0:
        return includes

    for exclude in excludes:
        for idx, include in enumerate(includes[pointer:]):
            if include[1] < exclude[0]:
                continue
            else:
                after_sub = interval_sub(include, exclude)
                result += after_sub

                # check if sets of includes reach end
                if idx < len(includes) - 1:
                    if exclude[1] < includes[idx+1][0]:
                        pointer = idx
                        break

    return result


if __name__ == '__main__':

    includes = [(10, 100), (200, 300), (400, 500)]
    excludes = [(95, 205), (410, 420)]

    merged_includes = merge_intervals(includes)
    merged_excludes = merge_intervals(excludes)
    result = intervals_sub(merged_includes, merged_excludes)

    # expect result is [(10, 94), (206, 300), (400, 409), (421, 500)]
    print(result)