# Nikita Smirnovs 221RDB433
# python3
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    command = input().strip().upper()
    
    match command:
        case "I":
            pattern = input().strip()
            text = input().strip()
            return (pattern, text)

        case "F":
            with open(f"tests/06") as f:
                lines = f.readlines()
                return (lines[0].strip(),lines[1].strip())
        case _:
            print("input error")
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    command = input().strip().upper()
    
    if command == "I":
        pattern = input().strip()
        text = input().strip()
        return (pattern, text)

    elif command == "F":
        with open(f"tests/06") as f:
            lines = f.readlines()
            return (lines[0].strip(),lines[1].strip())
    else:
        print("input error")
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    pa = len(pattern)
    te = len(text)
    occurrences = []

    paHash = 0
    teHash = 0

    for i in range(pa):
        paHash +=  ord(pattern[i])
        teHash +=  ord(text[i])

    for i in range(te - pa + 1):
        if paHash == teHash:
            if text[i:i+pa] == pattern:
                occurrences.append(i)

        if i < te - pa:
            teHash = teHash - ord(text[i]) + ord(text[i+pa])

    # and return an iterable variable
    return occurrences


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
