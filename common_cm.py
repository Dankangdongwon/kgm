import socket
import re

def start_client_cm(message, sip, sport):
    # 소켓 객체 생성 (IPv4, TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 IP 주소와 포트 번호
    server_address = (sip, sport)

    # 서버에 연결 시도
    client_socket.connect(server_address)
    print(f"connect: {server_address}")

    # 서버로 데이터 송신
    #client_socket.sendall(message.encode('utf-8'))
    client_socket.sendall(message.encode('cp949'))
    print(f"send: {message}")

    response = client_socket.recv(1024).decode('cp949')
    print(f"return message: {response}")

    # 연결 종료
    client_socket.close()
    print("connection closed.")
    return response

def conv_rcv_cm(res):
    original_string = res
    k = count_korean_chars_cm(res)
    if original_string[1] == '4':
        value_size = [4, 4, 2, 12, 20, 20, 4, 100 - k, 14, 10]
    else: value_size = [4, 4, 2, 12, 20, 10, 20, 4, 100 - k, 14, 10]
    
    value_dic = {}
    i = 0
    j = 0

    value_dic['Ver'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    value_dic['MsgLen'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    value_dic['CashGb'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    value_dic['SvcId'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    if original_string[1] == '4':
        value_dic['MchtTrId'] = original_string[i:i+value_size[j]]
        i = i + value_size[j]
        j = j + 1
        value_dic['MobilId'] = original_string[i:i+value_size[j]]
        i = i + value_size[j]
        j = j + 1
    else:
        value_dic['MchtTrId'] = original_string[i:i+value_size[j]]
        i = i + value_size[j]
        j = j + 1
        value_dic['PrdtPrice'] = original_string[i:i+value_size[j]]
        i = i + value_size[j]
        j = j + 1
        value_dic['CnclMchtTrId'] = original_string[i:i+value_size[j]]
        i = i + value_size[j]
        j = j + 1
    value_dic['ResultCD'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    value_dic['ResultMsg'] = original_string[i:i+value_size[j]].strip()
    #i = i - k
    i = i + value_size[j]
    j = j + 1
    value_dic['ActDate'] = original_string[i:i+value_size[j]]
    i = i + value_size[j]
    j = j + 1
    value_dic['Filler'] = original_string[i:i+value_size[j]]
    for key, value in value_dic.items():
        print(f'{key}: {value}')
    return value_dic

def count_korean_chars_cm(text):
    korean_chars = re.findall(r'[\u3131-\u3163\uac00-\ud7a3]+', text)
    count = 0
    for char in korean_chars:
        count += len(char)
    return count
