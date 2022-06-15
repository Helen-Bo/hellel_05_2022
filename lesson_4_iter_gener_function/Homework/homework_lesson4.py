from typing import Generator

FILENAME = "./lesson_4_iter_gener_function/generators/rockyou.txt"
SEARCH_KEYWORD = "user"


def read_lines_find_user_generator() -> Generator:
    with open(FILENAME, encoding="utf_8_sig") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")


def find_lines(line) -> bool:
    while True:
        questions = input(f"Do you want to add <<{line}>>? [Y/N]: ")

        if questions.lower() in ["y", "yes"]:
            return True
        elif questions.lower() in ["n", "no", "not"]:
            return False
        else:
            print("Try again!")


def lines_amount():
    results = []
    for line in read_lines_find_user_generator():
        if find_lines(line) is True:
            results.append(line)

    print(f"Results: {results}, \nAdded line: {len(results)}")


if __name__ == "__main__":
    lines_amount()
