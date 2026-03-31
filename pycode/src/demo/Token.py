def tokenize(lines, token='word'):
    if token == 'word':
        return [line.split() for line in lines]
    elif token == 'char':
        return [list(line) for line in lines]


if __name__ == '__main__':
    lines = ['the time machine by h g wells', 'twinkled and his usually pale face was flushed']
    print(lines[0])
    # print(lines[1])
    print(list(lines[0]))
    tokens = tokenize(lines)
    print(tokens[0])
