import socket

def start_client(message, sip, sport):
    # 소켓 객체 생성 (IPv4, TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 IP 주소와 포트 번호
    server_address = (sip, sport)

    # 서버에 연결 시도
    client_socket.connect(server_address)
    print(f"connect: {server_address}")

    # 서버로 데이터 송신
    client_socket.sendall(message.encode('utf-8'))
    print(f"send: {message}")

    response = client_socket.recv(1024).decode('cp949')
    print(f"return message: {response}")

    # 연결 종료
    client_socket.close()
    print("connection closed.")
    return response

def ji_calc(i, j):
    value_size = [4,1,1,2,20,12,40,32,13,14,4,75,20,137]
    return i + value_size[j], j + 1

def conv_rcv(res):
    original_string = res
    value_size = [4,1,1,2,20,12,40,32,13,14,4,75,20,137]

    value_dic = {}
    i = 0
    j = 0
    value_dic['Ver'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['CryptGB'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['KeySeq'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['MsgType'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['RecKey'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['SvcId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['MchtTrId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['PrdtPrice'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['MobilId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['ActDate'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['ResultCD'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    i = i + 25 - (count_korean_characters(value_dic['ResultMsg']))
    i,j = ji_calc(i, j)
    value_dic['AuthCode'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['Filler'] = original_string[i:i+value_size[j]]
    for key, value in value_dic.items():
        print(f'{key}: {value}')
    return value_dic

def enc_value(val, SvcId, McashSeed):
    CryptKey = SvcId[:-4]+SvcId[:-4]
    return str(McashSeed.encodeString(val, CryptKey.encode()))

def dec_value(val, SvcId, McashSeed):
    CryptKey = SvcId[:-4]+SvcId[:-4]
    return str(McashSeed.decodeString(val, CryptKey.encode()))

def ji_calc2(i, j):
    value_size = [4, 1, 1, 2, 2, 20, 12, 3, 50, 32, 1, 8, 4, 75, 15, 6, 15, 14, 10, 1, 1, 1, 15, 1, 1, 1, 20, 10, 10, 2, 20, 10, 50, 10, 47]
    return i + value_size[j], j + 1

def conv_rcv2(res):
    original_string = res
    value_size = [4, 1, 1, 2, 2, 20, 12, 3, 50, 32, 1, 8, 4, 75, 15, 6, 15, 14, 10, 1, 1, 1, 15, 1, 1, 1, 20, 10, 10, 2, 20, 10, 50, 10, 47]

    value_dic = {}
    i = 0
    j = 0

    value_dic['Ver'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['CryptGb'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['KeySeq'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['CashGb'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['MsgType'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['RecKey'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['SvcId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['CommId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['MchtTrId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['PrdtPrice'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['EmailFlag'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['Item'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['ResultCD'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['ResultMsg'] = original_string[i:i+value_size[j]].strip()
    i = i + 25 - (count_korean_characters(value_dic['ResultMsg']))
    i,j = ji_calc2(i, j)
    value_dic['PhoneId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['SmsVal'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['MobilId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['ActDate'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['RemainAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['CopyFlag'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['SafeGuard'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['AnsimFlag'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['AutoBillKey'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['AuthType'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['EventAgree_Yn'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['Wc499_Join_Stat'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['Wc499_Cust_No'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['OrnDcAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['KenDcAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['Filler'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['EasyKey'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['MobDcAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['PacketNo'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['ExcDdcAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc2(i, j)
    value_dic['Filler'] = original_string[i:i+value_size[j]]
    for key, value in value_dic.items():
        print(f'{key}: {value}')
    return value_dic

def count_korean_characters(s):
    count = 0
    for char in s:
        if '가' <= char <= '힣':
            count += 1
    return count
