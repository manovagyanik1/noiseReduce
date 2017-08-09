mkdir cleanedVideo

for /r %%i in (*) do echo %%i

# for i in $(ls);do
#     echo $i
#     if [[ $i =~ .*\.mp4$ ]] || [[ $i =~ .*\.MTS$ ]];then
#         ./noiseClean.sh $i cleanedVideo/$i
#     fi
# done