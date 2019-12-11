class Date:
    _formats = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == "":
            format_spec = 'ymd'
        fmt = self._formats[format_spec]
        return fmt.format(d=self)
