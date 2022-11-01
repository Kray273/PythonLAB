# 04_ContactInfo
class ContactInfo :
    def __init__(self, name, email): # 초기화 할 때 받아올 변수를 입력해서 초기화 하는 것이 일반적.
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
    cow = ContactInfo('소간지', 'coolCow@haha.com')
    wow = ContactInfo('와뜨거', 'hotWow@haha.com')

    cow.print_info()
    wow.print_info()