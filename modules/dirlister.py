import os


def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)

if __name__ == "__main__":
    print(run())
