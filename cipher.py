import secrets
import base64


def shuffle(data):
    copy = data.copy()
    return [copy.pop(secrets.randbelow(len(copy))) for _ in range(len(data))]

def generate_key(strength=10):
    ascii = [codes for codes in range(65, 90)] + [codes for codes in range(97, 122)] + [32]
    key_data = []
    key = ""
    
    for i in range(strength):key_data.append(shuffle(ascii))

    for i in range(len(ascii)):
        key += f"{ascii[i]}>{'.'.join([str(values[i]) for values in key_data]).strip('.')}|"
    
    key = key.removesuffix("|")

    return str(strength) + "*" + base64.b64encode(str.encode(key)).decode()

def decoder(output, key) -> str:
    strength = int(key.split("*")[0])
    decoded_key = base64.b64decode(str.encode(key.split("*")[1])).decode().split("|")
    akey = {}
    for value in decoded_key: akey[''.join([chr(int(character)) for character in value.split(">")[1].split(".")])] = value.split(">")[0]

    normalized_output = [output[i:i+strength] for i in range(0, len(output), strength)]
    
    decoded_output = ""
    for value in normalized_output:decoded_output += chr(int(akey[value]))

    return decoded_output
    

def encoder(input_str, key) -> str:
    key_data = base64.b64decode(str.encode(key.split("*")[1])).decode().split("|")

    output = ""

    for letter in input_str:
        for data in key_data:
            if data.startswith(str(ord(letter))):output += ''.join([chr(int(value)) for value in data.split(">")[1].split(".")])

    return output

