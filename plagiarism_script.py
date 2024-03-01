import os

def deactivate(mode=None):
    # reset old environment variables
    if os.environ.get("_OLD_VIRTUAL_PATH"):
        os.environ["PATH"] = os.environ["_OLD_VIRTUAL_PATH"]
        os.environ.pop("_OLD_VIRTUAL_PATH")
        
    if os.environ.get("_OLD_VIRTUAL_PYTHONHOME"):
        os.environ["PYTHONHOME"] = os.environ["_OLD_VIRTUAL_PYTHONHOME"]
        os.environ.pop("_OLD_VIRTUAL_PYTHONHOME")
    
    # This should detect bash and zsh, which have a hash command that must
    # be called to get it to forget past commands. Without forgetting
    # past commands the $PATH changes we made may not be respected
    if os.environ.get("BASH") or os.environ.get("ZSH_VERSION"):
        os.system("hash -r 2> /dev/null")
        
    if "_OLD_VIRTUAL_PS1" in os.environ:
        os.environ["PS1"] = os.environ["_OLD_VIRTUAL_PS1"]
        os.environ.pop("_OLD_VIRTUAL_PS1")
    
    os.environ.pop("VIRTUAL_ENV", None)
    os.environ.pop("VIRTUAL_ENV_PROMPT", None)
    
    if mode == "nondestructive":
        # Self destruct!
        del deactivate

# unset irrelevant variables
deactivate("nondestructive")

os.environ["VIRTUAL_ENV"] = "/home/wave444/Desktop/plagiarism-checker-flask/venv"
os.environ["_OLD_VIRTUAL_PATH"] = os.environ.get("PATH", "")
os.environ["PATH"] = os.path.join(os.environ["VIRTUAL_ENV"], "bin") + os.pathsep + os.environ["PATH"]

# unset PYTHONHOME if set
if os.environ.get("PYTHONHOME"):
    os.environ["_OLD_VIRTUAL_PYTHONHOME"] = os.environ["PYTHONHOME"]
    os.environ.pop("PYTHONHOME")

if not os.environ.get("VIRTUAL_ENV_DISABLE_PROMPT"):
    os.environ["_OLD_VIRTUAL_PS1"] = os.environ.get("PS1", "")
    os.environ["PS1"] = "(venv) " + os.environ.get("PS1", "")
    os.environ["VIRTUAL_ENV_PROMPT"] = "(venv)"

if os.environ.get("BASH") or os.environ.get("ZSH_VERSION"):
    os.system("hash -r 2> /dev/null")



# import os
# import sys
# import difflib

# def main():
#     # Get the directory paths from the command line arguments
#     dir1 = sys.argv[1]
#     dir2 = sys.argv[2]

#     # Check if the directories exist
#     if not os.path.isdir(dir1) or not os.path.isdir(dir2):
#         print("Error: One or both directories do not exist.")
#         return

#     # Get a list of all the files in the first directory
#     files1 = os.listdir(dir1)

#     # Iterate over the files in the first directory
#     for file1 in files1:
#         # Get the full path to the file
#         file1_path = os.path.join(dir1, file1)

#         # Check if the file is a regular file
#         if not os.path.isfile(file1_path):
#             continue

#         # Get a list of all the files in the second directory
#         files2 = os.listdir(dir2)

#         # Iterate over the files in the second directory
#         for file2 in files2:
#             # Get the full path to the file
#             file2_path = os.path.join(dir2, file2)

#             # Check if the file is a regular file
#             if not os.path.isfile(file2_path):
#                 continue

#             # Compare the contents of the two files
#             with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
#                 text1 = f1.read()
#                 text2 = f2.read()

#             # Calculate the similarity ratio between the two files
#             similarity = difflib.SequenceMatcher(None, text1, text2).ratio()

#             # Print the similarity ratio if it is above a certain threshold
#             if similarity > 0.8:
#                 print(f"Similarity between {file1} and {file2}: {similarity:.2f}")

# if __name__ == "__main__":
#     main()