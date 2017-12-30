import re, pyperclip

text = pyperclip.paste()

#para cada grupo, utilize o retrovisor '\1' + tab '\t'
replaced = re.sub(r'''((transação)|(Crédito|Debito)|(POS|PDV))''', r'\1\t',text)

print(replaced)

pyperclip.copy(replaced)
