def count_repetitions(tokens):
    occurences = {}
    current_word_counter = 0
    while current_word_counter < len(tokens):
        current_word = tokens[current_word_counter]
        if current_word not in occurences:
            for next_word in tokens[current_word_counter + 1:]:
                if current_word == next_word:
                    if current_word in occurences:
                        occurences[current_word] = occurences[current_word] + 1
                    else:
                        occurences[current_word] = 2

        current_word_counter += 1

    return occurences