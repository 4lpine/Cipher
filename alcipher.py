import argparse
import os
from cipher import *

def main():
    parser = argparse.ArgumentParser(description='Encode or decode using a custom key')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Choose whether to encode or decode the input')
    parser.add_argument('--input', help='Input file to encode/decode', required=True)
    parser.add_argument('--key', help='File containing the key for encoding/decoding')
    parser.add_argument('--strength', type=int, help='Strength of the encoding key', default=10)
    parser.add_argument('--output', help='Output directory or specify "screen" to print on the screen')
    args = parser.parse_args()

    output_dir = args.output

    if not os.path.isfile(args.input):
        print(f"Error: The specified input file '{args.input}' does not exist.")
        return

    if args.mode == 'encode':
        if args.key:
            if not os.path.isfile(args.key):
                print(f"Error: The specified key file '{args.key}' does not exist.")
                return

            with open(args.key, 'r') as kf:
                key = kf.read().strip()
        else:
            key = generate_key(args.strength)

        with open(args.input, 'r') as f:
            input_string = f.read().strip()

        encoded_output = encoder(input_string, key)

        if output_dir and output_dir.lower() != 'screen':
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, 'encoded_output.txt'), 'w') as ef:
                ef.write(encoded_output)
            if not args.key:
                with open(os.path.join(output_dir, 'key.txt'), 'w') as kf:
                    kf.write(key)
            print(f'Encoded output saved to {os.path.join(output_dir, "encoded_output.txt")}')
            if not args.key:
                print(f'Key saved to {os.path.join(output_dir, "key.txt")}')
        else:
            print(f'Encoded output: {encoded_output}')
            if not args.key:
                print(f'Generated Key: {key}')

    elif args.mode == 'decode':
        if not os.path.isfile(args.key):
            print(f"Error: The specified key file '{args.key}' does not exist.")
            return

        with open(args.key, 'r') as kf:
            key = kf.read().strip()

        with open(args.input, 'r') as f:
            input_string = f.read().strip()

        decoded_output = decoder(input_string, key)

        if output_dir and output_dir.lower() != 'screen':
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, 'decoded_output.txt'), 'w') as df:
                df.write(decoded_output)
            print(f'Decoded output saved to {os.path.join(output_dir, "decoded_output.txt")}')
        else:
            print(f'Decoded output: {decoded_output}')


if __name__ == '__main__':
    main()
