cd /home/pi/recording/
echo '请输入要保存的音频文件名：'
echo '（默认保存路径/home/pi/recording）'
read r
echo '保存的文件名为'$r'.wav'
echo '请设置录音时间：'
echo '（默认不输入为无限，至按ctrl+c结束）'
read t

if [-z "$t"]
then
  echo '开始录音...'
  arecord -D "plughw:1,0" $r'.wav'
else 
  if [[! $t =~ [0-9]]]
  then
    echo -e '输入时间有误！\n默认无限时间，至按ctrl+c结束'
    echo '开始录音...'
    arecord -D "plughw:1,0" $r ',wav'
  else
    echo '开始录音'$t'秒...'
    arecord -D "plughw:1,0" -d $t $r'.wav'
  fi
fi
