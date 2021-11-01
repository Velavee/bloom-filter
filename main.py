from hashing import *
from dict_actions import *

def process_input(input_list, bloom_filter):
    input_num = int(input_list.readline())

    for x in range(input_num):
        password = input_list.readline()
        hashes = Word_Hashes(password)
        sha1_hash = hashes.create_sha1_hash()
        md5_hash = hashes.create_md5_hash()
        blake2b_hash = hashes.create_blake3_hash()

        if bloom_filter.check_dict(sha1_hash) and bloom_filter.check_dict(md5_hash) and bloom_filter.check_dict(blake2b_hash):
            print('maybe')
            continue

        print('no')


def main():
    print('Loading passwords into bloom filter...')
    # Open password file and store hashes for each password in a dictionary
    bad_password_file = open('dictionary.txt', 'r')
    bloom_filter = Bloom_Filter_Dict(bad_password_file)
    bloom_filter.create_dict()

    user_input = input("Enter the name of your input file: ")
    input_file = open(user_input, 'r')
    process_input(input_file, bloom_filter)


if __name__ == '__main__':
    main()