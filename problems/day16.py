from pyperclip import copy
import utils


def part1(data):
    return packet(data)[0]


def part2(data):
    return packet(data)[1]


def packet(data):
    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)
    version_sum = version

    if type_id == 4:
        bin_bits = []
        i = 6
        while True:
            bin_bits.extend(data[i+1:i+5])
            i += 5
            if data[i-5] == '0':
                break
        value = int(''.join(bin_bits), 2)
    else:
        length_type_id = data[6]
        values = []
        if length_type_id == '0':
            total_length_bits = int(data[7:7+15], 2)
            i = 7+15
            while total_length_bits > 0:
                internal_version_sum, value, right = packet(data[i:])
                version_sum += internal_version_sum
                values.append(value)
                total_length_bits -= right
                i += right
        else:
            numb_imm_sub_packets = int(data[7:7+11], 2)
            i = 7+11
            for c in range(numb_imm_sub_packets):
                internal_version_sum, value, right = packet(data[i:])
                version_sum += internal_version_sum
                values.append(value)
                i += right

        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = 1
            for v in values:  # Freaking np.product and silent overflow error...
                value *= v
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        else:
            assert len(values) == 2
            if type_id == 5:
                value = int(values[0] > values[1])
            elif type_id == 6:
                value = int(values[0] < values[1])
            else:
                assert type_id == 7
                value = int(values[0] == values[1])

    return version_sum, value, i


def get_data():
    hex_numb = utils.get_lines(16)[0]
    return bin(int(hex_numb, 16))[2:].zfill(4*len(hex_numb))


if __name__ == '__main__':
    print(answer1 := part1(get_data()))
    print(answer2 := part2(get_data()))
    copy(answer2)
