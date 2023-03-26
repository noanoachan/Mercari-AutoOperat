from __future__ import annotations
import os
import sys


class Common:
    """
    @class      共通クラス
    """
    @classmethod
    def staticCommon(cls) ->  Common:
        """
         @brief     static関数
         @return    Common
        """
        return cls()



    # 実行環境までの絶対パス
    EXE_BASE_FILE_PATH: str = os.path.dirname(os.path.abspath(sys.argv[0]));   # ×：__file__  / ○：sys.argv[0]
    
    
    # ログインキャッシュが格納されているフォルダ名
    FOLDER_LOGIN_CACHE: str = 'LoginCache';
    

    # ユーザー情報が記載されているファイル名
    FILE_USER_INFO: str = 'UserInfo.xml';

    
    # 出品商品の写真が格納されているフォルダ名
    FOLDER_PRODUCT_PHOTO: str = 'ProductPhoto';