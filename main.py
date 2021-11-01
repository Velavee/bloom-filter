# Author: Gabrielle Josephson
# Project 2 - Bloom Filter
# CS 370 - Introduction to Security, Oregon State University, Fall 2021
# Sources: https://www.w3schools.com/python/python_file_write.asp , 
# https://www.geeksforgeeks.org/get-current-timestamp-using-python/

from hashing import *
from dict_actions import *
import calendar
import time

def process_input(input_list, output_file, bloom_filter):
    for password in input_list:
        hashes = Word_Hashes(bytes(password, 'utf-8'))
        sha1_hash = hashes.create_sha1_hash()
        md5_hash = hashes.create_md5_hash()
        blake2b_hash = hashes.create_blake3_hash()

        if bloom_filter.check_dict(sha1_hash) and bloom_filter.check_dict(md5_hash) and bloom_filter.check_dict(blake2b_hash):
            print('maybe')
            output_file.write('maybe\n')
            continue

        print('no')
        output_file.write('no\n')

def create_output_filename():
    gmt = time.gmtime()
    timestamp = calendar.timegm(gmt)
    return f'output_{timestamp}.txt'


def main():
    print('Loading passwords into bloom filter (this may take a moment)...')
    # Open password file and store hashes for each password in a dictionary
    bad_password_file = open('dictionary.txt', 'rb')
    bloom_filter = Bloom_Filter_Dict(bad_password_file)
    bloom_filter.create_dict()

    # Open input file and check if the passwords are in the list of bad passwords
    user_input = input("Enter the name of your input file: ")
    input_file = open(user_input, 'r')

    output_filename = create_output_filename()
    output_file = open(output_filename, 'x')

    print('\nResults:\n')
    process_input(input_file, output_file, bloom_filter)

    print(f'\nYour results have been written to {output_filename}\n')
    
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
