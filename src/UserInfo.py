from __future__ import annotations
import os
import xml.etree.ElementTree as ET
import Log
import Common.Common;


class UserInfo:
    """    
     @class     ユーザー情報クラス
    """
    # ログクラス
    LOG: Log.Log = Log.Log();

    
    # 共通設定クラス
    COMMON: Common.Common.Common = Common.Common.Common.staticCommon();
    
    __objUserInfo = None;
    
    __strEmail    : str   = '';       # メールアドレス
    __strPass     : str   = '';       # パスワード
    __blCache     : bool  = False;    # キャッシュ情報
    
    
    def __new__(cls) ->  UserInfo:
        """
         @detail        シングルトン
         @return        UserInfo
        """
        if cls.__objUserInfo is None:
            cls.__objUserInfo = super().__new__(cls);
            
        return cls.__objUserInfo;
    
            
    #! Setter
    def __setEmail(self, strEmail: str):
        """
         @detail        メールアドレスの設定
         @param[in]     __m_strEmail    メールアドレス
        """
        self.__strEmail = strEmail;
        
    def __setPass(self, strPass: str):
        """        
         @detail        パスワードの設定
         @param[in]     __m_strPass     パスワード
        """
        self.__strPass = strPass;
        
    def setExistCache(self, strExistCache: bool):
        """        
         @detail        ログインキャッシュの有無
         @param[in]     __m_blCache     キャッシュ情報
        """
        self.__blCache = strExistCache;
        
        
    #! Getter
    def getEmail(self) -> str:
        """
         @detail        メールアドレスの取得
         @param[in]     __m_strEmail    メールアドレス
        """
        return self.__strEmail;
    
    def getPass(self) -> str:
        """
         @detail        パスワードの取得
         @param[in]     __m_strPass     パスワード
        """
        return self.__strPass;
    
    def getExistCache(self) -> bool:
        """
         @detail        ログインキャッシュの有無を取得
         @param[in]     __m_blCache     キャッシュ情報
        """
        return self.__blCache;
    
    
    
    def readUserInfo(self) ->  None:
        """        
         @detail        ユーザー情報の取得
        """
        try:
            objElementTree: ET.ElementTree = ET.parse(os.path.normpath(os.path.join(self.COMMON.EXE_BASE_FILE_PATH, f'..\\doc\\{self.COMMON.FILE_USER_INFO}')));
            root: ... = objElementTree.getroot();       #! ※「Ellipsis (...)」調べる
            for userInfo in root.findall('UserInfo'):
                self.__setEmail(userInfo.find('Email').text);
                self.__setPass(userInfo.find('Pass').text);
            
            if self.__strEmail == '' or self.__strPass == '':
                self.LOG.LogError(f'各要素が空です。「{self.COMMON.FILE_USER_INFO}」に適切な情報を入力して下さい');
                exit();
                
        except Exception as ex:
            self.LOG.LogCritical(f'{self.COMMON.FILE_USER_INFO}の取得に失敗しました');
            print(ex);
            exit();

        self.LOG.LogInfo('ログイン情報の取得に成功しました');