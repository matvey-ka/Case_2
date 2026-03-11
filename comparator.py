# Case-study #2
# Developers: Popov M., Kartashov A.
#


OUR_RESULT_FILE = 'our_result.txt'
MAX_GROUP_NUMBER = 12
SAVE_REPORT_TO = 'comparison_report.txt'


def extract_artifacts(file_path):
    '''
    Function extracting artifacts from a file
    :param file_path: path to file
    :return: tuple containing list and set of artifacts
    '''
    artifacts_ordered = []
    seen = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line != '' and cleaned_line not in seen:
                seen.add(cleaned_line)
                artifacts_ordered.append(cleaned_line)
    return artifacts_ordered, seen


def main():
    try:
        our_artifacts_list, our_artifacts_set = extract_artifacts(OUR_RESULT_FILE)
    except FileNotFoundError:
        raise SystemExit(f'⛔ File {OUR_RESULT_FILE} not found. ⛔')

    our_total = len(our_artifacts_list)
    report = []

    report.append('=' * 50)
    report.append('🛡️ DATA SHIELD OPERATION COMPARISON REPORT 🛡️')
    report.append('=' * 50)
    report.append('#' * 50)
    report.append(f'🔎 The number of artifacts our group has: {our_total}')
    report.append('#' * 50)

    print('=' * 50)
    print('🛡️ DATA SHIELD OPERATION COMPARISON REPORT 🛡️')
    print('=' * 50)
    print('#' * 50)
    print(f'🔎 The number of artifacts our group has: {our_total}')
    print('#' * 50)

    for group_id in range(1, MAX_GROUP_NUMBER + 1):
        group_file_name = f'result{group_id}.txt'

        try:
            group_artifacts_list, group_artifacts_set = extract_artifacts(group_file_name)
        except FileNotFoundError:
            message = f'⛔ Group {group_id}: file {group_file_name} not found. ⛔'
            print(message)
            report.append(message)
            continue

        group_total = len(group_artifacts_list)
        same = our_artifacts_set & group_artifacts_set
        only_our = our_artifacts_set - group_artifacts_set
        only_their = group_artifacts_set - our_artifacts_set

        print('-' * 50)
        print(f'👉 Comparison with the group {group_id}:')
        print(f'🔎 The number of artifacts group {group_id} has: {group_total}')
        print(f'✅ Matching artifacts: {len(same)} ✅')
        print('-' * 50)

        report.append('-' * 50)
        report.append(f'👉 Comparison with the group {group_id}:')
        report.append(f'🔎 The number of artifacts group {group_id} has: {group_total}')
        report.append(f'✅ Matching artefacts: {len(same)} ✅')
        report.append('-' * 50)

        if len(only_our) > 0:
            print('/' * 50)
            print(f'⚠️ We have, but the group {group_id} does not {len(only_our)} artifacts. ⚠️')
            print('/' * 50)

            report.append('/' * 50)
            report.append(f'⚠️ We have, but the group {group_id} does not {len(only_our)} artifacts. ⚠️')
            report.append('/' * 50)

            for artifact in our_artifacts_list:
                if artifact in only_our:
                    print(artifact)
                    report.append(artifact)

        if len(only_their) > 0:
            print('/' * 50)
            print(f'❌ We do not have, but the group {group_id} has {len(only_their)} artifacts. ❌')
            print('/' * 50)

            report.append('/' * 50)
            report.append(f'❌ We do not have, but the group {group_id} has {len(only_their)} artifacts. ❌')
            report.append('/' * 50)

            for artifact in group_artifacts_list:
                if artifact in only_their:
                    print(artifact)
                    report.append(artifact)

        if len(only_our) == 0 and len(only_their) == 0:
            print('✅ The results are completely the same. ✅')
            report.append(f'✅ The results are completely the same. ✅')

    with open(SAVE_REPORT_TO, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))


if __name__ == '__main__':
    main()
