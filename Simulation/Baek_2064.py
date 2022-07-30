N = int(input())
IP = [[], [], [], []]

for _ in range(N):
    # IP 주소 . 기준으로 자르기
    ip0, ip1, ip2, ip3 = tuple(map(int, input().split('.')))
    IP[0].append(ip0), IP[1].append(ip1), IP[2].append(ip2), IP[3].append(ip3)

net_address = [0, 0, 0, 0]
net_mask = [0, 0, 0, 0]

# 공통 되는 범위 찾기
for i in range(4):
    # 해당 바이트가 공통이라면
    if len(set(IP[i])) == 1:
        # 해당 바이트의 NetworkAddress, NetworkMask 구하기
        # NetworkAddress 해당 바이트의 첫번째 숫자 넣기
        net_address[i] = IP[i][0]
        # NetworkMask 1로 채우기
        net_mask[i] = 255

    # 해당 바이트가 공통이 아니라면
    else:
        # 해당 바이트의 최소, 최대 주소를 구하기
        min_ = min(IP[i])
        max_ = max(IP[i])
        # m : 서로 다른 부분이므로, 최소, 최대 주소의 다른 부분의 길이 (0b를 제외하기 위해 -2를 한다.)
        m = len(bin(min_ ^ max_)) - 2
        # subnet : 공통된 부분을 1로 가득 채워야 하므로, 1 * (8 - m) + 0 * m
        subnet = int('1' * (8 - m) + '0' * m, 2)

        # 네트워크 주소 : 가장 작은 IP 주소에 네트워크 마스크를 & 연산
        net_address[i] = subnet & min_
        # 네트워크 마스크 : subnet
        net_mask[i] = subnet

        break

print('.'.join(tuple(map(str, net_address))))
print('.'.join(tuple(map(str, net_mask))))
