from functools import singledispatch

@singledispatch
def process_data(data):
    print(f"Default implementation: {data}")

@process_data.register(int)
def process_int_data(data):
    print(f"Processing integer data: {data * 2}")

@process_data.register(str)
def process_str_data(data):
    print(f"Processing string data: {data.upper()}")

@process_data.register(list)
def process_list_data(data):
    print(f"Processing list data: {sum(data)}")

# Test cases
process_data(42)
process_data("hello")
process_data([1, 2, 3, 4])
process_data(3.14)
