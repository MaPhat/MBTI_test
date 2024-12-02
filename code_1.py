import streamlit as st

st.header("Bài kiểm tra MBTI")
I = 0
E = 0
S = 0
N = 0
T = 0
F = 0
J = 0
P = 0
text = ''

#Cặp đối lập E và I
cau1 = st.radio(
    "**1. Bạn cảm thấy thế nào khi tham gia một bữa tiệc lớn?**",
    ["Tôi cảm thấy vui vẻ và năng động", "Tôi cảm thấy mệt mỏi và muốn tìm một không gian yên tĩnh "],
    index=None
)
if cau1 == "Tôi cảm thấy vui vẻ và năng động":
    E += 1
else:
    I += 1

cau2 = st.radio(
    "**2. Sau một ngày làm việc bận rộn, bạn thích làm gì?**",
    ["Gặp gỡ bạn bè hoặc tham gia hoạt động xã hội", "Ngồi một mình và thư giãn "],
    index=None
)
if cau2 == "Gặp gỡ bạn bè hoặc tham gia hoạt động xã hội":
    E += 1
else:
    I += 1

cau3 = st.radio(
    "**3. Khi làm việc nhóm, bạn có xu hướng:**",
    ["Chủ động chia sẻ ý tưởng và tương tác với mọi người", "Lắng nghe và suy nghĩ trước khi đóng góp ý kiến "],
    index=None
)
if cau3 == "Chủ động chia sẻ ý tưởng và tương tác với mọi người":
    E += 1
else:
    I += 1

cau4 = st.radio(
    "**4. Bạn cảm thấy thế nào khi phải làm việc một mình?**",
    ["Tôi cảm thấy thoải mái và dễ dàng tập trung", "Tôi cảm thấy cô đơn và dễ bị mất động lực"],
    index=None
)
if cau4 == "Tôi cảm thấy cô đơn và dễ bị mất động lực":
    E += 1
else:
    I += 1

cau5 = st.radio(
    "**5. Bạn thường tìm năng lượng từ đâu?**",
    ["Từ việc giao tiếp với người khác", "Từ thời gian dành cho bản thân và sự yên tĩnh"],
    index=None
)
if cau5 == "Từ việc giao tiếp với người khác":
    E += 1
else:
    I += 1

cau6 = st.radio(
    "**6. Bạn có thích trò chuyện với người lạ không?**",
    ["Có, tôi dễ dàng bắt chuyện với người lạ", "Không, tôi cảm thấy ngượng ngùng khi phải bắt chuyện"],
    index=None
)
if cau6 == "Có, tôi dễ dàng bắt chuyện với người lạ":
    E += 1
else:
    I += 1

cau7 = st.radio(
    "**7. Sau một ngày dài, bạn có xu hướng:**",
    ["Tham gia hoạt động xã hội hoặc gọi điện cho bạn bè", "Tìm một nơi yên tĩnh và nghỉ ngơi"],
    index=None
)
if cau7 == "Tham gia hoạt động xã hội hoặc gọi điện cho bạn bè":
    E += 1
else:
    I += 1

cau8 = st.radio(
    "**8. Khi có một quyết định quan trọng, bạn thường:**",
    ["Thảo luận với người khác để tìm ra quyết định", "Suy nghĩ một mình và ra quyết định cá nhân "],
    index=None
)
if cau8 == "Thảo luận với người khác để tìm ra quyết định":
    E += 1
else:
    I += 1

cau9 = st.radio(
    "**9. Bạn cảm thấy như thế nào khi có một cuộc họp dài và cần tương tác với nhiều người?**",
    ["Hào hứng và năng động", "Mệt mỏi và muốn có một khoảng thời gian yên tĩnh sau đó"],
    index=None
)
if cau9 == "Hào hứng và năng động":
    E += 1
else:
    I += 1

cau10 = st.radio(
    "**10. Bạn thích tìm kiếm thông tin từ đâu?**",
    ["Từ cuộc trò chuyện và gặp gỡ người khác", "Từ sách vở hoặc nghiên cứu độc lập"],
    index=None
)
if cau10 == "Từ cuộc trò chuyện và gặp gỡ người khác":
    E += 1
else:
    I += 1

#Cặp đối lặp S và N
cau11 = st.radio(
    "**11. Khi bạn gặp một vấn đề mới, bạn thường:**",
    ["Tập trung vào các chi tiết và thông tin cụ thể", "Suy nghĩ về các khái niệm và những khả năng tiềm năng"],
    index=None
)
if cau11 == "Tập trung vào các chi tiết và thông tin cụ thể":
    S += 1
else:
    N += 1

cau12 = st.radio(
    "**12. Bạn cảm thấy thoải mái hơn khi làm gì?**",
    ["Xử lý các vấn đề thực tế, rõ ràng và đã biết", "Khám phá các ý tưởng mới và chưa biết"],
    index=None
)
if cau12 == "Xử lý các vấn đề thực tế, rõ ràng và đã biết":
    S += 1
else:
    N += 1

cau13 = st.radio(
    "**13. Khi đọc một cuốn sách, bạn thích:**",
    ["Những câu chuyện thực tế, dễ hiểu và dễ áp dụng", "Những câu chuyện hư cấu hoặc các ý tưởng phức tạp"],
    index=None
)
if cau13 == "Những câu chuyện thực tế, dễ hiểu và dễ áp dụng":
    S += 1
else:
    N += 1

cau14 = st.radio(
    "**14. Bạn cảm thấy thế nào về việc làm theo quy trình, hướng dẫn cụ thể?**",
    ["Tôi cảm thấy thoải mái và tự tin khi làm theo quy trình", "Tôi cảm thấy hạn chế và muốn tự mình khám phá"],
    index=None
)
if cau14 == "Tôi cảm thấy thoải mái và tự tin khi làm theo quy trình":
    S += 1
else:
    N += 1

cau15 = st.radio(
    "**15. Khi đưa ra quyết định, bạn sẽ:**",
    ["Dựa vào những dữ liệu thực tế và kinh nghiệm trong quá khứ", "Dựa vào cảm giác về những khả năng và triển vọng trong tương lai"],
    index=None
)
if cau15 == "Dựa vào những dữ liệu thực tế và kinh nghiệm trong quá khứ":
    S += 1
else:
    N += 1

cau16 = st.radio(
    "**16. Bạn thích công việc có tính chất:**",
    ["Được xác định rõ ràng với các quy trình và kế hoạch", "Có không gian sáng tạo và thử nghiệm"],
    index=None
)
if cau16 == "Được xác định rõ ràng với các quy trình và kế hoạch":
    S += 1
else:
    N += 1

cau17 = st.radio(
    "**17. Bạn thường cảm thấy dễ chịu hơn khi:**",
    ["Tập trung vào công việc hàng ngày, chi tiết cụ thể", "Tưởng tượng và khám phá những ý tưởng hoặc các khả năng chưa biết"],
    index=None
)
if cau17 == "Tập trung vào công việc hàng ngày, chi tiết cụ thể":
    S += 1
else:
    N += 1

cau18 = st.radio(
    "**18. Khi có một dự án, bạn thích:**",
    ["Đặt ra các mục tiêu cụ thể và hoàn thành từng bước một", "Khám phá nhiều cách tiếp cận khác nhau và tìm ra hướng đi sáng tạo"],
    index=None
)
if cau18 == "Đặt ra các mục tiêu cụ thể và hoàn thành từng bước một":
    S += 1
else:
    N += 1

cau19 = st.radio(
    "**19. Bạn thích làm việc với:**",
    ["Các dữ liệu cụ thể, dễ hiểu", "Các khái niệm trừu tượng và lý thuyết"],
    index=None
)
if cau19 == "Các dữ liệu cụ thể, dễ hiểu":
    S += 1
else:
    N += 1

#Bộ đối lập I và F
cau20 = st.radio(
    "**20. Khi phải đưa ra quyết định khó khăn, bạn sẽ:**",
    ["Xem xét các sự kiện và dữ liệu để đưa ra quyết định hợp lý", "Dựa vào cảm giác và tác động đến người khác để đưa ra quyết định"],
    index=None
)
if cau20 == "Xem xét các sự kiện và dữ liệu để đưa ra quyết định hợp lý":
    I += 1
else:
    F += 1

cau21 = st.radio(
    "**21. Bạn cảm thấy như thế nào khi giải quyết xung đột?**",
    ["Cố gắng đưa ra một giải pháp công bằng và hợp lý", "Quan tâm đến cảm xúc và nhu cầu của tất cả mọi người"],
    index=None
)
if cau21 == "Cố gắng đưa ra một giải pháp công bằng và hợp lý ":
    I += 1
else:
    F += 1

cau22 = st.radio(
    "**22. Khi có một vấn đề trong công việc, bạn:**",
    ["Phân tích các sự kiện một cách logic và khách quan", "Quan tâm đến cảm xúc của mọi người khi giải quyết vấn đề"],
    index=None
)
if cau22 == "Phân tích các sự kiện một cách logic và khách quan":
    I += 1
else:
    F += 1

cau23 = st.radio(
    "**23. Khi bạn đưa ra một quyết định lớn, bạn thường:**",
    ["Dựa vào sự phân tích và lý trí", "Cảm thấy quyết định của mình sẽ ảnh hưởng đến mọi người như thế nào"],
    index=None
)
if cau23 == "Dựa vào sự phân tích và lý trí":
    I += 1
else:
    F += 1

cau24 = st.radio(
    "**24. Bạn cảm thấy như thế nào khi đối mặt với những tình huống cần sự quyết đoán?**",
    ["Tôi cảm thấy thoải mái khi đưa ra quyết định nhanh chóng và chắc chắn", "Tôi muốn xem xét các yếu tố cảm xúc và tránh gây tổn thương cho người khác"],
    index=None
)
if cau24 == "Tôi cảm thấy thoải mái khi đưa ra quyết định nhanh chóng và chắc chắn":
    I += 1
else:
    F += 1

cau25 = st.radio(
    "**25. Khi đối mặt với một dự án, bạn thường:**",
    ["Tập trung vào mục tiêu và làm việc theo kế hoạch để hoàn thành công việc", "Quan tâm đến các yếu tố cảm xúc của nhóm và cách mọi người cảm thấy"],
    index=None
)
if cau25 == "Tập trung vào mục tiêu và làm việc theo kế hoạch để hoàn thành công việc":
    I += 1
else:
    F += 1

cau26 = st.radio(
    "**26. Bạn thích nhận phản hồi về công việc:**",
    ["Phản hồi rõ ràng và có tính xây dựng, với sự phân tích logic", "Phản hồi mang tính động viên và đồng cảm"],
    index=None
)
if cau26 == "Phản hồi rõ ràng và có tính xây dựng, với sự phân tích logic":
    I += 1
else:
    F += 1

cau27 = st.radio(
    "**27. Bạn cảm thấy thế nào về sự công bằng trong các quyết định?**",
    ["Công bằng có nghĩa là đưa ra quyết định dựa trên lý trí và sự công bằng", "Công bằng có nghĩa là quan tâm đến cảm xúc và nhu cầu của mọi người"],
    index=None
)
if cau27 == "Công bằng có nghĩa là đưa ra quyết định dựa trên lý trí và sự công bằng":
    I += 1
else:
    F += 1

cau28 = st.radio(
    "**28. Bạn thường giải quyết vấn đề bằng cách:**",
    ["Tìm ra một giải pháp hợp lý và thực tế", "Cảm thấy và lắng nghe ý kiến của người khác"],
    index=None
)
if cau28 == "Tìm ra một giải pháp hợp lý và thực tế":
    I += 1
else:
    F += 1
#Cặp đối lập J và P
cau29 = st.radio(
    "**29. Bạn thích lên kế hoạch cho các hoạt động trước không?**",
    ["Có, tôi thích biết rõ kế hoạch và tuân thủ thời gian", "Không, tôi thích linh hoạt và sẵn sàng thay đổi kế hoạch"],
    index=None
)
if cau29 == "Có, tôi thích biết rõ kế hoạch và tuân thủ thời gian":
    J += 1
else:
    P += 1
    
cau30 = st.radio(
    "**30. Khi làm việc, bạn thích:**",
    ["Có một kế hoạch rõ ràng và hoàn thành công việc theo thời gian", "Có thể thay đổi cách làm việc khi cần thiết"],
    index=None
)
if cau30 == "Có một kế hoạch rõ ràng và hoàn thành công việc theo thời gian":
    J += 1
else:
    P += 1

cau31 = st.radio(
    "**31. Bạn cảm thấy như thế nào về việc xử lý công việc đột xuất?**",
    ["Tôi thích biết trước và có chuẩn bị kỹ lưỡng", "Tôi thích giải quyết vấn đề khi chúng xuất hiện"],
    index=None
)
if cau31 == "Tôi thích biết trước và có chuẩn bị kỹ lưỡng":
    J += 1
else:
    P += 1

cau32 = st.radio(
    "**32. Khi có một dự án dài hạn, bạn thường:**",
    ["Lập kế hoạch chi tiết và bắt tay vào thực hiện ngay", "Bắt đầu dự án và thay đổi kế hoạch nếu cần"],
    index=None
)
if cau32 == "Lập kế hoạch chi tiết và bắt tay vào thực hiện ngay":
    J += 1
else:
    P += 1

cau33 = st.radio(
    "**33. Bạn cảm thấy thế nào khi mọi thứ không theo kế hoạch?**",
    ["Tôi cảm thấy khó chịu và muốn khôi phục lại trật tự", "Tôi cảm thấy thoải mái và linh hoạt, không có vấn đề gì"],
    index=None
)
if cau33 == "Tôi cảm thấy khó chịu và muốn khôi phục lại trật tự":
    J += 1
else:
    P += 1

cau34 = st.radio(
    "**34. Bạn thích làm việc theo cách:**",
    ["Cố gắng hoàn thành công việc càng sớm càng tốt và theo quy trình", "Để mọi thứ mở và làm việc khi cảm thấy hứng thú"],
    index=None
)
if cau34 == "Cố gắng hoàn thành công việc càng sớm càng tốt và theo quy trình":
    J += 1
else:
    P += 1

cau35 = st.radio(
    "**35. Bạn thường lên kế hoạch trước khi thực hiện một việc gì?**",
    ["Có, tôi thích mọi thứ được tổ chức", "Không, tôi thích làm theo cảm hứng và theo tình huống"],
    index=None
)
if cau35 == "Có, tôi thích mọi thứ được tổ chức":
    J += 1
else:
    P += 1

cau36 = st.radio(
    "**36. Bạn cảm thấy như thế nào khi có quá nhiều lựa chọn mở?**",
    ["Tôi cảm thấy hoang mang và muốn thu hẹp lại các lựa chọn", "Tôi cảm thấy phấn khích và thích tự do khám phá nhiều lựa chọn"],
    index=None
)
if cau36 == "Tôi cảm thấy hoang mang và muốn thu hẹp lại các lựa chọn":
    J += 1
else:
    P += 1

cau37 = st.radio(
    "**37. Bạn thích:**",
    ["Xem xét mọi thứ trước khi đưa ra quyết định", "Đưa ra quyết định khi tình huống phát sinh"],
    index=None
)
if cau37 == "Xem xét mọi thứ trước khi đưa ra quyết định":
    J += 1
else:
    P += 1

if st.button("Kết quả"):
    if E > I:
        text += 'E'
    else:
        text += 'I'

    if S > N:
        text += 'S'
    else:
        text += 'N'

    if T > F:
        text += 'T'
    else:
        text += 'F'

    if J > P:
        text += 'J'
    else:
        text += 'P'
    image = "Image/" + text + '.png'
    st.image(image)
