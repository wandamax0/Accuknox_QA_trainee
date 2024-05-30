import os
import subprocess
from datetime import datetime

SOURCE_DIR = '/path/to/source/directory'
REMOTE_SERVER = 'user@remote_server'
REMOTE_DIR = '/path/to/remote/directory'
LOG_FILE = '/path/to/log/backup_log.txt'

def run_backup():
    rsync_command = [
        'rsync', '-avz', '--delete', SOURCE_DIR,
        f'{REMOTE_SERVER}:{REMOTE_DIR}'
    ]
    
    try:
        result = subprocess.run(rsync_command, capture_output=True, text=True)
        success = result.returncode == 0
        output = result.stdout
        error = result.stderr
    except Exception as e:
        success = False
        output = ''
        error = str(e)
    
    return success, output, error

def log_backup_result(success, output, error):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f'[{current_time}] Backup {"succeeded" if success else "failed"}\n')
        log_file.write('Output:\n')
        log_file.write(output + '\n')
        if error:
            log_file.write('Error:\n')
            log_file.write(error + '\n')
        log_file.write('\n')

def main():
    success, output, error = run_backup()
    
    log_backup_result(success, output, error)
    
    if success:
        print('Backup succeeded')
    else:
        print('Backup failed')
        print('Error:', error)

if __name__ == '__main__':
    main()
