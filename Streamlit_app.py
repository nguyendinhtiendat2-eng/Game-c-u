import time
import streamlit as st

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Hành Trình Tri Thức 20/10 💖",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. CSS Tùy chỉnh - Cố định màu chữ ĐEN / ĐẬM trên MỌI thành phần (Bất chấp Dark Mode/Light Mode)
st.markdown(
    """
    <style>
    /* Ép nền trang web thành màu sáng dịu */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #fff0f3 !important;
    }

    /* Đảm bảo toàn bộ chữ trên màn hình (p, h1, h2, h3, h4, span, label, div) luôn hiển thị màu tối */
    html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6, span, label, div {
        color: #1e293b !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* Định dạng lại nhãn của Checkbox, Radio, Slider, Text Input */
    .stCheckbox label span, .stRadio label span, .stSlider label span, .stSelectbox label span {
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* Thẻ thông điệp lời chúc nổi bật */
    .wish-card {
        background-color: #ffffff !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 16px !important;
        padding: 22px !important;
        margin-top: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.35) !important;
    }

    .wish-card h2, .wish-card h3 {
        color: #d63384 !important;
        font-weight: 800 !important;
        margin-bottom: 12px !important;
    }

    .wish-card p, .wish-card li {
        color: #1e293b !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        font-weight: 600 !important;
    }

    .highlight-text {
        color: #e11d48 !important;
        font-weight: bold !important;
    }

    /* Định dạng nút bấm */
    .stButton>button {
        width: 100%;
        border-radius: 12px !important;
        font-weight: bold !important;
        background: linear-gradient(90deg, #ff4d6d 0%, #ff758f 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 12px 20px !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 10px rgba(255, 77, 109, 0.3) !important;
    }
    
    .stButton>button * {
        color: #ffffff !important; /* Đảm bảo chữ bên trong nút luôn trắng */
    }

    /* Thanh tiến trình */
    .stProgress > div > div > div > div {
        background-color: #ff4d6d !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Khởi tạo State lưu trữ trạng thái Game
if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "current_subject" not in st.session_state:
  st.session_state.current_subject = 0

# Danh sách các môn học
SUBJECTS = [
    "🧪 Hóa Học",
    "📐 Toán Học",
    "⚡ Vật Lý",
    "📖 Văn Học",
    "🧬 Sinh Học",
    "🏛️ Lịch Sử",
    "🌍 Địa Lý",
    "💻 Tin Học",
    "🔤 Tiếng Anh",
]

# --- MÀN HÌNH BẮT ĐẦU (GAME LOBBY) ---
if not st.session_state.game_started:
  st.markdown(
      "<h1 style='text-align: center; color: #d63384;'>🎓 MINI GAME 20/10 💖</h1>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<h3 style='text-align: center; color: #334155;'>Hành Trình Tri Thức &"
      " Lời Chúc Môn Học</h3>",
      unsafe_allow_html=True,
  )

  st.write("")
  st.markdown(
      """
    <div class="wish-card" style="text-align: center;">
        <h3>🌸 Chào mừng bạn đến với Game 20/10!</h3>
        <p>Hãy cùng trải nghiệm các thí nghiệm và câu đố thú vị tương ứng với từng môn học để mở khóa những lời chúc ngọt ngào nhất dành riêng cho ngày Phụ nữ Việt Nam nhé!</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("🚀 BẮT ĐẦU KHÁM PHÁ NGAY"):
    st.session_state.game_started = True
    st.rerun()

# --- MÀN HÌNH CHÍNH CỦA GAME ---
else:
  curr_idx = st.session_state.current_subject

  # Thanh tiến trình
  progress_val = (curr_idx + 1) / len(SUBJECTS)
  st.progress(progress_val)
  st.markdown(
      f"<p style='text-align: center; font-weight: bold;'>Môn học"
      f" {curr_idx + 1}/{len(SUBJECTS)}: <span"
      f" class='highlight-text'>{SUBJECTS[curr_idx]}</span></p>",
      unsafe_allow_html=True,
  )

  st.write("---")

  # 1. HÓA HỌC
  if curr_idx == 0:
    st.subheader("🧪 Môn Hóa Học: Phản Ứng Bùng Nổ Tình Cảm")
    st.write(
        "**Nhiệm vụ:** Chọn đủ 2 chất xúc tác để kích hoạt phản ứng tỏa nhiệt"
        " trái tim."
    )

    chem1 = st.checkbox("Đổ dung dịch 💙 Chân Thành (CuSO₄)")
    chem2 = st.checkbox("Thêm xúc tác ✨ Rạng Rỡ (NaOH)")

    if st.button("🔥 Tiến hành phản ứng"):
      if chem1 and chem2:
        with st.spinner("Đang đun nóng ống nghiệm..."):
          time.sleep(1)
        st.balloons()
        st.markdown(
            """
                <div class="wish-card">
                    <h3>💥 BỤP! Phản ứng hoàn hảo!</h3>
                    <p>Chúc các bạn nữ ngày 20/10 luôn lung linh, tỏa sáng rực rỡ như phản ứng bùng nổ của Magie, luôn tràn đầy năng lượng tích cực và thu hút mọi điều may mắn trong cuộc sống! ❤️</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.warning("⚠️ Hãy tích chọn đủ cả 2 hóa chất để kích hoạt phản ứng!")

  # 2. TOÁN HỌC
  elif curr_idx == 1:
    st.subheader("📐 Môn Toán Học: Đồ Thị Hạnh Phúc")
    st.write("**Nhiệm vụ:** Tìm ẩn số nghiệm của phương trình trái tim.")

    ans = st.text_input("Nhập giá trị cần tìm (Gợi ý: Nhập '20/10'):")
    if st.button("📐 Giải Phương Trình"):
      if ans.strip().lower() in ["20/10", "20-10", "love"]:
        st.snow()
        st.markdown(
            """
                <div class="wish-card">
                    <h3>✨ Kết Quả: x = +∞ (Dương vô cực)</h3>
                    <p>Chúc nụ cười và nhan sắc của các bạn luôn là một hằng số cực đại, niềm vui đồng biến trên mọi khoảng cuộc sống và mọi nỗi buồn đều tiệm cận về 0! 💖</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.error("❌ Chưa đúng nghiệm rồi! Hãy thử nhập '20/10' nhé.")

  # 3. VẬT LÝ
  elif curr_idx == 2:
    st.subheader("⚡ Môn Vật Lý: Định Luật Bảo Toàn Nụ Cười")
    st.write(
        "**Nhiệm vụ:** Kéo thanh trượt để tích tụ điện áp năng lượng tích cực."
    )

    volt = st.slider("Điều chỉnh điện áp (Volt):", 0, 220, 100)
    if st.button("⚡ Đóng Mạch Điện"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>💡 Dòng Điện Tần Số {volt}V Đã Mở!</h3>
                <p>Chúc các bạn nữ luôn giữ được tần số năng lượng tích cực cao nhất, vận tốc tiến tới mục tiêu nhanh như ánh sáng và tỏa ra sức hút mạnh mẽ làm xiêu lòng mọi người xung quanh! ⚡🌸</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 4. VĂN HỌC
  elif curr_idx == 3:
    st.subheader("📖 Môn Văn Học: Thơ Ca Thanh Xuân")
    st.write("**Nhiệm vụ:** Nhấn nút mở phong bì lá thư mực tím.")

    if st.button("💌 Mở Phong Bì Thư"):
      st.markdown(
          """
            <div class="wish-card">
                <h3>📜 Đoản Văn Ngày 20/10:</h3>
                <p><i>"Tháng Mười nhung nhớ làn gió heo may,<br>
                Chúc cho cô gái luôn ngập tràn may mắn.<br>
                Nụ cười rạng rỡ như nắng ban mai,<br>
                Thanh xuân rực rỡ, đường dài thong dong."</i></p>
                <p>Chúc bạn viết nên những trang đời thật ngọt ngào, lãng mạn và trọn vẹn niềm vui! 🌷</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 5. SINH HỌC
  elif curr_idx == 4:
    st.subheader("🧬 Môn Sinh Học: Mã Gen Xinh Đẹp")
    st.write("**Nhiệm vụ:** Phân tích bộ mã Nucleotide đặc biệt.")

    gen = st.selectbox(
        "Chọn chuỗi gen muốn soi dưới kính hiển vi:",
        ["A - T - G - X", "S - M - I - L - E", "B - E - A - U - T - Y"],
    )
    if st.button("🔬 Phân Tích Mã Gen"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🧬 Kết quả giải mã chuỗi [{gen}]:</h3>
                <p>Hệ gen của bạn chứa 100% nhiễm sắc thể hạnh phúc, sự dịu dàng và tự tin. Chúc các bạn nữ luôn giữ vững phong độ xinh đẹp và tỏa sáng! 🌸</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 6. LỊCH SỬ
  elif curr_idx == 5:
    st.subheader("🏛️ Môn Lịch Sử: Cột Mốc Đáng Nhớ")
    st.write("**Nhiệm vụ:** Chọn mốc thời gian đặc biệt nhất trong năm.")

    event = st.radio("Chọn ngày lễ đặc biệt:", ["01/01", "20/10", "31/12"])
    if st.button("📜 Khai Quật Lịch Sử"):
      if event == "20/10":
        st.snow()
        st.markdown(
            """
                <div class="wish-card">
                    <h3>👑 Cột Mốc Vàng Trong Lịch Sử!</h3>
                    <p>Ngày 20/10 là ngày tôn vinh trọn vẹn dành cho phái đẹp. Chúc bạn sẽ tạo nên những mốc chói lọi trong hành trình phát triển bản thân và luôn là nữ hoàng trong câu chuyện của chính mình! ✨</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.info("Hãy chọn mốc ngày Phụ Nữ Việt Nam 20/10 nhé!")

  # 7. ĐỊA LÝ
  elif curr_idx == 6:
    st.subheader("🌍 Môn Địa Lý: Tọa Độ Hạnh Phúc")
    st.write("**Nhiệm vụ:** Định vị khu vực tràn ngập niềm vui.")

    region = st.select_slider(
        "Chọn vĩ độ cảm xúc:", options=["Bắc Cực", "Xích Đạo", "Tọa Độ 20/10"]
    )
    if st.button("📍 Định Vị Tọa Độ"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🗺️ Định vị thành công: [{region}]!</h3>
                <p>Chúc các bạn nữ đi đến bất kỳ đâu trên bản đồ thế giới cũng đều gặp được những phong cảnh tuyệt đẹp, những con người chân thành và luôn tràn ngập nụ cười! 🌷</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 8. TIN HỌC
  elif curr_idx == 7:
    st.subheader("💻 Môn Tin Học: Thuật Toán Yêu Thương")
    st.write("**Nhiệm vụ:** Chạy đoạn mã lệnh Python kiểm tra hệ thống.")

    st.code(
        "if day == '20/10':\n    status = 'Always Happy & Beautiful'\n   "
        " print(status)",
        language="python",
    )
    if st.button("▶️ Run Code"):
      st.balloons()
      st.markdown(
          """
            <div class="wish-card">
                <h3>🖥️ Output: SUCCESS (0 Errors, 0 Warnings)</h3>
                <p>Chúc bạn có cuộc sống tựa như đoạn code hoàn hảo: Không lỗi (Bug), không drama, và luôn được compile ra thật nhiều niềm vui mỗi ngày! 💻💖</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 9. TIẾNG ANH
  elif curr_idx == 8:
    st.subheader("🔤 Môn Tiếng Anh: Vocabulary of Happiness")
    st.write("**Nhiệm vụ:** Mở từ điển thông điệp đặc biệt.")

    if st.button("🔠 Mở Từ Điển Lời Chúc"):
      st.balloons()
      st.markdown(
          """
            <div class="wish-card">
                <h3>🔤 English Wish for You:</h3>
                <p><i>"Wishing all wonderful girls a fantastic Vietnamese Women's Day! May your day be filled with endless joy, sweet surprises, and absolute happiness!"</i> 🌺</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  st.write("---")

  # --- ĐIỀU HƯỚNG MẠCH GAME ---
  col_prev, col_next = st.columns(2)

  with col_prev:
    if curr_idx > 0:
      if st.button("⬅️ Môn trước"):
        st.session_state.current_subject -= 1
        st.rerun()

  with col_next:
    if curr_idx < len(SUBJECTS) - 1:
      if st.button("Môn tiếp theo ➔"):
        st.session_state.current_subject += 1
        st.rerun()
    else:
      if st.button("🎉 HOÀN THÀNH GAME"):
        st.balloons()
        st.success("Chúc mừng bạn đã hoàn thành tất cả các môn học ngày 20/10!")

  st.write("")
  if st.button("🏠 Quay lại trang chủ"):
    st.session_state.game_started = False
    st.session_state.current_subject = 0
    st.rerun()
  
