import whois
import time


def is_domain_available(domain):
    try:
        domain_info = whois.whois(domain)
        return False
    except:
        return True


def check_domains_from_file(input_file_path: str, output_file_path: str):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            word = line.strip()
            if 5 > len(word) > 1:
                domain_name = f"{word}.no"
                if is_domain_available(domain_name):
                    print(f"Available: {domain_name}")
                    outfile.write(domain_name + '\n')
                time.sleep(1)


input_file = 'words_alpha.txt'
output_file = 'available_domains.txt'

check_domains_from_file(input_file, output_file)
