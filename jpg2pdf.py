import os  # Import the os module to interact with the operating system (e.g., file operations)

# Get the current working directory (folder) where the script is running
current_folder = os.getcwd()

# Iterate over all files in the current directory
for filename in os.listdir(current_folder):
    
    # Check if the file has a .jpg extension (case-insensitive)
    if filename.lower().endswith('.jpg'):
        
        # Create a new filename by changing the extension from .jpg to .pdf
        new_filename = f"{os.path.splitext(filename)[0]}.pdf"
        
        # Prepare the shell command to convert the .jpg file to a .pdf using ImageMagick's 'convert' tool
        # The 'replace' method ensures that any spaces in filenames are escaped (to handle spaces in filenames properly in a shell)
        cmd = "convert "+filename.replace(" ", "\ ")+" "+new_filename.replace(" ", "\ ")
        
        # Execute the command in the system shell (this will invoke the 'convert' command to create a PDF from the JPG)
        os.system(cmd)
        
        # Optionally, you can print the command to see the action being performed (currently commented out)
        # print(cmd)

