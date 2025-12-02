import random
import copy
import sys
sys.setrecursionlimit(10000)

# ------------------------------------------------------------
# 2026 팀 목록 + 포트 배정
# (실제 48개국 가정 기반 — 필요 시 원하는 팀으로 교체 가능)
# ------------------------------------------------------------

pot1 = [
    "USA", "Mexico", "Canada",
    "Argentina", "Brazil", "France",
    "England", "Portugal", "Spain",
    "Germany", "Belgium", "Croatia"
]

pot2 = [
    "Korea Republic", "Netherlands", "Japan",
    "Switzerland", "Denmark", "Uruguay",
    "Colombia", "Morocco", "Austria",
    "Serbia", "Ukraine", "Senegal"
]

pot3 = [
    "Chile", "Nigeria", "Australia",
    "Ecuador", "Sweden", "Poland",
    "Cameroon", "Turkey", "Qatar",
    "Czech Republic", "Algeria", "Iran"
]

pot4 = [
    "South Africa", "New Zealand", "Honduras",
    "Panama", "Saudi Arabia", "Egypt",
    "Tunisia", "Costa Rica", "Paraguay",
    "Peru", "UAE", "Ghana"
]

pots = [pot1, pot2, pot3, pot4]

# ------------------------------------------------------------
# 대륙 정보
# ------------------------------------------------------------
continent = {
    # Pot 1
    "USA":"CONCACAF","Mexico":"CONCACAF","Canada":"CONCACAF",
    "Argentina":"CONMEBOL","Brazil":"CONMEBOL","France":"UEFA",
    "England":"UEFA","Portugal":"UEFA","Spain":"UEFA",
    "Germany":"UEFA","Belgium":"UEFA","Croatia":"UEFA",

    # Pot 2
    "Korea Republic":"AFC","Netherlands":"UEFA","Japan":"AFC",
    "Switzerland":"UEFA","Denmark":"UEFA","Uruguay":"CONMEBOL",
    "Colombia":"CONMEBOL","Morocco":"CAF","Austria":"UEFA",
    "Serbia":"UEFA","Ukraine":"UEFA","Senegal":"CAF",

    # Pot 3
    "Chile":"CONMEBOL","Nigeria":"CAF","Australia":"AFC",
    "Ecuador":"CONMEBOL","Sweden":"UEFA","Poland":"UEFA",
    "Cameroon":"CAF","Turkey":"UEFA","Qatar":"AFC",
    "Czech Republic":"UEFA","Algeria":"CAF","Iran":"AFC",

    # Pot 4
    "South Africa":"CAF","New Zealand":"OFC","Honduras":"CONCACAF",
    "Panama":"CONCACAF","Saudi Arabia":"AFC","Egypt":"CAF",
    "Tunisia":"CAF","Costa Rica":"CONCACAF","Paraguay":"CONMEBOL",
    "Peru":"CONMEBOL","UAE":"AFC","Ghana":"CAF"
}

groups = list("ABCDEFGHIJKL")  # 12 groups


# ------------------------------------------------------------
# 대륙 제약 검사
# ------------------------------------------------------------
def is_valid(group_team_list, team):
    team_cont = continent[team]

    # 1) 조가 이미 4팀이면 불가
    if len(group_team_list) >= 4:
        return False

    # 2) UEFA는 조당 2명까지 허용
    if team_cont == "UEFA":
        uefa_count = sum(continent[t] == "UEFA" for t in group_team_list)
        if uefa_count >= 2:
            return False

    # 3) 기타 대륙은 조당 1명만 허용 (UEFA 제외)
    if team_cont != "UEFA":
        for t in group_team_list:
            if continent[t] == team_cont:
                return False

    return True


# ------------------------------------------------------------
# 백트래킹 기반 조추첨
# ------------------------------------------------------------
def assign_from_pot(pot_idx, pots, result, team_idx=0):
    if pot_idx == len(pots):
        return True  # 완료

    pot = pots[pot_idx]

    if team_idx == len(pot):
        # 다음 포트로 이동
        return assign_from_pot(pot_idx + 1, pots, result, 0)

    team = pot[team_idx]
    random.shuffle(groups)  # 무작위 그룹 순서

    for g in groups:
        if is_valid(result[g], team):
            result[g].append(team)

            if assign_from_pot(pot_idx, pots, result, team_idx + 1):
                return True

            # 실패 → 백트래킹
            result[g].remove(team)

    return False


# ------------------------------------------------------------
# 전체 조추첨 함수
# ------------------------------------------------------------
def draw_worldcup():
    while True:
        result = {g: [] for g in groups}
        if assign_from_pot(0, pots, result, 0):
            return result
        # 실패시는 자동으로 다시 시도


# ------------------------------------------------------------
# 실행 및 출력
# ------------------------------------------------------------
def print_groups(result):
    print("\n===== 2026 월드컵 조추첨 결과 =====\n")
    for g in groups:
        print(f"Group {g}:")
        for t in result[g]:
            print(f"  - {t} ({continent[t]})")
        print()


if __name__ == "__main__":
    result = draw_worldcup()
    print_groups(result)
