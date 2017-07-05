#!/usr/bin/env python

import time
import sys

if len(sys.argv) != 2:
    print "!!!Please enter a test string length as the first script argument\n"
    exit(1)

test_string_length = int(sys.argv[1])
print "Testing for string length of {0}".format(test_string_length)

test_string = "a" * test_string_length
test_string_char = "z"
test_string_pos = int(test_string_length / 2)

def solve_concat(string, position, character):
    return string[:position] + character + string[position + 1:]

def solve_array(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l) 

def solve_iteration(string, position, character):
    new_string = ''
    for i in range(len(string)):
       new_string += string[i] if position != i else character 
    return new_string

def solve_generator(string, position, character):
    return "".join(solve_generator_generator(string, position, character))

def solve_generator_generator(string, position, character):
    for i in range(len(string)):
        yield string[position] if i != position else character


print "Solving with concatenation"
t0 = time.time()
solve_concat(test_string, test_string_pos, test_string_char)
t1 = time.time()
print "Elapsed time: " + str(t1 - t0)

print "Solving with array converstion"
t0 = time.time()
solve_array(test_string, test_string_pos, test_string_char)
t1 = time.time()
print "Elapsed time: " + str(t1 - t0)

print "Solving with normal iteration"
t0 = time.time()
solve_iteration(test_string, test_string_pos, test_string_char)
t1 = time.time()
print "Elapsed time: " + str(t1 - t0)

print "Solving with generato iteration"
t0 = time.time()
solve_generator(test_string, test_string_pos, test_string_char)
t1 = time.time()
print "Elapsed time: " + str(t1 - t0)

