def make_map():
    return {student[0] : student[1] for student in [l.strip().split() for l in (__import__("sys").stdin) if l != "\n"]}