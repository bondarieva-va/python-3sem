#Boyer–Moore–Horspool algorithm

def symbol_not_in_substring(symbol, substring):
    return symbol not in substring


def create_offsets(substring, substring_uniq_symbols):
    offset_table = {}

    for i in range(len(substring) - 2, -1, -1):
        index = substring[i]
        if symbol_not_in_substring(index, substring_uniq_symbols):
            offset_table[index] = len(substring) - i - 1
            substring_uniq_symbols.add(substring[i])
    return offset_table


def check_last_symbol_in_template(substring, substring_uniq_symbols, offset_table):
    if symbol_not_in_substring(substring[len(substring) - 1], substring_uniq_symbols):
        offset_table[substring[len(substring) - 1]] = len(substring)

    return offset_table


def generate_offset_table(substring):
    substring_uniq_symbols = set()
    offset_table = create_offsets(substring, substring_uniq_symbols)
    offset_table = check_last_symbol_in_template(substring, substring_uniq_symbols, offset_table)
    offset_table['$'] = len(substring)

    return offset_table


def compare_string_len(string, substring):
    return len(substring) <= len(string)


def process_find_substring(original_text, substring, offset_table):
    substring_index = len(substring) - 1
    while substring_index < len(original_text):
        k = 0
        j = 0
        for j in range(len(substring) - 1, -1, -1):
            if original_text[substring_index - k] != substring[j]:
                if j == len(substring) - 1:
                    if offset_table.get(original_text[substring_index], False):
                        offset = offset_table[original_text[substring_index]]
                    else:
                        offset = offset_table['$']
                else:
                    offset = offset_table[substring[j]]

                substring_index += offset
            k += 1
        if j == 0:
            return True
    else:
        return False


def find_substring(original_text, substring, offset_table,):
    if compare_string_len(original_text, substring):
        return process_find_substring(original_text, substring, offset_table)
    else:
        return False


def main():
    text = input("Enter text: ")
    template = input("Enter a template: ")
    my_file = open("file.txt", "w")

    offset_table = generate_offset_table(template)

    if find_substring(text, template, offset_table):
        print('Substring', template, 'found')
        my_file.write('Substring found')
    else:
        print('Substring not found')
        my_file.write('Substring not found')
    my_file.close()

main()
