import re
from collections import Counter
from datetime import datetime
LOG_FILE_PATH = '/path/to/webserver.log'
REPORT_FILE_PATH = '/path/to/report.txt'

log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[.+?\] "(?P<method>\S+) (?P<page>\S+) \S+" (?P<status>\d{3}) \S+ "\S+" "\S+"'
)

def parse_log(log_file_path):
    with open(log_file_path, 'r') as file:
        log_entries = file.readlines()

    ip_counter = Counter()
    page_counter = Counter()
    status_counter = Counter()

    for entry in log_entries:
        match = log_pattern.match(entry)
        if match:
            ip = match.group('ip')
            page = match.group('page')
            status = match.group('status')
            
            ip_counter[ip] += 1
            page_counter[page] += 1
            status_counter[status] += 1
    
    return ip_counter, page_counter, status_counter

def generate_report(ip_counter, page_counter, status_counter, report_file_path):
    with open(report_file_path, 'w') as report_file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report_file.write(f'Report generated on {current_time}\n')
        report_file.write('\n')
        
        report_file.write(f'Number of 404 errors: {status_counter["404"]}\n')
        report_file.write('\n')
        
        report_file.write('Most requested pages:\n')
        for page, count in page_counter.most_common(10):
            report_file.write(f'{page}: {count} requests\n')
        report_file.write('\n')
        
        report_file.write('IP addresses with the most requests:\n')
        for ip, count in ip_counter.most_common(10):
            report_file.write(f'{ip}: {count} requests\n')

def main():
    ip_counter, page_counter, status_counter = parse_log(LOG_FILE_PATH)
    generate_report(ip_counter, page_counter, status_counter, REPORT_FILE_PATH)
    print(f'Report generated and saved to {REPORT_FILE_PATH}')

if __name__ == '__main__':
    main()
