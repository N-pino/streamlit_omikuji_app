import random

import streamlit as st



def omikuji_model():
    # おみくじ
    omikuji_num = random.randint(1, 13)
    colour = random.randint(1, 5)

    omikuji = {}

    if omikuji_num == 1:
        omikuji["kekka"] = "大吉"
    elif omikuji_num <= 4:
        omikuji["kekka"] = "中吉"
    elif omikuji_num <= 8:
        omikuji["kekka"] = "小吉"
    else:
        omikuji["kekka"] = "吉"

    if colour == 1:
        omikuji["colour"] = "紫"
    elif colour == 2:
        omikuji["colour"] = "黒"
    elif colour == 3:
        omikuji["colour"] = "青"
    elif colour == 4:
        omikuji["colour"] = "緑"
    else:
        omikuji["colour"] = "白"

    return omikuji  # {"kekka": "大吉", "colour": "murasaki" }


def view():
    # タイトル
    st.title('おみくじ')
    st.caption('今日の運勢を占おう!!')
    # ボタン
    submit_btn = st.button('占う')
    if submit_btn:
        omikuji = omikuji_model()
        st.text(f'今日の運勢は{omikuji["kekka"]}!!')
        st.text(f'そんなあなたのラッキーカラーは{omikuji["colour"]}。')


if __name__ == "__main__":
    view()
