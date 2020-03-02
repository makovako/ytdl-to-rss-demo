# Youtube to podcast feed

This app should (will) be able to receive youtube url for downloading, download and extract audio and create podcast compatible rss feed, so I can add it to my podcast player.

## Usage

For now some basic usage:

- '/download' - use download_url parameter in json to download video
- '/info/youtube_id' - shows info about downloaded video
- '/all' - lists all downloaded videos
- '/generate' - generates rss podcast feed indo download folder with name feed.xml



## TODO

- [x] - understant, how youtube-dl work in python
- [x] - download video, extract audio, save to folder
- [x] - rename filenames so they dont have spaces - using video ids as filenames
- [x] - save video info somewhere (file, db) for already downloaded files - sqlite
- [ ] - check if file has already been downloaded, don't repeat
- [x] - after each download, update rss feed - manually for now
- [ ] - add option to delete video
- [ ] - add download_date into db, so pubdate in rss can be set
- [ ] - find out, if the download path is safe to use at it is
- [ ] - protect smhw the download path, with password or sth
- [ ] - make downloading of video async, so status page can be useful
- [ ] - make status page, to show what is downloading, downloaded, error, cause, also protected
- [ ] - maybe have page for setting up podcast metadata
- [ ] - maybe have edit page for each podcast entry
- [ ] - create env configuration file and load it
- [ ] - refactor, organize into files and functions
- [ ] - create docker image
- [ ] - create produciton ready docker image