import re
import keyword

name = input("Введите имя: ").strip()
is_valid = (
    bool(re.fullmatch(r'[a-z_][a-z0-9_]*', name)) and
    (name == '_' or set(name) != {'_'}) and
    not keyword.iskeyword(name)
)
print(is_valid)