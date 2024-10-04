# 获取用户输入的身高和体重
height_cm_str = input('你的身高(单位:cm)：')
weight_kg_str = input('你的体重(单位:kg)：')

# 将输入的字符串转换为数值
try:
    height_cm = float(height_cm_str)
    weight_kg = float(weight_kg_str)

    # 检查身高是否小于100或大于200厘米
    if height_cm < 100 or height_cm > 220:
        print("输入错误，请输入100到200之间的身高数值。")
    else:
        # 将身高从厘米转换为米
        height_m = height_cm/100

        if weight_kg <= 30 or weight_kg >= 150:
            print("输入错误，请输入30到150之间的体重数值。")
           
        else:
             # 计算BMI，并四舍五入为两位小数
            bmi_accurate = weight_kg / (height_m ** 2)
            bmi = round(bmi_accurate, 2)

            if bmi_accurate < 18.5:
                bmi_show = '过轻'
            elif bmi_accurate <= 25:
                bmi_show = '正常'
            elif bmi_accurate <= 28:
                bmi_show = '过重'
            elif bmi_accurate <= 32:
                bmi_show = '肥胖'
            else:
                bmi_show = '严重肥胖'
            print(f"你的BMI指数是{bmi}，并且你是 {bmi_show}")

        

except ValueError:
    print("输入无效，请输入有效的数字。")

