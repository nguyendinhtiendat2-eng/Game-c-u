import time
import streamlit as st

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Hành Trình Tri Thức 20/10 💖",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. CSS Tùy chỉnh - Ép màu chữ hiển thị rõ ràng trên mọi giao diện (Dark Mode / Light Mode)
st.markdown(
    """
    <style>
    /* Nền tổng thể mềm mại */
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
    }

    /* Thẻ thông điệp chính */
    .wish-card {
        background-color: #ffffff !important;
        border: 2px solid #ffb6c1 !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-top: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 16px rgba(255, 182, 193, 0.4) !important;
    }

    /* Ép màu chữ ĐẬM rõ ràng tuyệt đối */
    .wish-card h2, .wish-card h3, .wish-card h4 {
        color: #d63384 !important;
        font-weight: 800 !important;
        margin-bottom: 12px !important;
    }
    
    .wish-card p, .wish-card li, .wish-card span, .wish-card div {
        color: #2c3e50 !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        font-weight: 600 !important;
    }

    .highlight-text {
        color: #c2185b !important;
        font-weight: bold !important;
    }

    /* Thiết kế thanh tiến trình */
    .stProgress > div > div > div > div {
        background-color: #ff69b4 !important;
    }

    /* Chỉnh kiểu nút bấm */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        background-color: #ff6b81;
        color: white;
        border: none;
        padding: 10px 15px;
    }
    .stButton>button:hover {
        background-color: #ff4757;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Khởi tạo State lưu trữ trạng thái Game
if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "player_name" not in st.session_state:
  st.session_state.player_name = "Bạn nữ xinh đẹp"
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
      "<h1 style='text-align: center; color: #d63384;'>🎓 GAME INTERACTIVE"
      " 20/10 💖</h1>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<h3 style='text-align: center; color: #4a4a4a;'>Hành Trình Tri Thức &"
      " Lời Chúc Môn Học</h3>",
      unsafe_allow_html=True,
  )

  st.write("")
  st.markdown(
      """
    <div class="wish-card" style="text-align: center;">
        <p>Chào mừng bạn đến với phòng thí nghiệm lời chúc ngày 20/10!</p>
        <p>Hãy trải nghiệm các mini-game nhỏ tương ứng với từng môn học để mở khóa những thông điệp ngọt ngào nhất.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  name_input = st.text_input(
      "👉 Nhập tên bạn nữ nhận lời chúc (hoặc tên của bạn):",
      value="Nữ Sinh Xinh Đẹp",
  )

  if st.button("🚀 BẮT ĐẦU TRẢI NGHIỆM GAME"):
    st.session_state.player_name = name_input if name_input else "Bạn nữ"
    st.session_state.game_started = True
    st.rerun()

# --- MÀN HÌNH CHÍNH CỦA GAME ---
else:
  name = st.session_state.player_name
  curr_idx = st.session_state.current_subject

  # Thanh tiến trình
  progress_val = (curr_idx + 1) / len(SUBJECTS)
  st.progress(progress_val)
  st.caption(
      f"Môn học {curr_idx + 1}/{len(SUBJECTS)}: **{SUBJECTS[curr_idx]}** | Người"
      f" nhận: **{name}**"
  )

  st.write("---")

  # 1. HÓA HỌC
  if curr_idx == 0:
    st.subheader("🧪 Môn Hóa Học: Phản Ứng Bùng Nổ Tình Cảm")
    st.write(
        "**Nhiệm vụ:** Chọn đúng 2 chất xúc tác để tạo ra phản ứng nổ trái"
        " tim."
    )

    col1, col2 = st.columns(2)
    with col1:
      chem1 = st.checkbox("Đổ dung dịch 💙 Chân Thành (CuSO₄)")
    with col2:
      chem2 = st.checkbox("Thêm xúc tác ✨ Rạng Rỡ (NaOH)")

    if st.button("🔥 Tiến hành phản ứng"):
      if chem1 and chem2:
        with st.spinner("Đang đun nóng ống nghiệm..."):
          time.sleep(1)
        st.balloons()
        st.markdown(
            f"""
                <div class="wish-card">
                    <h3>💥 BỤP! Phản ứng tỏa nhiệt hoàn hảo!</h3>
                    <p>Chúc <span class="highlight-text">{name}</span> ngày 20/10 luôn lung linh, tỏa sáng rực rỡ như phản ứng bùng nổ của Magie, luôn tràn đầy năng lượng tích cực và thu hút mọi điều may mắn!</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.warning("⚠️ Hãy tích chọn đủ cả 2 chất hóa học để kích hoạt!")

  # 2. TOÁN HỌC
  elif curr_idx == 1:
    st.subheader("📐 Môn Toán Học: Đồ Thị Hạnh Phúc")
    st.write(
        "**Nhiệm vụ:** Tìm nghiệm ẩn số của hệ phương trình trái tim $y = f(x)$."
    )

    ans = st.text_input("Nhập nghiệm của niềm vui (Gợi ý: Nhập '20/10'):")
    if st.button("📐 Giải Phương Trình"):
      if ans.strip().lower() in ["20/10", "20-10", "love"]:
        st.snow()
        st.markdown(
            f"""
                <div class="wish-card">
                    <h3>✨ Kết Quả: $x = \\infty$ (Dương vô cực)</h3>
                    <p>Chúc <span class="highlight-text">{name}</span> có nhan sắc luôn là một hằng số cực đại, niềm vui đồng biến trên mọi khoảng cuộc sống và mọi nỗi buồn đều tiệm cận về 0!</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.error("❌ Chưa đúng nghiệm rồi! Hãy nhập '20/10' nhé.")

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
                <p>Chúc <span class="highlight-text">{name}</span> luôn giữ được tần số năng lượng cao nhất, vận tốc tiến tới thành công nhanh như ánh sáng và luôn phát ra sức hút mạnh mẽ làm xiêu lòng mọi người xung quanh!</p>
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
          f"""
            <div class="wish-card">
                <h3>📜 Đoản Văn Mới Xuất Bản:</h3>
                <p><i>"Tháng Mười nhung nhớ làn gió heo may,<br>
                Chúc cho cô gái luôn ngập tràn may mắn.<br>
                Nụ cười rạng rỡ như nắng ban mai,<br>
                Thanh xuân rực rỡ, đường dài thong dong."</i></p>
                <p>Chúc <span class="highlight-text">{name}</span> ngày 20/10 viết nên những trang đời ngọt ngào, lãng mạn và tuyệt đẹp nhất!</p>
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
    if st.button("🔬 Khảo Sát Mã Gen"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🧬 Kết quả giải mã chuỗi [{gen}]:</h3>
                <p>Hệ gen của <span class="highlight-text">{name}</span> chứa 100% nhiễm sắc thể hạnh phúc, sự dịu dàng và tự tin. Chúc bạn luôn giữ vững phong độ xinh đẹp và tỏa sáng!</p>
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
            f"""
                <div class="wish-card">
                    <h3>👑 Cột Mốc Vàng Trong Lịch Sử!</h3>
                    <p>Ngày 20/10 đánh dấu sự tôn vinh trọn vẹn dành cho phái đẹp. Chúc <span class="highlight-text">{name}</span> sẽ tạo nên những mốc chói lọi trong hành trình cá nhân và luôn là nữ hoàng trong câu chuyện của chính mình!</p>
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
        st.info("Hãy chọn mốc ngày Phụ Nữ Việt Nam 20/10 nhé!")

  # 7. ĐỊA LÝ
  elif curr_idx == 6:
    st.subheader("🌍 Môn Địa Lý: Tọa Độ Hạnh Phúc")
    st.write("**Nhiệm vụ:** Xoay quả địa cầu để định vị khu vực tràn ngập niềm vui.")

    region = st.select_slider(
        "Chọn vĩ độ cảm xúc:", options=["Bắc Cực", "Xích Đạo", "Tọa Độ 20/10"]
    )
    if st.button("📍 Định Vị Tọa Độ"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🗺️ Định vị thành công: [{region}]!</h3>
                <p>Chúc <span class="highlight-text">{name}</span> đi đến bất kỳ đâu trên bản đồ thế giới cũng đều gặp được những phong cảnh tuyệt đẹp, những con người chân thành và luôn tràn ngập niềm vui!</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 8. TIN HỌC
  elif curr_idx == 7:
    st.subheader("💻 Môn Tin Học: Thuật Toán Yêu Thương")
    st.write(
        "**Nhiệm vụ:** Chạy đoạn mã lệnh Python để kiểm tra kết quả System."
    )

    st.code(
        f"if user == '{name}':\n    status = 'Always Happy & Beautiful'\n   "
        " print(status)",
        language="python",
    )
    if st.button("▶️ Run Code"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🖥️ Output: SUCCESS (0 Errors, 0 Warnings)</h3>
                <p>Chúc <span class="highlight-text">{name}</span> có cuộc sống tựa như đoạn code hoàn hảo: Không lỗi (Bug), không drama, và luôn được compile ra thật nhiều niềm vui mỗi ngày!</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 9. TIẾNG ANH
  elif curr_idx == 8:
    st.subheader("🔤 Môn Tiếng Anh: Vocabulary of Happiness")
    st.write("**Nhiệm vụ:** Dịch thông điệp đặc biệt sang Tiếng Anh.")

    if st.button("🔠 Mở Từ Điển Lời Chúc"):
      st.balloons()
      st.markdown(
          f"""
            <div class="wish-card">
                <h3>🔤 English Wish for You:</h3>
                <p><i>"Wishing <span class="highlight-text">{name}</span> a wonderful Vietnamese Women's Day! May your day be filled with endless joy, sweet surprises, and absolute happiness!"</i></p>
            </div>
            """,
          unsafe_allow_html=True,
      )

  st.write("---")

  # --- ĐIỀU HƯỚNG MẠCH GAME (GAME NAVIGATION) ---
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
      if st.button("🎉 HOÀN THÀNH TẤT CẢ MÔN HỌC"):
        st.balloons()
        st.success(
            f"Chúc mừng {name} đã vượt qua toàn bộ thử thách tri thức ngày"
            " 20/10!"
        )

  # Nút quay về màn hình chính
  st.write("")
  if st.button("🏠 Quay lại trang chủ"):
    st.session_state.game_started = False
    st.session_state.current_subject = 0
    st.rerun()
  
