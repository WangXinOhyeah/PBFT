import time
from utils.Resolver import convert_into_dict, convert_dict2obj
import json


class Transaction():
    def __init__(self) -> None:
        self.first_party = None
        self.party_b = None
        self.content = None

    def set_content(self, content):
        self.content = content


class Block():
    def __init__(self) -> None:
        self.block_info = {}
        self.transaction = None
        self.timestamp = time.time()
        self.previous_hash = None
        self.voting_result = []
        self.permission = None


class BlockChain():
    def __init__(self) -> None:
        self.current_chain = None
        pass

    def persistence(self):
        pass

    def load_chain(self):
        pass

    def verify_chain(self):
        pass


def save_blocks_to_file(blocks, filename):
    with open(filename, 'w') as f:
        for block in blocks:
            convert_into_dict(block)
            block_str = str(block.param_dict) + '\n'
            f.write(block_str + '$&$&$&\n')  # 将字符串写入文件，每个区块之间使用'$&$&$&'分隔符
            f.close()


def save_chain_to_file(blocks, filename):
    chain = []
    for i, block in enumerate(blocks):
        if i == 0:
            block.previous_hash = "0"  # 设置previous_hash为"0"
        else:
            block.previous_hash = chain[-1].hash()  # 设置previous_hash为上一个区块的hash值

        chain.append(block)
    save_blocks_to_file(chain, filename)


def read_blockchain_file(filename):
    blockchain = []
    with open(filename, 'r') as file:
        file_contents = file.read()
        blocks = file_contents.split("$&$&$&")
        for block_str in blocks:
            if block_str.strip() == '':
                continue
            block_dict = json.loads(block_str)
            block_obj = convert_dict2obj(block_dict)
            blockchain.append(block_obj)
    return blockchain
