# Youtube to podcast feed

This app should (will) be able to receive youtube url for downloading, download and extract audio and create podcast compatible rss feed, so I can add it to my podcast player.

## TODO

- [x] - understant, how youtube-dl work in python
- [x] - download video, extract audio, save to folder
- [ ] - rename filenames so they dont have spaces
- [ ] - save video info somewhere (file, db) for already downloaded files
- [ ] - check if file has already been downloaded, don't repeat
- [ ] - after each download, update rss feed
- [ ] - find out, if the download path is safe to use at it is
- [ ] - protect smhw the download path, with password or sth
- [ ] - make status page, to show what is downloading, downloaded, also protected
- [ ] - create docker image
- [ ] - create produciton ready docker image