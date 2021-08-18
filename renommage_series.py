from enum import Enum
import argparse
import sys
import os
import pickle


class MemoisationOpt(Enum):
    """ Memoisation option enum

    Is able to tell you if a value is present in enum
    using has_value()
    """
    NONE = "none"
    TARGET = "by_target"
    ARG = "by_arg"
    DEFAULT = "default"
    GLOBAL = "global"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


def distance1(string1, string2):
    """Finds edition distance without memoisation
    """
    if (string1 == string2):
        return 0
    elif (len(string1) < 1):
        return len(string2)
    elif (len(string2) < 1):
        return len(string1)

    if (string1[0] == string2[0]):
        return min(0 + distance1(string1[1:], string2[1:]),
                   1 + distance1(string1[1:], string2),
                   1 + distance1(string1, string2[1:]))
    else:
        return min(1 + distance1(string1[1:], string2[1:]),
                   1 + distance1(string1[1:], string2),
                   1 + distance1(string1, string2[1:]))


def distance2(string1, string2, mem_dict):
    """Finds edition with memoisation
    """
    if (string1 == string2):
        return 0
    elif (string1 == ""):
        return len(string2)
    elif (string2 == ""):
        return len(string1)

    if ((string1, string2) in mem_dict):
        return mem_dict.get((string1, string2))
    elif((string2, string1) in mem_dict):
        return mem_dict.get((string2, string1))
    else:
        if (string1[0] == string2[0]):  # fixme memoise before testing length
            mem_dict[(string1, string2)] = min(
                0 + distance2(string1[1:], string2[1:], mem_dict),
                1 + distance2(string1[1:], string2, mem_dict),
                1 + distance2(string1, string2[1:], mem_dict))
        else:
            mem_dict[(string1, string2)] = min(
                1 + distance2(string1[1:], string2[1:], mem_dict),
                1 + distance2(string1[1:], string2, mem_dict),
                1 + distance2(string1, string2[1:], mem_dict))

        return mem_dict[(string1, string2)]


def closer(string1, possibilities):
    """Find closest string to `string1` in possibilities
    DEPRECATED
    """
    if(len(possibilities) < 1):
        print("Empty title list, exit")
        sys.exit()

    word = None
    dist = None
    for p in possibilities:
        tmpDist = distance2(string1, p, {})
        if(dist is None):
            word, dist = p, tmpDist
        elif (tmpDist < dist):
            word, dist = p, tmpDist
    return word


mem_dict = {}  # Dict for DEFAULT case


def closer_mem(string1, possibilities,
               mem_opt, path_to_mem_file=None):
    """Find closest string to `string1` in possibilities with memoisation
    """
    if(mem_opt == MemoisationOpt.NONE.value):
        print("DISCLAIMER: THIS MIGHT TAKE A WHILE TO COMPLETE ")

    if(not (MemoisationOpt.has_value(mem_opt))):
        print("Illegal memoisation option - send from closer_mem")
        sys.exit()

    if (mem_opt == MemoisationOpt.DEFAULT.value):
        global mem_dict

    if (mem_opt == MemoisationOpt.ARG.value):
        mem_dict = {}
    elif(mem_opt == MemoisationOpt.GLOBAL.value):
        if os.path.exists(path_to_mem_file):
            print("Opening memoisation file")
            with open(path_to_mem_file, "rb") as file:
                mem_dict = pickle.load(file)
        else:
            print("Non existing file, creating it..")
            open(path_to_mem_file, "x")
            mem_dict = {}

    word = None
    dist = None
    for p in possibilities:
        if(mem_opt == MemoisationOpt.NONE.value):
            tmpDist = distance1(string1, p)
        elif(mem_opt == MemoisationOpt.TARGET.value):
            tmpDist = distance2(string1, p, {})
        else:
            tmpDist = distance2(string1, p, mem_dict)

        if(dist is None):
            word = p
            dist = tmpDist
        elif (tmpDist < dist):
            word = p
            dist = tmpDist
        if(mem_opt == MemoisationOpt.TARGET.value):
            mem_dict = {}

    # saving mem file
    if(mem_opt == MemoisationOpt.GLOBAL.value):
        with open(path_to_mem_file, "wb") as file:
            pickle.dump(mem_dict, file)
    return word


def answer_question(index):
    """ Handling question answering
    """
    if(index == "7a"):
        print("A mesure que le dictionnaire de memoisation" +
              "augumente la vitesse du programme ralentit." +
              "Il y a un juste milieu a trouver.")
    elif(index == "7b"):
        print("Par exemple alex renvoie alice. Il n'y a pas" +
              " de tokenisation. On pourrait ajouter une" +
              " option où les termes ont une importance.")
    else:
        print("Question not found")


def launch_test(index):
    """Launching some tests
    """
    if(index is None):
        return
    if(index == "0"):
        print("INFO: Test case n°0")
        print("Distance sans memoisation entre abracadabra et macabre :")
        print(distance1("abracadabra", "macabre"))
        print("Distance avec memoisation entre abracadabra et macabre :")
        print(distance2("abracadabra", "macabre", {}))
    elif(index == "1"):
        print("INFO: Test case n°1")
        print("Distance sans memoisation entre deux mots vides :")
        print(distance1("", ""))
        print("Distance avec memoisation entre deux mots vides :")
        print(distance2("", "", {}))
    else:
        print("Illegal test index, exiting...")


def main():
    """ Handling user args
    """
    my_parser = argparse.ArgumentParser(description='Find closest title')
    my_parser.add_argument('path',
                           nargs='?',
                           const=None,
                           metavar='path',
                           type=str,
                           help='Absolute path to the file you want to test')
    my_parser.add_argument("titles",
                           type=str,
                           nargs="*",
                           metavar='titles',
                           help='List of titles you want to find.' +
                                'ex: python renommage_series.py ' +
                                ' assets/series_2000-2019.txt' +
                                ' "12 Mon" "ternell"...')
    my_parser.add_argument("--memoisation",
                           type=str,
                           metavar='<none | default | by_arg ' +
                                   ' | by_target | global>',
                           help='Set memoisation (--memoisation none,i ' +
                                '--memoisation by_target, by_arg ' +
                                '--memoisation default, --memoisation global)')
    my_parser.add_argument("--test",
                           type=str,
                           metavar='<test_index>',
                           help='--test 0 launches a basic test' +
                                '--test 1 launches.. TBA')
    my_parser.add_argument("--memo-file",
                           type=str,
                           metavar='<path_to_memoisation_file>',
                           help='--memo-file ./<file_name>')
    my_parser.add_argument("--question",
                           type=str,
                           metavar='<answer_index>',
                           help='--question 7a | 7b')

    p = "./assets/series_2000-2019.txt"
    ts = []
    mem = "default"
    mem_file = "./assets/memoisation_def"

    for arg, value in my_parser.parse_args()._get_kwargs():
        if(arg == "path"):
            p = value
        elif (arg == "titles"):
            ts = value
        elif (arg == "memoisation"):
            if(value is None):
                mem = MemoisationOpt.DEFAULT.value
            else:
                mem = value
        elif (arg == "question"):
            if(not(value is None)):
                answer_question(value)
                sys.exit()
        elif (arg == "test"):
            if(not(value is None)):
                launch_test(value)
                sys.exit()
        elif (arg == "memo_file"):
            if(value is None):
                mem_file = "./assets/memoisation_def"
            else:
                mem_file = value
        else:
            print(arg)
            print("Illegal argument, " +
                  "run 'python renommage_series.py -h' for help")

    if((p is None) or (ts == [])):
        print("Missing path or titles arguments, here is the doc \n")
        my_parser.print_help(sys.stderr)
        sys.exit()

    if(not(os.path.isfile(p))):
        print("File not found")
        sys.exit()

    with open(p, "r") as file_series:
        series = file_series.readlines()

    for title in ts:
        print(title + " --> " + closer_mem(title, series, mem, mem_file))


main()
