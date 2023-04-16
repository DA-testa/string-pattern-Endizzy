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

def getHash(text, Weight):
    tHash = 0
    for i in range(Weight):
        tHash +=  ord(text[i]) * pow(10,Weight - i -1)

    return tHash


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    pa = len(pattern)
    te = len(text)
    occurrences = []

    paHash = getHash(pattern,pa)
    teHash = getHash(text,te)

    for i in range(te - pa + 1):
        if paHash == teHash:
            continue

        if text[i:i+pa] == pattern:
            occurrences.append(i)


    # and return an iterable variable
    return occurrences





def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))




# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))