import os
import shutil

class SimpleFileOrganiser:
    def __init__(self, directory, keywords, unsorted_folder, invalid_folder, extensions):
        self.directory = directory
        self.keywords = keywords
        self.unsorted_folder = unsorted_folder
        self.invalid_folder = invalid_folder
        self.extensions = [extension.lower().strip() for extension in extensions]

    def run(self):
        # Create folders for every keyword, "Unsorted", and "Invalid" if they don't exist
        for keyword in self.keywords + [self.unsorted_folder, self.invalid_folder]:
            folder_path = os.path.join(self.directory, keyword)
            os.makedirs(folder_path, exist_ok=True)

        # Loop through files
        for filename in os.listdir(self.directory):
            self.process_file(filename)

    def process_file(self, filename):
        _, extension = os.path.splitext(filename)
        if extension.lower()[1:] in self.extensions:
            filepath = os.path.join(self.directory, filename)

            matching_keywords = [
                keyword for keyword in self.keywords if keyword.lower() in filename.lower()
            ]

            destination = None
            if len(matching_keywords) == 1:
                destination = os.path.join(self.directory, matching_keywords[0], filename)
            elif len(matching_keywords) > 1:
                destination = os.path.join(self.directory, self.invalid_folder, filename)
            else:
                destination = os.path.join(self.directory, self.unsorted_folder, filename)
            
            shutil.move(filepath, destination)
