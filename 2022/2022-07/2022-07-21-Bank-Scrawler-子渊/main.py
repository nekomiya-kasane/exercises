from ast import excepthandler
from encodings import utf_8
from numpy import zeros
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from info import *
import urllib
import peewee as pw
import datetime
import numpy as np
from pyquery import PyQuery as pq

import re
import time
import os

use_qr_code: bool = True
# headless: bool = True
sleep_time: int = 0.5
max_ite = 5

# utils


def find_span(dates: list[datetime.date], find: datetime.date) -> int:
    i = 0
    while find > dates[i]:
        i = i + 1
        if i >= len(dates):
            return i
    return i


def sort(res: list, index: int, new):
    for i in range(len(res)):
        if res[i] < 0:
            continue
        if i < index:
            res[i] = new
        else:
            return


def get_time(time: str) -> datetime.date:
    if type(time) == type(datetime.date):
        return time
    key = re.search(r'\d{4}\-\d{2}-\d{2}', time)
    if not key:
        return datetime.date(1970, 1, 1)
    return datetime.datetime.date(datetime.datetime.strptime(key[0], '%Y-%m-%d'))


def get_value(amount: str) -> str:
    res = re.search(r'\d+(\.\d+)?', amount.replace('\n', ''))
    return res[0] if res else '-1'


class Logger:
    def __init__(self, level: int = 0):
        self.level = level

    def trace(self, level: int = 0, msg: str = ""):
        if level > self.level:
            return
        print("{} {}".format(level, msg))


class BrowserDriver:
    def __init__(self, phone: str = "", logger=Logger(1)):
        self.phone = phone
        self.logger = logger
        self.ready = False

    def __getattribute__(self, __name: str):
        if __name.startswith('_'):
            return self.driver.__getattribute__(__name[1:])
        return object.__getattribute__(self, __name)

    def set_trace_level(self, level: int = 0):
        self.logger.level = level

    def trace(self, level: int = 0, msg: str = ""):
        self.logger.trace(level, msg)

    def setup(self) -> bool:
        self.ready = self.init() and self.login()
        return self.ready

    def init(self) -> bool:
        self.trace(1, "-- Preparing web browser...")
        self.options = webdriver.EdgeOptions()
        self.options.add_argument("--window-size=2440,1240")
        # self.options.add_argument("--headless")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                     options=self.options)
        self.driver.get("https://www.tianyancha.com/")
        return True

    def login(self) -> bool:
        login = self.driver.find_element(
            By.CSS_SELECTOR, "span[class^=treasure_nav-link]")
        login.click()
        if not use_qr_code:
            login_mode = self.driver.find_element(
                By.CLASS_NAME, "login-toggle")
            login_mode.click()
            mobile = self.driver.find_element(
                By.XPATH, "//input[@placeholder='请输入手机号']")
            mobile.send_keys(self.phone)
            captchar = self.driver.find_element(
                By.CSS_SELECTOR, '.code-wrapper .suffix')
            captchar.click()
            code = input('Validation code received:')
            code_input = self.driver.find_element(
                By.XPATH, "//input[@placeholder='请输入4位验证码']")
            code_input.send_keys(code)
            buttons = self.driver.find_element(
                By.CSS_SELECTOR, "._50ab4._c9d44._52bf6")
            buttons.click()
        else:
            input('\033[33m-- Please scan the QR code.\033[0m')
        return True


class Collector:
    def __init__(self, driver: BrowserDriver):
        driver.setup()
        self.driver = driver
        self.source = None
        self.current_url = ''

    def get_real_url(self, name: str):
        try:
            #url_keyword = urllib.parse.quote(name)
            self.name = name
            self.current_url = 'http://www.tianyancha.com/search/' + name
            self.driver._get(self.current_url)
            self.driver._implicitly_wait(3)
            source = pq(self.driver._page_source)
            results = source('a[class^=index_alink]')
            for result in results.items():
                if result.text() == name:
                    self.current_url = result[0].attrib['href']
                    return self.current_url
            return False
        except Exception:
            return False

    def set_source(self, url: str) -> bool:
        try:
            self.driver._get(url)
        except:
            return False
        return True

    def analyze(self) -> dict:
        source = pq(self.driver._page_source)
        res = {}

        _max_ite = max_ite
        succeed = False
        # changes
        while not succeed:
            try: 
                res['changes'] = self.__analyze_changes(source)
                succeed = True
            except: 
                time.sleep(1.5)
                _max_ite = _max_ite - 1
                if not _max_ite:
                    raise RuntimeError("\033[31m-- Error analyzing.\033[0m",)
            
        # branches
        try:
            res['branches'] = self.__analyze_branches(source)
        except:
            res['branches'] = []
        # shareholders
        res['shareholders'] = self.__analyze_shareholders(source)
        # basic
        basic = self.__analyze_basic(source)
        # past shareholders
        res['past_shareholders'] = self.__analyze_past_shareholders(source)
        self.info = {**res, **basic}

        return self.info

    def __analyze_changes(self, source) -> list:
        changes_page = self.driver._find_elements(
            By.CSS_SELECTOR, 'div[data-dim="change"] .table-footer')
        if not len(changes_page):
            return []
        changes_page = changes_page[0]
        changes_source = source('div[data-dim="change"] .table-wrap')
        changes = []

        title = changes_source('thead td').text().split(' ')

        def scan(retrieve_page_source: bool = False):
            # while True:
            #     more = self.driver._find_elements(
            #         By.CSS_SELECTOR, 'div[data-dim="change"] .index_openMore__A9Qxk')
            #     if not len(more):
            #         break
            #     more[0].click()
            changes_source = (pq(self.driver._page_source) if retrieve_page_source else source)(
                'div[data-dim="change"] .table-wrap')
            # record all lines
            for row in changes_source('tbody tr').items():
                col_ = 0
                new_item = {}
                for col in row('td').items():
                    if col_ == 0:
                        new_item[title[col_]] = int(col.text())
                    elif col_ == 1:
                        new_item[title[col_]] = get_time(col.text())
                    else:
                        new_item[title[col_]] = col.text()
                    col_ = (col_ + 1) % len(title)
                    if not col_:
                        changes.append(new_item)

        if len(changes_page.find_elements(By.XPATH, './/div[contains(text(), "1") and contains(@class, "num")]')):
            scan()
            for i in range(2, 100):  # max take 100 pages
                next_page = changes_page.find_elements(
                    By.XPATH, './/div[contains(text(), "{}") and contains(@class, "num")]'.format(i))
                if len(next_page):
                    next_page[0].click()
                    time.sleep(0.5)
                    scan(True)
                else:
                    break
        else:
            scan()
            # click all mores

        return changes

    def __analyze_branches(self, source) -> list:
        branches_source = source('div[data-dim="branch"] .table-wrap')
        branches = []

        title = branches_source('thead td').text().split(' ')
        for row in branches_source('tbody tr').items():
            col_ = 0
            new_item = {}
            for col in row('td').items():
                if col_ == 0:
                    new_item[title[col_]] = int(col.text())
                elif col_ == 3:
                    new_item[title[col_]] = get_time(col.text())
                else:
                    new_item[title[col_]] = col.text()
                col_ = (col_ + 1) % len(title)
                if not col_:
                    branches.append(new_item)
        return branches

    def __analyze_shareholders(self, source) -> list:
        shareholders_source = source('div[data-dim="holder"] .table-wrap')
        shareholders = []

        title = shareholders_source('thead td').text().split(' ')
        for row in shareholders_source('tbody tr').items():
            col_ = 0
            new_item = {}
            for col in row('td').items():
                if col_ == 0:
                    new_item[title[col_]] = int(col.text())
                elif col_ == 5:
                    new_item[title[col_]] = get_time(col.text())
                elif col_ == 1:
                    new_item[title[col_]] = col('.right-name').text().strip()
                else:
                    new_item[title[col_]] = float(get_value(col.text()))
                col_ = (col_ + 1) % len(title)
                if not col_:
                    shareholders.append(new_item)
        return shareholders

    def __analyze_past_shareholders(self, source) -> list:
        self.driver._get(self.current_url + '/past')
        time.sleep(0.5)
        past_shareholders_source = pq(self.driver._page_source)(
            'div[data-dim="pastHolder"] .table-wrap')
        past_shareholders = []

        title = past_shareholders_source('thead td').text().split(' ')
        for row in past_shareholders_source('tbody tr').items():
            col_ = 0
            new_item = {}
            for col in row('td').items():
                if col_ == 0:
                    new_item[title[col_]] = int(col.text())
                elif col_ == 5 or col_ == 4:
                    new_item[title[col_]] = get_time(col.text())
                elif col_ == 1:
                    new_item[title[col_]] = col('.right-name').text().strip()
                else:
                    new_item[title[col_]] = float(get_value(col.text()))
                col_ = (col_ + 1) % len(title)
                if not col_:
                    past_shareholders.append(new_item)
        return past_shareholders

    def __analyze_basic(self, source) -> list:
        basic_source = source('div[data-dim="baseInfo"] table')

        basic_raw = [item.text() for item in basic_source('td').items()]
        basic_raw[1] = basic_raw[1].split('\n')[0]  # repr
        del basic_raw[4:6]                          # tianyan grading

        basic = {basic_raw[2 * i]: basic_raw[2 * i + 1]
                 for i in range(len(basic_raw) >> 1)}
        basic['成立日期'] = get_time(basic['成立日期'])
        basic['法定代表人'] = basic_source('.right-info .right-name').text()
        basic['参保人数'] = int(get_value(basic['参保人数']))
        basic['注册资本'] = float(get_value(basic['注册资本']))
        basic['实缴资本'] = - \
            1 if basic['实缴资本'].strip(
        ) == '-' else float(get_value(basic['实缴资本'].strip()))
        basic['工商注册号'] = get_value(basic['工商注册号'])
        basic['注册地址'] = basic['注册地址'].split(
            '\n')[0].replace('复制', '').replace('附近公司', '')
        basic['统一社会信用代码'] = basic['统一社会信用代码'].split(
            '\n')[0].replace('复制', '', 1)
        basic['纳税人识别号'] = basic['纳税人识别号'].split('\n')[0].replace('复制', '', 1)
        basic['组织机构代码'] = basic['组织机构代码'].split('\n')[0].replace('复制', '', 1)
        basic['英文名称'] = basic['英文名称'].split('\n')[0].replace('复制', '', 1)
        basic['曾用名'] = basic['曾用名'].split('\n')[0].replace('复制', '', 1)
        basic['核准日期'] = get_time(basic['核准日期'])
        basic['营业期限'] = basic['营业期限'].split('\xa0')
        if len(basic['营业期限']) == 3:
            basic['营业期限'] = [basic['营业期限'][0], basic['营业期限'][2]]

        basic_source = source('div[class^=index_company-header-content]')

        basic['phone'] = basic_source(
            'span[class^=index_detail-tel]').text().strip()
        basic['email'] = basic_source(
            'span[class^=index_detail-email]').text().strip()
        basic['website'] = basic_source(
            'div[class^=index_first] .link-click').text().strip()

        basic['url'] = self.current_url
        return basic

    # utils
    def get_history_capital(self, info=None) -> list:
        info = info if info else self.info
        years = [datetime.date(i, 1, 1) for i in range(2008, 2023)]

        latest_capital = info["注册资本"]
        start_time = info['成立日期']

        span_index = find_span(years, start_time)
        res = [-1 if i <
               span_index - 1 else latest_capital for i in range(len(years))]

        changes = filter(lambda item: item['变更项目'].find(
            '注册资本') >= 0, info["changes"])
        changes = [{"time": item['变更日期'], "modified": float(get_value(
            item['变更前']))} for item in changes]
        for change in changes:
            sort(res, find_span(years, change['time']) - 1, change['modified'])
        return res

    def get_history_branches(self, info=None) -> list:
        info = info if info else self.info
        years = [datetime.date(i, 1, 1) for i in range(2008, 2023)]

        latest_branches = len(info['branches'])
        start_time = info['成立日期']

        span_index = find_span(years, start_time)
        res = [-1 if i <
               span_index - 1 else latest_branches for i in range(len(years))]

        # todo 注册资本 xx
        branch_num = latest_branches
        changes = filter(lambda item: item['经营状态'].find(
            '注销') < 0, info["branches"])
        changes = [{"time": item['成立日期']} for item in changes]
        for change in changes:
            branch_num = branch_num - 1
            sort(res, find_span(years, change['time']) - 1, branch_num)
        return res

    def get_largest_shareholder(self, info=None):
        if not len(info['shareholders']):
            print("\033[34m-- [Info] {} has no shareholders.\033[0m".format(self.name))
            return ("None", -1)
        info = info if info else self.info
        biggest = list(info['shareholders'][0].values())
        return (biggest[1].split('\n')[0], float(biggest[2]))

    def get_ex_shareholder(self, info=None):
        info = info if info else self.info
        # todo
        if not len(info['past_shareholders']):
            print("\033[34m-- [Info] {} has no past_shareholders.\033[0m".format(self.name))
            return ("None", -1)
        if len(info['past_shareholders']):
            biggest = info['past_shareholders'][0]
            return (biggest["股东"], biggest["退股日期"])
        else:
            return ("None", datetime.date(1970, 1, 1))


db = pw.SqliteDatabase('data.db')


class Runner:
    fails: list[str] = []

    def __init__(self, collector: Collector, list: list[str] = []):
        self.targets = list
        self.target_urls = []
        self.collector = collector

    class BaseModel(pw.Model):
        class Meta:
            database = db

    class Company(BaseModel):
        name = pw.TextField(default="", unique=True, primary_key=True)
        url = pw.TextField(default="")
        phone = pw.TextField(default="")
        email = pw.TextField(default="")
        website = pw.TextField(default="")
        start_time = pw.DateTimeField(default=datetime.date.fromtimestamp(0))
        shareholder = pw.TextField(default="")
        shareholder_ratio = pw.FloatField(default=-1)
        ex_shareholder = pw.TextField(default="")
        shareholder_renew_time = pw.DateTimeField(
            default=datetime.date.fromtimestamp(0))
        capital_history = pw.TextField(default="")
        branches_history = pw.TextField(default="")
        legal_representative = pw.TextField(default="")
        uscc = pw.TextField(default="")
        business_term = pw.TextField(default="")
        company_type = pw.TextField(default="")
        insured_number = pw.IntegerField(default=-1)
        ex_name = pw.TextField(default="")
        registered_address = pw.TextField(default="")
        status = pw.TextField(default="")
        establishment_date = pw.DateTimeField(
            default=datetime.date.fromtimestamp(0))
        registered_capital = pw.FloatField(default=-1)
        contributed_capital = pw.FloatField(default=-1)
        tin = pw.TextField(default="")
        taxpayer_qulification = pw.TextField(default="")
        industry = pw.TextField(default="")
        registration_authority = pw.TextField(default="")
        english_name = pw.TextField(default="")
        registration_mark = pw.TextField(default="")
        organization_id = pw.TextField(default="")
        approval_date = pw.DateTimeField(
            default=datetime.date.fromtimestamp(0))
        staff_size = pw.TextField(default="")
        business_scope = pw.TextField(default="")

    def run(self):
        db.connect()
        db.create_tables([self.Company], safe=True)
        db.close()
        os.makedirs('./res', exist_ok=True)
        with open('real_urls.txt', 'w+', encoding="utf-8") as f:
            index = len(self.targets)
            current_index = 0
            for name in self.targets:
                name = name.strip()
                print('\033[33m-- [{0:.2f} %] collecting {1}...\033[0m'.format(
                    current_index / float(index) * 100, name))
                real_url = self.collector.get_real_url(name)
                f.writelines(real_url or "fail")
                if not real_url:
                    self.fails.append(name)
                self.target_urls.append({"name": name, "url": real_url})

                if not real_url:
                    continue

                if not self.collector.set_source(real_url):
                    self.fails.append(name)
                    continue
                
                time.sleep(0.5)
                info = self.collector.analyze()

                holder, holder_ratio = self.collector.get_largest_shareholder(
                    info)
                ex, ex_time = self.collector.get_ex_shareholder(info)

                his_br = self.collector.get_history_branches(info)
                his_cp = self.collector.get_history_capital(info)

                info['largest_holder'] = holder
                info['largest_holder_ratio'] = holder_ratio
                info['ex_largest_holder'] = ex
                info['ex_largest_holder_change_time'] = ex_time
                info['history_branches'] = his_br
                info['history_capital'] = his_cp

                try:
                    company = self.Company.create(
                        name=name,
                        url=info['url'],
                        phone=info['phone'],
                        email=info['email'],
                        website=info['website'],
                        start_time=info['成立日期'],
                        branches_history=str(his_br),
                        capital_history=str(his_cp),
                        shareholder=str(holder),
                        shareholder_ratio=holder_ratio,
                        ex_shareholder=ex,
                        shareholder_renew_time=ex_time,
                        legal_representative=info['法定代表人'],
                        uscc=info['统一社会信用代码'],
                        business_term=str(info['营业期限']),
                        company_type=info['企业类型'],
                        insured_number=info['参保人数'],
                        ex_name=info['曾用名'],
                        registered_address=info['注册地址'],
                        status=info['经营状态'],
                        establishment_date=info['成立日期'],
                        registered_capital=info['注册资本'],
                        contributed_capital=info['实缴资本'],
                        tin=info['纳税人识别号'],
                        taxpayer_qulification=info['纳税人资质'],
                        industry=info['行业'],
                        registration_authority=info['登记机关'],
                        english_name=info['英文名称'],
                        registration_mark=info['工商注册号'],
                        organization_id=info['组织机构代码'],
                        approval_date=info['核准日期'],
                        staff_size=info['人员规模'],
                        business_scope=info['经营范围']
                    )
                    company.save()
                except pw.PeeweeException:
                    print('\033[34m-- Warning: {} already in database.\033[0m')
                    pass

                with open('./res/' + name + '.txt', 'w+', encoding='utf-8') as g:
                    g.write(str(info))

                current_index = current_index + 1
                print('\033[32m-- [{0:.2f} %] finished {1}...\033[0m'.format(
                    current_index / float(index) * 100, name))

    def get_fails(self) -> list[str]:
        return self.fails


def main():
    driver = BrowserDriver(phone=13230379995)
    collector = Collector(driver)
    lines = []
    with open('list.txt', 'rt', encoding="utf-8") as f:
        lines = f.readlines()
    runner = Runner(collector, lines)
    runner.run()
    fails = runner.get_fails()
    with open('fails.txt', 'w', encoding="utf-8") as f:
        f.writelines(fails)


if __name__ == "__main__":
    main()
