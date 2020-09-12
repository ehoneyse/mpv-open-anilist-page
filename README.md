# mpv-open-anilist-page
Script for mpv that opens the Anilist page for the currently playing (anime) file.

It does this by extracting/guessing the relevant metadata from the file name (using [guessit](https://github.com/guessit-io/guessit)), searching for it on Anilist, and then opening the page in a new tab on your default browser.

## Requirements
You will need Python 3 installed and in your system path, as well as the following libraries: `guessit`, `requests`:

```bash
pip install guessit requests
```

## Install
Copy or symlink the ```.lua``` and ```.py``` files to your mpv scripts folder (if you're unfamiliar with its location, check the [mpv documentation](https://mpv.io/manual/)).

## Usage
By default, the script binds itself to ```Ctrl+A```.\
To change default binding simply add following line into your **input.conf** file inside your mpv config directory.
```bash
A script-binding launch_anilist       # for mpv-open-anilist-page
```

You can also change the binding by editing the last line in the ```.lua``` script file.

```lua
-- change key binding as desired 
mp.add_key_binding('ctrl+a', 'launch_anilist', launch_anilist)
```

## Credits
**mpv-open-anilist-page** is heavily based on [mpv-open-imdb-page](https://github.com/ctlaltdefeat/mpv-open-imdb-page) by ctlaltdefeat. Thanks to [mpv-open-kinopoisk-page](https://github.com/WANDEX/mpv-open-kinopoisk-page) by WANDEX as well for a great README.md file!

Of course, this would not be possible without [guessit](https://github.com/guessit-io/guessit) and [Anilist GraphQL](https://github.com/AniList/ApiV2-GraphQL-Docs).

## License
[MIT](https://choosealicense.com/licenses/mit/)


