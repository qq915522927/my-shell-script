import sys
import os
"""
Usage python get_differences_between_2_branch.py <root_dir>  <origin_branch> <target_branch>
"""


ingore_dirs = ['.gitlab', '.vscode', 'tests_legacy']


def is_ignored_dir(dirpath):
    par_dirs = dirpath.split(os.path.sep)
    for par_dir in par_dirs:
        if par_dir in ingore_dirs:
            return True
    return False


def get_file_list(root_dir):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        if is_ignored_dir(dirpath):
            # print(f"Ingore dir path: {dirpath}")
            continue

        for file in filenames:
            filepath = os.path.join(dirpath, file)
            f.append(filepath)
    return set(f)

def change_branch(branch):
    os.system(f'git checkout {branch}')

def main():
    root_dir = sys.argv[1]
    origin_branch = sys.argv[2]
    target_branch = sys.argv[3]
    change_branch(origin_branch)
    files_origin = get_file_list(root_dir)
    change_branch(target_branch)
    files_target = get_file_list(root_dir)
    print("========================")
    print(f"Files count in {origin_branch} branch:")
    print(len(files_origin))
    print("========================")
    print(f"Files count in {target_branch} branch:")
    print(len(files_target))
    print("========================")
    print(f"The differences: {origin_branch} - {target_branch}")
    print(files_origin - files_target)
    print("========================")
    print(f"The differences: {target_branch} - {origin_branch}")
    print(files_target - files_origin)


if __name__ ==  "__main__":
    main()
