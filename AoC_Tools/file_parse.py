class AutoParse:

    def __init__(self):
        pass


    def txt_parse(self, txt):
        with open(txt) as f:
            data = f.readlines()
            return [l.strip() for l in data]

