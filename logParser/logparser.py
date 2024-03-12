import re
from collections import defaultdict, Counter

log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+\[(\d+/\d+/\d+:\d+:\d+:\d+)\s+(-\d+)\]\s+"(\w+)\s+(\S+)"\s+(\d+)\s+(\d+)\s+(\d+)')

logs = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
total_requests = 0
total_response_size = 0
error_requests = 0

with open('./input1.txt', 'r') as file:
    for line in file:
        match = log_pattern.match(line)
        if match:
            ip, timestamp, tz, method, path, status, response_size, request_size = match.groups()
            logs[ip][path][int(status)][int(response_size)] += 1
            total_requests += 1
            total_response_size += int(response_size)
            if int(status) >= 400:
                error_requests += 1

print("Top 3 IP addresses by request count:")
ip_counts = Counter()
for ip, paths in logs.items():
    count = sum(sum(count for sizes in statuses.values() for count in sizes.values()) for statuses in paths.values())
    ip_counts[ip] = count
for ip, count in ip_counts.most_common(3):
    print(f"  {ip}: {count} requests")

print(f"\nAverage response size: {total_response_size / total_requests:.2f} bytes")

error_rate = (error_requests / total_requests) * 100
print(f"Error rate: {error_rate:.2f}%")
