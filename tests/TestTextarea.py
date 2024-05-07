from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys
from textwrap import dedent

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
        self.assertTrue('0J' in element.text)

    def test_textarea(self):
        """フォーム入力のテスト
            * http://web/textarea.htmlにアクセスする
            * フォームに含まれる変数名 `input_text` に対し、以下のテキストを入力する: |
                これはサンプルのテキストです。
                改行コードも渡しています。
            * 送信ボタン(submit)を押して送信する
            * 2つめのpタグを取得し、上記テキストが値として渡されているかを確認する
        """
        self.driver.get("http://web/textarea.html")
        time.sleep(2)
        from os.path import dirname
        # テキストエリアに入力するテキストを、同じディレクトリにある input.txt ファイルから読み込み、text変数に入れておく
        # このとき本スクリプトはカレントディレクトリか親ディレクトリかのいずれかから呼ばれるため、適宜パスを徴すること
        with open(f"{dirname(__file__)}/input.txt") as f:
            text = f.read()
        self.driver.find_element(By.NAME, 'input_text').send_keys(text)
        # ここで `results/03-01-input.png` にスクショを入れる
        self.driver.save_screenshot('results/03-01-input.png')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)

        # ここで `results/03-02-result.png` にスクショを入れる
        self.driver.save_screenshot('results/03-02-result.png')
        # 2つめのpタグを取得
        element = self.driver.find_elements(By.TAG_NAME, 'p')[1]
        # テキストを取得し、改行コードがCRLFになっているのでLFに戻す
        rtext = element.text #.replace('\n', '\r\n')

        # text,rtextそれぞれの改行コードをスペースに変換する
        text = text.replace('\n', ' ')
        rtext = rtext.replace('\n', ' ')
        # text, rtextそれぞれの末尾改行を取り除く
        text = text.rstrip()
        rtext = rtext.rstrip()

        # テキストが一致するか確認
        self.assertEqual(text, rtext)

if __name__ == '__main__':
    unittest.main()
