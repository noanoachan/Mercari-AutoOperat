from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import UserInfo
import Log
import OperationWindow
import Common.Common;


class Main:
    """
     @class     Mainクラス
    """ 
    # ログクラス
    LOG: Log.Log = Log.Log();


    # 共通設定クラス
    COMMON: Common.Common.Common = Common.Common.Common.staticCommon();
        

    # ユーザー情報クラス
    objUserInfo: UserInfo.UserInfo = UserInfo.UserInfo();
    
    
    # WebDriver
    objWebDriver: WebDriver;
    
            
    
    def main(self) ->  None:
        """
        @details        main関数
        """
        # ログインキャッシュの確認と再び Webへアクセスしないための制限
        if not self.objUserInfo.getExistCache():
            try:
                # ログインキャッシュの有無
                strLoginChaceDir: str = os.path.normpath(os.path.join(self.COMMON.EXE_BASE_FILE_PATH, f'..\\dat\\{self.COMMON.FOLDER_LOGIN_CACHE}'));
                
                # オプション設定
                objOptions: Options = webdriver.ChromeOptions();
                
                # ログインキャッシュが存在するか否か
                if not os.path.exists(strLoginChaceDir):
                    os.makedirs(strLoginChaceDir, exist_ok=True);
                    objOptions.add_argument(f'--user-data-dir={strLoginChaceDir}');    
                    self.LOG.LogInfo('ログインキャッシュを生成しました');
                    
                # ログインキャッシュの有無を「有」へ変更
                else:
                    objOptions.add_argument(f'--user-data-dir={strLoginChaceDir}');
                    self.objUserInfo.setExistCache(True);
                    self.LOG.LogInfo('ログインキャッシュが確認できました');
                    
                
                # 環境に応じた webdriverを自動インストール
                self.objWebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=objOptions);
                self.objWebDriver.implicitly_wait(15);
                
                # UserInfo.xml：アカウント情報の取得
                self.objUserInfo.readUserInfo();
            
            
            except Exception as e:
                self.LOG.LogCritical('ログインキャッシュ情報の確認中に致命的なエラーが発生しました');
                self.LOG.LogCritical('続行不可能なため終了します');
                
                # 終了
                sys.exit();
            
            
        # ブラウザウィンドウサイズの最大化
        # self.m_objWebDriver.maximize_window();
        
        # ブラウザウィンドウサイズの指定
        self.objWebDriver.set_window_size(1920, 1080)
        
        # GUIインスタンスの生成及びメルカリログイン
        objOperationWindow: OperationWindow.OperationWindow = OperationWindow.OperationWindow(self.objWebDriver, self.objUserInfo);
        
        # ブラウザウィンドウサイズの最小化
        # self.m_objWebDriver.minimize_window();
        
        # GUI生成(ユーザー選択項目の取得)
        objOperationWindow.guiOperatKind();
        
        
    
if __name__ == '__main__':
    
    # Main
    objMain: Main = Main();
    objMain.main();
