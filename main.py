# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Brown')
    print("데이터를 불러오고 있습니다. 잠시만 기다려 주세요.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import datetime
from urllib.request import urlopen

from bs4 import BeautifulSoup

kma = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
kma_past = "https://www.weather.go.kr/weather/climate/past_table.jsp?stn=159&x=25&y=12&yy=2020&obs=07"
kma_past_table = "https://www.weather.go.kr/weather/climate/past_tendays.jsp?stn=159&yy=2020&mm=9&obs=11&x=22&y=16"
new_kma_forecast = "https://www.weather.go.kr/weather/forecast/digital_forecast.jsp?x=99&y=76&unit=K"

kma = urlopen(kma)
kma_past = urlopen(kma_past)
kma_past_table = urlopen(kma_past_table)
new_kma_forecast = urlopen(new_kma_forecast)

kma_int = BeautifulSoup(kma, "html.parser")
kma_past_int = BeautifulSoup(kma_past, "html.parser")
kma_past_table_int = BeautifulSoup(kma_past_table, "html.parser")
new_kma_forecast_int = BeautifulSoup(new_kma_forecast, "html.parser")

now = datetime.datetime.now()
nowdatetime = now.strftime('%Y년 %m월 %d일 %H시')
tomm_date = now.strftime('%dm월 %d일')

# 현재기온
kma_int_temp = kma_int.select_one("#content_weather > table > tbody > tr:nth-child(32) > td:nth-child(6)")
# 현재습도
kma_int_humid = kma_int.select_one("#content_weather > table > tbody > tr:nth-child(32) > td:nth-child(10)")
# 9.13 평균기온
kma_past_data = kma_past_int.select_one("#content_weather > table > tbody > tr:nth-child(13) > td:nth-child(10)")
# 9월 중순 평년기온
kma_past_table_lowdata = kma_past_table_int.select_one(
    "#content_weather > table > tbody > tr:nth-child(6) > td:nth-child(13)")
# 내일 아침 최저 예상기온
new_kma_forecast_low = new_kma_forecast_int.select_one(
    "#dfs-panel > div.timeseries_mar > table > tbody > tr:nth-child(6) > td.bg_tomorrow > span.low_deg")
# 내일 아침 최고 예상기온
new_kma_forecast_high = new_kma_forecast_int.select_one(
    "#dfs-panel > div.timeseries_mar > table > tbody > tr:nth-child(6) > td.bg_tomorrow > span.high_deg")

# 실시간 대기정보
PM25_noksan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221212"
PM25_Daejeo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221211"
PM25_bsharbor = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221902"
PM25_hwamyeong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221183"
PM25_deokcheon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221182"
PM25_deokpo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221282"
PM25_hakjang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221181"
PM25_dangri = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221284"
PM25_jangrim = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221202"
PM25_cheongryong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221191"
PM25_bugok = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221251"
PM25_oncheon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221162"
PM25_myeongjang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221163"
PM25_yeonsan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221221"
PM25_gaegeum = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221283"
PM25_jeonpo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221152"
PM25_daeshin = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221281"
PM25_sujeong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221241"
PM25_choryang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221131"
PM25_bsnharbor = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221901"
PM25_gwangbok = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221112"
PM25_cheonghak = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221142"
PM25_taejongdae = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221141"
PM25_daeyeon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221172"
PM25_gwangan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221271"
PM25_jaesong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221193"
PM25_left = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221192"
PM25_yongsuri = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221233"
PM25_gijang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10008&station_code=221231"
PM10_noksan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221212"
PM10_Daejeo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221211"
PM10_bsharbor = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221902"
PM10_hwamyeong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221183"
PM10_deokcheon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221182"
PM10_deokpo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221282"
PM10_hakjang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221181"
PM10_dangri = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221284"
PM10_jangrim = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221202"
PM10_cheongryong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221191"
PM10_bugok = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221251"
PM10_oncheon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221162"
PM10_myeongjang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221163"
PM10_yeonsan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221221"
PM10_gaegeum = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221283"
PM10_jeonpo = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221152"
PM10_daeshin = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221281"
PM10_sujeong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221241"
PM10_choryang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221131"
PM10_bsnharbor = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221901"
PM10_gwangbok = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221112"
PM10_cheonghak = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221142"
PM10_taejongdae = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221141"
PM10_daeyeon = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221172"
PM10_gwangan = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221271"
PM10_jaesong = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221193"
PM10_left = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221192"
PM10_yongsuri = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221233"
PM10_gijang = "https://www.airkorea.or.kr/web/vicinityStation?item_code=10007&station_code=221231"

PM25_noksan = urlopen(PM25_noksan)
PM25_Daejeo = urlopen(PM25_Daejeo)
PM25_bsharbor = urlopen(PM25_bsharbor)
PM25_hwamyeong = urlopen(PM25_hwamyeong)
PM25_deokcheon = urlopen(PM25_deokcheon)
PM25_deokpo = urlopen(PM25_deokpo)
PM25_hakjang = urlopen(PM25_hakjang)
PM25_dangri = urlopen(PM25_dangri)
PM25_jangrim = urlopen(PM25_jangrim)
PM25_cheongryong = urlopen(PM25_cheongryong)
PM25_bugok = urlopen(PM25_bugok)
PM25_oncheon = urlopen(PM25_oncheon)
PM25_myeongjang = urlopen(PM25_myeongjang)
PM25_yeonsan = urlopen(PM25_yeonsan)
PM25_gaegeum = urlopen(PM25_gaegeum)
PM25_jeonpo = urlopen(PM25_jeonpo)
PM25_daeshin = urlopen(PM25_daeshin)
PM25_sujeong = urlopen(PM25_sujeong)
PM25_choryang = urlopen(PM25_choryang)
PM25_bsnharbor = urlopen(PM25_bsnharbor)
PM25_gwangbok = urlopen(PM25_gwangbok)
PM25_cheonghak = urlopen(PM25_cheonghak)
PM25_taejongdae = urlopen(PM25_taejongdae)
PM25_daeyeon = urlopen(PM25_daeyeon)
PM25_gwangan = urlopen(PM25_gwangan)
PM25_jaesong = urlopen(PM25_jaesong)
PM25_left = urlopen(PM25_left)
PM25_yongsuri = urlopen(PM25_yongsuri)
PM25_gijang = urlopen(PM25_gijang)
PM10_noksan = urlopen(PM10_noksan)
PM10_Daejeo = urlopen(PM10_Daejeo)
PM10_bsharbor = urlopen(PM10_bsharbor)
PM10_hwamyeong = urlopen(PM10_hwamyeong)
PM10_deokcheon = urlopen(PM10_deokcheon)
PM10_deokpo = urlopen(PM10_deokpo)
PM10_hakjang = urlopen(PM10_hakjang)
PM10_dangri = urlopen(PM10_dangri)
PM10_jangrim = urlopen(PM10_jangrim)
PM10_cheongryong = urlopen(PM10_cheongryong)
PM10_bugok = urlopen(PM10_bugok)
PM10_oncheon = urlopen(PM10_oncheon)
PM10_myeongjang = urlopen(PM10_myeongjang)
PM10_yeonsan = urlopen(PM10_yeonsan)
PM10_gaegeum = urlopen(PM10_gaegeum)
PM10_jeonpo = urlopen(PM10_jeonpo)
PM10_daeshin = urlopen(PM10_daeshin)
PM10_sujeong = urlopen(PM10_sujeong)
PM10_choryang = urlopen(PM10_choryang)
PM10_bsnharbor = urlopen(PM10_bsnharbor)
PM10_gwangbok = urlopen(PM10_gwangbok)
PM10_cheonghak = urlopen(PM10_cheonghak)
PM10_taejongdae = urlopen(PM10_taejongdae)
PM10_daeyeon = urlopen(PM10_daeyeon)
PM10_gwangan = urlopen(PM10_gwangan)
PM10_jaesong = urlopen(PM10_jaesong)
PM10_left = urlopen(PM10_left)
PM10_yongsuri = urlopen(PM10_yongsuri)
PM10_gijang = urlopen(PM10_gijang)

PM25_noksan_int = BeautifulSoup(PM25_noksan, "html.parser")
PM25_Daejeo_int = BeautifulSoup(PM25_Daejeo, "html.parser")
PM25_bsharbor_int = BeautifulSoup(PM25_bsharbor, "html.parser")
PM25_hwamyeong_int = BeautifulSoup(PM25_hwamyeong, "html.parser")
PM25_deokcheon_int = BeautifulSoup(PM25_deokcheon, "html.parser")
PM25_deokpo_int = BeautifulSoup(PM25_deokpo, "html.parser")
PM25_hakjang_int = BeautifulSoup(PM25_hakjang, "html.parser")
PM25_dangri_int = BeautifulSoup(PM25_dangri, "html.parser")
PM25_jangrim_int = BeautifulSoup(PM25_jangrim, "html.parser")
PM25_cheongryong_int = BeautifulSoup(PM25_cheongryong, "html.parser")
PM25_bugok_int = BeautifulSoup(PM25_bugok, "html.parser")
PM25_oncheon_int = BeautifulSoup(PM25_oncheon, "html.parser")
PM25_myeongjang_int = BeautifulSoup(PM25_myeongjang, "html.parser")
PM25_yeonsan_int = BeautifulSoup(PM25_yeonsan, "html.parser")
PM25_gaegeum_int = BeautifulSoup(PM25_gaegeum, "html.parser")
PM25_jeonpo_int = BeautifulSoup(PM25_jeonpo, "html.parser")
PM25_daeshin_int = BeautifulSoup(PM25_daeshin, "html.parser")
PM25_sujeong_int = BeautifulSoup(PM25_sujeong, "html.parser")
PM25_choryang_int = BeautifulSoup(PM25_choryang, "html.parser")
PM25_bsnharbor_int = BeautifulSoup(PM25_bsnharbor, "html.parser")
PM25_gwangbok_int = BeautifulSoup(PM25_gwangbok, "html.parser")
PM25_cheonghak_int = BeautifulSoup(PM25_cheonghak, "html.parser")
PM25_taejongdae_int = BeautifulSoup(PM25_taejongdae, "html.parser")
PM25_daeyeon_int = BeautifulSoup(PM25_daeyeon, "html.parser")
PM25_gwangan_int = BeautifulSoup(PM25_gwangan, "html.parser")
PM25_jaesong_int = BeautifulSoup(PM25_jaesong, "html.parser")
PM25_left_int = BeautifulSoup(PM25_left, "html.parser")
PM25_yongsuri_int = BeautifulSoup(PM25_yongsuri, "html.parser")
PM25_gijang_int = BeautifulSoup(PM25_gijang, "html.parser")
PM10_noksan_int = BeautifulSoup(PM10_noksan, "html.parser")
PM10_Daejeo_int = BeautifulSoup(PM10_Daejeo, "html.parser")
PM10_bsharbor_int = BeautifulSoup(PM10_bsharbor, "html.parser")
PM10_hwamyeong_int = BeautifulSoup(PM10_hwamyeong, "html.parser")
PM10_deokcheon_int = BeautifulSoup(PM10_deokcheon, "html.parser")
PM10_deokpo_int = BeautifulSoup(PM10_deokpo, "html.parser")
PM10_hakjang_int = BeautifulSoup(PM10_hakjang, "html.parser")
PM10_dangri_int = BeautifulSoup(PM10_dangri, "html.parser")
PM10_jangrim_int = BeautifulSoup(PM10_jangrim, "html.parser")
PM10_cheongryong_int = BeautifulSoup(PM10_cheongryong, "html.parser")
PM10_bugok_int = BeautifulSoup(PM10_bugok, "html.parser")
PM10_oncheon_int = BeautifulSoup(PM10_oncheon, "html.parser")
PM10_myeongjang_int = BeautifulSoup(PM10_myeongjang, "html.parser")
PM10_yeonsan_int = BeautifulSoup(PM10_yeonsan, "html.parser")
PM10_gaegeum_int = BeautifulSoup(PM10_gaegeum, "html.parser")
PM10_jeonpo_int = BeautifulSoup(PM10_jeonpo, "html.parser")
PM10_daeshin_int = BeautifulSoup(PM10_daeshin, "html.parser")
PM10_sujeong_int = BeautifulSoup(PM10_sujeong, "html.parser")
PM10_choryang_int = BeautifulSoup(PM10_choryang, "html.parser")
PM10_bsnharbor_int = BeautifulSoup(PM10_bsnharbor, "html.parser")
PM10_gwangbok_int = BeautifulSoup(PM10_gwangbok, "html.parser")
PM10_cheonghak_int = BeautifulSoup(PM10_cheonghak, "html.parser")
PM10_taejongdae_int = BeautifulSoup(PM10_taejongdae, "html.parser")
PM10_daeyeon_int = BeautifulSoup(PM10_daeyeon, "html.parser")
PM10_gwangan_int = BeautifulSoup(PM10_gwangan, "html.parser")
PM10_jaesong_int = BeautifulSoup(PM10_jaesong, "html.parser")
PM10_left_int = BeautifulSoup(PM10_left, "html.parser")
PM10_yongsuri_int = BeautifulSoup(PM10_yongsuri, "html.parser")
PM10_gijang_int = BeautifulSoup(PM10_gijang, "html.parser")

PM25_noksan_int_exp = PM25_noksan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_Daejeo_int_exp = PM25_Daejeo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_bsharbor_int_exp = PM25_bsharbor_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_hwamyeong_int_exp = PM25_hwamyeong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_deokcheon_int_exp = PM25_deokcheon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_deokpo_int_exp = PM25_deokpo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_hakjang_int_exp = PM25_hakjang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_dangri_int_exp = PM25_dangri_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_jangrim_int_exp = PM25_jangrim_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_cheongryong_int_exp = PM25_cheongryong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_bugok_int_exp = PM25_bugok_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_oncheon_int_exp = PM25_oncheon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_myeongjang_int_exp = PM25_myeongjang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_yeonsan_int_exp = PM25_yeonsan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_gaegeum_int_exp = PM25_gaegeum_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_jeonpo_int_exp = PM25_jeonpo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_daeshin_int_exp = PM25_daeshin_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_sujeong_int_exp = PM25_sujeong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_choryang_int_exp = PM25_choryang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_bsnharbor_int_exp = PM25_bsnharbor_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_gwangbok_int_exp = PM25_gwangbok_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_cheonghak_int_exp = PM25_cheonghak_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_taejongdae_int_exp = PM25_taejongdae_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_daeyeon_int_exp = PM25_daeyeon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_gwangan_int_exp = PM25_gwangan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_jaesong_int_exp = PM25_jaesong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_left_int_exp = PM25_left_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_yongsuri_int_exp = PM25_yongsuri_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM25_gijang_int_exp = PM25_gijang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_noksan_int_exp = PM10_noksan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_Daejeo_int_exp = PM10_Daejeo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_bsharbor_int_exp = PM10_bsharbor_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_hwamyeong_int_exp = PM10_hwamyeong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_deokcheon_int_exp = PM10_deokcheon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_deokpo_int_exp = PM10_deokpo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_hakjang_int_exp = PM10_hakjang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_dangri_int_exp = PM10_dangri_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_jangrim_int_exp = PM10_jangrim_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_cheongryong_int_exp = PM10_cheongryong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_bugok_int_exp = PM10_bugok_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_oncheon_int_exp = PM10_oncheon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_myeongjang_int_exp = PM10_myeongjang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_yeonsan_int_exp = PM10_yeonsan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_gaegeum_int_exp = PM10_gaegeum_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_jeonpo_int_exp = PM10_jeonpo_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_daeshin_int_exp = PM10_daeshin_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_sujeong_int_exp = PM10_sujeong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_choryang_int_exp = PM10_choryang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_bsnharbor_int_exp = PM10_bsnharbor_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_gwangbok_int_exp = PM10_gwangbok_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_cheonghak_int_exp = PM10_cheonghak_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_taejongdae_int_exp = PM10_taejongdae_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_daeyeon_int_exp = PM10_daeyeon_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_gwangan_int_exp = PM10_gwangan_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_jaesong_int_exp = PM10_jaesong_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_left_int_exp = PM10_left_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_yongsuri_int_exp = PM10_yongsuri_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")
PM10_gijang_int_exp = PM10_gijang_int.select_one("body > div.Pd10 > table > tbody > tr:nth-child(3) > td")

def weather():
    print("---------------------------------------------------------------------------------------------")
    print(str(nowdatetime) + " 현재 부산지방 기온은 " + str(kma_int_temp.string) + "℃, 습도는 " + str(
        kma_int_humid.string) + "% 입니다.")
    print(
        "내일 아침 최저기온은 " + str(new_kma_forecast_low.string) + "℃, 낮 최고기온은 " + str(
            new_kma_forecast_high.string) + "℃로 예상됩니다.")
def ok():
    code = input("코드 입력 :")
    if code == "dew7a4b06cA":
        pass
    else:
        print("올바르지 않은 코드입니다. 다시 입력해주세요.")


def air_info():
    print("---------------------------------------------------------------------------------------------")
    print("실시간 미세먼지 현황판입니다. 부산지역 미세먼지 감시 기계는 아래 지역에 설치되어 있습니다.")
    print("   녹산, 대저, 부산신항, 화명, 덕천, 덕포, 학장, 당리, 장림, 종합터미널, 부곡, 온천, 명장, 연산, 개금, 전포")
    print("   대신, 수정, 초량, 부산북항, 광복, 청학, 태종대, 대연, 광안, 재송, 좌동, 용수리, 기장")
    print()

def menu():
    print("원하는 지역을 입력해주세요.")
    spot = input("지점 입력: ")
    if spot == "녹산":
        print("미세먼지(PM10: )" + str(PM10_noksan_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_noksan_int_exp.string))
    elif spot == "대저":
        print("미세먼지(PM10: )" + str(PM10_Daejeo_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_Daejeo_int_exp.string))
    elif spot == "부산신항":
        print("미세먼지(PM10: )" + str(PM10_bsharbor_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_bsharbor_int_exp.string))
    elif spot == "화명":
        print("미세먼지(PM10: )" + str(PM10_hwamyeong_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_hwamyeong_int_exp.string))
    elif spot == "덕천":
        print("미세먼지(PM10: )" + str(PM10_deokcheon_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_deokcheon_int_exp.string))
    elif spot == "덕포":
        print("미세먼지(PM10: )" + str(PM10_deokpo_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_deokpo_int_exp.string))
    elif spot == "학장":
        print("미세먼지(PM10: )" + str(PM10_hakjang_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_hakjang_int_exp.string))
    elif spot == "당리":
        print("미세먼지(PM10: )" + str(PM10_dangri_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_dangri_int_exp.string))
    elif spot == "장림":
        print("미세먼지(PM10: )" + str(PM10_jangrim_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_jangrim_int_exp.string))
    elif spot == "종합터미널":
        print("미세먼지(PM10: )" + str(PM10_cheongryong_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_cheongryong_int_exp.string))
    elif spot == "부곡":
        print("미세먼지(PM10: )" + str(PM10_bugok_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_bugok_int_exp.string))
    elif spot == "온천":
        print("미세먼지(PM10: )" + str(PM10_oncheon_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_oncheon_int_exp.string))
    elif spot == "명장":
        print("미세먼지(PM10: )" + str(PM10_myeongjang_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_myeongjang_int_exp.string))
    elif spot == "연산":
        print("미세먼지(PM10: )" + str(PM10_yeonsan_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_yeonsan_int_exp.string))
    elif spot == "개금":
        print("미세먼지(PM10: )" + str(PM10_gaegeum_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_gaegeum_int_exp.string))
    elif spot == "전포":
        print("미세먼지(PM10: )" + str(PM10_jeonpo_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_jeonpo_int_exp.string))
    elif spot == "대신":
        print("미세먼지(PM10: )" + str(PM10_daeshin_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_daeshin_int_exp.string))
    elif spot == "수정":
        print("미세먼지(PM10: )" + str(PM10_sujeong_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_sujeong_int_exp.string))
    elif spot == "초량":
        print("미세먼지(PM10: )" + str(PM10_choryang_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_choryang_int_exp.string))
    elif spot == "부산북항":
        print("미세먼지(PM10: )" + str(PM10_bsnharbor_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_bsnharbor_int_exp.string))
    elif spot == "광복":
        print("미세먼지(PM10: )" + str(PM10_gwangbok_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_gwangbok_int_exp.string))
    elif spot == "청학":
        print("미세먼지(PM10: )" + str(PM10_cheonghak_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_cheonghak_int_exp.string))
    elif spot == "태종대":
        print("미세먼지(PM10: )" + str(PM10_taejongdae_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_taejongdae_int_exp.string))
    elif spot == "대연":
        print("미세먼지(PM10: )" + str(PM10_daeyeon_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_daeyeon_int_exp.string))
    elif spot == "광안":
        print("미세먼지(PM10: )" + str(PM10_gwangan_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_gwangan_int_exp.string))
    elif spot == "재송":
        print("미세먼지(PM10: )" + str(PM10_jaesong_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_jaesong_int_exp.string))
    elif spot == "좌동":
        print("미세먼지(PM10: )" + str(PM10_left_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_left_int_exp.string))
    elif spot == "용수리":
        print("미세먼지(PM10: )" + str(PM10_yongsuri_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_yongsuri_int_exp.string))
    elif spot == "기장":
        print("미세먼지(PM10: )" + str(PM10_gijang_int_exp.string));
        print("초미세먼지(PM2.5: )" + str(PM25_gijang_int_exp.string))
    else :
        print("잘못된 값입니다. 다시 입력해 주세요.")
weather()
air_info()
while True: menu()