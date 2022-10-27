from time import sleep
from utils import *


def get_len_wallets():
    with open("wallets.txt") as file:
        tmp = file.readlines()
    return len(tmp)


def get_wallet(index):
    with open("wallets.txt") as file:
        tmp = file.readlines()
    wallet = tmp[index].strip().split(" ")
    return wallet


def module_5(index):
    module_5_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])


def module_10(index):
    module_10_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])


def module_11(index):
    module_11_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_11_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_11_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])


def module_13(index):
    module_13_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_13_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_13_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_13_d(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_13_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_13_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_13_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_13_h(address=get_wallet(index)[0], private_key=get_wallet(index)[1])


def module_16(index):
    module_16_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_16_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_16_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])


def module_17(index):
    module_17_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_d_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_17_d_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_17_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_h_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_17_h_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_17_i(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_17_j_1(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_17_j_2(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)


def module_18(index):
    module_18_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_18_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_18_c(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(15)
    module_18_d(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_18_e(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_18_f(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_18_g(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_18_h(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)


def module_21(index):
    module_21_a(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
    module_21_b(address=get_wallet(index)[0], private_key=get_wallet(index)[1])
    sleep(5)
