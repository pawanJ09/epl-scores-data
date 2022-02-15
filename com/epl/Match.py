class Match:

    def __init__(self):
        self.home = None
        self.away = None
        self.date = None

    def __str__(self):
        result = f'{self.home.name.rjust(20)}({self.home.result}) {self.home.score} - ' \
                 f'{self.away.score}({self.away.result}) {self.away.name.ljust(20)}'
        return f'{self.date} | {result} | {self.home.ground}'
