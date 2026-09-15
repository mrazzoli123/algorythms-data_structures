class ArrayOperations:
    def __init__(self, array):
        self.array = array

    def find_max(self):
        max_value = self.array[0]
        for num in self.array:
            if num > max_value:
                max_value = num
        return max_value

    def find_min(self):
        min_value = self.array[0]
        for num in self.array:
            if num < min_value:
                min_value = num
        return min_value

    def find_average(self):
        total = 0
        for num in self.array:
            total += num
        return total / len(self.array)

    def find_sum(self):
        total = 0
        for num in self.array:
            total += num
        return total

    def find_product(self):
        product = 1
        for num in self.array:
            product *= num
        return product

    def count_elements(self):
        count = 0
        for _ in self.array:
            count += 1
        return count

    def reverse_array(self):
        reversed_array = []
        for i in range(len(self.array)-1, -1, -1):
            reversed_array.append(self.array[i])
        return reversed_array

    def is_sorted(self):
        for i in range(len(self.array) - 1):
            if self.array[i] > self.array[i + 1]:
                return False
        return True

    def find_element(self, element):
        for i in range(len(self.array)):
            if self.array[i] == element:
                return i
        return -1

    def find_median(self):
        sorted_array = sorted(self.array)
        n = len(sorted_array)
        middle = n // 2
        if n % 2 == 0:
            median = (sorted_array[middle - 1] + sorted_array[middle]) / 2
        else:
            median = sorted_array[middle]
        return median

    def remove_duplicates(self):
        unique_elements = []
        for num in self.array:
            if num not in unique_elements:
                unique_elements.append(num)
        return unique_elements

    def find_second_largest(self):
        first = second = float('-inf')
        for num in self.array:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
        return second

    def rotate_left(self, k):
        n = len(self.array)
        rotated_array = []
        for i in range(n):
            rotated_array.append(self.array[(i + k) % n])
        return rotated_array
