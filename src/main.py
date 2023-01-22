from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import UserInfo
import Log
import Const
import OperationWindow


class Main:
    """
     @class     Mainクラス
    """ 
    # ログクラス
    m_objLog: Log.Log = Log.Log();

    
    # 固定値設定クラス
    m_objSettingFile: Const.SettingFile = Const.SettingFile.staticSettingFile();
        
    # ユーザー情報クラス
    m_objUserInfo: UserInfo.UserInfo = UserInfo.UserInfo();
    
    
    # WebDriver
    m_objWebDriver: WebDriver;
    
            
    
    def main(self) ->  None:
        """
        @details        main関数
        """
        # ログインキャッシュの確認と再び Webへアクセスしないための制限
        if not self.m_objUserInfo.getExistCache():
            try:
                # ログインキャッシュの有無
                strLoginChaceDir: str = os.path.normpath(os.path.join(self.m_objSettingFile.EXE_BASE_FILE_PATH, f'..\\dat\\{self.m_objSettingFile.FOLDER_LOGIN_CACHE}'));
                
                # オプション設定
                objOptions: Options = webdriver.ChromeOptions();
                
                # ログインキャッシュが存在するか否か
                if not os.path.exists(strLoginChaceDir):
                    os.makedirs(strLoginChaceDir, exist_ok=True);
                    objOptions.add_argument(f'--user-data-dir={strLoginChaceDir}');    
                    self.m_objLog.LogInfo('ログインキャッシュを生成しました');
                    
                # ログインキャッシュの有無を「有」へ変更
                else:
                    objOptions.add_argument(f'--user-data-dir={strLoginChaceDir}');
                    self.m_objUserInfo.setExistCache(True);
                    self.m_objLog.LogInfo('ログインキャッシュが確認できました');
                    
                
                # 環境に応じた webdriverを自動インストール
                self.m_objWebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=objOptions);
                self.m_objWebDriver.implicitly_wait(15);
                
                # UserInfo.xml：アカウント情報の取得
                self.m_objUserInfo.readUserInfo();
            
            
            except Exception as e:
                self.m_objLog.LogCritical('ログインキャッシュ情報の確認中に致命的なエラーが発生しました');
                self.m_objLog.LogCritical('続行不可能なため終了します');
                
                # 終了
                sys.exit();
            
            
        # ブラウザウィンドウサイズの最大化
        # self.m_objWebDriver.maximize_window();
        
        # ブラウザウィンドウサイズの指定
        self.m_objWebDriver.set_window_size(1920, 1080)
        
        # GUIインスタンスの生成及びメルカリログイン
        objOperationWindow: OperationWindow.OperationWindow = OperationWindow.OperationWindow(self.m_objWebDriver, self.m_objUserInfo);
        
        # ブラウザウィンドウサイズの最小化
        # self.m_objWebDriver.minimize_window();
        
        # GUI生成(ユーザー選択項目の取得)
        objOperationWindow.guiOperatKind();
        
        
    
if __name__ == '__main__':
    
    # Main
    objMain: Main = Main();
    objMain.main();
