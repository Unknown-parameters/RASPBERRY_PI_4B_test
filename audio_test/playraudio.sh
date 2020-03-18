cd /home/pi/recording/
echo '请输入要读取的音频文件名：'
echo '（默认的读取路径/home/pi/recording)'
read p
num = `find -name $p'.wav' |wc -l`
echo $num
if [ $num -eq 0];
then 
  echo '没有文件！'
else
  echo '开始播放'$p'.wav...'
  omxplayer -o local $p'.wav'

fi