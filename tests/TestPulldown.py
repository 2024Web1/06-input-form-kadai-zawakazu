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
        その値が"0J04"を含むならテストが通ります。
        """
        self.driver.get('http://web/password.html')
        time.sleep(2)
        # ここで 'results/before.png' にスクショを入れる
        self.driver.save_screenshot('results/02-01-password-usercheck.png')
        element = self.driver.find_element(By.TAG_NAME, 'h4')
        self.assertTrue('0J04' in element.text)

    def test_passwordform(self):
        """フォーム入力のテスト
            * http://web/pulldown.htmlにアクセスする
            * 以下のことを確認する
                * プルダウンの選択肢を「リンゴ」にする
                * 送信する
                * 受信後のpタグを取得する
                * pタグのテキストが「あなたの好きなフルーツは、リンゴですね。」となっていることを評価
            * この評価を「オレンジ」「メロン」に対しても行う
        """
        for item in ["リンゴ", "オレンジ", "メロン"]:
            self.driver.get('http://web/pulldown.html')
            time.sleep(1)
            self.driver.save_screenshot(f'results/02-02-01-pulldown-before-{item}-enter.png')
            self.driver.find_element(By.NAME, 'fruit').send_keys(item)
            self.driver.save_screenshot(f'results/02-02-02-pulldown-after-{item}-enter.png')
            # フォームを送信
            self.driver.find_element(By.NAME, 'submit').click()
            time.sleep(1)
            self.driver.save_screenshot(f'results/02-02-03-pulldown-{item}-result.png')
            # pタグの取得
            elements = self.driver.find_elements(By.TAG_NAME, 'p')
            self.assertTrue(f'あなたの好きなフルーツは、{item}ですね。' in elements[0].text)


if __name__ == '__main__':
    unittest.main()
