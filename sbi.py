from selenium import webdriver
import json

_DRIVER = 'D:\\Work\\_common\\chromedriver.exe'


class SBIcomm:
    """
    SBI証券サイトをスクレイピング
    """
    def __init__(self):
        """
        コンストラクタ
        """
        #情報ファイル,chromedriver読み込み
        self.info = json.load( open('D:\\Work\\_common\\sbi.json', 'r', encoding='UTF-8'))
        self.br = self.open_browser(self.info['url'])
        self.br.find_element_by_name('user_id').send_keys(self.info['id'])
        self.br.find_element_by_name('user_password').send_keys(self.info['pw'])
        self.br.find_element_by_name('ACT_login').click()

        
    def __del__(self):
        """
        デストラクタ
        """
    #    self.br.close()
    #    self.br.quit()

    def open_browser(self, url):
        """
        seleniumでurlを開く
        """
        driver = webdriver.Chrome(_DRIVER)
        driver.get(url)
        return driver




if __name__ == "__main__":
    sbi = SBIcomm()
    