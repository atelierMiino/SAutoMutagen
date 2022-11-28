import sys
from subprocess import check_output
import mutagen


class Colors:
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

all_files = []
music_files = []


# Finds all file from current directory into all child directories
# Returns binary encoded terminal output string array
def find_all_files():
    if len(sys.argv) >= 2:
        directory = sys.argv[-1]
    else:
        directory = '.'
    find_cmd = ['find', directory, '-type', 'f']
    cmd_output = check_output(find_cmd)
    return cmd_output.splitlines()

# Filters all_files into music_files
# Returns utf-8 decoded string array
def filter_all_files(file_list):
    filtered_file_list = []

    for enc_file_string in file_list:
        file_string = enc_file_string.decode('utf-8')
        try:
            audiofile_obj = mutagen.File(file_string)
        except mutagen.mp3.HeaderNotFoundError:
            print(f'{Colors.WARNING}Warning for {file_string}: File has no header metadata.{Colors.ENDC}')
            filtered_file_list.append(file_string)

        if audiofile_obj == None:
            print(f'{Colors.FAIL}Error for {file_string}: Filetype is not supported.{Colors.ENDC}')
        else:
            filtered_file_list.append(file_string)
            
    return filtered_file_list

# Writes to metadata based off filename
# Returns 0 if changes not saved. Returns 0 if changes saved
def write_file_metadata(filepath):
    # Parse data
    filepath_deconstruct = filepath.split('/')
    filename_deconstruct = filepath_deconstruct[-1].split(' - ')

    text_artist = 'Unkown Artist'
    text_title = ''

    # If file is not formatted correctly, filename = title
    if len(filename_deconstruct) == 2:
        text_artist = filename_deconstruct[0]
        text_title = filename_deconstruct[1].split('.')[0]
    else:
        print(f'{Colors.WARNING}Warning for {filepath}: Filename is not formatted correctly.{Colors.ENDC}')
        text_title = filename_deconstruct[0].split('.')[0]

    artist = mutagen.id3.TPE1(encoding = 3, text = text_artist)
    title = mutagen.id3.TIT2(encoding = 3, text = text_title)


    # Exit if data matches. Save metadata if data doesn't
    try:
        audiofile_obj = mutagen.id3.ID3(filepath)
    except mutagen.id3.ID3NoHeaderError:
        audiofile_obj = mutagen.id3.ID3()

    # If tag is identical, leave it alone
    change_artist = False
    if not 'TPE1' in audiofile_obj:
        audiofile_obj.add(mutagen.id3.TPE1(encoding = 3, text = text_artist))
        change_artist = True
    elif audiofile_obj['TPE1'] != artist:
        audiofile_obj['TPE1'] = artist
        change_artist = True


    # If tag dne, make it
    # If tag is identical, leave it alone
    change_title = False        
    if not 'TIT2' in audiofile_obj:
        audiofile_obj.add(mutagen.id3.TIT2(encoding = 3, text = text_title))
        change_title = True
    elif audiofile_obj['TIT2'] != title:
        audiofile_obj['TIT2'] = title
        change_title = True


    if change_artist or change_title:
        audiofile_obj.save(filepath)
        print(f'{Colors.OKCYAN}{filepath}: Metadata updated successful.{Colors.ENDC}')
        return 1
    else:
        print(f'{filepath}: Metadata up to date.')
        return 0


if __name__ == '__main__':

    all_files = find_all_files()
    music_files = filter_all_files(all_files)

    files_found = 0
    files_updated = 0
    for filepath in music_files:
        files_updated = files_updated + write_file_metadata(filepath)
        files_found = files_found + 1
    
    print(f'{files_updated} files updated!')
    print(f'{files_found} files are up to date!')