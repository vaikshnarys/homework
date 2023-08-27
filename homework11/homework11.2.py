import re
input = str(input("Please input e-mail:"))
def input_data(e_mail):
    textlookfor = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[A-Za-z0-9.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[a-z0-9{63}\-]+\.[a-z]+(?!\-)$"
    result = re.match(textlookfor,input) is not None
    print(result)
input_data(input)