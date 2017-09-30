license = """# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

"""

if __name__ == "__main__":
    import glob
    for file_name in glob.glob("engineer_number/**/*.py"):
#       print("file_name =", file_name)
        with open(file_name, "r") as f:
            codes = f.read()
        with open(file_name, "w") as f:
            print(license + codes, file=f, end="")
