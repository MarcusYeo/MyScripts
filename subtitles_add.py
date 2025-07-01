import os
import subprocess
import shlex

def add_subtitles_to_videos(directory_path):
    ffmpeg_path = r'C:\Users\marcus.yeo\Downloads\ffmpeg-7.0.2-full_build\ffmpeg-7.0.2-full_build\bin\ffmpeg.exe'

    for root, dirs, files in os.walk(directory_path):
        mp4_files = [f for f in files if f.endswith('.mp4')]
        
        for mp4_file in mp4_files:
            base_name = os.path.splitext(mp4_file)[0]
            mp4_path = os.path.join(root, mp4_file)
            srt_path = os.path.join(root, f'{base_name}.srt')
            temp_mp4_path = os.path.join(root, f'{base_name}_temp.mp4')
            
            if os.path.exists(srt_path):
                # Quote paths using shlex.quote
                mp4_path_quoted = shlex.quote(mp4_path)
                srt_path_quoted = shlex.quote(srt_path)
                temp_mp4_path_quoted = shlex.quote(temp_mp4_path)
                
                # Construct the command with properly quoted paths
                command = f'"{ffmpeg_path}" -i {mp4_path_quoted} -report -vf subtitles={srt_path_quoted} {temp_mp4_path_quoted}'
                
                # Print the command for debugging purposes
                print("Running command:", command)
                
                # Run the command
                subprocess.run(command, shell=True, check=True)
                
                # Remove the original files
                os.remove(mp4_path)
                os.remove(srt_path)
                
                # Rename the temporary file to the original name
                os.rename(temp_mp4_path, mp4_path)
                print(f'Processed and renamed: {mp4_path}')
            else:
                print(f'Subtitle file not found for {mp4_path}, skipping.')

if __name__ == '__main__':
    directory_path = r'E:\video\VideoFolder'
    add_subtitles_to_videos(directory_path)
