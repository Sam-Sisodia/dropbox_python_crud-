import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token
TOKEN = "sl.Bw9725yPBsAW8ljYw3xI-vdLr2s7Ww9Wbve687rrzswp6y2R9EjkdiB-zQnLv7Ddv8asb5Wt8p9dhEEpoVsN-UMzdApt5LypNlWZyZYBq1HzwYrOU2z2D7EbPGhGhUd4g2ORX0Od3RO1eNs5WxyrtNc"

# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)





# dbx = dropbox.Dropbox(TOKEN)

# def move_file(source_path, destination_path):
#     try:
#         # Move the file
#         dbx.files_move_v2(source_path, destination_path)
#         print(f"File '{source_path}' moved to '{destination_path}' successfully.")
#     except ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"A file with the same name already exists at '{destination_path}'.")
#         else:
#             print(f"Error moving file '{source_path}' to '{destination_path}': {e}")

# Example usage
            
# foldername = ""
# destination = ""
# files_move = ["kk.docx",]
# move_file(f"/myfoder/{foldername}/Ailyze.docx", f"/myfoder/{destination}/Ailyze.docx")


def move_files(source,destination,files):
    try:
        for i in files:
            source_path = f'/myfoder/{source}/{i}'
            destination_path= f"/myfoder/{destination}/{i}"
        
            dbx.files_move_v2(source_path,destination_path)
            print(f"File '{source}' moved to '{destination}' successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"A file with the same name already exists at '{destination}'.")
        else:
            print(f"Error moving file '{source}' to '{destination}': {e}")


    


source = "Newfolder"
destination = "oldfolder"
files = ["kk.docx",]
move_files(source,destination,files)











# def move_files(source, destination, files):
#     try:
#         # Initialize Dropbox client
#         dbx = dropbox.Dropbox(TOKEN)
        
#         for file_name in files:
#             source_path = f'/myfolder/{source}/{file_name}'
#             destination_path = f'/myfolder/{destination}/{file_name}'
        
#             dbx.files_move_v2(source_path, destination_path)
#             print(f"File '{file_name}' moved from '{source}' to '{destination}' successfully.")
#     except dropbox.exceptions.ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"A file with the same name already exists at '{destination}'.")
#         else:
#             print(f"Error moving file '{source}' to '{destination}': {e}")
