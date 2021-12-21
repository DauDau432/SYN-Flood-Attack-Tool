# Python2/3-SYN-Flood-Attack-Tool

[![](https://img.shields.io/github/issues/EmreOvunc/Python-SYN-Flood-Attack-Tool)](https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool/issues)
[![](https://img.shields.io/github/stars/EmreOvunc/Python-SYN-Flood-Attack-Tool)](https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool/stargazers)
[![](https://img.shields.io/github/forks/EmreOvunc/Python-SYN-Flood-Attack-Tool)](https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool/network/members)

Công cụ tấn công lũ lụt Python SYN

Bạn có thể bắt đầu cuộc tấn công SYN Flood bằng công cụ này.

Đơn giản và hiệu quả.

## Sự phụ thuộc
```
apt install python-scapy
apt install python3-scapy
```

## Cài đặt

```
git clone https://github.com/DauDau432/SYN-Flood-Attack-Tool
cd SYN-Flood-Attack-Tool
```

## Cách sử dụng

```
python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 5
python3 py3_SYN-Flood.py
python SYN-Flood.py
```
```
cách sử dụng: py3_synflood_cmd.py [--help] [--target TARGET] [--port PORT]
                           [--count COUNT] [--version]
đối số tùy chọn:
  --help, -h hiển thị thông báo trợ giúp này và thoát
  --target TARGET, -t Mục tiêu
địa chỉ IP mục tiêu
  --port PORT, -p PORT số cổng mục tiêu
  --count COUNT, -c ĐẾM
số lượng gói tin
  --version, -v hiển thị số phiên bản của chương trình và thoát

ví dụ: python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 1
```

![alt tag](https://emreovunc.com/projects/python_synflood_attack_cmd.png)

![alt tag](https://emreovunc.com/projects/Syn_Flood_01.png)

![alt tag](https://emreovunc.com/projects/Syn_Flood_02.png)
