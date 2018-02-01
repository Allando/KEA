#!/bin/python

import json


def main():
    # choice = input("1) Calculate\n2) See previous calculations\n> ")

    # FOR DEBUGGING
    choice = "2"

    if choice == "1":
        # a = input("Input first value: ")
        # b = input("Input second value: ")
        # op = input("Select an operation[ + - * / ]: ")

        """
        VALUES FOR DEBUGGING
        """
        a = 2
        b = 4
        op = "+"

        print(calculate(float(a), float(b), op))
    elif choice == "2":
        load_file()
    elif choice == "0":
        print("Exiting...")
        exit(0)


def calculate(value_a, value_b, op):
    if op == "+":
        result = value_a + value_b
        save_file(value_a, value_b, op, result)

        return result
    elif op == "-":
        result = value_a - value_b
        save_file(value_a, value_b, op, result)

        return result
    elif op == "*":
        result = value_a * value_b
        save_file(value_a, value_b, op, result)

        return result
    elif op == "/":
        result = value_a / value_b
        save_file(value_a, value_b, op, result)

        return result


def save_file(value_a, value_b, op, result):
    calculation = [{"Value A": value_a, "Value B": value_b, "Operator": op, "Result": result}]

    try:
        with open("calculations.json", "a") as f:
            json.dump(calculation, f)
            f.write("\n")
    except:
        print("save_file: Failed!")


def load_file():
    try:
        with open("calculations.json") as f:
            data = json.load(f)

        for l in data:
            print("Value A: {}".format(l['Value A']))
            print("Value B: {}".format(l['Value B']))
            print("Operator: {}".format(l['Operator']))
            print("Result: {}".format(l['Result']))
            print("-" * 50)
    except:
        print("load_file: Failed!!")


main()
