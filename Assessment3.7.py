def has_symbol(name):
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            return True
    return False


def remove_duplicates(name):
    unsorted_array = []
    for ch in name.lower():
        if ch != " " and ch not in unsorted_array:
            unsorted_array.append(ch)
    return unsorted_array


def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    full_name = input("Enter your Full Name: ").strip()

    if full_name == "" or has_symbol(full_name):
        print("Excluded: the name is empty or contains a symbol/number.")
        return

    unsorted_array = remove_duplicates(full_name)
    sorted_array = insertion_sort(unsorted_array)

    print("Unsorted array:", unsorted_array)
    print("Sorted array:  ", sorted_array)


if __name__ == "__main__":
    main()