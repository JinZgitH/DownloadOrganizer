# File Organizer Script

This script organizes files in the ~/Downloads directory based on specific rules.
It can move files into categorized folders such as images, audio, and video,
or prompt the user for a destination if the file doesn't match predefined categories.

**🚀 Overview**

- Automates the organization of files in the macOS Downloads directory.
- Sorts files into structured categories for enhanced file management.
- Prioritizes organizing files into subfolders based on filenames and colons (`:`).
- Handles files with colons hierarchically (e.g., `aa:1.txt` to `aa`, `aa:zz:2.txt` to `zz` in `aa`).
- Categorizing files by type of filename sorting with colons is not possible.
- Groups `.png` and `.jpg` into an `images` folder.
- Groups `.mp3` files into an `audio` folder.
- Groups `.mp4` and `.mov` files into a `video` folder.
- Creates distinct folders for each type within the specified directory or destination.
- Provides granular organization and easier file location.
- Reduces manual file management and improves file accessibility.

**✨ Functionality**

|                             |                                                                                                                                                                                                                                                           |
| :-------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|           Feature           |                                                                                                                        Description                                                                                                                        |
| 📂 Filename Prefix Sorting  |                             Sorts files into subfolders based on their filenames, with a focus on handling filenames containing colons (`:`). Files like `aa:1.txt` go into `aa`, and `aa:zz:2.txt` go into `zz` inside `aa`.                             |
| 📁 File Type Categorization | Sorts files in the Downloads folder by type if filename prefix sorting with colons is not possible. `.png` and `.jpg` files are grouped into an `images` folder, `.mp3` files into an `audio` folder, and `.mp4`, and `.mov` files into a `video` folder. |
|     📂 Folder Creation      |        Creates separate folders for each file type and filename prefix (including hierarchical folders based on colons) in the specified directory. The folders `images`, `audio`, and `video` are created to group files of corresponding types.         |

**🛠️ Usage**

- Run the script from the terminal.
- Ensure the script has the necessary permissions to read and modify files in the Downloads folder.

**⚠️ Assumptions**

- Designed for macOS.
- Assumes a standard Downloads folder in the user's home directory.
- File types are determined by file extensions.
- Filename-based sorting prioritizes filenames with colons (`:`) for hierarchical organization.

**💡 Future Improvements**

- Implement error handling for file operations.
- Add options to customize organization criteria.
- Include a feature to exclude specific file types or files.
- Provide a user interface for configuration and execution.
- Allow for configuration of delimiter other than `:`.

## Author:

- Jin Zheng: jinzheng@hioscar.com
- Prashanth Tekal: prashanth@hioscar.com
