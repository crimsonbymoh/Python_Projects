def remove_odd_index(characters):

    result = ""

    for i in range(len(characters)):

        if i % 2 == 1:

            result += characters[i]

    return result


