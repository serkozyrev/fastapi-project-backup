def log(tag="", message=""):
    with open("log.txt", "w+") as f:
        f.write(f"{tag}: {message}\n")