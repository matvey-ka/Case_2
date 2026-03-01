# Case-study #2
# Developers: Popov M., Kartashov A.
#

import re


##### BEGINNING OF FINANCIAL INVESTIGATOR'S CODE #####

def luhn_check(card_number):
    '''

    Function performing  Luhn algorithm check to validate the card number.
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


def save_financial_data(extracted_data, filename='card_artifacts.txt'):
    '''

    Function saving financial data to file with formatted output.
    :param extracted_data: dictionary containing financial data with valid and invalid card lists
    :param filename: string specifying output file name
    :return: None
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('=' * 50 + '\n')
        f.write('🛡️ DATA SHIELD OPERATION REPORT 🛡️\n')
        f.write('=' * 50 + '\n')
        f.write('#' * 50 + '\n')
        f.write('💵💸🤑💰💲 FINANCIAL DATA 💵💸🤑💰💲\n')
        f.write('#' * 50 + '\n')
        f.write('-' * 50 + '\n')
        f.write(f'✅ VALID UNIQUE CARDS ✅ ({len(extracted_data['financial_data']['valid'])} pieces):\n')
        f.write('-' * 50 + '\n')
        for card in report['financial_data']['valid']:
            f.write(f'{card}\n')
        f.write('-' * 50 + '\n')
        f.write(f'❌ INVALID UNIQUE CARDS ❌ ({len(extracted_data['financial_data']['invalid'])} pieces):\n')
        f.write('-' * 50 + '\n')
        for card in report['financial_data']['invalid']:
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

##### BEGINNING OF THE BASE CODE #####
def generate_comprehensive_report(leaked_data):
    '''

    Function generating a comprehensive report from text.
    :param leaked_data: raw text to analyze for information
    :return: dictionary containing all extracted and validated data
    '''
    extracted_data = {'financial_data': find_and_validate_credit_cards(leaked_data)}
    return extracted_data


def save_artifacts(extracted_data):
    '''

    Function saving all extracted artifacts to file with formatted output.
    :param extracted_data: dictionary containing all extracted data
    :return: None
    '''
    save_financial_data(extracted_data)


def print_report(extracted_data):
    '''

    Function printing formatted report to console.
    :param extracted_data: dictionary containing all extracted data
    :return: None
    '''
    print_financial_data(extracted_data)


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
