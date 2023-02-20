import speedtest
import time

st = speedtest.Speedtest()
st.get_best_server()

st_ping = st.results.ping
st_download = round(st.download() / 1000 / 1000, 1)
st_upload = round(st.upload() / 1000 / 1000, 1)

print(f"Download {st_download}")
print(f"Upload {st_upload}")
print(f"Ping {st_ping}")
