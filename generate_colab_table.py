import os
from urllib.parse import quote

# Настройки
GITHUB_USER = "KorgiBit"
GITHUB_REPO = "python-cheatsheets"
CHEATSHEETS_DIR = "cheatsheets"

# Получаем список всех .ipynb файлов
notebooks = [f for f in os.listdir(CHEATSHEETS_DIR) if f.endswith(".ipynb")]
notebooks.sort()

def filename_to_title(filename):
    # Убираем расширение и заменяем подчеркивания на пробелы (можно доработать под ваши правила)
    name = filename.replace(".ipynb", "")
    name = name.replace("_", " ")
    return name

# Генерируем таблицу
lines = []
lines.append("| Тема | Открыть в Colab |")
lines.append("|------|------------------|")
for nb in notebooks:
    title = filename_to_title(nb)
    local_link = f"{CHEATSHEETS_DIR}/{nb}"
    colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{GITHUB_REPO}/blob/main/{CHEATSHEETS_DIR}/{quote(nb)}"
    colab_badge = f"[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    lines.append(f"| [{title}]({local_link}) | {colab_badge} |")

# Автоматическая замена таблицы в README.md между маркерами
README_PATH = "README.md"
START_MARK = "<!-- START CHEATSHEETS TABLE -->"
END_MARK = "<!-- END CHEATSHEETS TABLE -->"

with open(README_PATH, encoding="utf-8") as f:
    readme = f.read()

if START_MARK in readme and END_MARK in readme:
    before = readme.split(START_MARK)[0]
    after = readme.split(END_MARK)[1]
    table_md = "\n".join(lines)
    new_readme = before + START_MARK + "\n" + table_md + "\n" + END_MARK + after
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("Таблица успешно обновлена в README.md между маркерами.")
else:
    print("Маркеры таблицы не найдены в README.md. Изменения не внесены.")
