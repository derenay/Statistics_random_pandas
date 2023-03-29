import random
import numpy as np
import pandas as pd


class DescriptiveStatistics:
    def __init__(self, data):
        self.data = data

    def frequency_table(self):
        possible_values = sorted(set(self.data))
        #print(possible_values)
        counters = {x: 0 for x in possible_values}
        for x in counters:
            counters[x] = self.data.count(x)
        cumulative_relative_frequency = 0.0
        table_lines = []
        for k, v in counters.items():
            cumulative_relative_frequency += v / len(self.data)
            table_lines.append([
                k, v, v / len(self.data), cumulative_relative_frequency
            ])
        return pd.DataFrame(
            table_lines,
            columns=["value", "Frequency", "relative Freq.", "cumulative Freq"]
        )

    def data_matrix(self):
        for i, x in enumerate(sorted(self.data)):
            print(f"{x:4d}", end="")
            if (i+1)%10 == 0:
                print("")

    def stem_and_leaf_plot(self, stems):
        for s in stems:
            v = [str(n-s[0]) for n in sorted(self.data) if n>=s[0] and n<=s[1]]
            v_str = " ".join(v)
            print(f"{s[0]//10} | {v_str}")



def main():
    random.seed(210316017)
    print("\n# Frequency Table #\n")
    data = [random.randint(1, 9) for i in range(100)]
    #print(data)
    descriptive_statistics = DescriptiveStatistics(data)
    print(descriptive_statistics.frequency_table())
    del data, descriptive_statistics

    print("\n # Data Matrix #\n")
    data = [random.randint(10, 99) for _ in range(100)]
    descriptive_statistics = DescriptiveStatistics(data)
    descriptive_statistics.data_matrix()
    print("\nStem-and-Leaf Plot\n")
    stems = [
        (10, 19),
        (20, 29),
        (30, 39),
        (40, 49),
        (50, 59),
        (60, 69),
        (70, 79),
        (80, 89),
        (90, 99)
    ]
    descriptive_statistics.stem_and_leaf_plot(stems)

if __name__ == "__main__":
    main()
