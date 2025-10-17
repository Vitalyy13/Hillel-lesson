import re
import keyword

name = input("Введите имя: ").strip()

pattern = r'^(?:_|(?!_+$)[a-z_][a-z0-9_]*)$'
is_valid = bool(re.fullmatch(pattern, name)) and not keyword.iskeyword(name)
print(is_valid)


