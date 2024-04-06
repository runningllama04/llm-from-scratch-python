import os
import shutil

source_directory = '/Users/akankshasoneja/Documents/Llama-2/Llm/Using-Llama2/course/subsets'
target_directory = '/Users/akankshasoneja/Documents/Llama-2/Llm/Using-Llama2/course/subsets/Extracted'

# Ensure the target directory exists
#os.makedirs(target_directory, exist_ok=True)

for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Construct the full file path
        print(file)
        file_path = os.path.join(root, file)
        print(file_path)
        # Construct the target file path
        target_path = os.path.join(target_directory, file)
        
        # Move the file
        shutil.move(file_path, target_path)

print("Files moved successfully.")
