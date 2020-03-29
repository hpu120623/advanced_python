# Python的魔法函数：以双下划线开始，双下划线结束
# 尽量使用Python自带的魔法函数
class Language:
    def __init__(self, language_list):
        self.language_list = language_list

    def __getitem__(self, item):
        return self.language_list[item]

    def __len__(self):
        return len(self.language_list)


language_list = Language(['Python', 'Java', 'Scala', 'Go'])

for language in language_list:
    print(language)

print('-' * 20)

print(len(language_list))
