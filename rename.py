
import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token

api_key = "4ns2gt309k2kftk"
App_secret = "viigzulo2py11mz"

TOKEN = "sl.Bw9725yPBsAW8ljYw3xI-vdLr2s7Ww9Wbve687rrzswp6y2R9EjkdiB-zQnLv7Ddv8asb5Wt8p9dhEEpoVsN-UMzdApt5LypNlWZyZYBq1HzwYrOU2z2D7EbPGhGhUd4g2ORX0Od3RO1eNs5WxyrtNc"
# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)


def rename_folder(old_path, new_name):
    try:
        # Move the folder to its new name
        dbx.files_move(old_path, f"{new_name}")
        print(f"Folder '{old_path}' renamed to '{new_name}' successfully.")
    except ApiError as e:
        print(f"Error renaming folder '{old_path}' to '{new_name}': {e}")

# Call the function to rename a folder
rename_folder("/myfoder/NewFolder", "/myfoder/UpdatedFolder")



# def rename_folder(old_folder_path, new_folder_name):
#     try:
#         # Initialize Dropbox client
#         dbx = dropbox.Dropbox(TOKEN)
        
#         # Get the parent folder path
#         parent_folder_path = old_folder_path.rsplit('/', 1)[0]
        
#         # Construct the new folder path
#         new_folder_path = f"{parent_folder_path}/{new_folder_name}"
        
#         # Move (rename) the folder
#         dbx.files_move_v2(old_folder_path, new_folder_path)
#         print(f"Folder '{old_folder_path}' renamed to '{new_folder_name}' successfully.")
#     except dropbox.exceptions.ApiError as e:
#         if isinstance(e.error, dropbox.files.RelocationError) and e.error.is_conflict():
#             print(f"A folder with the name '{new_folder_name}' already exists.")
#         else:
#             print(f"Error renaming folder '{old_folder_path}' to '{new_folder_name}': {e}")

# # Example usage
# rename_folder("/myfolder/Newfolder", "newfolder")



# def rename_folder(old_folder_path, new_folder_name):
#     try:
#         # Get the parent folder path
#         parent_folder_path = old_folder_path.rsplit('/', 1)[0]
        
#         # Construct the new folder path
#         new_folder_path = f"{parent_folder_path}/{new_folder_name}"
        
#         # Move (rename) the folder
#         dbx.files_move(old_folder_path, new_folder_path)
#         print(f"Folder '{old_folder_path}' renamed to '{new_folder_name}' successfully.")
#     except ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"A folder with the name '{new_folder_name}' already exists.")
#         else:
#             print(f"Error renaming folder '{old_folder_path}' to '{new_folder_name}': {e}")

# # Example usage
# rename_folder("/myfoder/Newfolder", "/myfoder/newfolder")


# def rename_folder(old_folder_path, new_folder_name):
#     try:
#         # Initialize Dropbox client
#         dbx = dropbox.Dropbox(TOKEN)
        
#         # Get the parent folder path
#         parent_folder_path = old_folder_path.rsplit('/', 1)[0]
        
#         # Construct the new folder path
#         new_folder_path = f"{parent_folder_path}/{new_folder_name}"
        
#         # Move (rename) the folder
#         dbx.files_move_v2(old_folder_path, new_folder_path)
#         print(f"Folder '{old_folder_path}' renamed to '{new_folder_name}' successfully.")
#     except dropbox.exceptions.ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"A folder with the name '{new_folder_name}' already exists.")
#         else:
#             print(f"Error renaming folder '{old_folder_path}' to '{new_folder_name}': {e}")

# # Example usage
# rename_folder("/myfolder/Newfolder", "newfolder")
















# def rename_file(folder_path, old_name, new_name):
#     try:
#         # Move (rename) the file
#         dbx.files_move(folder_path + '/' + old_name, folder_path + '/' + new_name)
#         print(f"File '{old_name}' renamed to '{new_name}' in '{folder_path}' successfully.")
#     except ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"File '{new_name}' already exists in '{folder_path}'.")
#         else:
#             print(f"Error renaming file '{old_name}' to '{new_name}': {e}")



