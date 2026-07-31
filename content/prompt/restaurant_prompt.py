RESTAURANT_SYSTEM_PROMPT = """
너는 네이버 블로그 음식점 리뷰 전문 작가다.

사용자가 제공한 방문 경험을 기반으로
자연스럽고 읽기 좋은 블로그 글을 작성한다.

조건:

- 실제 방문자가 작성한 것처럼 자연스럽게 작성한다.
- 과장된 광고 표현은 사용하지 않는다.
- 음식의 특징과 경험 중심으로 작성한다.
- 검색 노출을 고려하되 키워드를 억지로 반복하지 않는다.
- 적절한 소제목을 사용한다.
- 사진이 들어갈 위치를 고려한다.
"""


def build_restaurant_prompt(data: dict) -> str:

    return f"""
{RESTAURANT_SYSTEM_PROMPT}


아래 방문 정보를 기반으로 글을 작성해.


[방문 정보]

가게명:
{data.get("store_name")}

지역:
{data.get("location")}

방문 날짜:
{data.get("visit_date")}


[방문 경험]

방문 인원:
{data.get("companion")}

웨이팅:
{data.get("waiting")}

방문 시간:
{data.get("visit_time")}


[주문]

메뉴:
{data.get("menu")}

가격:
{data.get("price")}


[후기]

음식:
{data.get("food")}

분위기:
{data.get("atmosphere")}

서비스:
{data.get("service")}


좋았던 점:
{data.get("good")}

아쉬웠던 점:
{data.get("bad")}


[마무리]

재방문 의사:
{data.get("revisit")}

추천 대상:
{data.get("recommend")}

사진 메모:
{data.get("photo_note")}
"""