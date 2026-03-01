# Case-study #2
# Developers: Popov M., Kartashov A.
#

import re


##### BEGINNING OF FINANCIAL INVESTIGATOR'S CODE #####

def luhn_check(card_number):
    digits = [int(digit) for digit in card_number]
    for position in range(len(digits) - 2, -1, -2):
        digits[position] *= 2
        if digits[position] > 9:
            digits[position] = sum(int(d) for d in str(digits[position]))
    return sum(digits) % 10 == 0


def find_and_validate_credit_cards(text):
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


def save_financial_data(report, filename='card_artifacts.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('=' * 50 + '\n')
        f.write('🛡️ DATA SHIELD OPERATION REPORT 🛡️\n')
        f.write('=' * 50 + '\n')
        f.write('#' * 50 + '\n')
        f.write('💵💸🤑💰💲 FINANCIAL DATA 💵💸🤑💰💲\n')
        f.write('#' * 50 + '\n')
        f.write('-' * 50 + '\n')
        f.write(f'✅ VALID UNIQUE CARDS ✅ ({len(report['financial_data']['valid'])} pieces):\n')
        f.write('-' * 50 + '\n')
        for card in report['financial_data']['valid']:
            f.write(f'{card}\n')
        f.write('-' * 50 + '\n')
        f.write(f'❌ INVALID UNIQUE CARDS ❌ ({len(report['financial_data']['invalid'])} pieces):\n')
        f.write('-' * 50 + '\n')
        for card in report['financial_data']['invalid']:
            f.write(f'{card}\n')


def print_financial_data(report):
    print('=' * 50)
    print('🛡️ DATA SHIELD OPERATION REPORT 🛡️')
    print('=' * 50)
    sections = [('💵💸🤑💰💲 FINANCIAL DATA 💵💸🤑💰💲', report['financial_data'])]
    for title, data in sections:
        print('#' * 50)
        print(f'{title}')
        print('#' * 50)
        print('-' * 50)
        print(f'✅ VALID CARDS ✅ ({len(data['valid'])} pieces):')
        print('-' * 50)
        for card in data['valid']:
            print(f'{card}')
        print('-' * 50)
        print(f'❌ INVALID CARDS ❌ ({len(data['invalid'])} pieces):')
        print('-' * 50)
        for card in data['invalid']:
            print(f'{card}')


##### END OF FINANCIAL INVESTIGATOR'S CODE #####

##### BEGINNING OF THE BASE CODE #####
def generate_comprehensive_report(main_text):
    report = {'financial_data': find_and_validate_credit_cards(main_text)}
    return report


def save_artifacts(report):
    save_financial_data(report)


def print_report(report):
    print_financial_data(report)


if __name__ == '__main__':
    try:
        with open('data_leak_sampl.txt', 'r', encoding='utf-8') as f:
            main_text = f.read()
    except FileNotFoundError:
        raise SystemExit('File not found')
    report = generate_comprehensive_report(main_text)
    print_report(report)
    save_artifacts(report)

##### END OF THE BASE CODE #####
