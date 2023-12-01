import chardet

def decode_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

        encoding_info = chardet.detect(data)
        detected_encoding = encoding_info['encoding']

        try:
            decoded_content = data.decode(detected_encoding)
            print(f"Decoded content using {detected_encoding} encoding:")
            print(decoded_content)
        except Exception as e:
            print(f"Error decoding the file: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file you want to decode: ")
    decode_file(file_path)
