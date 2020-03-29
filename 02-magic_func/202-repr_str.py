class Language:
    def __init__(self, language_list):
        self.language_list = language_list

    # 对对象描述
    # def __str__(self):
    #     return ','.join(self.language_list)

    # 开发模式使用
    def __repr__(self):
        return ','.join(self.language_list)


language_list = Language(['Python', 'Java', 'Scala', 'Go'])
print(language_list)
