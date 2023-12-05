import whois
import time


def is_domain_available(domain: str) -> bool:
    try:
        domain_info = whois.whois(domain)
        return False
    except Exception as e:
        if "Connection reset by peer" in str(e):
            print(f"Connection error for {domain}, retrying...")
            time.sleep(5)
            return is_domain_available(domain)
        return True


def check_domains_from_file(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            word = line.strip()
            if 6 > len(word) > 1:
                domain_name = f"{word}.no"
                if is_domain_available(domain_name):
                    print(f"Available: {domain_name}")
                    outfile.write(domain_name + '\n')
                time.sleep(1)


input_file = 'clean_words_alpha.txt'
output_file = 'available_domains.txt'

check_domains_from_file(input_file, output_file)
