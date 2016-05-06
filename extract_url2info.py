import urllib.request
import re
import os
import bs4

class Extract_url():

    def __init__(self, html):
        self.extract_number = re.findall("\d+\s*Closed|\d+\s*Open", str(html))
        self.get_numbers = sorted(re.findall("\d+", str(self.extract_number)))
        self.init_number = min(self.get_numbers)       #string 형이지만 문자에서도 숫자가 크면 문자열에서도 큰 값임
        self.last_number = max(self.get_numbers)       #string 형이지만 문자에서도 숫자가 작으면 문자열에서도 작은 값임

    def get_init_number(self):
        return int(self.init_number)

    def get_last_number(self):
        return int(self.last_number)

class Extract_file():

    def readfile(self):
        self.path = os.getcwd() + "\\project\\htmlfile\\"
        self.init_number = 140#urls().get_init_number()
        self.last_number = urls().get_last_number()
        for number in range(self.init_number, self.last_number + 1):
            file = open(self.path + str(number) + ".txt", "r")
            print(file)


class urls():
    init_number = 140
    define = False
    req = urllib.request
    url = req.urlopen("http://github.com/jyheo/JavaExercise/pulls")
    pull_first_url = "https://github.com/jyheo/JavaExercise/pull/"
    pulls_list_html = url.read()

    def __init__(self):
        extract = Extract_url(self.pulls_list_html)
        #self.init_number = Extract_number(self.pulls_list_html).get_init_number()
        self.last_number = Extract_url(self.pulls_list_html).get_last_number()
        self.define = True
        self.url_list = ''

    def find_pull_url(self):
        for number in range(self.init_number, self.last_number+1):
            if number == self.last_number:
                self.url_list += self.pull_first_url + str(number)
            else:
                self.url_list += self.pull_first_url + str(number) + ','
            '''try:
                self.pulls_url += req.urlopen(self.pull_url + str(number))
                print("a")
            except urllib.error.HTTPError:
                continue'''
        url_list_array = re.split(',',self.url_list)
        return url_list_array


    def get_urls_html_downloading(self):
        f = File()
        for url in self.find_pull_url():
            try:
                html = self.req.urlopen(url).read()
                print("downloading........"+url)
                f.make_htmlfile(re.findall("\d+", url)[0]).write(str(html))
            except urllib.error.HTTPError:
                print("urllib.error.HTTPErro........" + url)
                continue
        print("*** downloading Complete ***")

    def get_url_pull_info(self):
        f = File().make_content_a()

    def get_init_number(self):
        return int(self.init_number)

    def get_last_number(self):
        return int(self.last_number)

class File():
    def __init__(self):
        try:  # 동일한 폴더가 있을 경우를 예외처리
            os.mkdir(os.getcwd() + "\project")
            os.mkdir(os.getcwd() + "\project\\htmlfile")
            os.mkdir(os.getcwd() + "\project\\pullrequest_info")

        except FileExistsError:
            """돌일한 폴더가 존재"""
    def make_content_w(self):                         #id, 수정파일 이름 정보를 담는 파일 생성
        return open(os.getcwd() + "\project\pullrequest_info\pull_request_content.txt", "w")

    def make_content_a(self):  # id, 수정파일 이름 정보를 담는 파일 생성
        return open(os.getcwd() + "\project\pullrequest_info\pull_request_content.txt", "a")

    def make_htmlfile(self, number):                #html정보를 저장할 파일 생성
        return open(os.getcwd()+"\project\\htmlfile\\"+str(number)+".txt", "w")


if __name__ == '__main__':

    while (True):
        print("1. pullrequest_html_downloading")
        print("2. pullrequest_information_renew")
        print("3. print_pullrequest_total_information")
        print("4. search_pullrequest_information")
        print("5. Exit")

        try:
            choice = int(input(">>"))  # input
        except ValueError:
            print("**** choice value is error choice. input again ****")
            continue

        if (choice == 1):    # pullrequest html 다운로드
            urls().get_urls_html_downloading()
        elif (choice == 2):  # 정보 갱신
            print("2. pullrequest_information_download")
            Extract_file().readfile()
        elif (choice == 3):  # 정보 출력
            print("3. pullrequest_information_renew")
        elif (choice == 4):  # 정보 검색
            print("4. search_pullrequest_information")
        elif (choice == 5):  # 종료
            print("5. Exit")
            break
        else:
            print("**** choice value is error choice. input again ****")
