import os
import json


def add_list(f):
    fs = os.listdir(f)
    fs.sort()
    return fs


def count_times_in_list(want_str, dir_list_n):
    cnt = 0
    # print(f"{type(want_str)}")
    for tmp_str in dir_list_n:
        if want_str in tmp_str:
            cnt += 1
    return cnt


def get_dic(original_list):
    re_dic = {}
    for key in original_list:
        re_dic[key] = 0
    return re_dic


def count_key_dic(key_dic, dir_list):
    for want_key in key_dic:
        key_dic[want_key] += count_times_in_list(want_key, dir_list)


def main():
    with open("config.json", "r") as file:
        config = json.loads(file.read())
    path = config["dir_path"]
    key_words = config["key_word_list"]
    dir_list_name = add_list(path)
    key_dic = get_dic(key_words)
    count_key_dic(key_dic, dir_list_name)
    for key, val in key_dic.items():
        if val == 0:
            print(f"{key} is not in the list!")
        elif val != 1:
            print(f"{key} is appear {val}! ")


if __name__ == "__main__":
    main()
