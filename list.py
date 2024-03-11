import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token
TOKEN = "sl.Bw9725yPBsAW8ljYw3xI-vdLr2s7Ww9Wbve687rrzswp6y2R9EjkdiB-zQnLv7Ddv8asb5Wt8p9dhEEpoVsN-UMzdApt5LypNlWZyZYBq1HzwYrOU2z2D7EbPGhGhUd4g2ORX0Od3RO1eNs5WxyrtNc"

# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)

def list_folder_contents(folder_path):
    try:
        # List contents of the folder
        result = dbx.files_list_folder(folder_path)
        
        print(f"Contents of folder '{folder_path}':")
        for entry in result.entries:
            if isinstance(entry, dropbox.files.FileMetadata):
                print(f"File: {entry.name}")
            elif isinstance(entry, dropbox.files.FolderMetadata):
                print(f"Folder: {entry.name}")
    except ApiError as e:
        print(f"Error listing contents of folder '{folder_path}': {e}")

# Example usage
list_folder_contents("/myfoder")