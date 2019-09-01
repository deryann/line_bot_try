# line_bot_try

根據幾個網路上的說明，寫出基本的line bot

*  請由 config_template\config.json 把檔案拷貝到 root 目錄底下
   並且註冊 line developer 取得 token and web hook handler 填入該 json 檔案
   最後希望能取得一個給予訊息的 user id/ group id
   
* 主要檔案
   - app.py 聽取訊息，並且回復(若是被加入某一群組，會馬上打招呼，並且秀出該群組的group id
   - main.py 負責利用 access token 把訊息單向的傳給某人或者是某群組( 可作為簡訊訊息通知用 )
   
*  Reference 
   - https://yaoandy107.github.io/line-bot-tutorial/


