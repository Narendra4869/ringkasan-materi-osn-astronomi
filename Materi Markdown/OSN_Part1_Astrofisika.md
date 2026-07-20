# BAB I — ASTROFISIKA

## Daftar Isi Bab I

1. [Hukum Radiasi, Radiasi Benda Hitam, Efek Doppler, Spektrum EM](#1)
2. [Spektroskopi](#2)
3. [Fotometri](#3)
4. [Struktur Atom, Energi Ikat, Radioaktivitas, Neutrino](#4)
5. [Kesetimbangan Termodinamika, Gas Ideal, Transfer Energi, Luminositas](#5)
6. [Hukum Kuadrat-Terbalik, Magnitudo, Diagram H-R](#6)
7. [Radiasi Benda Hitam Detail: Rayleigh-Jeans, Planck, Wien, Stefan-Boltzmann](#7)
8. [Sifat Cahaya: Dualisme, Kirchhoff, Model Bohr, Doppler](#8)

---

<a name="1"></a>
## 1. Hukum Radiasi, Radiasi Benda Hitam, Efek Doppler, Spektrum EM

### A. Konsep Inti

Semua informasi astronomi (kecuali sampel *in-situ* dan gelombang gravitasi) datang dalam bentuk **radiasi elektromagnetik**. Tiga besaran radiasi paling mendasar yang wajib dibedakan:

- **Intensitas spesifik** $I_\nu$ — energi per satuan luas, waktu, sudut ruang, dan frekuensi. **Tidak berkurang dengan jarak** (dalam ruang hampa) — ini sering jadi jebakan soal OSN.
- **Fluks (flux density)** $F$ — energi per satuan luas per satuan waktu, diintegralkan atas semua arah datang. **Berkurang sebagai $1/r^2$**.
- **Luminositas** $L$ — total energi yang dipancarkan per satuan waktu ke segala arah (watt). Sifat intrinsik bintang, tidak bergantung jarak pengamat.

Hubungan: $L = 4\pi r^2 F(r)$ untuk sumber yang memancar isotropik.

**Spektrum elektromagnetik** terentang dari gelombang radio (λ terpanjang, E terendah) hingga sinar gamma (λ terpendek, E tertinggi): radio → mikro → inframerah → cahaya tampak (~400–700 nm) → ultraviolet → sinar-X → gamma. Atmosfer Bumi hanya "transparan" pada jendela optik dan sebagian jendela radio — ini alasan observatorium ruang angkasa penting untuk UV/X/gamma/sebagian IR.

**Efek Doppler** — pergeseran panjang gelombang akibat gerak relatif sumber-pengamat sepanjang garis pandang (*radial velocity*).

### B. Rumus Penting

| Nama | Rumus | Variabel | Satuan SI | Syarat berlaku |
|---|---|---|---|---|
| Hubungan fluks–luminositas | $F(r) = \dfrac{L}{4\pi r^2}$ | $F$: fluks, $L$: luminositas, $r$: jarak | W/m² | Sumber titik isotropik, ruang hampa (tanpa ekstingsi) |
| Doppler (non-relativistik) | $\dfrac{\Delta\lambda}{\lambda_0} = \dfrac{v_r}{c}$ | $v_r$: kecepatan radial (+ menjauh), $c$: laju cahaya | — | $v_r \ll c$ |
| Doppler relativistik | $\dfrac{\lambda_{obs}}{\lambda_0} = \sqrt{\dfrac{1+\beta}{1-\beta}}$, $\beta = v_r/c$ | | — | Untuk kecepatan tinggi (quasar, jet relativistik) |
| Energi foton | $E = h\nu = \dfrac{hc}{\lambda}$ | $h = 6{,}626\times10^{-34}$ J·s | J | Selalu (definisi foton) |

### C. Derivasi Singkat

**Hubungan fluks-luminositas:** energi total $L$ dipancarkan isotropik menyebar merata pada permukaan bola berjari-jari $r$ berluas $4\pi r^2$. Karena tidak ada energi yang hilang di ruang hampa, energi per satuan luas per satuan waktu pada radius itu adalah $F = L/(4\pi r^2)$ — inilah asal hukum kuadrat-terbalik.

**Efek Doppler non-relativistik:** jika sumber bergerak menjauh dengan $v_r$, setiap puncak gelombang berikutnya dipancarkan dari posisi yang sedikit lebih jauh, menambah jarak tempuh sebesar $v_r T$ (T = periode). Panjang gelombang teramati bertambah $\Delta\lambda = v_r T = v_r \lambda_0/c$, sehingga $\Delta\lambda/\lambda_0 = v_r/c$.

### D. Intuisi dan Interpretasi

- Intensitas tidak berkurang dengan jarak karena sudut ruang yang "dilihat" detektor mengecil sebanding $1/r^2$, tapi jumlah sumber pemancar yang masuk sudut pandang itu justru bertambah $r^2$ — dua efek saling meniadakan. Inilah mengapa **kecerahan permukaan Matahari tampak sama** dari Bumi maupun dari Mars (meski fluks totalnya beda jauh).
- Doppler **radial** saja yang menggeser panjang gelombang; komponen kecepatan tangensial (*transverse*) tidak menghasilkan pergeseran garis spektrum orde pertama.
- Pergeseran merah (*redshift*, menjauh) vs biru (*blueshift*, mendekat) — hati-hati: ini beda konsep dengan *redshift kosmologis* (Bab XI) yang disebabkan ekspansi ruang, bukan gerak lokal.

### E. Contoh Soal OSN

**Soal:** Garis Hα (λ₀ = 656,3 nm) suatu galaksi teramati pada 660,0 nm. Tentukan kecepatan radial galaksi dan arah geraknya (mendekat/menjauh).

**Penyelesaian:**
$$\Delta\lambda = 660{,}0 - 656{,}3 = 3{,}7 \text{ nm (bertambah → menjauh)}$$
$$v_r = c\frac{\Delta\lambda}{\lambda_0} = 3\times10^8 \times \frac{3{,}7}{656{,}3} \approx 1{,}69\times10^6 \text{ m/s} \approx 1690 \text{ km/s}$$
Galaksi ini **menjauh** (redshift) dengan $v_r \approx 1690$ km/s — konsisten dengan hukum Hubble untuk galaksi jauh (lihat Bab XI).

**Kesalahan umum:** siswa sering lupa tanda (mendekat = blueshift = $\Delta\lambda$ negatif) dan tertukar rumus non-relativistik vs relativistik saat $v_r$ mendekati $c$ (umum terjadi pada soal quasar/jet AGN).

---

<a name="2"></a>
## 2. Spektroskopi

### A. Konsep Inti

Spektrum bintang membawa informasi temperatur, komposisi kimia, kecepatan, tekanan, medan magnet, dan rotasi. Ada tiga jenis spektrum dasar, dirangkum **Hukum Kirchhoff**:

1. **Spektrum kontinu** — dipancarkan benda padat/cair/gas bertekanan tinggi yang panas (mis. permukaan bintang/fotosfer).
2. **Spektrum garis emisi** — gas panas bertekanan rendah, dilihat langsung (tanpa sumber cahaya kontinu di belakangnya) → menghasilkan garis-garis terang pada latar gelap.
3. **Spektrum garis absorpsi** — gas dingin bertekanan rendah di depan sumber kontinu → garis gelap pada latar terang kontinu. Inilah yang mendominasi spektrum bintang (gas kontinu dari fotosfer, diserap oleh atmosfer bintang yang lebih dingin di atasnya).

**Pelebaran garis spektrum (line broadening)** — garis spektral tidak pernah benar-benar tak berhingga tajam:
- **Pelebaran alami (natural broadening)** — konsekuensi Prinsip Ketidakpastian Heisenberg ($\Delta E \Delta t \gtrsim \hbar$); makin pendek umur keadaan tereksitasi, makin lebar garis.
- **Pelebaran Doppler termal** — gerak termal acak atom sepanjang garis pandang menghasilkan profil Gaussian.
- **Pelebaran tekanan (pressure/collisional broadening)** — tumbukan antar-partikel di gas rapat memperpendek waktu hidup fase koheren.
- **Pelebaran rotasi** — rotasi bintang membuat satu sisi mendekat (blueshift) dan sisi lain menjauh (redshift), melebarkan garis secara simetris.
- Profil gabungan disebut **profil Voigt** (kombinasi Lorentzian dari pelebaran alami/tekanan + Gaussian dari Doppler).

**Polarisasi** — cahaya terpolarisasi jika medan listriknya bergetar tidak merata ke semua arah. Terjadi pada: hamburan (langit biru), medan magnet kuat (efek Zeeman pada bintik Matahari, pulsar), sinkrotron dari elektron relativistik.

### B. Rumus Penting

| Nama | Rumus | Variabel | Keterangan |
|---|---|---|---|
| Lebar alami garis | $\gamma = \dfrac{1}{T_i} + \dfrac{1}{T_f}$ | $T_i, T_f$: waktu hidup rata-rata keadaan awal/akhir | dari relasi ketidakpastian $\Delta E \Delta t \approx \hbar$ |
| Profil Lorentzian | $I_\nu = \dfrac{\gamma}{2\pi}\dfrac{I_0}{(\nu-\nu_0)^2+\gamma^2/4}$ | | Bentuk garis akibat pelebaran alami/tekanan |
| Prinsip ketidakpastian | $\Delta x \Delta p_x \approx \hbar$; $\Delta E \Delta t \approx \hbar$ | $\hbar = h/2\pi$ | Dasar kuantum semua pelebaran garis |

### C. Derivasi Singkat

Dari relasi ketidakpastian energi-waktu, jika rerata umur keadaan tereksitasi adalah $T$, ketidakpastian energinya $\Delta E \approx \hbar/T$. Karena $E=h\nu$, ketidakpastian frekuensi $\Delta\nu = \Delta E/h$. Karena transisi punya keadaan awal dan akhir yang sama-sama tak-pasti, total lebar garis $\gamma = 1/T_i + 1/T_f$ (dalam satuan sudut, dikali $2\pi$ untuk versi frekuensi biasa).

### D. Intuisi dan Interpretasi

- **Hukum Kirchhoff** paling gampang diingat lewat analogi: gas panas rendah tekanan "menyanyikan nada murni" (garis emisi tajam); saat gas itu mendingin & menyerap dari sumber kontinu, ia "menyerap nada yang sama" (garis absorpsi di frekuensi identik) — makanya panjang gelombang emisi dan absorpsi suatu unsur selalu sama.
- Lebar garis rotasi memberi cara mengukur $v \sin i$ bintang (kecepatan rotasi proyeksi garis pandang) tanpa perlu meresolusi piringan bintang secara spasial — teknik penting untuk bintang jauh yang tampak seperti titik.
- Pelebaran tekanan lebih dominan di bintang deret utama bertekanan tinggi (kerdil), sedangkan bintang raksasa (tekanan rendah, atmosfer mengembang) punya garis lebih tajam — ini basis **klasifikasi luminositas Yerkes/MK** (Bab VIII).

### E. Contoh Soal OSN

**Soal:** Suatu garis spektrum punya lebar akibat pelebaran termal sesuai kecepatan termal atom hidrogen pada $T=6000$ K. Perkirakan $\Delta\lambda/\lambda$ untuk garis Hα ($\lambda_0=656{,}3$ nm), dengan $v_{th}=\sqrt{2kT/m_H}$.

**Penyelesaian:**
$$v_{th}=\sqrt{\frac{2(1{,}38\times10^{-23})(6000)}{1{,}67\times10^{-27}}} \approx \sqrt{9{,}9\times10^{7}} \approx 9{,}95\times10^3 \text{ m/s}$$
$$\frac{\Delta\lambda}{\lambda_0} \approx \frac{v_{th}}{c} = \frac{9{,}95\times10^3}{3\times10^8}\approx 3{,}3\times10^{-5}$$
$$\Delta\lambda \approx 656{,}3\times3{,}3\times10^{-5} \approx 0{,}022 \text{ nm}$$

**Kesalahan umum:** menyamakan pelebaran Doppler *termal* (acak, menghasilkan profil simetris Gaussian, terkait $T$ gas) dengan Doppler dari kecepatan radial *bulk* bintang (pergeseran garis secara keseluruhan, bukan pelebaran).

---

<a name="3"></a>
## 3. Fotometri

### A. Konsep Inti

Fotometri adalah pengukuran kuantitatif kecerahan benda langit. Sistem **magnitudo** adalah skala logaritmik terbalik: makin besar angka magnitudo, makin **redup** objeknya (warisan sejarah dari Hipparchus, bintang paling terang = magnitudo 1, paling redup terlihat mata = magnitudo 6).

- **Magnitudo semu (apparent, $m$)** — kecerahan yang teramati, bergantung jarak & ekstingsi.
- **Magnitudo absolut ($M$)** — kecerahan intrinsik, didefinisikan sebagai magnitudo semu andai objek berada tepat 10 parsek dari pengamat.
- **Indeks warna** (mis. $B-V$, $U-B$) — selisih magnitudo pada dua filter berbeda, mengukur temperatur permukaan tanpa perlu tahu jarak: bintang biru punya $B-V$ kecil/negatif (panas), bintang merah punya $B-V$ besar (dingin).
- **Ekstingsi atmosfer** — atmosfer Bumi meredupkan & memerahkan cahaya; makin besar jarak zenit (*airmass* $X$), makin besar ekstingsi.

### B. Rumus Penting

| Nama | Rumus | Variabel | Satuan | Syarat |
|---|---|---|---|---|
| **Skala magnitudo (Pogson)** | $m_1 - m_2 = -2{,}5\log_{10}\dfrac{F_1}{F_2}$ | $F$: fluks | mag | Definisi dasar skala magnitudo |
| **Modulus jarak** | $m - M = 5\log_{10}\left(\dfrac{r}{10\text{ pc}}\right)$ atau $m-M = 5\log_{10}r - 5$ | $r$ dalam parsek | mag | Tanpa ekstingsi |
| **Modulus jarak + ekstingsi** | $m-M = 5\log_{10}\left(\dfrac{r}{10\text{pc}}\right) + A$ | $A$: ekstingsi total (mag) | mag | Ada medium antarbintang |
| **Magnitudo absolut bolometrik** | $M_{bol}-M_{bol,\odot} = -2{,}5\log_{10}(L/L_\odot)$ | $L$: luminositas | mag | $M_{bol,\odot}\approx4{,}74$ |
| **Ekstingsi vs airmass** | $m = m_0 + kX$, $X=\sec z$ | $k$: koefisien ekstingsi, $z$: jarak zenit | mag | $z<70°$ (atmosfer datar) |
| **Hubungan warna–ekstingsi** | $A_V \approx 3{,}0\, E_{B-V}$ | $E_{B-V}=(B-V)-(B-V)_0$ | mag | Rerata medium antarbintang Galaksi |
| **Radius bintang (dari L, T)** | $L = 4\pi R^2 \sigma T_{eff}^4$ | $R$: radius, $T_{eff}$: temperatur efektif | — | Bintang sebagai benda hitam bola |

### C. Derivasi Singkat

**Skala Pogson:** ditetapkan agar selisih 5 magnitudo = faktor kecerahan tepat 100× (kesepakatan historis mendekati persepsi logaritmik mata manusia, hukum Weber-Fechner). Maka setiap 1 magnitudo = faktor $100^{1/5}\approx2{,}512$. Karena $100 = 100^{5/5}$, dan kita ingin $m_1-m_2 = -2{,}5\log_{10}(F_1/F_2)$: cek — jika $F_1/F_2=100$, maka $m_1-m_2=-2{,}5\times2=-5$ ✓ (objek lebih terang punya magnitudo lebih kecil).

**Modulus jarak:** dari hukum kuadrat-terbalik, $F(r)/F(10\text{pc}) = (10\text{pc}/r)^2$. Substitusi ke Pogson:
$$m-M = -2{,}5\log_{10}\frac{F(r)}{F(10)} = -2{,}5\log_{10}\left(\frac{10\text{pc}}{r}\right)^2 = 5\log_{10}\left(\frac{r}{10\text{pc}}\right)$$

### D. Intuisi dan Interpretasi

- Modulus jarak adalah "penggaris" utama astronomi jarak dekat–menengah: begitu $M$ diketahui (dari tipe spektrum, *standard candle*, dsb.) dan $m$ diukur, jarak langsung didapat.
- Warna ($B-V$) adalah termometer bintang yang **tidak butuh tahu jarak** — sangat berguna karena jarak sulit diukur tapi warna mudah.
- Ekstingsi selalu membuat bintang tampak **lebih redup dan lebih merah** dari aslinya — jika diabaikan, jarak yang dihitung dari modulus jarak akan **diremehkan** (underestimate) karena sebagian keredupan salah diatribusikan ke jarak, bukan debu.

### E. Contoh Soal OSN

**Soal:** Sebuah bintang memiliki magnitudo semu $V=8{,}2$ dan diketahui berjarak 250 pc. Ekstingsi menuju bintang tersebut adalah $A_V = 0{,}6$ mag. Hitung magnitudo absolut bintang.

**Penyelesaian:**
$$M = m - 5\log_{10}\left(\frac{r}{10\text{pc}}\right) - A_V = 8{,}2 - 5\log_{10}(25) - 0{,}6$$
$$\log_{10}25 = 1{,}398 \Rightarrow 5\times1{,}398=6{,}99$$
$$M = 8{,}2 - 6{,}99 - 0{,}6 = 0{,}61$$

**Kesalahan umum:** (1) lupa mengurangkan $A_V$ (paling sering!), (2) memakai $\log$ basis $e$ alih-alih basis 10, (3) tertukar tanda — magnitudo makin kecil = makin terang, jadi objek "lebih terang 5 magnitudo" berarti $\Delta m = -5$, bukan $+5$.

---

<a name="4"></a>
## 4. Struktur Atom, Energi Ikat, Radioaktivitas, Neutrino

### A. Konsep Inti

Atom terdiri dari inti (proton bermuatan $+e$, neutron netral) dikelilingi elektron. **Nomor atom** $Z$ = jumlah proton (identitas unsur kimia); **nomor massa** $A = Z+N$ (proton + neutron). Isotop = unsur sama ($Z$ sama), neutron beda.

**Energi ikat inti** — massa inti selalu **lebih kecil** dari jumlah massa nukleon penyusunnya secara terpisah (*mass defect*, $\Delta m$); selisih ini setara energi ikat lewat $E=\Delta m\,c^2$ — energi yang harus diberikan untuk memecah inti jadi nukleon bebas.

**Radioaktivitas** — inti tak stabil meluruh spontan (alfa, beta, gamma) mengikuti hukum peluruhan eksponensial, dicirikan **waktu paruh** $t_{1/2}$. Penting untuk penanggalan (mis. usia meteorit → usia Tata Surya) dan sebagai sumber panas interior planet.

**Neutrino** $[\text{Tambahan}]$ — partikel nyaris tak bermassa, tak bermuatan, berinteraksi sangat lemah, dihasilkan dalam reaksi fusi nuklir (rantai proton-proton, siklus CNO) dan peluruhan beta. Neutrino Matahari lolos hampir tanpa hambatan dari inti Matahari ke Bumi dalam ~8 menit (sementara foton butuh ~ratusan ribu tahun berdifusi keluar) — deteksinya memberi bukti langsung reaksi inti Matahari *saat ini*, bukan proksi tertunda seperti cahaya.

### B. Rumus Penting

| Nama | Rumus | Variabel | Satuan |
|---|---|---|---|
| Kesetaraan massa-energi | $E=mc^2$ | | J |
| Energi ikat inti | $E_b = \Delta m\, c^2 = [Zm_p+Nm_n-m_{inti}]c^2$ | $m_p,m_n$: massa proton/neutron | J |
| Hukum peluruhan radioaktif | $N(t)=N_0 e^{-\lambda t}$ | $\lambda$: konstanta peluruhan | — |
| Waktu paruh | $t_{1/2} = \dfrac{\ln 2}{\lambda}$ | | s |
| Aktivitas | $A=\lambda N$ | | Bq (peluruhan/s) |

### C. Derivasi Singkat

Hukum peluruhan: laju peluruhan sebanding jumlah inti tersisa, $dN/dt=-\lambda N$. Integrasi: $N(t)=N_0e^{-\lambda t}$. Waktu paruh dicari dari $N(t_{1/2})=N_0/2$: $e^{-\lambda t_{1/2}}=1/2 \Rightarrow t_{1/2}=\ln2/\lambda$.

### D. Intuisi dan Interpretasi

- Energi ikat per nukleon **maksimum di sekitar besi (Fe-56)** — inilah alasan fusi menghasilkan energi untuk unsur ringan (naik menuju puncak) sementara fisi menghasilkan energi untuk unsur berat (turun menuju puncak); ini fondasi nukleosintesis bintang (Bab VIII).
- "Masalah neutrino Matahari" historis (jumlah neutrino terdeteksi lebih sedikit dari prediksi) terpecahkan oleh osilasi neutrino (neutrino berubah jenis/*flavor* dalam perjalanan) — bukti fisika partikel di luar Model Standar sederhana, ditemukan lewat astronomi!

### E. Contoh Soal OSN

**Soal:** Sampel isotop punya waktu paruh 5730 tahun (karbon-14). Jika aktivitas awal sampel adalah $A_0$ dan setelah $t$ tahun aktivitasnya tinggal $0{,}25A_0$, berapa $t$?

**Penyelesaian:** $0{,}25 = (1/2)^n \Rightarrow n=2$ waktu paruh. $t = 2\times5730 = 11460$ tahun.

---

<a name="5"></a>
## 5. Kesetimbangan Termodinamika, Gas Ideal, Transfer Energi, Luminositas

### A. Konsep Inti

Interior bintang dimodelkan sebagai gas panas nyaris ideal dalam **kesetimbangan hidrostatik** — tekanan gas ke luar menahan gravitasi yang menekan ke dalam — dan **kesetimbangan termal** — energi yang dibangkitkan inti sama dengan energi yang mengalir keluar sebagai luminositas permukaan. Tiga mekanisme transfer energi di interior bintang:

1. **Radiasi** — foton berdifusi keluar lewat penyerapan-emisi ulang berulang kali (perjalanan zig-zag/*random walk* sangat lambat).
2. **Konveksi** — gerak massal gas panas naik & gas dingin turun (seperti air mendidih); dominan bila gradien temperatur radiatif terlalu curam (opasitas tinggi, mis. selubung bintang bermassa rendah, atau inti bintang masif).
3. **Konduksi** — biasanya tidak signifikan di bintang normal (penting di bintang kompak seperti katai putih, elektron terdegenerasi).

### B. Rumus Penting

| Nama | Rumus | Variabel | Syarat |
|---|---|---|---|
| Hukum gas ideal | $PV=Nk_BT$ atau $P=\dfrac{\rho k_B T}{\mu m_H}$ | $P$: tekanan, $\rho$: densitas, $\mu$: berat molekul rata-rata, $k_B$: konstanta Boltzmann | Gas non-degenerate, non-relativistik |
| Kesetimbangan hidrostatik | $\dfrac{dP}{dr}=-\dfrac{G m(r)\rho(r)}{r^2}$ | $m(r)$: massa dalam radius $r$ | Bintang statis (tak berdenyut) |
| Konservasi massa | $\dfrac{dm}{dr}=4\pi r^2\rho(r)$ | | Selalu (definisi) |
| Konservasi energi (luminositas) | $\dfrac{dL}{dr}=4\pi r^2\rho(r)\,\varepsilon(r)$ | $\varepsilon$: laju pembangkitan energi per satuan massa | Kesetimbangan termal |
| Transpor energi radiatif | $\dfrac{dT}{dr}=-\dfrac{3\kappa\rho}{4ac T^3}\dfrac{L(r)}{4\pi r^2}$ | $\kappa$: opasitas, $a$: konstanta radiasi | Transpor didominasi radiasi |

*(Keempat persamaan pertama + persamaan transpor energi adalah "empat/lima persamaan struktur bintang" — akan dibahas mendalam di Bab VIII dengan syarat batas dan solusi model.)*

### C. Derivasi Singkat

**Kesetimbangan hidrostatik:** tinjau lapisan gas tipis setebal $dr$ pada radius $r$ dengan luas penampang $A$. Gaya gravitasi ke dalam pada lapisan tersebut adalah $GM(r)\,dm/r^2$ dengan $dm=\rho A\,dr$; gaya tekanan neto ke luar adalah $-A\,dP$ (tekanan berkurang keluar). Menyamakan (kesetimbangan, percepatan nol):
$$-A\,dP = \frac{GM(r)\rho A\,dr}{r^2} \Rightarrow \frac{dP}{dr}=-\frac{GM(r)\rho}{r^2}$$

### D. Intuisi dan Interpretasi

- Tanda minus pada $dP/dr$ artinya tekanan **selalu berkurang keluar** — masuk akal karena makin ke luar, makin sedikit massa yang "ditopang".
- Bintang adalah pertarungan abadi gravitasi (menekan) vs tekanan gas+radiasi (menahan) — begitu bahan bakar fusi habis, kesetimbangan runtuh → evolusi akhir bintang (Bab VIII).
- Konveksi muncul ketika radiasi "tidak cukup efisien" mengangkut energi — kriteria Schwarzschild membandingkan gradien temperatur adiabatik vs radiatif (detail di Bab VIII).

### E. Contoh Soal OSN

**Soal (konseptual):** Mengapa inti Matahari menggunakan transpor radiatif sedangkan selubung luarnya konvektif?

**Jawaban:** Di inti, gas terionisasi penuh dan opasitas relatif rendah sehingga foton dapat berdifusi (meski lambat) — radiasi cukup efisien. Di selubung luar, temperatur lebih rendah sehingga rekombinasi parsial hidrogen/helium meningkatkan opasitas drastis (elektron terikat menyerap foton lebih efektif); radiasi jadi tidak efisien, gradien temperatur radiatif jadi lebih curam dari gradien adiabatik → gas jadi tidak stabil dan mulai bergolak (konveksi) untuk mengangkut kelebihan energi.

---

<a name="6"></a>
## 6. Hukum Kuadrat-Terbalik, Intensitas, Kecerlangan-Jarak, Magnitudo, Radius Bintang, Diagram H-R

### A. Konsep Inti

Bagian ini menyatukan konsep-konsep §1 dan §3 menjadi alat praktis: bagaimana luminositas, jarak, temperatur, dan radius saling berkaitan lewat pengukuran yang bisa dilakukan pengamat.

**Diagram Hertzsprung-Russell (H-R)** memplot luminositas (atau magnitudo absolut) vs temperatur efektif (atau tipe spektral/indeks warna) untuk populasi bintang. Ini adalah "peta" evolusi bintang paling penting dalam astrofisika:

- **Deret utama (main sequence)** — pita diagonal tempat ~90% bintang (termasuk Matahari) menghabiskan sebagian besar hidupnya membakar hidrogen di inti.
- **Raksasa (giants) & maharaksasa (supergiants)** — di kanan atas: dingin tapi sangat terang → radius besar (dari $L=4\pi R^2\sigma T^4$).
- **Katai putih (white dwarfs)** — di kiri bawah: panas tapi redup → radius sangat kecil.

### B. Rumus Penting

(Lihat tabel lengkap di §3B — magnitudo, modulus jarak, radius dari $L$ dan $T_{eff}$ — semua berlaku di sini.) Tambahan:

| Nama | Rumus | Keterangan |
|---|---|---|
| Radius relatif ke Matahari | $\dfrac{R}{R_\odot}=\sqrt{\dfrac{L/L_\odot}{(T_{eff}/T_{eff,\odot})^4}}$ | Diturunkan dari $L=4\pi R^2\sigma T^4$, sangat sering dipakai di OSN |

### D. Intuisi dan Interpretasi

Garis-garis diagonal pada diagram H-R (jika sumbu $\log L$ vs $\log T_{eff}$) mewakili **radius konstan** — karena $L\propto R^2T^4$, garis $R$=konstan berbentuk garis lurus miring di ruang log-log. Ini alasan raksasa merah (dingin tapi terang) berada jauh dari deret utama: mereka *harus* punya radius sangat besar untuk mengimbangi temperatur rendah dan tetap terang.

### E. Contoh Soal OSN

**Soal:** Bintang raksasa memiliki $T_{eff}=4000$ K (Matahari: 5778 K) dan luminositas $100\,L_\odot$. Berapa radiusnya dalam $R_\odot$?

**Penyelesaian:**
$$\frac{R}{R_\odot}=\sqrt{\frac{100}{(4000/5778)^4}} = \sqrt{\frac{100}{0{,}230}} \approx \sqrt{435} \approx 20{,}8$$
Radius bintang ini ≈ 21 kali radius Matahari — konsisten dengan klasifikasi raksasa.

---

<a name="7"></a>
## 7. Radiasi Benda Hitam: Rayleigh-Jeans, Planck, Wien, Stefan-Boltzmann, Kelas Spektrum & Luminositas

### A. Konsep Inti

**Benda hitam (blackbody)** adalah idealisasi penyerap & pemancar sempurna — spektrumnya hanya bergantung pada satu parameter: **temperatur**. Bintang mendekati benda hitam dengan cukup baik (meski ada garis absorpsi di atasnya). Sejarah fisika kuantum lahir dari usaha menjelaskan spektrum ini:

- **Hukum Rayleigh-Jeans** (klasik, fisika sebelum kuantum) — cocok di panjang gelombang panjang, tapi meramalkan energi tak berhingga di UV (**bencana ultraviolet**) — gagal total di λ pendek.
- **Hukum Planck** — solusi kuantum penuh, mengasumsikan energi radiasi terkuantisasi $E=h\nu$; cocok di semua panjang gelombang, dan menjadi dasar seluruh fisika kuantum modern.
- **Hukum pergeseran Wien** — panjang gelombang puncak emisi berbanding terbalik dengan temperatur (diturunkan dari memaksimumkan fungsi Planck).
- **Hukum Stefan-Boltzmann** — total energi yang dipancarkan (integral fungsi Planck atas semua λ) sebanding $T^4$.

**Kelas spektrum bintang** (deret Harvard, dari panas ke dingin): **O B A F G K M** (mnemonic populer: "*Oh Be A Fine Girl/Guy, Kiss Me*"), dengan subkelas 0–9. Kelas luminositas (Yerkes/MK) memakai angka Romawi: **I** (maharaksasa) hingga **V** (deret utama/katai), membedakan bintang bertemperatur sama tapi radius/tekanan atmosfer beda (lewat lebar garis, §2).

| Kelas | Temperatur (K) | Warna | Ciri garis utama |
|---|---|---|---|
| O | >30.000 | Biru | He II terionisasi |
| B | 10.000–30.000 | Biru-putih | He I netral |
| A | 7.500–10.000 | Putih | H (Balmer) sangat kuat |
| F | 6.000–7.500 | Putih-kuning | Logam terionisasi (Ca II) |
| G | 5.200–6.000 | Kuning (Matahari: G2V) | Ca II H&K kuat |
| K | 3.700–5.200 | Oranye | Garis logam netral, molekul mulai |
| M | <3.700 | Merah | Pita molekul (TiO) |

### B. Rumus Penting

| Nama | Rumus | Variabel | Syarat |
|---|---|---|---|
| **Hukum Rayleigh-Jeans** | $B_\nu(T)=\dfrac{2\nu^2 k_BT}{c^2}$ | | Hanya valid $h\nu \ll k_BT$ (λ panjang) |
| **Hukum Planck** | $B_\nu(T)=\dfrac{2h\nu^3}{c^2}\dfrac{1}{e^{h\nu/k_BT}-1}$ atau $B_\lambda(T)=\dfrac{2hc^2}{\lambda^5}\dfrac{1}{e^{hc/\lambda k_BT}-1}$ | $B$: intensitas spesifik benda hitam | Selalu (bentuk umum, eksak) |
| **Hukum pergeseran Wien** | $\lambda_{max}\,T = b = 2{,}8978\times10^{-3}$ m·K | $\lambda_{max}$: panjang gelombang puncak | Untuk $B_\lambda$ (bukan $B_\nu$! puncaknya beda karena Jacobian $d\lambda$ vs $d\nu$) |
| **Hukum Stefan-Boltzmann** | $F = \sigma T^4$ (fluks permukaan); $L=4\pi R^2\sigma T_{eff}^4$ | $\sigma=5{,}67\times10^{-8}$ W/m²K⁴ | Benda hitam sempurna, atau $T_{eff}$ efektif bintang nyata |

### C. Derivasi Singkat

**Wien dari Planck:** maksimumkan $B_\lambda(T)$ terhadap $\lambda$: set $\dfrac{d B_\lambda}{d\lambda}=0$. Substitusi $x=hc/(\lambda k_BT)$ menghasilkan persamaan transendental $xe^x/(e^x-1)=5$, yang solusi numeriknya $x\approx4{,}965$. Maka $\lambda_{max}T = hc/(4{,}965\,k_B) = b \approx2{,}898\times10^{-3}$ m·K.

**Stefan-Boltzmann dari Planck:** integralkan $B_\nu(T)$ atas semua frekuensi dan atas sudut ruang $\pi$ (setengah bola, radiasi keluar):
$$F=\pi\int_0^\infty B_\nu(T)\,d\nu = \pi\frac{2h}{c^2}\int_0^\infty \frac{\nu^3\,d\nu}{e^{h\nu/k_BT}-1}$$
Substitusi $x=h\nu/k_BT$ mengubah integral menjadi $\int_0^\infty \frac{x^3}{e^x-1}dx = \pi^4/15$ (integral baku), menghasilkan $F=\sigma T^4$ dengan $\sigma = \dfrac{2\pi^5 k_B^4}{15h^3c^2}$.

### D. Intuisi dan Interpretasi

- Rayleigh-Jeans adalah **limit klasik** Planck untuk $h\nu\ll k_BT$ — cek: untuk $x=h\nu/k_BT\to0$, $e^x-1\approx x$, sehingga $B_\nu\to\dfrac{2h\nu^3}{c^2}\cdot\dfrac{1}{x}=\dfrac{2\nu^2k_BT}{c^2}$ — cocok dengan Rayleigh-Jeans. Ini cara cepat verifikasi/derivasi cepat saat lupa rumus persis di ujian.
- Wien: bintang panas memancar puncak di λ pendek (biru/UV), bintang dingin di λ panjang (merah/IR) — cara cepat menaksir $T_{eff}$ dari warna tanpa spektroskopi detail.
- Stefan-Boltzmann $T^4$: sangat sensitif — bintang 2× lebih panas memancar **16×** lebih terang per satuan luas.
- **Peringatan notasi krusial:** $\lambda_{max}$ dari $B_\lambda$ TIDAK sama dengan $c/\nu_{max}$ dari $B_\nu$ — soal OSN sering menjebak dengan meminta konversi ini.

### E. Contoh Soal OSN

**Soal:** Bintang memancar sebagai benda hitam dengan puncak spektrum pada $\lambda_{max}=290$ nm. (a) Berapa $T_{eff}$-nya? (b) Jika radiusnya $2R_\odot$, berapa luminositasnya dalam $L_\odot$?

**Penyelesaian (a):**
$$T = \frac{b}{\lambda_{max}} = \frac{2{,}898\times10^{-3}}{290\times10^{-9}} \approx 9993 \text{ K} \approx 10.000 \text{ K (kelas B/A)}$$

**Penyelesaian (b):**
$$\frac{L}{L_\odot} = \left(\frac{R}{R_\odot}\right)^2\left(\frac{T}{T_\odot}\right)^4 = (2)^2\left(\frac{10000}{5778}\right)^4 \approx 4\times 8{,}96 \approx 35{,}8\,L_\odot$$

**Kesalahan umum:** memasukkan $T$ dalam Celsius alih-alih Kelvin (fatal karena hukum radiasi selalu pakai T mutlak); lupa memangkatkan 4 pada rasio temperatur.

---

<a name="8"></a>
## 8. Sifat Cahaya: Dualisme Gelombang-Partikel, Hukum Kirchhoff, Model Atom Bohr, Efek Doppler

### A. Konsep Inti

**Dualisme gelombang-partikel** — cahaya berperilaku sebagai gelombang (interferensi, difraksi, polarisasi — dijelaskan oleh $\lambda,\nu$) sekaligus partikel/foton diskret (efek fotolistrik, hamburan Compton — dijelaskan oleh $E=h\nu$, momentum $p=h/\lambda$). Prinsip komplementer ini juga berlaku untuk materi (elektron, dsb.) — dasar mekanika kuantum modern, termasuk model atom.

**Model atom Bohr** (untuk hidrogen) — lihat §1 buku sumber untuk turunan lengkap tingkat energi $E_n=-13{,}6\text{ eV}/n^2$ dan deret spektral (Lyman, Balmer, Paschen, dst.) — detail derivasi ada di bagian Spektroskopi (§2) dan referensi utama.

**Tiga Hukum Kirchhoff tentang spektrum** (ringkasan praktis dari §2):
1. Benda padat/cair/gas rapat panas → spektrum kontinu.
2. Gas panas renggang → spektrum garis emisi.
3. Sumber kontinu dilihat lewat gas dingin renggang → spektrum garis absorpsi (garis di panjang gelombang sama seperti pada hukum 2).

### B. Rumus Penting

| Nama | Rumus | Keterangan |
|---|---|---|
| Energi foton | $E=h\nu=hc/\lambda$ | Aspek partikel |
| Momentum foton | $p=h/\lambda$ | Dipakai pada tekanan radiasi (Bab VI) |
| Tingkat energi Bohr | $E_n = -\dfrac{13{,}6\text{ eV}}{n^2} = -2{,}18\times10^{-18}/n^2$ J | Hanya eksak untuk atom mirip-hidrogen (1 elektron) |
| Rumus deret spektral | $\dfrac{1}{\lambda}=R\left(\dfrac{1}{n_1^2}-\dfrac{1}{n_2^2}\right)$ | $R=1{,}097\times10^7$ m⁻¹ (Rydberg), $n_2>n_1$ |

### D. Intuisi dan Interpretasi

- Setiap unsur kimia punya "sidik jari" spektral unik karena struktur tingkat energinya unik — inilah dasar penentuan komposisi kimia bintang jauh tanpa perlu menyentuhnya sama sekali.
- Deret Lyman ($n_1=1$, UV), Balmer ($n_1=2$, tampak — makanya paling terkenal dalam spektroskopi bintang optik), Paschen ($n_1=3$, IR) — makin besar $n_1$, makin panjang gelombangnya (energi transisi makin kecil).
- Dualisme gelombang-partikel bukan "cahaya kadang gelombang kadang partikel bergantian" — melainkan satu entitas kuantum yang deskripsi klasiknya (gelombang ATAU partikel) hanya cocok pada eksperimen tertentu.

### E. Contoh Soal OSN

**Soal:** Hitung panjang gelombang foton yang dipancarkan saat elektron hidrogen turun dari $n=3$ ke $n=2$ (garis Hα, bagian deret Balmer).

**Penyelesaian:**
$$\frac{1}{\lambda}=R\left(\frac{1}{2^2}-\frac{1}{3^2}\right)=1{,}097\times10^7\left(\frac{1}{4}-\frac{1}{9}\right)=1{,}097\times10^7\times0{,}1389$$
$$\frac{1}{\lambda}\approx1{,}524\times10^6 \text{ m}^{-1} \Rightarrow \lambda \approx 656{,}3\text{ nm}$$
Ini persis garis Hα (merah) yang dipakai di §1 dan §2 — konsisten dan sering muncul lintas-topik di soal OSN.

---

## Daftar Rumus Ringkas — Bab I Astrofisika

**Radiasi & Doppler**
- $F=L/4\pi r^2$
- $\Delta\lambda/\lambda_0 = v_r/c$ (non-relativistik)
- $E=h\nu=hc/\lambda$, $p=h/\lambda$

**Benda Hitam**
- Planck: $B_\nu=\dfrac{2h\nu^3}{c^2}\dfrac{1}{e^{h\nu/k_BT}-1}$
- Wien: $\lambda_{max}T=2{,}898\times10^{-3}$ m·K
- Stefan-Boltzmann: $F=\sigma T^4$, $L=4\pi R^2\sigma T_{eff}^4$
- Rayleigh-Jeans (limit λ panjang): $B_\nu=2\nu^2k_BT/c^2$

**Fotometri**
- Pogson: $m_1-m_2=-2{,}5\log_{10}(F_1/F_2)$
- Modulus jarak: $m-M=5\log_{10}(r/10\text{pc})\;[+A]$
- $M_{bol}-M_{bol,\odot}=-2{,}5\log_{10}(L/L_\odot)$
- $A_V\approx3{,}0E_{B-V}$

**Atom Bohr / Rydberg**
- $E_n=-13{,}6\text{eV}/n^2$
- $1/\lambda=R(1/n_1^2-1/n_2^2)$

**Struktur Bintang (pengantar)**
- Hidrostatik: $dP/dr=-GM(r)\rho/r^2$
- Massa: $dm/dr=4\pi r^2\rho$
- Energi: $dL/dr=4\pi r^2\rho\varepsilon$

**Nuklir**
- $E=\Delta mc^2$; $N(t)=N_0e^{-\lambda t}$; $t_{1/2}=\ln2/\lambda$

---

## Peta Konsep Bab I

```
Cahaya (dualisme gelombang-partikel)
   │
   ├── Sebagai gelombang → Spektrum EM, Doppler, Polarisasi
   │                            │
   │                     Spektroskopi (garis emisi/absorpsi,
   │                     Kirchhoff, pelebaran garis)
   │                            │
   │                     Model atom Bohr (tingkat energi,
   │                     deret Lyman/Balmer/Paschen)
   │
   └── Sebagai paket energi (E=hν) → Radiasi benda hitam
                                          │
                          Planck → Wien (λmax) + Stefan-Boltzmann (L,T)
                                          │
                                   Fotometri: m, M, modulus jarak
                                          │
                                Diagram H-R (L vs T, radius bintang)
                                          │
                          → dasar Bab VIII (Bintang) & Bab XI (Kosmologi: redshift)

Struktur atom & inti → energi ikat, radioaktivitas, neutrino
                                          │
                          → dasar reaksi fusi (Bab VI Matahari, Bab VIII Bintang)

Termodinamika & transfer energi (gas ideal, hidrostatik, radiasi/konveksi)
                                          │
                          → dasar model struktur bintang (Bab VIII)
```

---

## Topik Paling Sering Muncul di OSN (Bab I)

Berdasarkan pola soal OSN/IOAA tahun-tahun sebelumnya, prioritas belajar:

1. **Modulus jarak + ekstingsi** (hampir selalu muncul, sering digabung dengan Wien/Stefan-Boltzmann dalam satu soal multi-tahap)
2. **Hukum Wien & Stefan-Boltzmann** untuk mencari $T_{eff}$, $R$, $L$ bintang dari data foto/spektrum
3. **Efek Doppler** (radial velocity, redshift — sering dikombinasikan dengan Bab IX sistem biner atau Bab XI kosmologi)
4. **Rumus Rydberg/Bohr** untuk deret spektral hidrogen
5. **Diagram H-R** — interpretasi kualitatif posisi bintang, radius relatif
6. Kesetimbangan hidrostatik — biasanya versi konseptual/kualitatif, jarang derivasi penuh di tingkat Penyisihan

---

*Bagian selanjutnya (Bab II: Astronomi Bola & Bab III: Sistem Waktu dan Kalendar) menyusul — balas "lanjut" kapan saja untuk melanjutkan.*
