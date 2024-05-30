import requests
from datetime import datetime

APPLICATION_URL = 'http://your-application-url.com'
TIMEOUT = 5  
LOG_FILE = '/path/to/uptime_log.txt'

def check_application_status(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if 200 <= response.status_code < 300:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return 'down'

def log_application_status(status):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{current_time}] Application is {status}\n'
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(log_entry)

def main():
    status = check_application_status(APPLICATION_URL)
    print(f'Application is {status}')
    log_application_status(status)

if __name__ == '__main__':
    main()
