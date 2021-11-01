import hashlib

# Creates three different kinds of hashes for a value
class Word_Hashes:
    def __init__(self, word):
        self.word = word

    def create_sha1_hash(self):
        hash_setup = hashlib.sha1()
        hash_setup.update(self.word)
        return hash_setup.hexdigest()

    def create_md5_hash(self):
        hash_setup = hashlib.md5()
        hash_setup.update(self.word)
        return hash_setup.hexdigest()

    def create_blake3_hash(self):
        hash_setup = hashlib.blake2b()
        hash_setup.update(self.word)
        return hash_setup.hexdigest()
