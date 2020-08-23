import json 
import string
import random

SPEC_FILE = 'spec.json'
FIXED_FILE_NAME = 'fixed_width.txt'
DELIMITED_FILE_NAME = 'delimited'

def read_spec(spec_file):
    with open(spec_file) as specfile:
        return json.load(specfile)
    return None

def write_fixed(offsets, data, headings=None, encoding=None):
    with open(FIXED_FILE_NAME, 'w',encoding=encoding) as fixed_width_file:
        offset_ints = map(int,offsets)
        if headings != None:
            fixed_width_file.write("".join("%*s" % i for i in zip(offset_ints,headings)))
        for row in data:
            offset_ints = map(int,offsets)
            fixed_width_file.write("\n")
            fixed_width_file.write("".join("%*s" % i for i in zip(offset_ints,row)))

def write_delimited(data, ext=".csv", delimiter=",", headings=None, encoding=None):
    with open(DELIMITED_FILE_NAME + ext, "w", encoding=encoding) as del_file:
        if headings != None:
            del_file.write(delimiter.join(headings))
        for row in data:
            del_file.write("\n")
            del_file.write(delimiter.join(row))

def generate_data(offsets,lines=1):
    data = []
    chr_index = 65
    for i in range(0,lines):
        data.append([])
        for idx, length in enumerate(offsets):
            data[i] = data[i] + [get_string_with(int(length), chr_index + idx)]
    return data

def get_string_with(length, chr_index):
    if chr_index % 2 == 0:
        chr_index += 32
    result_str = ''.join(chr(chr_index) for i in range(length))
    return result_str

def main():
    print("Welcome to the Jungle\n")

    specification = read_spec(SPEC_FILE)
    if specification != None:
        data = generate_data(specification['Offsets'],20)
        write_fixed(specification['Offsets'],data,headings=specification['ColumnNames'],encoding=specification['FixedWidthEncoding'])
        write_delimited(data,headings=specification['ColumnNames'],encoding=specification['DelimitedEncoding'])

if __name__ == "__main__":
    main()