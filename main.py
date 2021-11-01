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
    dict = open('dictionary.txt', 'r')

    bloom_filter = Bloom_Filter_Dict(dict)
    bloom_filter.create_dict()

    input = open('sample_input.txt', 'r')
    process_input(input, bloom_filter)


if __name__ == '__main__':
    main()