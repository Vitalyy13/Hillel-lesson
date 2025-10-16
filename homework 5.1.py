import re
import keyword

name = input("Введите имя: ").strip()
is_valid = (
    bool(re.fullmatch(r'[a-z_][a-z0-9_]*', name)) and
    (name.count('_') <= 1) and
    (not keyword.iskeyword(name))
)
print(is_valid)
