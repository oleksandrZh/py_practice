def count_words(args):
    return len(args.rsplit())


def create_hokku(*args):
    final_string = ""
    for i in args:
        final_string = final_string + i + "\n"
    return final_string.rstrip()
