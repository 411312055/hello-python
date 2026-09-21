def calculate_bmi():
    print("=== BMI 計算器 ===")
    try:
        height_cm = float(input("請輸入您的身高 (公分 cm)："))
        weight_kg = float(input("請輸入您的體重 (公斤 kg)："))

        if height_cm <= 0 or weight_kg <= 0:
            print("身高和體重必須大於 0！")
            return

        # 身高公分換算為公尺
        height_m = height_cm / 100
        # 計算 BMI = 體重(kg) / 身高(m)^2
        bmi = weight_kg / (height_m ** 2)

        print(f"\n您的 BMI 指數為：{bmi:.2f}")

        # 根據衛生福利部標準判斷體位
        if bmi < 18.5:
            category = "體重過輕 (Underweight)"
        elif 18.5 <= bmi < 24:
            category = "正常範圍 (Normal)"
        elif 24 <= bmi < 27:
            category = "過重 (Overweight)"
        elif 27 <= bmi < 30:
            category = "輕度肥胖 (Mild obesity)"
        elif 30 <= bmi < 35:
            category = "中度肥胖 (Moderate obesity)"
        else:
            category = "重度肥胖 (Severe obesity)"

        print(f"體位判定結果：{category}")

    except ValueError:
        print("輸入錯誤，請輸入有效的數字！")

if __name__ == "__main__":
    calculate_bmi()
