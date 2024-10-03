#질병 및 관련 증상에 대한 지식 베이스 정의
knowledge_base = {
    "감기": {
        "증상": ["발열", "기침", "목 통증"],
        "설명": "감기나 독감일 가능성이 높습니다. 휴식을 취하고 물을 충분히 섭취하세요."
    },
    "뇌수막염": {
        "증상": ["두통", "발열", "구토"],
        "설명": "뇌수막염일 가능성이 있으므로 즉시 의사와 상담하십시오."
    },
    "심장 질환": {
        "증상": ["가슴 통증", "호흡 곤란"],
        "설명": "심장 질환일 가능성이 있으므로 즉시 병원에 방문하십시오."
    },
    "위장염": {
        "증상": ["복통", "설사", "메스꺼움"],
        "설명": "위장염일 가능성이 높습니다. 물을 충분히 마시고 휴식을 취하세요."
    },
    "당뇨병": {
        "증상": ["피로", "체중 감소", "잦은 소변"],
        "설명": "당뇨병 초기 증상일 수 있ㅆ으므로 병원에서 검사를 받아보세요."
    }
}

def diagnose(symptoms):
    #각 질병에 대해 증상과의 일치도를 계산합니다.
    diagnose_scores = {}

    for disease, info in knowledge_base.items():
        matching_symptoms = set(symptoms) & set(info["증상"])
        score = len(matching_symptoms) / len(info["증상"]) #일치 비율 계산
        diagnose_scores[disease] = score

        #가장 높은 점수를 가진 질병을 진단
        best_match = max(diagnose_scores, key=diagnose_scores.get)
        
        #진단 결과 반환
        if diagnose_scores[best_match] > 0:
            return f"[best_match]: {knowledge_base[best_match]['설명']}"
        else:
            return "알 수 없는 증상입니다. 정확한 진단을 위해 병원 방문을 권장합니다."
        
        #사용자가 증상을 입력하는 부분
        print("의료진단 전문가 시스템에 오신 것을 환영합니다.")
        print("아래의 증상 중 해당하는 것을 모두 입력하세요. (입력이 끝나면 '종료'를 입력하세요.)")
        print("증상: 발열, 기침, 목 통증, 두통, 구토, 가슴 통증, 호흡 곤란, 복통, 설사, 메스꺼움, 피로, 체중 감소, 잦은 소변")

        user_symptoms = []

        while True:
            symptoms = input("증상 입력: ")
            if symptoms == "종료":
                break
            user_symptoms.append(symptoms)

            #진단 결과 출력
            result = diagnose(user_symptoms)
            print("\n 진단 결과:")
            print(result)