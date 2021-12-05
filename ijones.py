def IJones(height, width, plate):
    result_path = [[0 for _ in range(width)] for _ in range(height)]
    memoized_paths = {}

    for row in range(height):
        current_letter = plate[row][0]
        result_path[row][0] = 1
        memoized_paths[current_letter] = memoized_paths.setdefault(current_letter, 0) + 1

    for column in range(1, width):
        paths_to_letter = {}

        for row in range(height):
            current_letter = plate[row][column]
            result_path[row][column] = memoized_paths.get(current_letter, 0)

            if plate[row][column-1] != current_letter:
                result_path[row][column] += result_path[row][column-1]
            paths_to_letter[current_letter] = paths_to_letter.setdefault(current_letter, 0) + result_path[row][column]

        for letter in paths_to_letter:
            memoized_paths[letter] = memoized_paths.setdefault(letter, 0) + paths_to_letter[letter]

    if height == 1:
        return result_path[0][width-1]

    return result_path[0][width-1] + result_path[height-1][width-1]