import streamlit as st

# Data for units
data = {
    "Direktorat": [
        "Direktorat Akademik", "Direktorat Pemelajaran", "Direktorat Kemahasiswaan",
        "Direktorat Digitalisasi", "Direktorat Manajemen Aset, Keuangan, dan Sarana Prasarana",
        "Direktorat Organisasi dan Sumber Daya Insani", "Direktorat Urusan Internasional, Kerja Sama, dan Alumni",
        "Direktorat Perencanaan Strategis dan Pemasaran", "Direktorat Pengelolaan Bisnis, Inovasi dan Kewirausahaan"
    ],
    "Lembaga": [
        "Lembaga Penjamin Mutu", "Lembaga Pengembangan Humaniora", "Lembaga Penelitian dan Pengabdian Kepada Masyarakat"
    ],
    "Fakultas dan Jurusan": {
        "Fakultas Ekonomi": ["Ekonomi Pembangunan", "Manajemen", "Akuntansi"],
        "Fakultas Filsafat": ["Filsafat", "Studi Humanitas"],
        "Fakultas Hukum": ["Hukum"],
        "Fakultas Ilmu Sosial dan Ilmu Politik": ["Administrasi Publik", "Administrasi Bisnis", "Hubungan Internasional"],
        "Fakultas Keguruan dan Ilmu Pendidikan": ["Pendidikan Guru"],
        "Fakultas Kedokteran": ["Kedokteran"],
        "Fakultas Teknik": ["Teknik Sipil", "Arsitektur"],
        "Fakultas Teknologi Industri": ["Teknik Industri", "Teknik Kimia", "Teknik Elektro"],
        "Fakultas Teknologi Informasi dan Sains": ["Teknik Informatika", "Matematika", "Fisika"],
        "Program Vokasi": ["Sarjana Terapan Bisnis Kreatif", "Sarjana Terapan Teknologi Rekayasa Pangan"]
    }
}

# SDG Points and Topics
sdg_points = [
    {"title": "No Poverty", "description": "End poverty in all its forms everywhere", "topics": [
        {"topic": "Proportion of students receiving financial aid to attend university because of poverty", "description": "Persentase mahasiswa yang menerima bantuan keuangan karena kemiskinan, dengan fokus pada jumlah mahasiswa berpenghasilan rendah yang menerima bantuan tersebut.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "University anti-poverty programmes", "description": "Universitas menerapkan program anti-kemiskinan dengan menargetkan penerimaan dan keberhasilan mahasiswa dari kelompok pendapatan terbawah 20%, serta menyediakan dukungan seperti makanan, perumahan, transportasi, dan layanan hukum untuk mahasiswa berpenghasilan rendah, termasuk mahasiswa dari negara berpenghasilan rendah atau menengah ke bawah.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Community anti-poverty programmes", "description": "Universitas mendukung program anti-kemiskinan komunitas dengan memberikan bantuan untuk memulai bisnis berkelanjutan melalui edukasi, sumber daya, dan bantuan finansial, serta mengorganisir pelatihan untuk meningkatkan akses ke layanan dasar dan berpartisipasi dalam pembuatan kebijakan di berbagai tingkatan untuk mengakhiri kemiskinan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition, and promote sustainable agriculture", "topics": [
        {"topic": "Campus food waste", "description": "Universitas melacak jumlah limbah makanan yang dihasilkan dari makanan yang disajikan di kampus, dengan pengukuran yang mencakup seluruh universitas atau sebagian, serta mencatat total limbah makanan dan populasi kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Student hunger", "description": "Universitas memiliki program untuk mengatasi ketidakamanan pangan dan kelaparan di kalangan mahasiswa, menyediakan intervensi seperti akses ke bank makanan, serta menawarkan pilihan makanan sehat, terjangkau, dan berkelanjutan di semua atau beberapa gerai makanan di kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of graduates in agriculture and aquaculture including sustainability aspects", "description": "Universitas mengukur proporsi lulusan dari program pertanian dan akuakultur yang mencakup aspek keberlanjutan, dengan menghitung jumlah total lulusan dan jumlah lulusan dari program yang mencakup keberlanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    # Add more SDG points and their topics as needed
]

# Initialize session state
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'unit_type' not in st.session_state:
    st.session_state.unit_type = None
if 'page' not in st.session_state:
    st.session_state.page = "Unit Selection"
if 'current_sdg_index' not in st.session_state:
    st.session_state.current_sdg_index = 0
if 'sdg_complete' not in st.session_state:
    st.session_state.sdg_complete = False
if 'program_inputs' not in st.session_state:
    st.session_state.program_inputs = {}
if 'add_program_key' not in st.session_state:
    st.session_state.add_program_key = {}

# Set up the Streamlit app
st.title("SDG Form Application")
st.sidebar.title("Navigation")

# Sidebar navigation
if st.session_state.page == "Unit Selection":
    st.sidebar.write("Please select your unit and click 'Next'")
else:
    st.sidebar.write(f"Selected Unit: {st.session_state.selected_option}")
    if st.button("Back to Unit Selection"):
        st.session_state.page = "Unit Selection"
        st.session_state.current_sdg_index = 0
        st.experimental_rerun()

# Unit selection
if st.session_state.page == "Unit Selection":
    unit_type = st.sidebar.selectbox(
        "Choose your unit type",
        ["Direktorat", "Lembaga", "Fakultas dan Jurusan"]
    )
    st.session_state.unit_type = unit_type

    options = []
    if unit_type == "Direktorat":
        options = data["Direktorat"]
    elif unit_type == "Lembaga":
        options = data["Lembaga"]
    elif unit_type == "Fakultas dan Jurusan":
        for faculty, majors in data["Fakultas dan Jurusan"].items():
            options.append(faculty)
            options.extend(majors)

    selected_option = st.sidebar.selectbox("Choose your specific unit", options)

    if st.sidebar.button("Next"):
        st.session_state.selected_option = selected_option
        st.session_state.page = "SDG Entry"
        st.experimental_rerun()

# SDG Entry
if st.session_state.page == "SDG Entry":
    sdg_index = st.session_state.current_sdg_index
    sdg = sdg_points[sdg_index]

    st.header(f"SDG Entry - {sdg['title']}")
    st.write(sdg["description"])

    # Display all subtopics for the current topic
    for topic_index, topic in enumerate(sdg["topics"]):
        st.write(f"### {topic['topic']}")
        st.write(topic["description"])  # Display subtopic description
        answer = st.radio(topic["question"], ("Yes", "No"), key=f"{sdg_index}_{topic_index}_question")

        if answer == "Yes":
            key = f"{sdg_index}_{topic_index}_add_program"
            if key not in st.session_state.add_program_key:
                st.session_state.add_program_key[key] = 0

            if (sdg_index, topic_index) not in st.session_state.program_inputs:
                st.session_state.program_inputs[(sdg_index, topic_index)] = []

            # Display program inputs
            for i in range(st.session_state.add_program_key[key]):
                program_inputs = st.session_state.program_inputs[(sdg_index, topic_index)]
                if len(program_inputs) <= i:
                    program_inputs.append({"program_name": "", "year": "", "pic": ""})

                with st.expander(f"Program {i+1}", expanded=True):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        program_name = st.text_input("Program Name", key=f"{sdg_index}_{topic_index}_name_{i}", value=program_inputs[i]["program_name"])
                    with col2:
                        year = st.text_input("Year of Implementation", key=f"{sdg_index}_{topic_index}_year_{i}", value=program_inputs[i]["year"])
                    with col3:
                        pic = st.text_input("Program PIC", key=f"{sdg_index}_{topic_index}_pic_{i}", value=program_inputs[i]["pic"])

                    st.session_state.program_inputs[(sdg_index, topic_index)][i] = {
                        "program_name": program_name,
                        "year": year,
                        "pic": pic
                    }
                    st.markdown("---")  # Add separator line

            # Add more program button
            if st.button("Add More Programs", key=f"{sdg_index}_{topic_index}_add"):
                st.session_state.add_program_key[key] += 1
                st.experimental_rerun()

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if sdg_index > 0 and st.button("Previous"):
            st.session_state.current_sdg_index -= 1
            st.experimental_rerun()
    with col2:
        if sdg_index < len(sdg_points) - 1:
            if st.button("Next"):
                st.session_state.current_sdg_index += 1
                st.experimental_rerun()
        else:
            if st.button("Final Submit"):
                st.session_state.sdg_complete = True
                st.session_state.page = "Summary"
                st.experimental_rerun()

# Summary Page
if st.session_state.page == "Summary":
    st.header("Summary of Program Activities")

    # Group the data by SDG point
    grouped_data = {}
    for (sdg_index, topic_index), programs in st.session_state.program_inputs.items():
        sdg = sdg_points[sdg_index]
        topic = sdg["topics"][topic_index]
        sdg_title = sdg["title"]
        topic_title = topic["topic"]

        if sdg_title not in grouped_data:
            grouped_data[sdg_title] = []

        grouped_data[sdg_title].append({
            "topic": topic_title,
            "programs": programs
        })

    # Display the grouped data in a summary table
    for sdg_title, topics in grouped_data.items():
        st.write(f"## {sdg_title}")

        for topic in topics:
            st.write(f"### {topic['topic']}")

            for i, program in enumerate(topic["programs"]):
                st.write(f"**Program {i+1}:**")
                st.write(f"Program Name: {program['program_name']}")
                st.write(f"Year of Implementation: {program['year']}")
                st.write(f"Program PIC: {program['pic']}")
                st.markdown("---")  # Add separator line

    # Option to export summary to Excel
    if st.button("Export to Excel"):
        # Code to export data to Excel
        pass

    # Back button to return to SDG Entry
    if st.button("Back to SDG Entry"):
        st.session_state.page = "SDG Entry"
        st.experimental_rerun()
