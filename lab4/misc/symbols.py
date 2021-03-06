"""Peter Rasmussen, Lab 4, symbols.py

This module provides the allowable numerals, node_names, operators, variables, and other symbols
commonly encountered when parsing and cleaning files.

"""


class Symbols:
    """
    Bundle of symbols used for syntax error checking and polynomial expression simplification and evaluation.
    """

    def __init__(self):
        self.numerals = "0123456789"
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet = self.lowercase + self.uppercase
        self.operators = "+-*/$^"
        self.other_symbols = "\t\n "
        self.accepted_symbols = (self.numerals + self.operators + self.alphabet)

    def is_accepted_symbol(self, symbol: str) -> bool:
        """
        Determine if symbol is an accepted symbol.
        :param symbol: Symbol to evaluate
        :return: True if symbol is an accepted symbol
        """
        return symbol in self.accepted_symbols

    def is_numeral(self, symbol: str) -> bool:
        """
        Determine if symbol is a numeral.
        :param symbol: Symbol to evaluate
        :return: True if symbol is numeral
        """
        return symbol in self.numerals

    def is_operator(self, symbol: str) -> bool:
        """
        Determine if symbol is an operator.
        :param symbol: Symbol to evaluate
        :return: True if symbol is operator
        """
        return symbol in self.operators

    def is_other_symbol(self, symbol: str) -> bool:
        """
        Determine if symbol is a tab, newline, or space.
        :param symbol: Symbol to evaluate
        :return: True if symbol is a tab, newline, or space
        """
        return symbol in self.other_symbols
