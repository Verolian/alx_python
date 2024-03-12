from sys import argv

if __name__ == '__main__':
    
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}{'.' if num_args == 0 else ':'}")

    for i in range(1, num_args + 1):
        print(f"{i}: {argv[i]}")