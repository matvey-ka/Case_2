# Case-study #2
# Developers: Popov M., Kartashov A.
#

import re


##### BEGINNING OF FINANCIAL INVESTIGATOR'S CODE #####

def luhn_check(card_number):
    '''
    Function performing Luhn algorithm check to validate the card number.
    :param card_number: string containing 16-digit card number without separators
    :return: True if card number passes Luhn check, False otherwise
    '''
    digits = [int(digit) for digit in card_number]
    for index in range(len(digits) - 2, -1, -2):
        digits[index] *= 2
        if digits[index] > 9:
            digits[index] = sum(int(d) for d in str(digits[index]))
    return sum(digits) % 10 == 0


def find_and_validate_credit_cards(text):
    '''
    Function finding all credit cards numbers and validating them using Luhn algorithm.
    :param text: string containing raw text to search for credit cards patterns
    :return: dictionary with two keys: 'valid' list of valid cards, 'invalid' list of invalid cards
    '''
    result = {'valid': [], 'invalid': []}
    card_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    found_raw_cards = re.findall(card_pattern, text)
    for raw_card in found_raw_cards:
        clean_card = re.sub(r'[^0-9]', '', raw_card)
        if len(clean_card) != 16:
            continue
        if luhn_check(clean_card):
            if clean_card not in result['valid']:
                result['valid'].append(clean_card)
        else:
            if clean_card not in result['invalid']:
                result['invalid'].append(clean_card)
    return result


def save_financial_data(extracted_data, filename='our_result.txt'):
    '''
    Function saving financial data to file.
    :param extracted_data: dictionary containing financial data with valid and invalid card lists
    :param filename: string specifying output file name
    :return: None
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        for card in extracted_data['financial_data']['valid']:
            f.write(f'{card}\n')
        for card in extracted_data['financial_data']['invalid']:
            f.write(f'{card}\n')


def print_financial_data(extracted_data):
    '''
    Function printing formatted financial data to console.
    :param extracted_data: dictionary containing financial data with valid and invalid card lists
    :return: None
    '''
    print('=' * 50)
    print('🛡️ DATA SHIELD OPERATION REPORT 🛡️')
    print('=' * 50)
    sections = [('💵💸🤑💰💲 FINANCIAL DATA 💵💸🤑💰💲', extracted_data['financial_data'])]
    for title, card_data in sections:
        print('#' * 50)
        print(f'{title}')
        print('#' * 50)
        print('-' * 50)
        print(f'✅ VALID CARDS ✅ ({len(card_data['valid'])} pieces):')
        print('-' * 50)
        for card in card_data['valid']:
            print(f'{card}')
        print('-' * 50)
        print(f'❌ INVALID CARDS ❌ ({len(card_data['invalid'])} pieces):')
        print('-' * 50)
        for card in card_data['invalid']:
            print(f'{card}')


##### END OF FINANCIAL INVESTIGATOR'S CODE #####


##### BEGINNING OF SECRETS HUNTER'S CODE #####

def find_secrets(text):
    '''
    Searches for API keys, passwords in text
    :param text: source text to analyze
    :return: dictionary with found secrets
    '''
    all_secrets = []
    secrets = {'API-keys': [], 'passwords': []}

    api_keys = re.findall(r'(?:sk_live_|pk_test_)[A-Za-z0-9]+', text)

    for api_key in api_keys:
        secrets['API-keys'].append(api_key)
        all_secrets.append(f'API-keys: {api_key}')

    passwords = re.findall(r'(?=.*[!_#@$%^&*])(?=.*\d)[A-Za-z0-9_!#@$%^&*]{8,}', text)

    for password in passwords:
        is_api = False
        for api in api_keys:
            if password == api or api in password or password in api:
                is_api = True
                break
        if not is_api:
            secrets['passwords'].append(password)
            all_secrets.append(f'password: {password}')

    no_repeats = []
    seen = set()
    for secret in all_secrets:
        if secret not in seen:
            seen.add(secret)
            no_repeats.append(secret)

    return {'all': no_repeats, 'organized': secrets}


def save_secrets_data(extracted_data, filename='our_result.txt'):
    '''
    Function for saving secret data to a file
    :param extracted_data: dictionary with all extracted data
    :param filename: output file name
    :return: None
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        secrets_data = extracted_data['secrets_data']['organized']
        for key in secrets_data['API-keys']:
            f.write(f'{key}\n')
        for password in secrets_data['passwords']:
            f.write(f'{password}\n')


def print_secrets_data(extracted_data):
    '''
    Function for displaying secret data in the console
    :param extracted_data: dictionary with all extracted data
    :return: None
    '''
    print('=' * 50)
    print('🛡️ DATA SHIELD OPERATION REPORT 🛡️')
    print('=' * 50)
    print('#' * 50)
    print('🔑🔐🎫 SECRETS DATA 🔑🔐🎫')
    print('#' * 50)

    secrets_data = extracted_data['secrets_data']['organized']

    if secrets_data['API-keys']:
        print('-' * 50)
        print(f'🔑 API KEYS ({len(secrets_data['API-keys'])} pieces):')
        print('-' * 50)
        for key in secrets_data['API-keys']:
            print(f'{key}')

    if secrets_data['passwords']:
        print('-' * 50)
        print(f'🔐 PASSWORDS ({len(secrets_data['passwords'])} pieces):')
        print('-' * 50)
        for password in secrets_data['passwords']:
            print(f'{password}')


##### END OF SECRETS HUNTER'S CODE #####


##### BEGINNING OF THE BASE CODE (combined) #####

def generate_comprehensive_report(leaked_data):
    '''
    Function generating a comprehensive report from text.
    :param leaked_data: raw text to analyze for information
    :return: dictionary containing all extracted and validated data
    '''
    extracted_data = {'financial_data': find_and_validate_credit_cards(leaked_data),
                      'secrets_data': find_secrets(leaked_data)}
    return extracted_data


def save_artifacts(extracted_data):
    '''
    Function saving all extracted artifacts to file with formatted output.
    :param extracted_data: dictionary containing all extracted data
    :return: None
    '''
    save_financial_data(extracted_data)
    save_secrets_data(extracted_data)


def print_report(extracted_data):
    '''
    Function printing formatted report to console.
    :param extracted_data: dictionary containing all extracted data
    :return: None
    '''
    print_financial_data(extracted_data)
    print_secrets_data(extracted_data)


if __name__ == '__main__':
    try:
        with open('data_leak_sample.txt', 'r', encoding='utf-8') as input_file:
            leaked_data = input_file.read()
    except FileNotFoundError:
        raise SystemExit('File not found')

    report = generate_comprehensive_report(leaked_data)
    print_report(report)
    save_artifacts(report)

##### END OF THE BASE CODE #####
