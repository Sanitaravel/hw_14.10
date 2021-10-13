import logged_in, counter


def main():
    print("Hello. This is my homework for 14.10.")
    while True:
        print()
        print("To see logged_in decorator task enter '"'logged_in'"'. To finish server press CTRL+C")
        print("To see counter decorator task enter '"'counter'"'.")
        print("To exit enter '"'exit'"'")
        com = input()
        if com == "logged_in":
            logged_in.start_flask()
        elif com == "counter":
            counter.counter()
        elif com == "exit":
            print("Goodbuy")
            break
        else:
            print("Command is unknown")
            continue


if __name__ == "__main__":
    main()
