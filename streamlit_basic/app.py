import streamlit as st
import pandas as pd
import numpy as np


"""
ドキュメント
https://docs.streamlit.io/library/api-reference/write-magic/st.write
"""

# st.title("Sample App")
# st.write("Sample App")
# # st.markdown("# 見出し1")
# # st.markdown("## 見出し2")
# # st.markdown("### 見出し3")
# st.markdown(
#     """
#     # 見出し
#     ## 見出し2
#     ### 見出し3

#     - 箇条書き1
#     - 箇条書き2
#     - 箇条書き3
#     """
# )

# st.code(
#     """
# import numpy as np
# import pandas as pd
# a = 123
# pd.DataFrame()
# """
# )


# df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [-1, -2, -3, -4]})
# st.dataframe(df.style.highlight_max(axis=0))
# st.json(
#     {
#         "data": {
#             "name": "abc",
#             "age": "123",
#         }
#     }
# )

# NOTE: チャートの作成
# df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# NOTE: Input Widgets
if st.button("Click Me!!!!!!!"):
    st.write("Clicked")

if st.checkbox("Click Me!!!!!!!"):
    st.write("Clicked")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write(f"選択肢: {options}")

# NOTE: Layouts and containers
number = st.sidebar.slider("Pick a Num", 0, 100, 40)
st.sidebar.write(f"number: {number}")
left_col, center_col, rigth_col = st.columns(3)
left_col.slider("Pick a Num in Left", 0, 100)
center_col.slider("Pick a Num in Center", 0, 100)
rigth_col.slider("Pick a Num in Rigth", 0, 100)
