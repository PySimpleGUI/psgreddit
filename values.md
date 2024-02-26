
[description]
Search Your Favorite Reddit Subs

[features]
* Integrates PySimpleGUI with PRAW API
* Provides stating point for custom Reddit user interface
* Search your favorite subreddits and their comments

[extras]
## Requirements

To use the GUI you'll need to install PySimpleGUI (http://www.PySimpleGUI.org for instructions)

One of these will install it for you.
```
pip install PySimpleGUI
pip3 install PySimpleGUI
```

You will also need to install the PRAW package which provides the APIs for accessing Reddit

## PRAW Credentials

You must signup with Reddit to in order to get own Reddit API credentials.

To sign up go to - https://www.reddit.com/prefs/apps/ 

For security reasons, the credentials are not stored in the source code, but instead in a "settings file".  The User Settings APIs were added to PySimpleGUI in Nov 2020 and are perfect for storing login credentials.  
    
When you first start the program, it will figure out that you don't have any credentials defined and will show you this settings window:
   
<p align="center"><img scale="100%" src="screenshotA.jpg"><p>


You can also use the "Settings" button in the main window to bring up the settings window.  

## Search History

The items you search for are stored in the settings file as well.  This makes future searches easier as you can select the search term from a drop-down list instead of typing them in.


## Running

Once the packages are installed, you only need to run the single Python file found in this repository - `Reddit_Searcher.py`

When running on Windows, launching with `pythonw` instead of plain `python` will start the program without showing a console window.
