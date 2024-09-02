#!/usr/bin/env python3
"""
601.465/665 — Natural Language Processing
Assignment 1: Designing Context-Free Grammars

Assignment written by Jason Eisner
Modified by Kevin Duh
Re-modified by Alexandra DeLucia

Code template written by Alexandra DeLucia,
based on the submitted assignment with Keith Harrigian
and Carlos Aguirre Fall 2019
"""
import os
import sys
import random
import argparse

# Want to know what command-line arguments a program allows?
# Commonly you can ask by passing it the --help option, like this:
#     python randsent.py --help
# This is possible for any program that processes its command-line
# arguments using the argparse module, as we do below.
#
# NOTE: When you use the Python argparse module, parse_args() is the
# traditional name for the function that you create to analyze the
# command line.  Parsing the command line is different from parsing a
# natural-language sentence.  It's easier.  But in both cases,
# "parsing" a string means identifying the elements of the string and
# the roles they play.

from collections import defaultdict

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        args (an argparse.Namespace): Stores command-line attributes
    """
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generate random sentences from a PCFG")
    # Grammar file (required argument)
    parser.add_argument(
        "-g",
        "--grammar",
        type=str, required=True,
        help="Path to grammar file",
    )
    # Start symbol of the grammar
    parser.add_argument(
        "-s",
        "--start_symbol",
        type=str,
        help="Start symbol of the grammar (default is ROOT)",
        default="ROOT",
    )
    # Number of sentences
    parser.add_argument(
        "-n",
        "--num_sentences",
        type=int,
        help="Number of sentences to generate (default is 1)",
        default=1,
    )
    # Max number of nonterminals to expand when generating a sentence
    parser.add_argument(
        "-M",
        "--max_expansions",
        type=int,
        help="Max number of nonterminals to expand when generating a sentence",
        default=450,
    )
    # Print the derivation tree for each generated sentence
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Print the derivation tree for each generated sentence",
        default=False,
    )
    return parser.parse_args()

def process_line(line):
    if line[0]=="#":
        return None
    line = line.strip()
    if "#" in line:
        line = line[:line.index("#")]
    line = line.strip()
    line = line.split(" ")
    line = line[0].split("\t") + line[1:]
    if len(line)==1:
        return None
    return line

class Grammar:
    def __init__(self, grammar_file):
        """
        Context-Free Grammar (CFG) Sentence Generator

        Args:
            grammar_file (str): Path to a .gr grammar file
        
        Returns:
            self
        """
        # Parse the input grammar file
        self.rules = None # rules is a list of rule. Each rule is a triplet [weight, lhs, rhs]. rhs might also be a list
        self.dict_prob = None # Given a lhs, dict_prob tells you what probs do the rhs-s have?
        self.dict_rhs = None # Given a lhs, dict_rhs tells you what rhs-s does this lhs have?
        self._load_rules_from_file(grammar_file)

    def _load_rules_from_file(self, grammar_file = None):
        """
        Read grammar file and store its rules in self.rules

        Args:
            grammar_file (str): Path to the raw grammar file 
        """
        if not grammar_file:
            grammar_file = 'grammar.gr'
        filename = grammar_file
        rules = list()
        dict_prob = defaultdict(list)
        dict_rhs = defaultdict(list)
        # RHS: right hand side
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = process_line(line)
                if not line:
                    continue
                weight = line[0]
                lhs = line[1]
                rhs = line[2:]
                dict_prob[lhs].append(weight)
                dict_rhs[lhs].append(rhs)
                rules.append([weight, lhs, rhs])
        self.rules = rules
        self.dict_prob = dict_prob
        self.dict_rhs = dict_rhs
        return None

    def sample(self, derivation_tree, max_expansions, start_symbol):
        """
        Sample a random sentence from this grammar

        Args:
            derivation_tree (bool): if true, the returned string will represent 
                the tree (using bracket notation) that records how the sentence 
                was derived
                               
            max_expansions (int): max number of nonterminal expansions we allow

            start_symbol (str): start symbol to generate from

        Returns:
            str: the random sentence or its derivation tree
        """
        self.derivation_tree = derivation_tree
        self.max_expansions = max_expansions
        self.expansion_count = 0
        return self._sample_helper(start_symbol)
    
    def _sample_helper(self, start_symbol):
        # Base case: If the symbol is a terminal, return it
        if start_symbol not in self.dict_rhs:
            return start_symbol
        
        # It should just print "..." if M is reached
        if self.expansion_count >= self.max_expansions:
            return "..."
        
        # Increment expansion count
        self.expansion_count += 1
        
        # Select a rule based on weights
        rule = self._weighted_choice(self.dict_rhs[start_symbol], self.dict_prob[start_symbol])
        
        # Recursively expand each symbol in the selected rule
        result = []
        if self.derivation_tree:
            result.append(start_symbol)
            for sub_symbol in rule:
                result.append(self._sample_helper(sub_symbol))
            
            return "(" + " ".join(result) + ")"
        else:
            for sub_symbol in rule:
                result.append(self._sample_helper(sub_symbol))
            
            return " ".join(result)
    
    def _weighted_choice(self, rules, weights):
        total = sum(float(w) for w in weights)
        # Get distribution
        normalized_weights = [float(w) / total for w in weights]

        rand_val = random.uniform(0, 1)
        cumulative_weight = 0
        for rule, weight in zip(rules, normalized_weights):
            cumulative_weight += weight
            if rand_val <= cumulative_weight:
                return rule


####################
### Main Program
####################
def main():
    # Parse command-line options
    args = parse_args()

    # Initialize Grammar object
    grammar = Grammar(args.grammar)

    # Generate sentences
    for i in range(args.num_sentences):
        # Use Grammar object to generate sentence
        sentence = grammar.sample(
            derivation_tree=args.tree,
            max_expansions=args.max_expansions,
            start_symbol=args.start_symbol
        )

        # Print the sentence with the specified format.
        # If it's a tree, we'll pipe the output through the prettyprint script.
        if args.tree:
            prettyprint_path = os.path.join(os.getcwd(), 'prettyprint')
            t = os.system(f"echo '{sentence}' | perl \"{prettyprint_path}\" ")
        else:
            print(sentence)


if __name__ == "__main__":
    main()
