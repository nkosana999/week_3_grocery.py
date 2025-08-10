def main():
    item_list = []   # The items that the user puts in basket

    # A loop to continuos collection of user items into the list
    while True:
        try:
            item_val = input("Item: ").upper()
            item_list.append(item_val)
        except EOFError:
            break

    item_set = set(item_list)
    # A loop to count the different items in the list and print how many times each appears
    for item in item_set:
        count = item_list.count(item)
        print(f"{count} {item}")

main()