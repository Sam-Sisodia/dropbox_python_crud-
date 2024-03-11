import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token
TOKEN = "sl.Bw-7ExNO29464ssnw7vIxcoOGupAt82-jNFkgrewfnhe2Q171dfsjW9M5z3ms8CSNBXSj3UmL9jc2yXK34Rrpc7iz62CnwnRQztN0KozEDrNqK4jVBDZxRLFiAFGWAPDPNPzKcDh116v1LgNKpIjJgM"
# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)





                                                                 

def list_folder_contents(folder_path):
    try:
        result = dbx.files_list_folder(folder_path)
        
        print(f"Folders in folder '{folder_path}':")
        for entry in result.entries:
            if isinstance(entry, dropbox.files.FolderMetadata):
                print(f"Folder: {entry.name}")
    except ApiError as e:
        print(f"Error listing contents of folder '{folder_path}': {e}")

# # Example usage
list_folder_contents("/myfoder")



#files 
# def list_folder_contents(folder_path):
#     try:
#         # List contents of the folder
#         result = dbx.files_list_folder(folder_path)
        
#         print(f"Files in folder '{folder_path}':")
#         for entry in result.entries:
#             if isinstance(entry, dropbox.files.FileMetadata):
#                 print(f"File: {entry.name}")
#     except ApiError as e:
#         print(f"Error listing contents of folder '{folder_path}': {e}")

# # Example usage
# list_folder_contents("/myfoder")