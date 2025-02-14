import os
import json


def add_list(f):
    fs = os.listdir(f)
    fs.sort()
    return fs


def is_in_list(want_str, dir_list_n):
    for tmp_str in dir_list_n:
        if want_str in tmp_str:
            return True
    return False


def main():
    with open("config.json", "r") as file:
        config = json.loads(file.read())
    path = config["dir_path"]
    key_words = config["key_word_list"]
    dir_list_name = add_list(path)
    for want_key in key_words:
        if not is_in_list(want_key, dir_list_name):
            print(want_key)


if __name__ == "__main__":
    main()
