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
    {"title": "No Poverty", "description": "", "topics": [
        {"topic": "Proportion of students receiving financial aid to attend university because of poverty", "description": "Persentase mahasiswa yang menerima bantuan keuangan karena kemiskinan, dengan fokus pada jumlah mahasiswa berpenghasilan rendah yang menerima bantuan tersebut.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "University anti-poverty programmes", "description": "Universitas menerapkan program anti-kemiskinan dengan menargetkan penerimaan dan keberhasilan mahasiswa dari kelompok pendapatan terbawah 20%, serta menyediakan dukungan seperti makanan, perumahan, transportasi, dan layanan hukum untuk mahasiswa berpenghasilan rendah, termasuk mahasiswa dari negara berpenghasilan rendah atau menengah ke bawah.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Community anti-poverty programmes", "description": "Universitas mendukung program anti-kemiskinan komunitas dengan memberikan bantuan untuk memulai bisnis berkelanjutan melalui edukasi, sumber daya, dan bantuan finansial, serta mengorganisir pelatihan untuk meningkatkan akses ke layanan dasar dan berpartisipasi dalam pembuatan kebijakan di berbagai tingkatan untuk mengakhiri kemiskinan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Zero Hunger", "description": "", "topics": [
        {"topic": "Campus food waste", "description": "Universitas melacak jumlah limbah makanan yang dihasilkan dari makanan yang disajikan di kampus, dengan pengukuran yang mencakup seluruh universitas atau sebagian, serta mencatat total limbah makanan dan populasi kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Student hunger", "description": "Universitas memiliki program untuk mengatasi ketidakamanan pangan dan kelaparan di kalangan mahasiswa, menyediakan intervensi seperti akses ke bank makanan, serta menawarkan pilihan makanan sehat, terjangkau, dan berkelanjutan di semua atau beberapa gerai makanan di kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of graduates in agriculture and aquaculture including sustainability aspects", "description": "Universitas mengukur proporsi lulusan dari program pertanian dan akuakultur yang mencakup aspek keberlanjutan, dengan menghitung jumlah total lulusan dan jumlah lulusan dari program yang mencakup keberlanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Good Health and Well-being", "description": "", "topics": [
        {"topic": "Number graduating in health professions ", "description": "Universitas menghitung jumlah lulusan di bidang profesi kesehatan dan menentukan proporsi mereka dibandingkan dengan total jumlah lulusan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Collaborations and health services", "description": "Universitas menjalin kolaborasi dengan institusi kesehatan lokal, nasional, dan global untuk meningkatkan kesehatan dan kesejahteraan. Mereka menyelenggarakan program penyuluhan kesehatan bagi komunitas lokal, kelompok terpinggirkan, dan komunitas pengungsi, serta berbagi fasilitas olahraga dengan masyarakat. Universitas menyediakan layanan kesehatan seksual dan reproduksi, serta dukungan kesehatan mental bagi mahasiswa dan staf, termasuk akses gratis atau berbayar. Selain itu, mereka menerapkan kebijakan kampus bebas rokok atau merokok di area tertentu.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "Community anti-poverty programmes", "description": "Universitas mendukung program anti-kemiskinan komunitas dengan memberikan bantuan untuk memulai bisnis berkelanjutan melalui edukasi, sumber daya, dan bantuan finansial, serta mengorganisir pelatihan untuk meningkatkan akses ke layanan dasar dan berpartisipasi dalam pembuatan kebijakan di berbagai tingkatan untuk mengakhiri kemiskinan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Quality Education", "description": "", "topics": [
        {"topic": "Proportion of graduates with teaching qualification ", "description": "Universitas mengukur proporsi lulusan yang memiliki kualifikasi yang relevan untuk mengajar dengan menghitung jumlah total lulusan dan jumlah lulusan yang mendapatkan kualifikasi untuk mengajar di tingkat sekolah dasar.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Lifelong learning measures", "description": "Universitas menyediakan akses gratis ke sumber daya pendidikan seperti komputer, perpustakaan, kursus online, dan kuliah untuk umum. Mereka menyelenggarakan acara publik dan pelatihan vokasional yang terbuka untuk umum, baik secara ad hoc maupun terjadwal, serta melakukan kegiatan pendidikan di luar kampus seperti kuliah dan demonstrasi di sekolah-sekolah dan komunitas. Universitas juga memiliki kebijakan akses pembelajaran sepanjang hayat yang inklusif, memastikan akses bagi semua orang tanpa memandang etnis, agama, disabilitas, status imigrasi, atau jenis kelamin.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of first-generation students", "description": "Universitas mengukur proporsi lulusan yang memiliki kualifikasi relevan untuk mengajar dengan menghitung jumlah mahasiswa yang memulai gelar dan jumlah mahasiswa generasi pertama yang memulai gelar.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Gender Equality", "description": "", "topics": [
        {"topic": "Proportion of graduates with teaching qualification ", "description": "Universitas mengukur proporsi lulusan dengan kualifikasi mengajar dan proporsi perempuan generasi pertama yang memulai gelar dengan menghitung jumlah total perempuan yang memulai gelar dan jumlah perempuan generasi pertama yang memulai gelar.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Student access measures", "description": "Universitas melacak secara sistematis tingkat aplikasi, penerimaan, atau masuknya perempuan. Mereka memiliki kebijakan, seperti rencana Akses dan Partisipasi, yang menangani aplikasi, penerimaan, masuk, dan partisipasi perempuan di universitas. Universitas juga menyediakan skema akses khusus untuk perempuan, termasuk mentoring, beasiswa, atau dukungan lainnya. Selain itu, mereka mendorong aplikasi perempuan di bidang-bidang yang kurang terwakili melalui kegiatan outreach universitas atau kolaborasi dengan universitas lain, kelompok komunitas, pemerintah, atau LSM dalam kampanye regional atau nasional.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of senior female academics", "description": "Universitas mengukur proporsi akademisi senior perempuan dengan menghitung jumlah total staf akademik senior dan jumlah staf akademik senior perempuan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of women receiving degrees", "description": "Universitas mengukur proporsi lulusan perempuan dengan menghitung jumlah total lulusan dan jumlah lulusan perempuan, serta memecahnya berdasarkan area studi (STEM, Kedokteran, Seni & Humaniora / Ilmu Sosial). Mereka juga menghitung jumlah lulusan dalam masing-masing area studi dan jumlah lulusan perempuan dalam masing-masing area studi tersebut (STEM, Kedokteran, Seni & Humaniora / Ilmu Sosial).", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Women’s progress measures", "description": "Universitas memiliki kebijakan non-diskriminasi terhadap perempuan dan juga kebijakan non-diskriminasi untuk orang transgender. Mereka memiliki kebijakan cuti hamil dan cuti ayah yang mendukung partisipasi perempuan, serta fasilitas penitipan anak yang mudah diakses bagi mahasiswa dan staf, baik gratis maupun berbayar. Universitas juga menyediakan skema mentoring khusus untuk perempuan, dengan partisipasi minimal 10% mahasiswa perempuan. Mereka melacak tingkat kelulusan perempuan dan memiliki skema untuk menutupi setiap kesenjangan yang ada, serta kebijakan yang melindungi pelapor diskriminasi dari kerugian pendidikan atau kerja.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Clean Water and Sanitation", "description": "", "topics": [
        {"topic": "Water consumption per person", "description": "Universitas mengukur total volume air yang digunakan, baik dari suplai utama, desalinasi, atau ekstraksi dari sungai, danau, atau akuifer, dengan mengukur secara keseluruhan atau sebagian, serta menghitung konsumsi air per orang dan volume air yang masuk ke universitas, disesuaikan dengan populasi kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Water usage and care", "description": "Universitas mengukur total volume air yang digunakan, baik dari suplai utama, desalinasi, atau ekstraksi dari sungai, danau, atau akuifer, dengan mengukur secara keseluruhan atau sebagian, serta menghitung konsumsi air per orang dan volume air yang masuk ke universitas, disesuaikan dengan populasi kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Water usage and care", "description": "Universitas memiliki kebijakan untuk memaksimalkan penggunaan ulang air di seluruh kampus dan mengukur penggunaan ulang air tersebut secara teratur.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Water in the community", "description": "Universitas menyediakan kesempatan pendidikan bagi komunitas lokal untuk belajar tentang manajemen air yang baik, baik secara gratis maupun berbayar. Mereka juga secara aktif mempromosikan penggunaan air yang sadar baik di kampus maupun di masyarakat luas. Universitas mendukung konservasi air di luar kampus dan menerapkan teknologi ekstraksi air yang berkelanjutan di lokasi universitas yang terkait dengan sumber air seperti akuifer, danau, atau sungai. Selain itu, universitas berkolaborasi dengan pemerintah lokal, regional, nasional, atau global dalam hal keamanan air, sesuai dengan kebutuhan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Affordable and Clean Energy", "description": "", "topics": [
        {"topic": "University measures towards affordable and clean energy", "description": "Universitas memiliki kebijakan untuk memastikan semua renovasi atau pembangunan baru mengikuti standar efisiensi energi, serta rencana untuk meningkatkan efisiensi energi bangunan yang ada. Mereka memiliki proses manajemen karbon dan pengurangan emisi karbon, serta rencana efisiensi energi untuk mengurangi konsumsi energi secara keseluruhan. Universitas juga melakukan tinjauan energi untuk mengidentifikasi area-area di mana pemborosan energi tertinggi terjadi. Selain itu, mereka memiliki kebijakan divestasi untuk mengalihkan investasi dari industri energi berintensitas karbon, khususnya batu bara dan minyak.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Energy use density", "description": "Universitas mengukur kepadatan penggunaan energi dengan menghitung konsumsi energi per meter persegi (m²) dari total energi yang digunakan, sebanding dengan luas lantai universitas.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Energy and the community", "description": "Universitas menyediakan program untuk komunitas lokal agar memahami pentingnya efisiensi energi dan energi bersih. Mereka juga mempromosikan komitmen publik untuk mencapai 100% energi terbarukan di luar lingkungan universitas. Universitas memberikan layanan langsung kepada industri lokal untuk meningkatkan efisiensi energi dan menggunakan energi bersih, termasuk penilaian efisiensi energi, workshop, dan penelitian tentang opsi energi terbarukan. Selain itu, universitas terlibat dalam pengembangan kebijakan teknologi energi bersih untuk mendukung pemerintah lokal, regional, nasional, dan global. Mereka juga memberikan bantuan bagi startup yang mendorong dan mendukung ekonomi atau teknologi beremisi rendah.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Decent Work and Economic Growth", "description": "", "topics": [
        {"topic": "Employment practice", "description": "Universitas mempraktikkan kebijakan untuk membayar semua staf dan fakultas setidaknya dengan upah hidup, yang didefinisikan sebagai upah hidup lokal atau indikator kemiskinan finansial lokal untuk keluarga empat orang (dinyatakan sebagai upah per jam). Mereka mengakui serikat pekerja dan hak-hak buruh (kebebasan berserikat dan negosiasi bersama) untuk semua, termasuk perempuan dan staf internasional. Universitas memiliki kebijakan untuk mengakhiri diskriminasi di tempat kerja, termasuk diskriminasi berdasarkan agama, seksualitas, gender, usia, atau status pengungsi.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Expenditure per employee", "description": "Pengeluaran per karyawan di universitas dihitung dengan membagi total pengeluaran universitas dengan jumlah karyawan yang ada.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of students taking work placements", "description": "Proporsi mahasiswa yang mengikuti magang kerja dihitung dengan membagi jumlah mahasiswa yang melakukan magang dengan jumlah total mahasiswa. Sedangkan jumlah mahasiswa yang melakukan magang selama lebih dari satu bulan adalah data terpisah yang mencatat jumlah mahasiswa yang melakukan magang dalam waktu yang lebih lama.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of employees on secure contracts", "description": "Proporsi karyawan dengan kontrak yang aman dihitung dengan membagi jumlah karyawan dengan kontrak yang aman (misalnya, kontrak lebih dari 24 bulan) dengan jumlah total karyawan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Industry, Innovation and Infrastructure", "description": "", "topics": [
        {"topic": "University spin offs", "description": "Jumlah spin-off universitas adalah jumlah perusahaan atau inisiatif bisnis yang didirikan berdasarkan teknologi atau inovasi yang berasal dari universitas itu sendiri.menerima bantuan keuangan karena kemiskinan, dengan fokus pada jumlah mahasiswa berpenghasilan rendah yang menerima bantuan tersebut.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Research income from industry and commerce", "description": "Pendapatan penelitian dari industri dan perdagangan adalah total pendapatan yang diperoleh universitas dari kegiatan penelitian yang didanai oleh industri dan perdagangan. Ini dapat dihitung per staf akademik untuk mengetahui rata-rata kontribusi setiap staf akademik dalam masing-masing bidang studi, seperti STEM, Kedokteran, dan Seni & Ilmu Sosial. Jumlah staf akademik dihitung berdasarkan bidang studi tertentu, seperti STEM, Kedokteran, dan Seni & Ilmu Sosial.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "Community anti-poverty programmes", "description": "Universitas mendukung program anti-kemiskinan komunitas dengan memberikan bantuan untuk memulai bisnis berkelanjutan melalui edukasi, sumber daya, dan bantuan finansial, serta mengorganisir pelatihan untuk meningkatkan akses ke layanan dasar dan berpartisipasi dalam pembuatan kebijakan di berbagai tingkatan untuk mengakhiri kemiskinan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Reduced Inequalities   ", "description": "", "topics": [
        {"topic": "First-generation students", "description": "Mahasiswa generasi pertama adalah mereka yang orangtuanya tidak pernah mengenyam pendidikan perguruan tinggi atau sarjana sebelumnya. Proporsi mahasiswa generasi pertama dihitung dengan membagi jumlah mahasiswa generasi pertama dengan jumlah total mahasiswa yang memulai gelar.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "International students from developing countries", "description": "Mahasiswa internasional dari negara-negara berkembang adalah mereka yang berasal dari negara-negara dengan ekonomi yang sedang berkembang. Proporsi mahasiswa internasional dari negara-negara berkembang dihitung dengan membagi jumlah mahasiswa internasional dari negara-negara berkembang dengan jumlah total mahasiswa.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of students with disabilities", "description": "Proporsi mahasiswa dengan disabilitas dihitung dengan membagi jumlah mahasiswa yang memiliki disabilitas dengan jumlah total mahasiswa.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of employees with disabilities", "description": "Proporsi karyawan dengan disabilitas dihitung dengan membagi jumlah karyawan yang memiliki disabilitas dengan jumlah total karyawan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Measures against discrimination", "description": "Universitas memiliki kebijakan penerimaan non-diskriminatif dan menjelaskan kebijakan positif diskriminasi. Mereka melacak aplikasi dan penerimaan dari kelompok-kelompok kurang terwakili seperti minoritas etnis, mahasiswa berpenghasilan rendah, mahasiswa non-tradisional, perempuan, mahasiswa LGBT, dan mahasiswa dengan disabilitas, serta mahasiswa pengungsi baru. Universitas juga menerapkan kebijakan anti-diskriminasi dan anti-pelecehan, serta mendukung kelompok-kelompok yang kurang terwakili melalui program mentoring, konseling, dan dukungan sebaya. Fasilitas yang dapat diakses bagi orang dengan disabilitas dan kebijakan akomodasi wajar juga tersedia.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Sustainable Cities ", "description": "", "topics": [
        {"topic": "Support of arts and heritage", "description": "Universitas ini berkomitmen untuk mendukung seni dan warisan budaya dengan menyediakan akses publik ke bangunan-bangunan bersejarah dan lanskap alam yang memiliki nilai budaya, dengan beberapa bangunan dapat diakses secara gratis. Perpustakaannya juga tersedia secara bebas dengan akses otomatis. Museum dan ruang pameran universitas dapat diakses secara permanen secara gratis untuk masyarakat umum, memungkinkan akses yang lebih luas terhadap seni dan artefak.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Expenditure on arts and heritage", "description": "Pertanyaan tersebut mengacu pada biaya atau pengeluaran yang dilakukan universitas untuk mendukung kegiatan seni dan warisan budaya. Biasanya mencakup biaya untuk mengelola fasilitas seni seperti teater, galeri seni, konser, serta proyek-proyek untuk memelihara dan merekam warisan budaya seperti tradisi lokal, bahasa, dan pengetahuan budaya yang tak berwujud.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Sustainable practices", "description": "Universitas telah mengambil langkah-langkah untuk menerapkan praktik berkelanjutan, termasuk mengukur dan menetapkan target untuk mempromosikan komuting berkelanjutan dan membangun bangunan baru dengan standar berkelanjutan. Mereka juga mempromosikan kerja jarak jauh untuk karyawan dan menyediakan perumahan terjangkau baik untuk karyawan maupun mahasiswa. Selain itu, universitas memberikan prioritas pada akses pejalan kaki di kampus dan bekerja sama dengan otoritas lokal untuk merencanakan pembangunan yang inklusif dan berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Responsible Consumption and Production", "description": "", "topics": [
        {"topic": "Operational measures", "description": "Universitas mengadopsi berbagai kebijakan operasional untuk memastikan sumber daya dan limbah dikelola secara etis dan berkelanjutan. Ini meliputi kebijakan pengadaan secara etis untuk makanan dan persediaan, serta kebijakan pembuangan limbah untuk bahan berbahaya dan pengurangan penggunaan plastik serta barang sekali pakai. Universitas juga menetapkan kebijakan agar praktik ini diperluas kepada layanan yang dioutsourcing dan ke supplier di rantai pasokan mereka.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of recycled waste", "description": "Universitas mengukur jumlah limbah yang dihasilkan dan didaur ulang di seluruh kampus untuk menentukan proporsi limbah yang didaur ulang. Data ini membantu dalam mengelola keberlanjutan lingkungan dan menilai dampak lingkungan kampus. Selain itu, universitas juga memantau jumlah limbah yang dikirim ke tempat pembuangan akhir, menunjukkan komitmen untuk mengurangi dampak lingkungan negatif dari limbah yang dihasilkan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Publication of a sustainability report", "description": "Universitas dapat memilih untuk menerbitkan laporan keberlanjutan secara tahunan, dua kali setahun (bi-annual), atau dengan frekuensi yang lebih jarang tergantung pada kebijakan internal dan kebutuhan untuk mengkomunikasikan pencapaian dan progres mereka dalam hal keberlanjutan. Laporan ini mencakup berbagai inisiatif dan hasil terkait dengan praktik berkelanjutan di seluruh universitas, seperti pengelolaan limbah, efisiensi energi, keberlanjutan lingkungan, dan upaya sosial.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Climate Action", "description": "", "topics": [
        {"topic": "Low-carbon energy use", "description": "Universitas melakukan pelacakan dan pengukuran penggunaan energi rendah karbon di seluruh kampusnya, dengan fokus pada penggunaan energi dari sumber-sumber rendah karbon. Data ini mencakup total energi yang digunakan dan persentase energi yang berasal dari sumber energi rendah karbon, seperti energi terbarukan dan teknologi energi bersih lainnya. Hal ini membantu universitas untuk mengukur dan memantau kemajuan mereka dalam mengadopsi praktik energi yang lebih berkelanjutan dan mengurangi jejak karbon mereka di lingkungan kampus.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Environmental education measures", "description": "Universitas memiliki program pendidikan lokal tentang risiko, dampak, mitigasi, adaptasi, pengurangan dampak, dan peringatan dini terkait perubahan iklim. Selain itu, universitas memiliki Rencana Aksi Iklim yang dibagi dengan pemerintah lokal dan kelompok masyarakat setempat untuk mengatasi dampak perubahan iklim. Universitas juga berpartisipasi dalam perencanaan bersama untuk bencana terkait perubahan iklim, termasuk kerjasama dengan pemerintah lokal dan regional serta organisasi non-pemerintah dalam adaptasi iklim dan peringatan dini terhadap risiko bencana.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Commitment to carbon neutral university", "description": "Universitas berkomitmen untuk mencapai status karbon netral dengan target tanggal tertentu sesuai dengan Protokol Gas Rumah Kaca, mencakup ruang lingkup 1, 2, dan 3. Upaya ini mencakup pengurangan emisi langsung dari sumber-sumber internal (ruang lingkup 1), emisi dari energi yang dibeli (ruang lingkup 2), dan emisi tidak langsung dari kegiatan seperti perjalanan dan pembuangan sampah (ruang lingkup 3). Target ini merupakan bagian dari strategi universitas dalam memimpin upaya mitigasi perubahan iklim di komunitas pendidikan dan sekitarnya.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Life Below Water", "description": "", "topics": [
        {"topic": "Supporting aquatic ecosystems through education", "description": "Universitas kami aktif dalam mendukung ekosistem akuatik melalui pendidikan masyarakat. Program-program edukasi kami mencakup ekosistem air tawar, praktik irigasi air, dan manajemen/konservasi air untuk komunitas lokal dan nasional. Kami juga menyediakan program pendidikan tentang manajemen berkelanjutan perikanan, akuakultur, dan pariwisata untuk memastikan keberlanjutan sumber daya ikan bagi masyarakat setempat. Selain itu, kami berkomitmen untuk meningkatkan kesadaran tentang masalah seperti penangkapan ikan berlebihan, penangkapan ikan secara ilegal, tidak dilaporkan, dan tidak diatur, serta praktik penangkapan ikan yang merusak, melalui kegiatan edukasi yang tersedia secara gratis bagi masyarakat lokal dan nasional.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Supporting aquatic ecosystems through action", "description": "Universitas ini aktif dalam mendukung ekosistem akuatik melalui tindakan nyata. Kami mendukung dan menyelenggarakan berbagai acara yang bertujuan untuk mempromosikan konservasi dan pemanfaatan berkelanjutan dari lautan, laut, dan sumber daya perairan lainnya. Selain itu, terdapat kebijakan untuk memastikan bahwa makanan yang berasal dari ekosistem akuatik yang ada di kampus dihasilkan secara berkelanjutan. Universitas ini juga terlibat langsung dalam menjaga dan memperluas keberagaman hayati ekosistem yang ada, baik tumbuhan maupun hewan, terutama ekosistem yang terancam. Selain itu, melakukan penelitian dan/atau berkolaborasi dengan industri untuk mengembangkan teknologi atau praktik yang membantu industri perikanan dalam meminimalkan atau mencegah kerusakan pada ekosistem akuatik.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Water sensitive waste disposal", "description": "Universitas ini menerapkan kebijakan yang ketat terkait dengan pengelolaan limbah sensitif terhadap air. Kami memiliki standar dan pedoman kualitas air untuk pembuangan limbah, yang bertujuan untuk menjaga kualitas air demi perlindungan ekosistem, satwa liar, serta kesehatan dan kesejahteraan manusia. Selain itu, universitas ini telah menetapkan rencana aksi untuk mengurangi limbah plastik di kampus, sebagai bagian dari komitmen kami terhadap keberlanjutan lingkungan. Kami juga memiliki kebijakan yang jelas untuk mencegah dan mengurangi polusi laut dari berbagai sumber, terutama dari aktivitas yang berasal dari daratan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Maintaining a local ecosystem", "description": "Universitas ini berkomitmen untuk menjaga ekosistem lokal dengan berbagai langkah konkret. Terdapat rencana untuk meminimalkan perubahan fisik, kimia, dan biologis dalam ekosistem akuatik terkait. Monitoring kesehatan ekosistem akuatik dilakukan secara rutin untuk memastikan keberlanjutan mereka. Universitas juga aktif mengembangkan dan mendukung program serta insentif yang mendorong praktik pengelolaan ekosistem akuatik yang baik, baik melalui program ad hoc maupun berkelanjutan. Kolaborasi dengan komunitas lokal dilakukan dalam upaya bersama untuk menjaga ekosistem akuatik yang kita bagi. Strategi pengelolaan daerah aliran sungai telah diimplementasikan berdasarkan keragaman spesies akuatik yang spesifik di lokasi universitas.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Life On Land", "description": "", "topics": [
        {"topic": "Supporting land ecosystems through education", "description": "Universitas ini aktif dalam mendukung ekosistem daratan melalui berbagai inisiatif pendidikan dan program. Acara-acara diselenggarakan untuk mempromosikan konservasi dan penggunaan lahan secara berkelanjutan, termasuk hutan dan lahan liar. Kebijakan juga telah diterapkan untuk memastikan bahwa makanan yang disediakan di kampus berasal dari praktik pertanian yang berkelanjutan. Selain itu, upaya langsung dilakukan untuk memelihara dan memperluas keanekaragaman hayati ekosistem yang ada, termasuk tumbuhan dan hewan yang menghadapi ancaman.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Supporting land ecosystems through action", "description": "Universitas ini mengambil langkah konkret untuk mendukung ekosistem daratan melalui berbagai kebijakan dan tindakan. Kebijakan telah diterapkan untuk memastikan konservasi, restorasi, dan penggunaan berkelanjutan dari ekosistem daratan yang terkait dengan universitas, termasuk hutan, pegunungan, dan daerah kering. Selain itu, terdapat kebijakan untuk mengidentifikasi, memantau, dan melindungi spesies yang terdaftar dalam IUCN Red List dan daftar konservasi nasional yang berada di area yang dipengaruhi oleh operasi universitas.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Land sensitive waste disposal", "description": "Untuk mengelola limbah secara sensitif terhadap lingkungan daratan, universitas telah menetapkan berbagai kebijakan yang mendukung praktik berkelanjutan. Ini termasuk memiliki standar dan panduan kualitas air untuk pengeluaran air, yang bertujuan untuk menjaga kualitas air demi perlindungan ekosistem, satwa liar, serta kesehatan dan kesejahteraan manusia. Selain itu, universitas memiliki kebijakan untuk mengurangi limbah plastik di kampus dan untuk membuang limbah berbahaya seperti bahan-bahan berbahaya dengan proses atau praktik yang sesuai.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": " Peace, Justice and Strong Institutions", "description": "", "topics": [
        {"topic": "University governance measures", "description": "Universitas ini menerapkan berbagai langkah dalam tata kelola mereka. Ini meliputi keberadaan perwakilan yang terpilih dari mahasiswa (baik sarjana maupun pascasarjana), fakultas, dan staf (pegawai non-fakultas) di badan pengelola tertinggi universitas. Selain itu, universitas mengakui keberadaan serikat mahasiswa independen yang memberikan masukan dalam tata kelola universitas, serta menyediakan dukungan untuk mahasiswa dalam berbagai aktivitas sosial.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Working with government", "description": "Bekerja dengan berbagai tingkat pemerintahan merupakan bagian integral dari strategi keterlibatan universitas ini. Mereka memberikan saran ahli khusus kepada pemerintah lokal, regional, dan nasional, menyediakan wawasan melalui panduan kebijakan, partisipasi dalam komite, dan penyediaan bukti. Selain itu, universitas mengadakan program outreach dan pendidikan untuk meningkatkan keterampilan dan pengetahuan para pembuat kebijakan dalam berbagai topik seperti ekonomi, hukum, teknologi, migrasi, perubahan iklim, dan lainnya.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Proportion of graduates in law and civil enforcement", "description": "Hal ini meliputi jumlah lulusan dari program-program terkait hukum dan penegakan hukum. Universitas akan melacak jumlah lulusan dari jurusan hukum serta program terkait penegakan hukum untuk memastikan kontribusi mereka dalam menghasilkan tenaga profesional yang siap berkontribusi dalam bidang hukum dan penegakan hukum di masyarakat.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
    ]},
    {"title": "Partnerships for the Goals", "description": "", "topics": [
        {"topic": "Relationships to support the goals", "description": "Universitas terlibat secara aktif dalam mendukung pencapaian Tujuan Pembangunan Berkelanjutan (SDGs) melalui beberapa inisiatif kolaboratif. Hal ini mencakup keterlibatan langsung dalam pengembangan kebijakan SDGs dengan pemerintah dan organisasi non-pemerintah regional, termasuk identifikasi masalah, pengembangan kebijakan, strategi, pemodelan masa depan dengan dan tanpa intervensi, serta pemantauan dan pelaporan terhadap intervensi yang dilakukan, untuk mendukung manajemen adaptif.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Publication of SDG reports", "description": "Universitas menerbitkan laporan SDG yang mencatat kemajuan terhadap setiap SDG secara terpisah dalam laporan tahunan, baik dalam laporan keseluruhan maupun laporan terpisah untuk setiap SDG. Laporan-laporan ini menunjukkan komitmen universitas dalam mengukur dan melaporkan perkembangan terhadap tujuan-tujuan pembangunan berkelanjutan secara transparan dan terstruktur.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        {"topic": "Education for the SDGs", "description": "Universitas memiliki komitmen untuk memberikan pendidikan yang bermakna tentang SDGs di seluruh kurikulumnya, yang relevan dan dapat diaplikasikan oleh semua mahasiswa. Pendidikan ini terintegrasi secara menyeluruh dalam kurikulum, baik bersifat wajib maupun opsional bagi semua mahasiswa. Selain itu, universitas juga menawarkan kursus khusus tentang keberlanjutan dan SDGs, baik dalam bentuk program penuh maupun mata kuliah pilihan. Untuk mencapai komunitas yang lebih luas, universitas melaksanakan kegiatan edukasi khusus bagi alumni, masyarakat lokal, dan orang-orang yang terdampak seperti pengungsi.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
        #{"topic": "National hunger", "description": "Universitas menyediakan akses gratis atau berbayar pada pengetahuan, keterampilan, dan teknologi tentang ketahanan pangan serta pertanian dan akuakultur berkelanjutan bagi petani dan produsen pangan lokal, mengadakan acara untuk transfer pengetahuan, memberikan akses ke fasilitas universitas, serta memprioritaskan pembelian produk dari sumber lokal yang berkelanjutan.", "question": "Apakah ada program kerja pada unit yang berkaitan dengan subtopik ini?"},
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
#st.title("SDG Form Application")
st.sidebar.title("Navigation")

# Sidebar navigation
if st.session_state.page == "Unit Selection":
    st.sidebar.write("Please select your unit and click 'Next'")
else:
    st.sidebar.write(f"{st.session_state.selected_option}")
    
    # Display SDG topics in the sidebar for navigation
    st.sidebar.write("## Sustainable Development Goals Topics")
    for i, sdg in enumerate(sdg_points):
        if st.sidebar.button(sdg["title"]):
            st.session_state.page = "SDG Entry"
            st.session_state.current_sdg_index = i
            st.rerun()

    if st.sidebar.button("Back to Unit Selection"):
        st.session_state.page = "Unit Selection"
        st.session_state.current_sdg_index = 0
        st.rerun()

# Unit selection
if st.session_state.page == "Unit Selection":
    st.image("https://raw.githubusercontent.com/DrSaragih/NewSGD-s/main/Sustainable_Development_Goals.png", caption="Selamat datang di Tujuan Pembangunan Berkelanjutan (TPB) Aplikasi Form")  # Replace with your image URL
    
    # Add a caption about the SDGs in Bahasa Indonesia
    st.markdown("""
    <div style='text-align: center;'>
    Tujuan Pembangunan Berkelanjutan (TPB) adalah kumpulan dari 17 tujuan global yang dirancang sebagai cetak biru untuk mencapai masa depan yang lebih baik dan berkelanjutan untuk semua. 
    TPB ditetapkan pada tahun 2015 oleh Majelis Umum Perserikatan Bangsa-Bangsa dan ditujukan untuk dicapai pada tahun 2030. 
    Mereka menangani tantangan global yang kita hadapi, termasuk kemiskinan, ketidaksetaraan, perubahan iklim, degradasi lingkungan, perdamaian, dan keadilan.
    </div>
    """, unsafe_allow_html=True)

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
            #options.append(faculty)
            options.extend(majors)

    selected_option = st.sidebar.selectbox("Choose your specific unit", options)

    if st.sidebar.button("Next"):
        st.session_state.selected_option = selected_option
        st.session_state.page = "SDG Entry"
        st.rerun()

# SDG Entry
if st.session_state.page == "SDG Entry":
    sdg_index = st.session_state.current_sdg_index
    sdg = sdg_points[sdg_index]

    st.header(f"Sustainable Development Goals Topics - {sdg['title']}")
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
                st.rerun()

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if sdg_index > 0 and st.button("Previous"):
            st.session_state.current_sdg_index -= 1
            st.rerun()
    with col2:
        if sdg_index < len(sdg_points) - 1:
            if st.button("Next"):
                st.session_state.current_sdg_index += 1
                st.rerun()
        else:
            if st.button("Final Submit"):
                st.session_state.sdg_complete = True
                st.session_state.page = "Summary"
                st.rerun()

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

        # Filter out empty programs
        filled_programs = [program for program in programs if program["program_name"] or program["year"] or program["pic"]]
        if filled_programs:
            if sdg_title not in grouped_data:
                grouped_data[sdg_title] = []

            grouped_data[sdg_title].append({
                "topic": topic_title,
                "programs": filled_programs
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
        st.rerun()
