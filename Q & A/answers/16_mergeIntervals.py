def merge_intervals(intervals):
    # If there are no intervals, return an empty list
    if not intervals:
        return []

    # Sort the intervals by the start of each interval
    intervals.sort(key=lambda x: x[0])

    # Initialize the result list with the first interval
    merged = [intervals[0]]

    for current in intervals[1:]:
        # Get the last interval in the merged list
        last_merged = merged[-1]

        # If the current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge the intervals by updating the end of the last merged interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, so add the current interval to the result list
            merged.append(current)

    return merged
