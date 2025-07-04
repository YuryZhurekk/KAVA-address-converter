import bech32

def eth_to_kava_address(eth_address):
    if not eth_address.startswith("0x"):
        raise ValueError("Invalid EVM address")

    eth_bytes = bytes.fromhex(eth_address[2:])
    converted_bits = bech32.convertbits(eth_bytes, 8, 5)
    kava_address = bech32.bech32_encode('kava', converted_bits)
    return kava_address

def main():
    with open("evmwallets.txt", "r") as file:
        evm_addresses = file.readlines()

    with open("kavawallets.txt", "w") as output_file:
        for evm_address in evm_addresses:
            evm_address = evm_address.strip()
            kava_address = eth_to_kava_address(evm_address)
            output_file.write(kava_address + "\n")
            print(f"EVM Address: {evm_address} -> Kava Address: {kava_address}")

if __name__ == "__main__":
    main()





