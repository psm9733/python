#make Sangmin
import urllib.request
import re
import os
from bs4 import BeautifulSoup

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

    def read_extract_file(self):
        self.path = os.getcwd() + "\\project\\"
        self.init_number = Urls().get_init_number()
        self.last_number = Urls().get_last_number()
        try:
            editfile = open(self.path + "pullrequest_info\\pullrequest_info.txt", "w")
        except FileNotFoundError:
            print("*****Error happen*****")
            print("File data is not exist. -> You should be downloading Pullrequest_html Now!!\n")
            return
        for number in range(self.init_number, self.last_number + 1):
            try:
                file = open(self.path + "htmlfile\\" + str(number) + ".txt", "r")
                f = str(file.readlines())
                bs = BeautifulSoup(f)
                name = bs.find_all(rel="contributor")
                editfile_name = bs.find_all(class_="message")
                editfile.write(str(number)+"    :    "+name[0].string +"   :   "+ editfile_name[0].string)
                print("Extracting..."+str(number)+"/"+str(self.last_number)+"...waiting")
            except FileNotFoundError:
                print("***** Error happen *****")
                print("File data is not exist. -> You should be downloading Pullrequest_html Now!!\n")
                return
            else:
                print("Extracting..."+str(number)+"/"+str(self.last_number)+"Complete")

class Urls():
    define = False
    req = urllib.request
    url = req.urlopen("http://github.com/jyheo/JavaExercise/pulls")
    pull_first_url = "https://github.com/jyheo/JavaExercise/pull/"
    pulls_list_html = url.read()

    def __init__(self):
        extract = Extract_url(self.pulls_list_html)
        self.init_number = extract.get_init_number()
        self.last_number = extract.get_last_number()
        self.define = True
        self.url_list = ''


    def find_pull_url(self):
        for number in range(self.init_number, self.last_number+1):
            if number == self.last_number:
                self.url_list += self.pull_first_url + str(number)
            else:
                self.url_list += self.pull_first_url + str(number) + ','
        url_list_array = re.split(',',self.url_list)
        return url_list_array


    def get_urls_html_downloading(self):
        f = File()
        for url in self.find_pull_url():
            try:
                html = self.req.urlopen(url).read()
                print(str(re.findall("\d+",url)[0])+"/"+str(self.last_number)+".....downloading....."+url)
                f.make_htmlfile(re.findall("\d+", url)[0]).write(str(html))
            except urllib.error.HTTPError:
                print("urllib.error.HTTPErro........" + url+"\n")
                return
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
            os.mkdir(os.getcwd() + "\\project")
            os.mkdir(os.getcwd() + "\\project\\htmlfile")
            os.mkdir(os.getcwd() + "\\project\\pullrequest_info")

        except FileExistsError:
            print("동일한 폴더가 존재")

    def make_htmlfile(self, number):                #html정보를 저장할 파일 생성
        return open(os.getcwd()+"\\project\\htmlfile\\"+str(number)+".txt", "w")

    def print_file(self):
        try:
            contents = open(os.getcwd() + "\\project\\pullrequest_info\\pullrequest_info.txt","r")
        except FileNotFoundError:
            print("***** Error happen *****")
            print("File data is not exist. -> You should be renewing Pullrequest_informaion Now!!\n")
            return
        print("Number   :    Name   :   EditFile")
        for content in contents:
            print(content)


if __name__ == '__main__':

    while (True):
        print("1. pullrequest_html_downloading")
        print("2. pullrequest_information_renew")
        print("3. print_pullrequest_total_information")
        print("4. Exit")

        try:
            choice = int(input(">>"))  # input
        except ValueError:
            print("***** Error happen *****")
            print("**** choice value is error choice. input again ****\n")
            continue

        if (choice == 1):    # pullrequest html 다운로드
            Urls().get_urls_html_downloading()
        elif (choice == 2):  # 정보 갱신
            Extract_file().read_extract_file()
        elif (choice == 3):  # 정보 출력
            File().print_file()
        elif (choice == 4):  # 종료
            print("4. Exit")
            break
        else:
            print("**** choice value is error choice. input again ****")
