"""
fileorganizer.py

This script organizes files in the ~/Downloads directory based on specific rules. It can move files into categorized folders such as images, audio, and video, or prompt the user for a destination if the file doesn't match predefined categories.

Functions:
- create_and_move(file_path, folder_path, new_filename): Creates a directory if it doesn't exist and moves the file to the specified location.
- organize_files(download_dir): Main function that iterates over files in the download directory and organizes them based on their type or user input.

Usage:
Run this script to automatically organize files in your Downloads folder. It will categorize files into images, audio, and video folders based on their extensions. For files with a ':' in their name, it will create nested directories. If a file doesn't match any category, you'll be prompted to enter a destination.

Example:
- A file named 'DOC:aa:11.txt' will be moved to '~/Documents/aa/11.txt'.
- A file named 'image.png' will be moved to '~/Downloads/images/image.png'.
- If prompted and you enter 'aa:bb', the file will be moved to '~/Downloads/aa/bb/filename'.
"""

import os
import shutil

def create_and_move(file_path, folder_path, new_filename):
    """Create directory if it doesn't exist and move the file."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    shutil.move(file_path, os.path.join(folder_path, new_filename))

def organize_files(download_dir):
    # Define the target directories for different file types
    extensions_map = {
        '.png': 'images',
        '.jpg': 'images',
        '.mp3': 'audio',
        '.mp4': 'video',
        '.mov': 'video'
    }
    
    # Iterate over all files in the download directory
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        
        # Only process files, not directories
        if os.path.isfile(file_path):
            # Check if the filename contains a ':' sign
            if ':' in filename:
                parts = filename.split(':')
                if parts[0] == "DOC":
                    folder_path = os.path.join(os.path.expanduser('~/Documents'), *parts[1:-1])
                else:
                    folder_path = os.path.join(download_dir, *parts[:-1])
                create_and_move(file_path, folder_path, parts[-1])
            else:
                # Group files by type
                file_extension = os.path.splitext(filename)[1].lower()
                if file_extension in extensions_map:
                    folder_path = os.path.join(download_dir, extensions_map[file_extension])
                else:
                    # Prompt user for destination
                    destination = input(f"Enter destination for {filename} (e.g., 'aa' or 'DOC:aa'): ")
                    if not destination:
                        continue
                    if destination.startswith("DOC:"):
                        folder_path = os.path.join(os.path.expanduser('~/Documents'), *destination.split(':')[1:])
                    else:
                        folder_path = os.path.join(download_dir, *destination.split(':'))
                create_and_move(file_path, folder_path, filename)

if __name__ == "__main__":
    download_directory = os.path.expanduser('~/Downloads')
    organize_files(download_directory)
