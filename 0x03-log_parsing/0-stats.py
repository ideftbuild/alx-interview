#!/usr/bin/python3
"""Module: 0-stats"""
import sys


def print_stats(total_size, status_counts):
    """Prints the computed metrics"""
    print(f'File size: {total_size}')
    for key in sorted(status_counts.keys()):
        if status_counts[key] > 0:
            print(f'{key}: {status_counts[key]}')


def parse_log():
    """Reads stdin line by line and computes metrics"""
    from re import compile
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0
    regex = compile(
        r"(.+)\s?-\s?\[([^\]]+)\] \""
        r"GET /projects/260 HTTP/1.1\" (.+) (.+)"
    )

    try:
        for line in sys.stdin:
            # Check if line matches the expected format
            result = regex.search(line)
            # Parse the line
            if result:
                try:
                    file_size = int(result.group(4))
                    total_size += file_size

                    status_code = int(result.group(3))
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                    line_count += 1
                    # Increment line_count and print results every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_counts)
                except ValueError:
                    continue

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    parse_log()
