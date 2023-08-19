class Meta(type):
    def __new__(cls,name,base,attrs):
        attrs.update({"Min_row": 1, "Max_row" : 10})
        return type.__new__(cls,name,base,attrs)

class Row(metaclass=Meta):
    def get_data(self):
        return(0, 0)

row = Row()
print(row.Min_row)gi