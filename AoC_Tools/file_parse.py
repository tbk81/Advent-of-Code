class AutoParse:


    def list_parse(self, li):
        with open(li) as f:
            data = f.readlines()
            return [l.strip() for l in data]