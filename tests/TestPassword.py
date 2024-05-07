from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys

# リモートサーバーのアドレス
REMOTE_URL = 'http://selenium:4444/wd/hub'

class SampleTest(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())
            assert self.driver is not None

    def tearDown(self):
        self.driver.quit()

    def test_name(self):
        """h4タグ取得のテスト
        最初のh4タグの値を取得します。
        その値が"0J"を含むならテストが通ります。
        """
        self.driver.get('http://web/password.html')
        time.sleep(2)
        # ここで 'results/before.png' にスクショを入れる
        self.driver.save_screenshot('results/01-01-password-usercheck.png')
        element = self.driver.find_element(By.TAG_NAME, 'h4')
        self.assertTrue('0J' in element.text)

    def test_passwordform(self):
        """フォーム入力のテスト
            * http://web/paassword.htmlにアクセスする
            * フォームのname変数の値として "fugafuga" と入れる
            * フォームのpass変数の値として "guhaguha" と入れる
            * フォームを送信する
            * 受信後のpタグを2つ取得する
                * 最初のpタグの値に "fugafuga" が入っていることを確認する
                * 次のpタグの値に "hogehoge" が入っていることを確認する
        """
        self.driver.get('http://web/password.html')
        time.sleep(2)
        self.driver.save_screenshot('results/01-02-01-password-before-enter.png')
        # フォームに入力
        self.driver.find_element(By.NAME, 'user').send_keys('fugafuga')
        self.driver.find_element(By.NAME, 'pass').send_keys('hogehoge')
        self.driver.save_screenshot('results/01-02-02-password-after-enter.png')
        # フォームを送信
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        self.driver.save_screenshot('results/01-02-03-password-result.png')
        # pタグの取得
        elements = self.driver.find_elements(By.TAG_NAME, 'p')
        self.assertTrue('fugafuga' in elements[0].text)
        self.assertTrue('hogehoge' in elements[1].text)

if __name__ == '__main__':
    unittest.main()
