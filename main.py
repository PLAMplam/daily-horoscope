import os
import random
from datetime import datetime

PREDICTIONS = {
    "มหาโชค (Great Luck) 🌟🌟🌟🌟🌟": {
        "work": "งานทะลุเป้า โปรเจกต์ผ่านราบรื่น มีเกณฑ์ได้รับการยอมรับสูงมาก",
        "finance": "ลาภลอยโดดเด่น มีโอกาสได้ผลตอบแทนเกินคาด",
        "love": "เสน่ห์แรงเกินต้าน คนมีคู่เข้าใจกันดี คนโสดมีเกณฑ์เจอคนโปรไฟล์ดี",
        "health": "พลังงานเต็มเปี่ยม ร่างกายสดชื่น ฟื้นตัวเร็ว"
    },
    "โชคดี (Good Luck) 🌟🌟🌟🌟": {
        "work": "การงานดำเนินไปได้ด้วยดี มีคนคอยสนับสนุนเมื่อติดขัด",
        "finance": "การเงินคล่องตัว สภาพคล่องดี ไม่ตึงมือ",
        "love": "ความสัมพันธ์ราบเรียบแต่ลึกซึ้ง พึ่งพาอาศัยกันได้ดี",
        "health": "แข็งแรงดี แต่างอาจมีพักผ่อนน้อยนิดหน่อย"
    },
    "ปานกลาง (Neutral) 🌟🌟🌟": {
        "work": "เรื่อยๆ มาทรงๆ ต้องใช้ความอดทนและรอบคอบมากกว่าปกติ",
        "finance": "รายรับพอดีรายจ่าย วางแผนการเงินให้ดี หลีกเลี่ยงการเสี่ยงโชคหนัก",
        "love": "คนโสดเรื่อยๆ ไม่รีบร้อน คนมีคู่อาจมีความเห็นไม่ตรงกันเล็กน้อย",
        "health": "ระวังเรื่อง Office Syndrome หรือการปวดเมื่อย"
    },
    "เตือนสติ (Caution) ⚠️🌟🌟": {
        "work": "งานอาจมีเอกสารผิดพลาด หรือสื่อสารคลาดเคลื่อน ต้องเช็กให้ถี่ถ้วน",
        "finance": "มีเกณฑ์เสียเงินกับเรื่องไม่เป็นเรื่อง ชะลอการลงทุนใหญ่",
        "love": "ใช้อารมณ์ให้น้อยลง นึกถึงใจเขาใจเราให้มาก",
        "health": "พักผ่อนให้เพียงพอ ระวังเรื่องสายตาและโภชนาการ"
    }
}

LUCKY_COLORS = ["น้ำเงินเข้ม", "เขียวเหนี่ยวทรัพย์", "ส้มสดใส", "เทาเงิน", "ดำลึกลับ", "ขาวบริสุทธิ์", "ทองร่ำรวย"]

def run_horoscope():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # สุ่มระดับดวงชะตา
    luck_levels = list(PREDICTIONS.keys())
    overall_luck = random.choices(luck_levels, weights=[25, 45, 20, 10], k=1)[0]
    
    lucky_number = f"{random.randint(0, 9)}{random.randint(0, 9)}"
    lucky_color = random.choice(LUCKY_COLORS)
    data = PREDICTIONS[overall_luck]

    # จัดรูปแบบ Markdown สำหรับแสดงผล
    markdown_content = f"""
## 🔮 ผลทำนายดวงชะตาประจำวันที่ {today_str}

* **ภาพรวมดวง:** {overall_luck}
* **💼 การงาน:** {data['work']}
* **💰 การเงิน:** {data['finance']}
* **❤️ ความรัก:** {data['love']}
* **🩺 สุขภาพ:** {data['health']}
* **🎨 สีมงคล:** {lucky_color}
* **🔢 เลขนำโชค:** {lucky_number}

---
"""

    # 1. เขียนลง GitHub Step Summary (แสดงบนหน้า Actions Log)
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(markdown_content)

    # 2. บันทึกเก็บประวัติลงไฟล์ Markdown ใน Repo
    history_file = "horoscope_history.md"
    if not os.path.exists(history_file):
        with open(history_file, "w", encoding="utf-8") as f:
            f.write("# 📜 ประวัติคำทำนายดวงชะตารายวัน\n\n")

    with open(history_file, "a", encoding="utf-8") as f:
        f.write(markdown_content)

    print("✅ คำนวณดวงชะตาและบันทึกข้อมูลเรียบร้อยแล้ว!")

if __name__ == "__main__":
    run_horoscope()
