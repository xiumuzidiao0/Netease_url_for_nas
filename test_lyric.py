import sys
import asyncio
from pathlib import Path
sys.path.append('/home/xmzd/vscode/Netease_url')

from main import APIConfig, MusicAPIService
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, USLT

async def test_download_and_verify():
    config = APIConfig()
    # 强制开启 WebDL 使其走到打包逻辑验证单曲
    config.webdl = False
    config.downloads_dir = 'temp'
    
    api_service = MusicAPIService(config)
    print("开始下载英文演示曲目: The Rose - Westlife (515453363)")
    
    # 获取音乐流
    result = api_service.downloader.download_music_file(515453363, 'standard')
    
    if result.success:
        print(f"下载成功！路径: {result.file_path}")
        
        # 验证歌词写入
        audio = MP3(result.file_path, ID3=ID3)
        lyrics = ""
        for tag in audio.tags.values():
            if isinstance(tag, USLT):
                lyrics = tag.text
                break
                
        if lyrics:
            print("\n============ 提取到的内嵌歌词（前 10 行） ============")
            lines = lyrics.split('\n')
            limit = min(10, len(lines))
            for i in range(limit):
                print(f"{i+1}: {lines[i]}")
            print(f"... 共 {len(lines)} 行")
        else:
            print("未在文件中找到内嵌歌词！")
    else:
        print(f"下载失败: {result.error_message}")

if __name__ == '__main__':
    asyncio.run(test_download_and_verify())
