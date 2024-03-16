import argparse
from simple_file_organiser import SimpleFileOrganiser

def run():
    parser = argparse.ArgumentParser(description="Organize files based on keywords.")
    parser.add_argument("directory", help="The directory containing your files")
    parser.add_argument("keywords", nargs="+", help="List of keywords to search for")
    parser.add_argument("-u", "--unsorted_folder", default="Unsorted", help="Folder for files without keywords")
    parser.add_argument("-i", "--invalid_folder", default="Invalid", help="Folder for files with multiple keywords")
    parser.add_argument("-e", "--extensions", nargs="+", default=['pdf'], help="List of valid file extensions (default: pdf)") 
    
    args = parser.parse_args()
    SimpleFileOrganiser(
        args.directory,
        args.keywords,
        args.unsorted_folder,
        args.invalid_folder,
        args.extensions
    ).run()
    
    print("File organisation complete!")
