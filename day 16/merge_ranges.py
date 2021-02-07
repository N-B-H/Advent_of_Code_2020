def merge_ranges(ranges):
    # sort input by start-times
    ranges = sorted(ranges)

    # start time of a new group of tuples
    new_range_start = int()

    # potential end time to close the newly merged tuple
    new_range_end = int()

    # collect merged meetings in new_ranges[]
    new_ranges = []

    # one iteration for every group of tuples that shall be merged until input is emptied out
    while len(ranges) > 0:

        # initialise first or new group of tuples
        new_range_start = ranges[0][0]
        new_range_end = ranges[0][1]  # to be augmented in case there is an intersection or direct neighbour-tuple

        # one iteration for every single tuple
        while len(ranges) > 1:

            if ranges[0][1] >= ranges[1][0]:  # =intersection or neighbour with next, merge!

                if ranges[0][1] <= ranges[1][1]:  # if end time of next tuple is later than current end time
                    new_range_end = ranges[1][1]  # extend current merge by setting new_range_end to end of next tuple

                else:  # next tuple starts later but finishes earlier.-> already within range of current merge!

                    # maintain current start and end time, remove next (irrelevant) tuple and compare to second next tuple with continue
                    new_range_end = ranges[0][1]
                    ranges.pop(1)
                    continue  # otherwise last item will cause an empty pop in next line

                ranges.pop(0)  # remove first tuple from list, because start has been saved before and end is somewhere later

            else:  # =no intersection/neighbour with next
                # close current merge by removing "open" meeting time
                # append current merge result(new_range_start,new_range_end) to new_ranges
                # so the next merge can begin with the next tuple in list, that will be at index 0 then
                ranges.pop(0)
                new_ranges.append((new_range_start, new_range_end))
                break

        else:  # last tuple in list

            # close current merge, append to new_ranges and break, because no more work to do
            ranges.pop(0)
            new_ranges.append((new_range_start, new_range_end))

    return new_ranges