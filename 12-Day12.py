# Day 12: Wap to get number of terms from user and print Fibonacci sequence.
def fibonacci_series(n):
 a, b = 0, 1
 for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
terms = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_series(terms)















# import os

# def create_python_files(folder_path, start, end):
#     try:
#         # Ensure the folder exists
#         os.makedirs(folder_path, exist_ok=True)

#         # Create Python files with the specified names
#         for i in range(start, end + 1):
#             file_name = f"{i:02d}-Day{i}.py"
#             file_path = os.path.join(folder_path, file_name)

#             # Write a placeholder comment in each file
#             with open(file_path, 'w') as file:
#                 file.write(f"# This is {file_name}\n")

#             print(f"Created: {file_name}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the folder and range
# folder_path = "path/to/your/folder"  # Replace with your folder path
# create_python_files(folder_path, 12, 30)
































# import os

# def rename_files(folder_path):
#     try:
#         # Get a list of files in the folder
#         files = sorted(os.listdir(folder_path))
        
#         # Rename each file sequentially
#         for i, file_name in enumerate(files, start=1):
#             # Construct the new file name
#             new_name = f"{i:02d}-Day{i}{os.path.splitext(file_name)[1]}"
            
#             # Get the full paths
#             old_file_path = os.path.join(folder_path, file_name)
#             new_file_path = os.path.join(folder_path, new_name)
            
#             # Rename the file
#             os.rename(old_file_path, new_file_path)
#             print(f"Renamed: {file_name} -> {new_name}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the folder containing the files
# folder_path = "D:/30 day challange"  # Replace with your folder path
# rename_files(folder_path)
