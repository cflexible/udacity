def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    values = collections.OrderedDict(sorted(values.items()))
    boxesCount = len(square_units)
    # print("Wir haben ", boxesCount, " Boxen\n")
    for bi in range(boxesCount):
        box = square_units[bi]
        full = ''
        # first I put all the values together in a string
        for sbi in box:
            subValue = values[sbi]
            if len(subValue) > 1:
                full = full + subValue

        """ This is optional for eleminating values where we already have a single value like in D5
        singleslist = []

        for sbi in box:
            subValue = values[sbi]
            if len(subValue) == 1:
                full = full.replace(subValue, '')
                singleslist.append(subValue)
        """

        # Now I check the characters in the full and if it is only one time there I use it
        for sbi in box:
            subValue = values[sbi]
            """ This is for the optional single value part
            for item in singleslist:
                if item in subValue and len(subValue) > 1:
                    subValue = subValue.replace(item, '')
                    values[sbi] = subValue
            """

            if len(subValue) > 1:
                for s in range(len(subValue)):
                    subChar = subValue[s]
                    if full.count(subChar) == 1:
                        values[sbi] = subChar
                        # print("Setze ", sbi, " auf ", subChar)
    
    return values
