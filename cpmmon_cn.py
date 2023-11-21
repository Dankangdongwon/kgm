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
    value_size = [6,4,4,1,1,20,32,4,75,80,32,20,8,6,50,10,10,1,12,4]
    return i + value_size[j], j + 1

def conv_rcv(res, McashSeed):
    original_string = res
    value_size = [6,4,4,1,1,20,32,4,75,80,32,20,8,6,50,10,10,1,12,4]

    value_dic = {}
    i = 0
    j = 0
    value_dic['Length'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['Type'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['Ver'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['CryptGB'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['KeySeq'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['RecKey'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['SvcId'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['ResultCD'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['ResultMsg'] = original_string[i:i+value_size[j]].strip()    
    i = i + 25 - (count_korean_characters(value_dic['ResultMsg']))
    i,j = ji_calc(i, j)
    value_dic['MrctTrdNo'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['EncPrdtPrice'] = original_string[i:i+value_size[j]]
    value_dic['DecPrdtPrice'] = dec_value(value_dic['EncPrdtPrice'], value_dic['SvcId'], McashSeed)
    i,j = ji_calc(i, j)
    value_dic['TrdNo'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['CnclDt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['CnclTm'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['PtnCnclTrdNo'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['PayMethod'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['CouponPrice'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['PartCnclYn'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['RemainAmt'] = original_string[i:i+value_size[j]]
    i,j = ji_calc(i, j)
    value_dic['PartCnclSeq'] = original_string[i:i+value_size[j]]
    for key, value in value_dic.items():
        print(f'{key}: {value}')
    return value_dic

def enc_value(val, SvcId, McashSeed):
    CryptKey = SvcId[:-4]+SvcId[:-4]
    return str(McashSeed.encodeString(val, CryptKey.encode()))

def dec_value(val, SvcId, McashSeed):
    CryptKey = SvcId[:-4]+SvcId[:-4]
    return str(McashSeed.decodeString(val, CryptKey.encode())).replace('\x00', '')

def count_korean_characters(s):
    count = 0
    for char in s:
        if '가' <= char <= '힣':
            count += 1
    return count
