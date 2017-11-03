# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

LICENSE = """# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

"""

if __name__ == "__main__":
    import glob
    for file_name in glob.glob("engineer_number/**/*.py", recursive=True):
        print("file_name =", file_name)
        with open(file_name, "r") as f:
            codes = f.read()
        with open(file_name, "w") as f:
            print(LICENSE + codes, file=f, end="")
