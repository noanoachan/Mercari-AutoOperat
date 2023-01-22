from __future__ import annotations
import os
import xml.etree.ElementTree as ET
import Log
import Const


class UserInfo:
    """    
     @class     ユーザー情報クラス
    """
    # ログクラス
    m_objLog: Log.Log = Log.Log();

    
    # 固定値設定クラス
    m_objSettingFile: Const.SettingFile = Const.SettingFile.staticSettingFile();
    
    
    __m_objUserInfo = None;
    
    __m_strEmail    : str   = '';       # メールアドレス
    __m_strPass     : str   = '';       # パスワード
    __m_blCache     : bool  = False;    # キャッシュ情報
    
    
    def __new__(cls) ->  UserInfo:
        """
         @detail        シングルトン
         @return        UserInfo
        """
        if cls.__m_objUserInfo is None:
            cls.__m_objUserInfo = super().__new__(cls);
            
        return cls.__m_objUserInfo;
    
            
    #! Setter
    def __setEmail(self, strEmail: str):
        """
         @detail        メールアドレスの設定
         @param[in]     __m_strEmail    メールアドレス
        """
        self.__m_strEmail = strEmail;
        
    def __setPass(self, strPass: str):
        """        
         @detail        パスワードの設定
         @param[in]     __m_strPass     パスワード
        """
        self.__m_strPass = strPass;
        
    def setExistCache(self, strExistCache: bool):
        """        
         @detail        ログインキャッシュの有無
         @param[in]     __m_blCache     キャッシュ情報
        """
        self.__m_blCache = strExistCache;
        
        
    #! Getter
    def getEmail(self) -> str:
        """
         @detail        メールアドレスの取得
         @param[in]     __m_strEmail    メールアドレス
        """
        return self.__m_strEmail;
    
    def getPass(self) -> str:
        """
         @detail        パスワードの取得
         @param[in]     __m_strPass     パスワード
        """
        return self.__m_strPass;
    
    def getExistCache(self) -> bool:
        """
         @detail        ログインキャッシュの有無を取得
         @param[in]     __m_blCache     キャッシュ情報
        """
        return self.__m_blCache;
    
    
    
    def readUserInfo(self) ->  None:
        """        
         @detail        ユーザー情報の取得
        """
        try:
            objElementTree: ET.ElementTree = ET.parse(os.path.normpath(os.path.join(self.m_objSettingFile.EXE_BASE_FILE_PATH, f'..\\doc\\{self.m_objSettingFile.FILE_USER_INFO}')));
            root: ... = objElementTree.getroot();       #! ※「Ellipsis (...)」調べる
            for userInfo in root.findall('UserInfo'):
                self.__setEmail(userInfo.find('Email').text);
                self.__setPass(userInfo.find('Pass').text);
            
            if self.__m_strEmail == '' or self.__m_strPass == '':
                self.m_objLog.LogError(f'各要素が空です。「{self.m_objSettingFile.FILE_USER_INFO}」に適切な情報を入力して下さい');
                exit();
                
        except Exception as ex:
            self.m_objLog.LogCritical(f'{self.m_objSettingFile.FILE_USER_INFO}の取得に失敗しました');
            print(ex);
            exit();

        self.m_objLog.LogInfo('ログイン情報の取得に成功しました');