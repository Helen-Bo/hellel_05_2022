from datetime import datetime
from os import listdir

PREFIX = "./lesson_6_conman_decor/classwork/"
LOG_FILE = PREFIX + "actions.log"


def get_log_message(username: str, message: str) -> str:
    return f"{datetime.now()} {username}: {message}"


def log_action(text: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"{text}\n")


def read_usb(username: str):
    log_action(get_log_message(username, "Opened USB"))
    filename = PREFIX + "/f-disc/"
    dirs = listdir(filename)
    filtered = [dir for dir in dirs if not dir.startswith(".")]
    return filtered


def read_cd(username: str):
    log_action(get_log_message(username, "Opened Cd"))
    return listdir(PREFIX + "c-disc/")


def main():
    username = input("Enter your name: ")

    if not username:
        raise ValueError("No username specified...")

    while user_input := input("Enter the option [usd / cd]: "):
        if user_input == "cd":
            files = read_cd(username)
        elif user_input == "usb":
            files = read_usb(username)
        else:
            print("Wrong input.Please use the options from brackets!\n")
            log_action(f"{datetime.now()} {username}: Wrong input - {user_input}")
            continue

        for file in files:
            print("File:", file, sep=" ")
            print("=" * 10)

    print("Goodbye\n")


if __name__ == "__main__":
    main()
