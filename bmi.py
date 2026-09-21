# -*- coding: utf-8 -*-

MESSAGES = {
    "1": {
        "name": "繁體中文",
        "title": "=== BMI 計算器 ===",
        "prompt_height": "請輸入您的身高 (公分 cm)：",
        "prompt_weight": "請輸入您的體重 (公斤 kg)：",
        "invalid_positive": "身高和體重必須大於 0！",
        "result_bmi": "您的 BMI 指數為：{:.2f}",
        "result_category": "體位判定結果：{}",
        "invalid_number": "輸入錯誤，請輸入有效的數字！",
        "categories": [
            (18.5, "體重過輕"),
            (24.0, "正常範圍"),
            (27.0, "過重"),
            (30.0, "輕度肥胖"),
            (35.0, "中度肥胖"),
            (float("inf"), "重度肥胖"),
        ],
    },
    "2": {
        "name": "English",
        "title": "=== BMI Calculator ===",
        "prompt_height": "Please enter your height (cm): ",
        "prompt_weight": "Please enter your weight (kg): ",
        "invalid_positive": "Height and weight must be greater than 0!",
        "result_bmi": "Your BMI is: {:.2f}",
        "result_category": "Health Category: {}",
        "invalid_number": "Invalid input! Please enter a valid number.",
        "categories": [
            (18.5, "Underweight"),
            (25.0, "Normal weight"),
            (30.0, "Overweight"),
            (35.0, "Obesity Class I"),
            (40.0, "Obesity Class II"),
            (float("inf"), "Obesity Class III"),
        ],
    },
    "3": {
        "name": "日本語",
        "title": "=== BMI 計算ツール ===",
        "prompt_height": "身長を入力してください (cm)：",
        "prompt_weight": "体重を入力してください (kg)：",
        "invalid_positive": "身長と体重は 0 より大きい数値を入力してください！",
        "result_bmi": "あなたの BMI 値：{:.2f}",
        "result_category": "判定結果：{}",
        "invalid_number": "入力エラー！有効な数値を入力してください。",
        "categories": [
            (18.5, "低体重 (痩せ型)"),
            (25.0, "普通体重"),
            (30.0, "肥満 (1度)"),
            (35.0, "肥満 (2度)"),
            (40.0, "肥満 (3度)"),
            (float("inf"), "肥満 (4度)"),
        ],
    },
    "4": {
        "name": "한국어",
        "title": "=== BMI 계산기 ===",
        "prompt_height": "키를 입력해주세요 (cm): ",
        "prompt_weight": "체중을 입력해주세요 (kg): ",
        "invalid_positive": "키와 체중은 0보다 커야 합니다!",
        "result_bmi": "당신의 BMI 지수는: {:.2f}",
        "result_category": "비만도 판정 결과: {}",
        "invalid_number": "입력 오류! 올바른 숫자를 입력해주세요.",
        "categories": [
            (18.5, "저체중 (Underweight)"),
            (23.0, "정상 체중 (Normal)"),
            (25.0, "비만 전단계 / 과체중 (Overweight)"),
            (30.0, "1단계 비만 (Obesity Class I)"),
            (35.0, "2단계 비만 (Obesity Class II)"),
            (float("inf"), "3단계 고도비만 (Severe obesity)"),
        ],
    },
}

def get_category(bmi, categories):
    for upper_bound, label in categories:
        if bmi < upper_bound:
            return label
    return categories[-1][1]

def calculate_bmi():
    print("Please select language / 請選擇語言 / 언어를 선택하세요:")
    print("1. 繁體中文")
    print("2. English")
    print("3. 日本語")
    print("4. 한국어")
    lang_choice = input("Choice (1-4, default 1): ").strip()

    if lang_choice not in MESSAGES:
        lang_choice = "1"

    lang = MESSAGES[lang_choice]
    print(f"\n{lang['title']}")

    try:
        height_cm = float(input(lang["prompt_height"]))
        weight_kg = float(input(lang["prompt_weight"]))

        if height_cm <= 0 or weight_kg <= 0:
            print(lang["invalid_positive"])
            return

        # 身高換算公尺並計算 BMI
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        print("\n" + lang["result_bmi"].format(bmi))
        category = get_category(bmi, lang["categories"])
        print(lang["result_category"].format(category))

    except ValueError:
        print(lang["invalid_number"])

if __name__ == "__main__":
    calculate_bmi()
