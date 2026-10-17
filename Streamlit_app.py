import time
import streamlit as st

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Hành Trình Tri Thức 20/10 💖",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. CSS Tùy chỉnh - Giao diện sáng sủa & Bảng tổng kết lời chúc hoành tráng
st.markdown(
    """
    <style>
    /* Ép nền trang web thành màu sáng dịu */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #fff0f3 !important;
    }

    /* Đảm bảo toàn bộ chữ hiển thị màu tối rõ nét */
    html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6, span, label, div {
        color: #1e293b !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* Nhãn của các thành phần */
    .stCheckbox label span, .stRadio label span, .stSlider label span, .stSelectbox label span {
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* Khung code */
    pre, code, [data-testid="stCode"] {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    pre span, code span {
        color: #f43f5e !important;
    }

    /* Menu dropdown */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 1px solid #ffb6c1 !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #ffffff !important;
    }
    ul[data-baseweb="menu"] li {
        color: #1e293b !important;
        background-color: #ffffff !important;
    }
    ul[data-baseweb="menu"] li:hover {
        background-color: #ffe4e1 !important;
        color: #d63384 !important;
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
        text-align: center;
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

    /* Thẻ tổng kết hoàn thành Game */
    .final-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff0f3 100%) !important;
        border: 3px solid #ff4d6d !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin-top: 20px !important;
        box-shadow: 0 10px 25px rgba(255, 77, 109, 0.4) !important;
        text-align: center;
    }

    .highlight-text {
        color: #e11d48 !important;
        font-weight: bold !important;
    }

    /* Hiệu ứng nổ trái tim */
    @keyframes pulse-boom {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.15); opacity: 1; text-shadow: 0 0 20px #ff4d6d; }
        100% { transform: scale(1); opacity: 1; }
    }
    .boom-effect {
        font-size: 4rem;
        text-align: center;
        animation: pulse-boom 0.8s ease-in-out infinite alternate;
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
        color: #ffffff !important;
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
if "chem_mixed" not in st.session_state:
  st.session_state.chem_mixed = False
if "game_finished" not in st.session_state:
  st.session_state.game_finished = False

# Danh sách các môn học
SUBJECTS = [
    "🧪 Hóa Học (Thí Nghiệm Nổ Trái Tim)",
    "📐 Toán Học",
    "⚡ Vật Lý",
    "📖 Văn Học",
    "🧬 Sinh Học",
    "🏛️ Lịch Sử",
    "🌍 Địa Lý",
    "💻 Tin Học",
    "🔤 Tiếng Anh",
]

# --- TÍCH HỢP NHẠC NỀN (Music 2010.mp3) ---
st.sidebar.markdown("### 🎵 Trình Phát Nhạc 20/10")
try:
  # Phát file nhạc nằm cùng thư mục trên GitHub
  st.sidebar.audio("Music 2010.mp3", format="audio/mp3", autoplay=True)
except Exception:
  st.sidebar.warning(
      "⚠️ Chưa tìm thấy file 'Music 2010.mp3' trên GitHub. Hãy tải file nhạc lên"
      " repo nhé!"
  )


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
    <div class="wish-card">
        <h3>🌸 Chào mừng bạn đến với Game 20/10!</h3>
        <p>Hãy bật nhạc nền ở thanh bên trái (Sidebar) và cùng trải nghiệm các thí nghiệm thú vị tương ứng với từng môn học để mở khóa những lời chúc ngọt ngào nhất nhé!</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.write("")
  if st.button("🚀 BẮT ĐẦU KHÁM PHÁ NGAY"):
    st.session_state.game_started = True
    st.session_state.game_finished = False
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
    st.subheader(
        "🧪 Môn Hóa Học: Thí Nghiệm Rót Hóa Chất & Kích Hoạt Phản Ứng Nổ"
    )
    st.write(
        "**Nhiệm vụ:** Đổ dung dịch từ Bình A sang Bình B, lắc đều và kích hoạt"
        " phản ứng nổ tạo làn khói trái tim!"
    )

    col1, col2 = st.columns(2)
    with col1:
      st.markdown(
          "<div style='text-align: center;'><b>🧪 Bình A</b><br>Dung dịch"
          " Chân Thành (💙)</div>",
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown(
          "<div style='text-align: center;'><b>🧪 Bình B</b><br>Dung dịch Yêu"
          " Thương (💖)</div>",
          unsafe_allow_html=True,
      )

    st.write("")
    if not st.session_state.chem_mixed:
      if st.button("💥 Đổ hóa chất sang nhau & Kích hoạt phản ứng!"):
        with st.spinner("Đang rót dung dịch và tiến hành phản ứng hóa học..."):
          time.sleep(1.2)
        st.session_state.chem_mixed = True
        st.rerun()
    else:
      st.markdown("<div class='boom-effect'>💖 ☁️ 💥 ☁️ 💖</div>", unsafe_allow_html=True)
      st.balloons()
      st.markdown(
          """
            <div class="wish-card">
                <h3>🎉 BÙM! PHẢN ỨNG NỔ HOÀN HÀO!</h3>
                <p>Một làn khí hình trái tim rực rỡ đã bùng nổ giữa không trung, mang theo vô số lời chúc tốt đẹp nhất:</p>
                <hr style="border: 1px dashed #ffb6c1;">
                <p>❤️ <b>Chúc các bạn nữ ngày 20/10 luôn luôn xinh đẹp, rạng rỡ như đóa hoa tươi!</b></p>
                <p>💖 <b>Luôn tràn ngập niềm vui, tiếng cười và gặt hái thật nhiều thành công rực rỡ trong học tập cũng như cuộc sống!</b></p>
                <p>✨ <b>Mong mọi điều may mắn và ngọt ngào nhất sẽ đến với một nửa thế giới hôm nay và mãi về sau!</b></p>
            </div>
            """,
          unsafe_allow_html=True,
      )

      if st.button("🔄 Làm lại thí nghiệm"):
        st.session_state.chem_mixed = False
        st.rerun()

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
        st.session_state.game_finished = False
        st.rerun()

  with col_next:
    if curr_idx < len(SUBJECTS) - 1:
      if st.button("Môn tiếp theo ➔"):
        st.session_state.current_subject += 1
        st.session_state.game_finished = False
        st.rerun()
    else:
      if st.button("🎉 HOÀN THÀNH GAME"):
        st.session_state.game_finished = True
        st.rerun()

  # HIỂN THỊ LỜI CHÚC TỔNG KẾT KHI BẤM HOÀN THÀNH GAME
  if st.session_state.game_finished:
    st.balloons()
    st.markdown(
        """
        <div class="final-card">
            <h2>🎉 CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH TẤT CẢ MÔN HỌC! 🎉</h2>
            <hr style="border: 1px solid #ff4d6d;">
            <p style="font-size: 1.25rem !important; color: #d63384 !important; font-weight: bold;">
                🌸 BẢNG VÀNG LỜI CHÚC 20/10 DÀNH TẶNG CÁC BẠN NỮ 🌸
            </p>
            <p>Mỗi môn học là một mảnh ghép tri thức, và bạn chính là mảnh ghép hoàn hảo nhất tạo nên vẻ đẹp của cuộc sống này!</p>
            <p>✨ Chúc một nửa thế giới luôn xinh đẹp, rạng rỡ, tự tin chinh phục mọi ước mơ và tràn ngập hạnh phúc bên những người thân yêu! ✨</p>
            <h3 style="margin-top: 15px;">💐 Happy Vietnamese Women's Day 20/10! 💐</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.write("")
  if st.button("🏠 Quay lại trang chủ"):
    st.session_state.game_started = False
    st.session_state.current_subject = 0
    st.session_state.game_finished = False
    st.rerun()
