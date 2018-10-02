import pickle

with open('data/banner.p', 'rb') as f:
    banner = pickle.load(f)
    for line in banner:
        for run in line:
            char, count = run
            print(char*count, end="")
        print("")
