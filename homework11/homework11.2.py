import re
input = str(input("Please input e-mail:"))
def input_data(e_mail):
    textlookfor = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[\w.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[\w{63}\-]+\.[\w]+(?!\-)$"
    result = re.match(textlookfor,input) is not None
    print(result)

input_data(input)