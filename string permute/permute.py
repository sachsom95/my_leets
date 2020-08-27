"This is manual"

def permutations(str):
    if len(str) == 1:
        return [str]
    if len(str) == 2:
        return [str, str[::-1]]
    else:
        current_level = str[0]
        next_level = permutations(str[1:])
        output = []
        for x in next_level:
            for y in range(len(x) + 1):
                temp_list = []
                temp_data = x
                temp_word = ""
                for z in range(len(x) + 1):
                    if z == y:
                        temp_word += current_level
                    else:
                        temp_word += temp_data[0]
                        temp_data = temp_data[1:]
                output.append([temp_word])
        return output
