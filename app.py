import streamlit as st

st.set_page_config(page_title="IRGETAS", page_icon="🏠", layout="centered")

st.title("🏠 IRGETAS")
st.caption("ИИ-помощник частного застройщика: технология, смета и план действий. Алматы, дома 80–200 м²")

st.info("Прототип в разработке: сейчас это пустая форма. Расчёт будет подключён к КТ 3 (29 ноября).")

# Шаг 1. Запрос словами (функция 1: ИИ извлекает параметры)
with st.form("request_form"):
    st.subheader("1. Опишите дом")
    description = st.text_area(
        "Описание обычными словами",
        placeholder="Например: двухэтажный дом 120 м² в Алматы, 3 спальни, бюджет до 40 млн тг, хочу построить за год",
        height=120,
    )

    st.markdown("**Или заполните параметры вручную**")
    col1, col2 = st.columns(2)
    with col1:
        city = st.selectbox("Город", ["Алматы"])
        area = st.number_input("Площадь, м²", min_value=80, max_value=200, value=120, step=5)
        floors = st.selectbox("Этажность", ["1 этаж", "2 этажа"])
    with col2:
        budget = st.number_input("Бюджет, млн тг", min_value=0.0, value=0.0, step=1.0)
        deadline = st.selectbox("Желаемый срок", ["Не важно", "До 6 месяцев", "До 1 года", "Больше года"])
        technology = st.multiselect(
            "Технологии для сравнения",
            ["Газоблок", "Кирпич", "Каркас"],
            default=["Газоблок", "Кирпич", "Каркас"],
        )
    wishes = st.text_input("Пожелания (необязательно)", placeholder="гараж, тёплый пол, мансарда...")

    submitted = st.form_submit_button("Продолжить")

if submitted:
    # Шаг 2. Подтверждение параметров (здесь позже появится ответ ИИ)
    st.subheader("2. Проверьте параметры")
    st.json(
        {
            "description": description,
            "city": city,
            "area_m2": area,
            "floors": floors,
            "budget_mln_tg": budget,
            "deadline": deadline,
            "technologies": technology,
            "wishes": wishes,
        }
    )
    st.warning(
        "Следующие шаги пока не реализованы: подбор технологий, смета с источниками цен, "
        "план действий, PDF-отчёт."
    )
