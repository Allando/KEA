#!/bin/python


def main():
    print("Hello, there!")

    choice = input("1) Write\n2) Read\n\n0) Exit\n> ")

    filename = "coolfile.txt"

    if choice == "1":
        with open(filename, 'a') as f:
            m = True
            while m == True:
                w = input("> ")
                f.write(w + '\n')
                if w == "":
                    m = False
        f.close()
    elif choice == "2":
        with open(filename, 'r') as f:
            print(f.read())

    elif choice == "0":
        print("Exiting...")
        exit(0)


if __name__ == '__main__':
    main()
