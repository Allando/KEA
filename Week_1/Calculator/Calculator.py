#!/bin/python

import json


def main():
    choice = input("1) Calculate\n2) See previous calculations\n> ")

    if choice == "1":
        a = input("Input first value: ")
        b = input("Input second value: ")

        op = input("Select an operation[ + - * / ]: ")

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
        with open("calculations.json", "w") as f:
            json.dump(calculation, f)
    except:
        print("save_file: Failed!")

def load_file():
    try:
        with open("calculations.json") as f:
            print(json.load(f))
    except:
        print("load_file: Failed!!")


main()

