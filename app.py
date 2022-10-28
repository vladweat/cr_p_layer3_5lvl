from time import sleep
from modules import *
from utils import *
from sys import argv
from loguru import logger

script, module = argv


def get_len_wallets():
    with open("wallets.txt") as file:
        tmp = file.readlines()
    return len(tmp)


def get_wallet(index):
    with open("wallets.txt") as file:
        tmp = file.readlines()
    wallet = tmp[index].strip().split(" ")
    return wallet


if __name__ == "__main__":
    logger.success("Creator: vladweat - https://t.me/vladweat")

    if module == "module_5":
        for index in range(get_len_wallets()):
            module_5(index)

    if module == "module_10":
        for index in range(get_len_wallets()):
            module_10(index)

    if module == "module_11":
        for index in range(get_len_wallets()):
            module_11(index)

    if module == "module_13":
        for index in range(get_len_wallets()):
            module_13(index)

    if module == "module_16":
        for index in range(get_len_wallets()):
            module_16(index)

    if module == "module_17":
        for index in range(get_len_wallets()):
            module_17(index)

    if module == "module_18":
        for index in range(get_len_wallets()):
            module_18(index)

    if module == "module_21":
        for index in range(get_len_wallets()):
            module_21(index)

    if module == "module_11_a":
        for index in range(get_len_wallets()):
            module_11_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_11_b":
        for index in range(get_len_wallets()):
            module_11_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_11_c":
        for index in range(get_len_wallets()):
            module_11_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_a":
        for index in range(get_len_wallets()):
            module_13_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_b":
        for index in range(get_len_wallets()):
            module_13_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_c":
        for index in range(get_len_wallets()):
            module_13_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_d":
        for index in range(get_len_wallets()):
            module_13_d(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_e":
        for index in range(get_len_wallets()):
            module_13_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_f":
        for index in range(get_len_wallets()):
            module_13_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_g":
        for index in range(get_len_wallets()):
            module_13_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_13_h":
        for index in range(get_len_wallets()):
            module_13_h(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_16_a":
        for index in range(get_len_wallets()):
            module_16_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_16_b":
        for index in range(get_len_wallets()):
            module_16_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_16_c":
        for index in range(get_len_wallets()):
            module_16_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_a":
        for index in range(get_len_wallets()):
            module_17_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_b":
        for index in range(get_len_wallets()):
            module_17_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_c":
        for index in range(get_len_wallets()):
            module_17_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_d_1":
        for index in range(get_len_wallets()):
            module_17_d_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_d_2":
        for index in range(get_len_wallets()):
            module_17_d_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_e":
        for index in range(get_len_wallets()):
            module_17_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_f":
        for index in range(get_len_wallets()):
            module_17_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_g":
        for index in range(get_len_wallets()):
            module_17_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_h_1":
        for index in range(get_len_wallets()):
            module_17_h_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_h_2":
        for index in range(get_len_wallets()):
            module_17_h_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_i":
        for index in range(get_len_wallets()):
            module_17_i(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_j_1":
        for index in range(get_len_wallets()):
            module_17_j_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_j_2":
        for index in range(get_len_wallets()):
            module_17_j_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_17_k":
        for index in range(get_len_wallets()):
            module_17_k(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_a":
        for index in range(get_len_wallets()):
            module_18_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_b":
        for index in range(get_len_wallets()):
            module_18_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_c":
        for index in range(get_len_wallets()):
            module_18_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_d":
        for index in range(get_len_wallets()):
            module_18_d(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_e":
        for index in range(get_len_wallets()):
            module_18_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_f":
        for index in range(get_len_wallets()):
            module_18_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_g":
        for index in range(get_len_wallets()):
            module_18_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_18_h":
        for index in range(get_len_wallets()):
            module_18_h(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_21_a":
        for index in range(get_len_wallets()):
            module_21_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    if module == "module_21_b":
        for index in range(get_len_wallets()):
            module_21_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])

    logger.success(f"Завершено. Аккаунтов прогнано {get_len_wallets()}")
