import sys
from subprocess import check_output
import music_tag


class colors:
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# As seen on https://github.com/KristoforMaynard/music-tag
supported_file_types = [
    'aac',
    'aiff',
    'dsf',
    'flac',
    'm4a',
    'mp3',
    'ogg',
    'opus',
    'wav',
    'wv'
]

all_files = []
music_files = []


# Finds all file from current directory into all child directories
def find_all_files():
    if len(sys.argv) >= 2:
        directory = sys.argv[-1]
    else:
        directory = '.'
    find_cmd = ['find', directory, '-type', 'f']
    cmd_output = check_output(find_cmd)
    return cmd_output.splitlines()

# Filters all_files into music_files
def check_all_compatibility(file_list):
    filtered_file_list = []

    for file_byte_obj in file_list:
        file_string = file_byte_obj.decode('utf-8')
        file_type = file_string.split('.')[-1]

        if file_type in supported_file_types:
            filtered_file_list.append(file_string)
        else:
            print(f'{colors.FAIL}Error for {file_string}: Filetype is not supported.{colors.ENDC}')
    return filtered_file_list

# Writes to metadata based off filename
def write_to_metadata(filepath):
    # Parse data
    filepath_deconstruct = filepath.split('/')
    filename_deconstruct = filepath_deconstruct[-1].split(' - ')

    # If file is not formatted correctly, filename = title
    if len(filename_deconstruct) == 2:
        artist = filename_deconstruct[0]
        title = filename_deconstruct[1].split('.')[0]
    else:
        print(f'{colors.WARNING}Warning for {filepath}: Filename is not formatted correctly.{colors.ENDC}')
        artist = ''
        title = filename_deconstruct[0].split('.')[0]

    # Save metadata
    audiofile_obj = music_tag.load_file(filepath)
    audiofile_obj['artist'] = artist
    audiofile_obj['title'] = title
    audiofile_obj.save()
    print(f'{colors.OKCYAN}{filepath}: Metadata updated successful.{colors.ENDC}')


if __name__ == '__main__':


    all_files = find_all_files()
    music_files = check_all_compatibility(all_files)

    for filepath in music_files:
        write_to_metadata(filepath)