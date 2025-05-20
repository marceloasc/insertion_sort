"""Insertion sort algorithm implementation."""

def insertion_sort(input_list: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the Insertion Sort algorithm.

    This algorithm builds the sorted list one element at a time by comparing the current
    element to its predecessors and inserting it into the correct position.

    Parameters:
        input_list (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list in ascending order.
    """
    iteration = 0
    for primary_index in range(1, len(input_list)):
        iteration += 1
        for secondary_index in range(primary_index-1, -1, -1):
            if input_list[primary_index] < input_list[secondary_index]:
                input_list[secondary_index + 1], input_list[secondary_index] = \
                input_list[secondary_index], input_list[secondary_index + 1]
                primary_index -= 1

        print(f"List after iteration {iteration}: {input_list}")

    return input_list


if __name__ == "__main__":
    input_list = "Declare list here, example: [5, 4, 3, 2, 1]."
    input_list_sorted = insertion_sort(input_list.copy())
    print(f"The list {input_list} sorted: {input_list_sorted}")
