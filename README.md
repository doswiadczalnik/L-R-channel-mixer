# L&R Channel Mixer
This tool mix left and right channel of video file into one, mono WAV file. It can be usefull in situations, where you record video using two microphones or one microphone with two capsules and your video file contains audios from these microphones in separate channels. With this tool you can easily mix them without using combinations in your video editor.

### Features

- Written in Python
- Uses ffmpeg
- Automatically extracts left and right audio channel from video file and mix them into one WAV file
- doesn't modify oryginal videos

### Usage
**You need ffmpeg.exe file in the same folder as script. You must download it from Internet before use!**

1. copy your video files into one folder
2. open script in your favorite Python editor (I recommend Thonny, because you can easly edit and run script from it)
3. set **"video_folder"** variable to path from 1st point; use double slash in path
4. you can expand supported video files by modyfing **"video_extensions"** variable, but I haven't tested it.
5. save and run script

Script will process all video files. Each of them will get WAV file with the same name as oryginal video with "_mixed" added.


**Oryginal video files won't be changed.** Use created WAVs in your video editor.
