import sys; sys.path.append("../"); from utils import *

# lol this is a mess...

class Entry:
    def __init__(self, entry):
        self.signal_patterns = entry[0].strip().split()
        self.outputs = entry[1].split()

    def __repr__(self):
        return f"Entry(Signals: {self.signals}, Output: {self.output})"


def get_list_from_string(string):
    return [char for char in string]

def decode_value(self, mapping, outputs):
    digits = []
    for val in map(mapping, outputs):
        digits.append(mapping[val])
    return int("".join(digs))

segment_count_to_digits = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

digits_to_segments = {
    0: get_list_from_string("abcefg"),
    1: get_list_from_string("cf"),
    2: get_list_from_string("acdeg"),
    3: get_list_from_string("acdfg"),
    4: get_list_from_string("bcdf"),
    5: get_list_from_string("abdfg"),
    6: get_list_from_string("abdefg"),
    7: get_list_from_string("acf"),
    8: get_list_from_string("abcdefg"),
    9: get_list_from_string("abcdfg"),
}

def part1(entries):
    unique_digits_in_output = []
    for entry in entries:
        for output in entry.outputs:
            if len(segment_count_to_digits[len(output)]) == 1:
                unique_digits_in_output.append(output)
    print("Part 1:", len(unique_digits_in_output))


def part2(entries):
    def done(signal_map):
        sum_of_values = sum([len(values) for values in signal_map.values()])
        print("Sum:", sum_of_values) 
        return sum_of_values == len(signal_map)
    returns = []
    for entry in entries:
        signal_map = {
            signal: [] for signal in get_list_from_string("abcdefg")
        }
        # Get initial possible signals for each signal
        for signal_pattern in entry.signal_patterns:
            digits = segment_count_to_digits[len(signal_pattern)]
            if len(digits) == 1:
                digit = digits[0]
                possible_signals = digits_to_segments[digit]
                for signal in get_list_from_string(signal_pattern):
                    current_signals = signal_map[signal]
                    if not current_signals or len(possible_signals) < len(current_signals):
                        signal_map[signal] = set(possible_signals)
            else:
                segments = set()
                for digit in digits:
                    segments = segments.union(set(digits_to_segments[digit]))
                #print(f"{signal_pattern} -> {digits} -> {segments}")
        # Narrow down possible signals using current signal_map
        complete = []
        count = 2
        while not done(signal_map):
            print(signal_map)
            remove_signals = set()
            for signal, possible_signals in signal_map.items():
                for possible_signal in possible_signals:
                    if signal == possible_signal:
                        signal_map[signal] = signal_map[signal] - {signal}
            for signal, possible_signals in signal_map.items():
                if len(possible_signals) == count and signal not in complete:
                    remove_signals = remove_signals.union(possible_signals)
                    complete.append(signal)
                    print("BREAK:", signal, possible_signals, complete)
                    break
            if not remove_signals:
                breakpoint()
            new_remove_signals = set()
            for signal in signal_map:
                possible_signals = signal_map[signal]
                if len(possible_signals) != count:
                    signal_map[signal] = possible_signals - remove_signals
                    if len(signal_map[signal]) == 1:
                        new_remove_signals.add(list(signal_map[signal])[0])
            for signal in signal_map:
                possible_signals = signal_map[signal]
                if len(possible_signals) != 1:
                    signal_map[signal] = possible_signals - new_remove_signals
        returns.append(decode_value(signal_map, outputs))
            
    print("Part 2:", sum(returns))

lines = read_file_lines("sample.txt")
entries = []
for i, line in enumerate(lines):
    entries.append(Entry(line.split("|")))

part1(entries)

part2(entries)
