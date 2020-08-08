import os


def run(**args):
    print("[*] In environment module.")
    return str(os.environ)

if __name__ == "__main__":
    print(run())