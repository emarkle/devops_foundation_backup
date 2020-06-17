#  Backup the user's home directory using RSync

import os
from pathlib import Path

#Rsync command to run
rsync_command = "rsync -avz"
# The user's home directory
backup_location = str(Path.home())

# Location of stored backups
backup_storage = backup_location + "/backups"

#Create backup directory if it does not exist
def create_backup_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Created backup directory: " + file_path)


def run_backup(backup_folder, backup_location):
    #Add any excludes from the backup
    exclude = " --exclude '~/backups/***' "

    #Rsync command
    rsync_command_run = rsync_command + exclude + backup_folder + " " + backup_storage

    try:
        os.system(rsync_command_run)
    except:
        print("Error backing up folder")
        return


#main program
#Create backup directory if it does not exist
create_backup_dir(backup_location + backup_storage)

#Complete the backup
run_backup(backup_location, backup_storage)