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

def get_reason(MyTeam, CoWorkTeam, CoffeePrice, UnitPrice):
    if MyTeam == 'PGDEV':
        member_list = ['김규성','강동원', '안지은', '이재우', '황지산', '김지현']
    elif MyTeam == 'SVCOP':
        member_list = ['장치암','이창현', '김지현', '오유진', '황휘람', '안인택', '김영수']
    elif MyTeam == 'DB':    
        member_list = ['박선희','김문성', '장사라']
    elif MyTeam == 'INFRA':
        member_list = ['전상호','양동국', '허정호', '박상한', '이두한', '배동규', '이재철', '류아란', '조은이']

    if CoWorkTeam == 'PGDEV':
        cowork_mem_list = ['김규성','강동원', '안지은', '이재우', '황지산', '김지현']
    elif CoWorkTeam == 'SVCOP':
        cowork_mem_list = ['장치암','이창현', '김지현', '오유진', '황휘람', '안인택', '김영수']
    elif CoWorkTeam == 'DB':    
        cowork_mem_list = ['박선희','김문성', '장사라']
    elif CoWorkTeam == 'INFRA':
        cowork_mem_list = ['전상호','양동국', '허정호', '박상한', '이두한', '배동규', '이재철', '류아란', '조은이']
    elif CoWorkTeam == 'MyTeamOnly':
        cowork_mem_list = []
    CoffeeCount = ceil(CoffeePrice/UnitPrice) - 1
    if CoffeeCount > len(member_list) + len(cowork_mem_list):
        CoffeeCount = len(member_list)+ len(cowork_mem_list)
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
    else:
        print('사유: ' + sample(CoWorkReason,1)[0])
