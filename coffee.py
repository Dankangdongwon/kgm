from random import sample
from math import ceil
CoffeReason = ['프로젝트 진행 상황을 논의.', \
            '아이디어를 도출하기 위해 브레인스토밍.', \
            '프로젝트의 목표를 설정.', \
            '팀원들에게 업무 관련 교육을 제공.', \
            '업무 성과에 대해 피드백.', \
            '프로젝트 계획을 수립.', \
            '팀원들에게 업무 관련 교육을 제공.', \
            '신규 팀원을 멘토링.', \
            '팀의 유대감을 강화.', \
            '프로젝트의 문제를 해결하기 위해 논의.', \
            '조사한 자료를 팀원들과 공유.', \
            '팀원의 업무 성과를 평가.', \
            '업무 일정을 조정.', \
            '기술적 문제를 토론.', \
            '혁신적인 아이디어를 논의.', \
            '프로젝트 진행 상황을 리뷰.', \
            '팀 내 업무 역할을 분담.', \
            '분석 결과를 공유.', \
            '시장 동향을 분석.', \
            '향후 목표를 설정.', \
            '협업 방안을 논의.', \
            '자원 배분 계획을 세웠다.', \
            '위기 상황에 대응 방안을 마련.', \
            '고객의 의견을 공유.', \
            '성과 목표를 설정.', \
            '서비스 개발에 대해 논의.', \
            '비용 절감 방안을 마련.', \
            '인력 충원 계획 수립.', \
            '성과 결과를 보고.', \
            '시장 트렌드를 분석.', \
            '고객 관계를 강화.', \
            '팀의 성과를 평가.', \
            '서비스 개선 방안을 논의.', \
            '서비스 품질을 향상 논의.', \
            '내부 소통을 강화.', \
            '회의 자료를 준비.']

CoWorkReason = ['협력 프로젝트의 계획을 수립.', \
                '부서 간 목표를 조율.', \
                '자원 공유 방안을 협의.', \
                '공동 연구 주제를 논의.', \
                '프로세스 개선 방안을 논의.', \
                '인력 교환 방안을 협의.', \
                '공동 마케팅 전략을 수립.', \
                '기술 이전에 대해 협상.', \
                '시장 확장 계획을 논의.', \
                '공동 고객 관리 방안을 협의.', \
                '리소스 최적화 방안을 논의.', \
                '경쟁 분석 결과를 공유.', \
                '리스크 관리 방안을 논의.', \
                '프로젝트 우선순위를 설정.', \
                '정보 보안 강화 방안을 논의.', \
                '크로스 트레이닝 계획을 수립.', \
                '지식 공유 세션을 진행.', \
                '통합 보고서를 작성.', \
                '서비스 통합 방안을 논의.', \
                '공동 예산 계획을 수립.', \
                '벤치마킹 방안을 협의.', \
                '부서 간 충돌 해결 방안을 논의.', \
                '공동 이벤트 계획을 .', \
                '고객 만족도 조사 결과를 논의.', \
                '통합 마케팅 캠페인을 계획.', \
                '다양성 및 포용성 전략을 논의.', \
                '공동 리더십 훈련 계획을 .', \
                '사업 확장 방안을 논의.', \
                '기술 협력 방안을 강화.', \
                '공동 브랜드 전략을 수립.', \
                '프로젝트 성과를 리뷰.', \
                '글로벌 진출 전략을 논의.', \
                '공동 제품 개발 계획.', \
                '서비스 품질 개선 방안을 논의.', \
                '고객 서비스 통합 방안을 협의.', \
                '지속 가능성 프로젝트를 계획.', \
                '비즈니스 연속성 계획을 수립.', \
                '합작 투자 방안을 논의.', \
                '디지털 전환 전략을 논의.', \
                '혁신 이니셔티브를 계획.']

CoWorkReason_svcop = ['소프트웨어 테스트 계획을 논의.', \
                        '버그 보고서 내용을 공유.', \
                        '테스트 케이스 작성 방안을 협의.', \
                        '테스트 자동화 도구를 논의.', \
                        '품질 보증 프로세스를 개선.', \
                        '성능 테스트 결과를 공유.', \
                        '신규 기능의 테스트 전략을 수립.', \
                        '운영 중인 시스템의 안정성을 점검.', \
                        '장애 대응 계획을 논의.', \
                        '서비스 레벨 협약(SLA)을 검토.', \
                        '배포 일정 조율을 논의.', \
                        '운영 이슈를 해결하기 위한 방안을 협의.', \
                        'QA와 운영 간의 커뮤니케이션 프로세스를 개선.', \
                        '릴리스 노트를 작성.', \
                        '회귀 테스트 계획을 수립.', \
                        '사용자 피드백을 QA 팀과 공유.', \
                        '시스템 모니터링 도구를 검토.', \
                        '데이터 백업 전략을 논의.', \
                        '운영 환경의 변경 사항을 검토.', \
                        '품질 지표를 설정하고 분석.', \
                        'QA 테스트 환경을 구성.', \
                        '운영 절차를 표준화.', \
                        '비상 대응 시나리오를 논의.', \
                        '성능 최적화 방안을 협의.', \
                        '운영 리포트를 작성.', \
                        '데이터 무결성 검사를 논의.', \
                        '배포 후 검증 절차를 수립.', \
                        '테스트 커버리지를 확대.', \
                        '보안 테스트 계획을 논의.', \
                        '시스템 업타임을 유지하기 위한 방안을 협의.', \
                        '사용자 교육 자료를 준비.', \
                        '신규 시스템의 운영 매뉴얼을 작성.', \
                        '테스트 결과를 운영팀과 공유.', \
                        '시스템 로그 분석 방법을 논의.', \
                        '운영팀의 피드백을 반영한 QA 개선안을 마련.', \
                        '시스템 복구 테스트를 계획.', \
                        '신규 프로젝트의 QA 및 운영 요구 사항을 논의.', \
                        '테스트 결과에 따른 수정 사항을 협의.']

CoWorkReason_db = ['데이터베이스 아키텍처를 설계.', \
                        '쿼리 최적화 방안을 논의.', \
                        '데이터 백업 전략을 검토.', \
                        '데이터 마이그레이션 계획을 논의.', \
                        '데이터 무결성 검사 방법을 논의.', \
                        '성능 모니터링 도구를 검토.', \
                        '데이터베이스 보안 방안을 협의.', \
                        '장애 복구 시나리오를 계획.', \
                        '스토리지 용량 관리를 논의.', \
                        '데이터 모델링 기법을 공유.', \
                        '인덱스 최적화 방안을 논의.', \
                        '쿼리 성능 분석 결과를 공유.', \
                        '새로운 데이터베이스 기술을 검토.', \
                        '데이터 아카이빙 전략을 협의.', \
                        '데이터베이스 스키마 변경 계획을 수립.', \
                        '자동화된 백업 및 복구 절차를 논의.', \
                        '데이터베이스 접근 제어 방안을 검토.', \
                        '데이터베이스 로그 관리 방안을 논의.', \
                        '트랜잭션 관리 최적화 방안을 협의.', \
                        '데이터베이스 클러스터링 전략을 검토.', \
                        '레플리케이션 설정을 논의.', \
                        '데이터베이스 업그레이드 계획을 논의.', \
                        '데이터 정규화 방법을 검토.', \
                        '데이터베이스 모니터링 지표를 설정.', \
                        '데이터베이스 사용량 보고서를 작성.', \
                        '대규모 데이터 처리 방안을 논의.', \
                        '데이터베이스 통합 계획을 협의.', \
                        '데이터베이스 환경 설정을 검토.', \
                        '테스트 데이터 준비 방안을 논의.', \
                        '데이터 보존 정책을 협의.', \
                        '데이터베이스 장애 대응 방안을 논의.', \
                        '실시간 데이터 처리 방안을 검토.', \
                        '데이터베이스 서버 자원 관리를 협의.', \
                        '데이터베이스 성능 테스트 결과를 공유.', \
                        '데이터베이스 자동화 스크립트를 작성.', \
                        '데이터베이스 감사 로그 설정을 논의.', \
                        '데이터베이스 복제 전략을 검토.', \
                        '데이터베이스 캐시 관리 방안을 협의.', \
                        '데이터베이스 유지보수 계획을 논의.', \
                        '데이터베이스와 애플리케이션 간의 통합 방안을 논의.']

CoWorkReason_infra = ['네트워크 보안 정책을 검토.', \
                        '침입 탐지 시스템을 설정.', \
                        '보안 취약점 스캔 결과를 공유.', \
                        '방화벽 규칙을 업데이트.', \
                        '데이터 암호화 방안을 논의.', \
                        '접근 제어 정책을 수립.', \
                        '보안 로그 분석 방법을 논의.', \
                        '보안 사고 대응 절차를 검토.', \
                        '다중 인증 시스템을 설정.', \
                        '보안 감사 계획을 논의.', \
                        '피싱 방지 교육을 기획.', \
                        '보안 패치 관리 방안을 협의.', \
                        'DDoS 공격 대응 전략을 논의.', \
                        '보안 인시던트 대응 훈련을 계획.', \
                        'VPN 설정을 검토.', \
                        '보안 이벤트 모니터링 도구를 설정.', \
                        '데이터 유출 방지(DLP) 전략을 논의.', \
                        '서버 보안 설정을 점검.', \
                        '클라우드 보안 정책을 수립.', \
                        '위협 모델링을 수행.', \
                        '최신 보안 트렌드를 공유.', \
                        '보안 규정 준수 상태를 검토.', \
                        '보안 기술 도입을 논의.', \
                        '모바일 기기 보안 방안을 협의.', \
                        '악성 코드 분석 결과를 공유.', \
                        '보안 경고 시스템을 설정.', \
                        '백업 및 복구 전략을 논의.', \
                        '사용자 권한 관리를 검토.', \
                        '보안 인프라 성능을 평가.', \
                        '물리적 보안 방안을 논의.', \
                        'SSL/TLS 인증서를 관리.', \
                        '이메일 보안 설정을 검토.', \
                        '보안 정책 위반 사례를 분석.', \
                        'IoT 보안 전략을 논의.', \
                        '취약점 관리 프로그램을 검토.', \
                        '컴플라이언스 요구 사항을 논의.', \
                        '데이터베이스 보안 강화를 협의.', \
                        '로그 관리 정책을 검토.', \
                        '악성 트래픽 분석 결과를 공유.', \
                        '보안 시스템 업데이트 계획을 논의.']

CoWorkReason_pgdev = ['API 설계 방안을 논의.', \
                        '데이터베이스 스키마 변경을 협의.', \
                        '성능 최적화 방안을 검토.', \
                        '코드 리뷰 피드백을 공유.', \
                        '새로운 프레임워크 도입을 논의.', \
                        '마이크로서비스 아키텍처를 설계.', \
                        '서버 로드 밸런싱 전략을 협의.', \
                        '캐싱 전략을 논의.', \
                        '백엔드 테스트 계획을 수립.', \
                        '배포 자동화 도구를 검토.', \
                        '보안 취약점을 분석.', \
                        '로그 관리 방안을 협의.', \
                        '에러 모니터링 시스템을 설정.', \
                        'RESTful API 표준을 검토.', \
                        'CI/CD 파이프라인을 구축.', \
                        '데이터 이행 계획을 논의.', \
                        '서비스 장애 대응 전략을 마련.', \
                        '클라우드 인프라 설정을 협의.', \
                        '기술 부채 관리 방안을 논의.', \
                        '스케일링 전략을 검토.', \
                        '새로운 기능 구현 방안을 협의.', \
                        '코드베이스 리팩토링을 계획.', \
                        '백엔드 로드 테스트 결과를 공유.', \
                        'API 문서화를 협의.', \
                        '서버 보안 설정을 검토.', \
                        '서비스 연동 방안을 논의.', \
                        '지속적인 통합 전략을 협의.', \
                        '로그 분석 도구를 검토.', \
                        '서버 자원 최적화 방안을 논의.', \
                        '메시지 큐 사용 방안을 협의.', \
                        '데이터 동기화 전략을 검토.', \
                        '서버 배포 전략을 논의.', \
                        '서버 상태 모니터링 계획을 수립.', \
                        '데이터 백업 및 복구 방안을 협의.', \
                        '서버 환경 설정을 논의.', \
                        '새로운 기술 스택 도입을 검토.', \
                        '서비스 상태 확인 도구를 설정.', \
                        '코드 성능 분석 결과를 공유.', \
                        '데이터베이스 쿼리 최적화 방안을 논의.', \
                        '시스템 업타임을 유지하기 위한 방안을 협의.']

CoWorkReason_paydev = ['결제 처리 시스템을 설계.', \
                        '정산 프로세스 자동화 방안을 논의.', \
                        '데이터 정확성 검증 방안을 협의.', \
                        '거래 기록 저장 구조를 검토.', \
                        '새로운 결제 게이트웨이 통합을 논의.', \
                        '정산 주기 최적화 방안을 검토.', \
                        '재무 보고서 생성 자동화를 협의.', \
                        '보안 결제 시스템을 설계.', \
                        '환불 처리 시스템을 논의.', \
                        '세금 계산 모듈을 검토.', \
                        '결제 오류 해결 절차를 협의.', \
                        '실시간 정산 시스템을 설계.', \
                        '통화 변환 로직을 논의.', \
                        '사용자 결제 이력 조회 기능을 검토.', \
                        '결제 알림 시스템을 협의.', \
                        '수익 분배 알고리즘을 논의.', \
                        '결제 시스템의 성능 최적화를 검토.', \
                        '고객 청구서 자동 생성 방안을 협의.', \
                        '정산 데이터 백업 전략을 논의.', \
                        '결제 시스템 모니터링 도구를 검토.', \
                        '정산 보고서 포맷을 협의.', \
                        '다중 통화 지원 방안을 논의.', \
                        '정산 데이터베이스 설계를 검토.', \
                        '외부 결제 API 통합을 협의.', \
                        '월말 정산 절차를 논의.', \
                        '고객 포인트 적립 시스템을 검토.', \
                        '매출 데이터 분석 방안을 협의.', \
                        '지불 승인 로직을 논의.', \
                        '정산 시스템 로그 관리를 검토.', \
                        '보안 결제 인증 절차를 협의.', \
                        '정산 주기 알림 시스템을 논의.', \
                        '결제 내역 오류 검출 방안을 검토.', \
                        '비용 분배 모델을 협의.', \
                        '결제 데이터 암호화 방안을 논의.', \
                        '재무 시스템 통합을 검토.', \
                        '정산 데이터의 실시간 동기화를 협의.', \
                        '정산 프로세스의 테스트 계획을 논의.', \
                        '다양한 결제 방법 지원 방안을 검토.', \
                        '대시보드 설계를 협의.', \
                        '결제 시스템의 규정 준수 상태를 논의.']

def get_reason(MyTeam, CoWorkTeam, CoffeePrice, UnitPrice):
    if MyTeam == 'PGDEV':
        member_list = ['김규성','강동원', '안지은', '이재우', '황지산', '김지현']
    elif MyTeam == 'SVCOP':
        member_list = ['장치암','이창현', '김지현', '오유진', '황휘람', '안인택', '김영수']
    elif MyTeam == 'DB':    
        member_list = ['박선희','김문성', '장사라']
    elif MyTeam == 'INFRA':
        member_list = ['전상호','양동국', '허정호', '박상한', '이두한', '배동규', '이재철', '류아란', '조은이']
    elif MyTeam == 'PAYDEV':
        member_list = ['문현식','김선애', '박주일', '정광민']

    if CoWorkTeam == 'PGDEV':
        cowork_mem_list = ['김규성','강동원', '안지은', '이재우', '황지산', '김지현']
    elif CoWorkTeam == 'SVCOP':
        cowork_mem_list = ['장치암','이창현', '김지현', '오유진', '황휘람', '안인택', '김영수']
    elif CoWorkTeam == 'DB':    
        cowork_mem_list = ['박선희','김문성', '장사라']
    elif CoWorkTeam == 'INFRA':
        cowork_mem_list = ['전상호','양동국', '허정호', '박상한', '이두한', '배동규', '이재철', '류아란', '조은이']
    elif CoWorkTeam == 'PAYDEV':
        cowork_mem_list = ['문현식','김선애', '박주일', '정광민']
    elif CoWorkTeam == 'MyTeamOnly':
        cowork_mem_list = []
    CoffeeCount = ceil(CoffeePrice/UnitPrice) - 1
    if CoffeeCount > len(member_list)-1 + len(cowork_mem_list):
        CoffeeCount = len(member_list)-1 + len(cowork_mem_list)
    if len(cowork_mem_list) > 0:
        CoffeeCount_my = ceil(CoffeeCount/2)
        CoffeeCount_co = CoffeeCount - CoffeeCount_my
    else:
        CoffeeCount_my = CoffeeCount
        CoffeeCount_co = 0
    Attendee = sample(member_list[1:], CoffeeCount_my)
    print(f'참석자: {member_list[0]} ', end='')
    for att in Attendee:
        print(att, end=' ')
    if CoffeeCount_co > 0:
        Attendee = sample(cowork_mem_list, CoffeeCount_co)
        for att in Attendee:
            print(att, end=' ')
    print('\n')
    if CoffeeCount_co == 0:
        print('사유: ' + sample(CoffeReason,1)[0])
    elif CoWorkTeam == 'SVCOP':
        print('사유: ' + sample(CoWorkReason_svcop,1)[0])
    elif CoWorkTeam == 'DB':
        print('사유: ' + sample(CoWorkReason_db,1)[0])
    elif CoWorkTeam == 'INFRA':
        print('사유: ' + sample(CoWorkReason_infra,1)[0])
    elif CoWorkTeam == 'PGDEV':
        print('사유: ' + sample(CoWorkReason_pgdev,1)[0])
    elif CoWorkTeam == 'PAYDEV':
        print('사유: ' + sample(CoWorkReason_paydev,1)[0])
    else:
        print('사유: ' + sample(CoWorkReason,1)[0])
