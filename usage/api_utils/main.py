from square_commons import get_api_output_in_standard_format

output = get_api_output_in_standard_format(
    data=[1, 2, 3], message="Data fetched successfully!", log={"time_taken": 23.563}
)
print(output)
