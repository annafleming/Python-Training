
if __name__ == '__main__':
    sequence = []
    done = False
    while not done:
        try:
            sequence.append(input("Write something: \n"))
        except EOFError:
            for i in range(len(sequence)):
                print(sequence.pop())
            done = True


