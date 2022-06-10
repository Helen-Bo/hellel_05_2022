from typing import Generator


FILENAME = "./lesson_4_iter_gener_function/generators/rockyou.txt"
SEARCH_KEYWORD = "user"


def read_lines_find_user_generator() -> Generator:

    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")


def count_results(*args):
    results = []

    print("Do you want to count the number of passwords?")

    my_message = input("Plese input your answer(Yes or No): ")
    if my_message == "Yes":
        with open(FILENAME, encoding="utf-8") as file:
            for word in file.readlines():
                if SEARCH_KEYWORD in word:
                    results.append(word)
        print(f"{results} , Added line: {len(results)}")
    if my_message == "No":
        for line in read_lines_find_user_generator():
            print(line)
    else:
        print("Error")


count_results()
