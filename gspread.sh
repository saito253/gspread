#/bin/bsah -f

# GAS URLの動作確認用
#curl -X POST -d "co2=355" -o /dev/null https://script.google.com/macros/s/AKfycbyQzdsuLCg2x2ozFPDWXRp9wlcju4TL0If2agwl3t0ESO_b81eJ-LYhDc5w2taA-npN/exec
#exit

while true
do
  result=`./gspread.py`
  #result=`cu -s 9600 -l /dev/ttyACM0`
  curl -X POST -d "co2=${result}" -o /dev/null https://script.google.com/macros/s/AKfycbwYjAkKhn0ZFWTM-PhXYi_abkrNCrxZ_eSM5v3C8D4NbDs_1D21HN9TQfz75JXcFrW3/exec
  sleep 10
done
