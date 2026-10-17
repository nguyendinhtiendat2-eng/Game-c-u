import time
import streamlit as strlit

# Cấu hình trang web
strlit.set_page_config(
    page_title="Hộp Thư 20/10 - Khoa Học & Yêu Thương",
    page_icon="🎁",
    layout="centered",
)

# Giao diện CSS tùy chỉnh màu sắc và hiệu ứng
strlit.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        color: #ff4b4b;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .subtitle {
        text-align: center;
        color: #555555;
        font-size: 1.1rem;
    }
    .card {
        background-color: #fff0f3;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ffccd5;
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

strlit.markdown(
    "<h1 class='main-title'>🧪 Trạm Thí Nghiệm & Tri Thức 20/10 💖</h1>",
    unsafe_allow_html=True,
)
strlit.markdown(
    "<p class='subtitle'>Giải mã những công thức yêu thương dành riêng cho một nửa thế giới!</p>",
    unsafe_allow_html=True,
)

strlit.write("---")

# Chọn môn học
subject = strlit.selectbox(
    "🔬 Chọn lĩnh vực/môn học bạn muốn trải nghiệm:",
    [
        "Hóa học (Phản ứng xúc tác trái tim)",
        "Toán học (Hệ phương trình hạnh phúc)",
        "Vật lý (Định luật bảo toàn nụ cười)",
        "Văn học (Đoản khúc cảm xúc)",
        "Sinh học (ADN của sự hoàn hảo)",
    ],
)

strlit.write("")

if subject == "Hóa học (Phản ứng xúc tác trái tim)":
  strlit.subheader("🧪 Thí nghiệm: Tổng hợp hợp chất 'Yêu Thương'")
  strlit.write(
      "**Hướng dẫn:** Thêm dung dịch lòng chân thành ($CuSO_4$) kết hợp với bột nụ"
      " cười ($NaOH$) vào ống nghiệm."
  )

  col1, col2 = strlit.columns(2)
  with col1:
    chem1 = strlit.checkbox("Đổ dung dịch 💙 Chân thành")
  with col2:
    chem2 = strlit.checkbox("Thêm xúc tác ✨ Nụ cười")

  if strlit.button("🔥 Tiến hành đun nóng & Kích hoạt phản ứng"):
    if chem1 and chem2:
      with strlit.spinner("Đang tiến hành phản ứng nhiệt độ cao..."):
        time.sleep(1.5)
      strlit.balloons()
      strlit.markdown(
          """
                <div class='card'>
                <h3>💥 BỤP! Phản ứng hoàn tất!</h3>
                <p>Xuất hiện kết tủa màu hồng rực rỡ mang công thức hóa học:</p>
                <p><b>❤️ Chúc bạn một ngày 20/10 luôn lung linh, tỏa sáng như một ánh lửa bùng nổ, luôn vui vẻ và đạt được mọi ước mơ trong cuộc sống! ❤️</b></p>
                </div>
                """,
          unsafe_allow_html=True,
      )
    else:
      strlit.warning(
          "⚠️ Bạn chưa chọn đủ các thành phần hóa chất để kích hoạt phản ứng!"
      )

elif subject == "Toán học (Hệ phương trình hạnh phúc)":
  strlit.subheader("📐 Định lý & Hệ phương trình Thanh xuân")
  strlit.write(
      "**Hướng dẫn:** Giải hệ phương trình tọa độ trái tim để mở khóa ẩn số."
  )

  equation = strlit.text_input(
      "Nhập giá trị cần tìm (Gợi ý: Nhập từ 'love' hoặc '20/10'):"
  )

  if strlit.button("📐 Giải phương trình"):
    if equation.lower() in ["love", "20/10", "20-10"]:
      with strlit.spinner("Đang tính toán đạo hàm và tích phân nụ cười..."):
        time.sleep(1.2)
      strlit.snow()
      strlit.markdown(
          """
                <div class='card'>
                <h3>✨ Kết quả nghiệm tuyệt đối ($x = \\infty$):</h3>
                <p><b>📐 Chúc bạn luôn có độ dốc cuộc đời luôn hướng lên dương vô cực, niềm vui nhân đôi, muộn phiền triệt tiêu về 0 vào ngày 20/10 này nhé! 💖</b></p>
                </div>
                """,
          unsafe_allow_html=True,
      )
    else:
      strlit.error(
          "❌ Nghiệm chưa chính xác hoặc thiếu dữ kiện. Hãy thử nhập '20/10'"
          " xem sao nhé!"
      )

elif subject == "Vật lý (Định luật bảo toàn nụ cười)":
  strlit.subheader("⚡ Thí nghiệm: Gia tốc cảm xúc & Năng lượng tích cực")
  strlit.write(
      "**Hướng dẫn:** Kéo thanh trượt điều chỉnh nguồn điện năng lượng tích cực"
      " tích lũy."
  )

  energy_level = strlit.slider(
      "Mức độ năng lượng tích cực ($W$):", 0, 100, 50
  )

  if strlit.button("⚡ Đóng mạch điện"):
    with strlit.spinner("Dòng điện đang chạy qua mạch trái tim..."):
      time.sleep(1)
    strlit.balloons()
    strlit.markdown(
        f"""
            <div class='card'>
            <h3>⚡ Đã đạt mức năng lượng {energy_level}V!</h3>
            <p><b>💡 Chúc dòng điện hạnh phúc luôn lan tỏa trong không gian của bạn, tiếp thêm thật nhiều động lực, sức khỏe và năng lượng để chinh phục mọi thử thách! 🌸</b></p>
            </div>
            """,
        unsafe_allow_html=True,
    )

elif subject == "Văn học (Đoản khúc cảm xúc)":
  strlit.subheader("📖 Giải mã thông điệp qua từng con chữ")
  strlit.write(
      "**Hướng dẫn:** Nhấn nút để mở lá thư cổ điển được viết bằng bút mực tím."
  )

  if strlit.button("💌 Mở phong bì thư"):
    with strlit.spinner("Đang lật giở từng trang kỷ niệm..."):
      time.sleep(1)
    strlit.markdown(
        """
            <div class='card'>
            <h3>📜 Đoản khúc ngày 20/10:</h3>
            <p><i>"Tháng Mười về gió heo may ngập lối,<br>
            Chúc một nửa thế giới mãi bình yên.<br>
            Tươi như hoa nở bên thềm,<br>
            Ngập tràn hạnh phúc, ấm êm trọn đời."</i></p>
            <p><b>🌸 Chúc bạn ngày 20/10 thật trọn vẹn, luôn giữ nụ cười trên môi và viết tiếp những chương thật đẹp trong thanh xuân của mình! 💖</b></p>
            </div>
            """,
        unsafe_allow_html=True,
    )

elif subject == "Sinh học (ADN của sự hoàn hảo)":
  strlit.subheader("🧬 Giải mã chuỗi ADN hạnh phúc")
  strlit.write(
      "**Hướng dẫn:** Khớp các chuỗi nucleotide để kích hoạt mã gen tuyệt vời"
      " nhất."
  )

  gen_code = strlit.selectbox(
      "Chọn chuỗi mã gen:", ["A - T - G - X", "S - M - I - L - E", "L - O - V -"
      " E"]
  )

  if strlit.button("🔬 Phân tích chuỗi ADN"):
    with strlit.spinner("Đang quét kính hiển vi điện tử..."):
      time.sleep(1.2)
    strlit.balloons()
    strlit.markdown(
        f"""
            <div class='card'>
            <h3>🧬 Kết quả phân tích chuỗi [{gen_code}]:</h3>
            <p><b>✨ Mã gen của bạn được cấu thành từ sự dịu dàng, thông minh và tuyệt vời nhất. Chúc bạn ngày 20/10 ngập tràn hoa quà, yêu thương và luôn tự tin là chính mình! 🌷</b></p>
            </div>
            """,
        unsafe_allow_html=True,
    )

strlit.write("---")
strlit.markdown(
    "<p style='text-align: center; color: #888;'>Made with ❤️ for 20/10 using"
    " Streamlit & Python</p>",
    unsafe_allow_html=True,
                )
