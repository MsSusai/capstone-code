## bash脚本并行程序
sparallel()
{
  # parallel function
  [ -e ./fd1 ] || mkfifo ./fd1
  exec 3<> ./fd1
  rm -rf ./fd1
  for i in `seq 1 $1`; # 确定并行数量
  do
    echo >&3                   
  done
}

eparallel()
{
  wait
  exec 3<&-
  exec 3>&-
}