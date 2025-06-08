import streamlit as st

def recycling_bot(user_input):
        user_input = user_input.lower()

        if "페트병" in user_input or "플라스틱 뚜껑" in user_input:
            return "페트병은 라벨을 제거하고 플라스틱으로 분리하세요. 뚜껑은 플라스틱 전용으로 따로 분리해 주세요."
        elif "종이컵" in user_input:
            return "내용물을 비우고 플라스틱 코팅 여부에 따라 종이나 일반쓰레기로 분리하세요."
        elif "캔" in user_input:
            return "캔은 내용물을 비우고 금속류로 분리하세요."
        elif "음식물" in user_input:
            return "음식물 쓰레기와 일반 쓰레기를 구분해서 처리해주세요."
        elif "닭갈비" in user_input or "호두껍질" in user_input or "조개껍질" in user_input:
            return "조개껍질, 호두, 닭갈비 등은 음식물 쓰레기로 처리되지 않으므로 일반쓰레기로 버려야 합니다."
        elif "치킨 뼈" in user_input or "생선 뼈" in user_input or "과일 씨" in user_input:
            return "치킨 뼈, 생선 뼈, 과일 씨 등은 음식물 쓰레기로 분류되지 않으므로 일반쓰레기로 버려야 합니다."
        elif "김치" in user_input:
            return "김치는 음식물 쓰레기지만 국물 없이 건더기만 버려야 하며, 익지 않은 상태태면 일반쓰레기로 버려야 해요."
        elif "라면 봉지" in user_input or "과자 봉지" in user_input:
            return "라면/과자 봉지는 대부분 비닐(플라스틱)로, 안쪽을 깨끗이 헹구어 비닐류로 분리하세요."
        elif "피자박스" in user_input:
            return "깨끗한 피자박스는 종이로 재활용 가능하지만, 기름이나 치즈 등으로 오염됐다면 일반쓰레기로 버려야 해요."
        elif "유리컵" in user_input or "깨진 유리" in user_input:
            return "깨진 유리컵은 일반 유리병과 달라 재활용이 불가하므로 신문지 등에 감싸 일반쓰레기로 버리세요."
        elif "일회용 종이컵" in user_input:
            return "일회용 종이컵은 내부 플라스틱 코팅 때문에 종이로 재활용이 어렵습니다. 깨끗하면 일부 지역에서 종이로 분리 가능해요."
        elif "영수증" in user_input:
            return "영수증은 대부분 감열지로, 화학 코팅되어 있어 재활용이 안 되므로 일반쓰레기로 버리세요."
        elif "휴지" in user_input or "키친타올" in user_input:
            return "사용한 휴지나 키친타올은 재활용이 어려워 일반쓰레기로 버리세요. 단, 깨끗한 키친타올은 종이로 분리 가능해요."
        else:
            return "죄송해요, 해당 품목은 아직 학습되지 않았어요."

st.title("♻️ 분리수거 챗봇: 쓰까비")
user_input = st.text_input("무엇을 버릴지 입력해 주세요:")
if user_input:
        response = recycling_bot(user_input)
        st.write("🤖", response)
