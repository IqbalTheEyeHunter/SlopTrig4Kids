# Panduan Pengguna
## Enjin Pembuktian Trigonometri v0.6.1 — Edisi Bahasa Melayu

**Pengguna sasaran:** Murid Matematik Tambahan Tingkatan 5 dan guru Matematik sekolah menengah  
**Platform:** Desktop Windows  
**Operasi:** Luar talian  
**Versi:** 0.6.1

---

## 1. Pengenalan

Enjin Pembuktian Trigonometri ialah aplikasi pembelajaran matematik yang membantu pengguna menyemak dan membina pembuktian identiti trigonometri. Aplikasi ini memberi tumpuan kepada enam fungsi trigonometri asas:

- sinus — `sin`
- kosinus — `cos`
- tangen — `tan`
- kotangen — `cot`
- sekan — `sec`
- kosekan — `csc`

Tidak seperti kalkulator biasa, aplikasi ini cuba membina rantaian transformasi matematik yang menunjukkan sebab sebelah kiri (LHS) dan sebelah kanan (RHS) sesuatu identiti adalah setara.

Antara fungsi utamanya ialah:

- pengesahan identiti secara simbolik;
- paparan langkah penggantian identiti dan transformasi algebra;
- pembuktian geometri bebas bagi identiti Pythagoras trigonometri F08;
- penggunaan semula teorem yang telah dibuktikan;
- penjejakan syarat domain asal;
- penyimpanan bank teorem;
- eksport laporan pembuktian dan sijil dalam format JSON.

Aplikasi ini ialah alat sokongan pembelajaran. Aplikasi ini bukan pengganti pengajaran guru, latihan kendiri atau penulisan pembuktian matematik oleh murid.

## 2. Memulakan aplikasi

### 2.1 Menjalankan fail boleh laksana

1. Muat turun fail `EnjinPembuktianTrigonometri.exe` daripada keluaran Bahasa Melayu.
2. Simpan fail tersebut dalam folder yang sesuai.
3. Klik dua kali fail `.exe`.
4. Tunggu sehingga tetingkap aplikasi dipaparkan.

Sambungan Internet tidak diperlukan untuk penggunaan biasa.

### 2.2 Tiga ruang utama

Aplikasi mempunyai tiga tab utama:

| Tab | Fungsi |
|---|---|
| **Ruang Pembuktian** | Memasukkan LHS dan RHS, memilih strategi dan menjana laporan pembuktian. |
| **Bank Teorem** | Menyimpan, menambah, membuang, mengimport dan mengeksport identiti atau hasil yang telah dibuktikan. |
| **Pustaka Identiti** | Mencari rujukan enam fungsi trigonometri berdasarkan ID, rumus atau kata kunci. |

## 3. Tutorial sintaks input matematik

Aplikasi menggunakan sintaks ungkapan matematik yang menyerupai sintaks Python. Pengguna tidak perlu mengetahui pengaturcaraan Python. Pengguna hanya perlu menulis ungkapan matematik menggunakan simbol yang disokong.

**Penting:** Aplikasi ini bukan pentafsir Python penuh. Jangan masukkan arahan pengaturcaraan seperti `import`, `for`, `while` atau takrif fungsi.

### 3.1 Operator asas

| Operasi matematik | Sintaks input | Contoh |
|---|---|---|
| Tambah | `+` | `a+b` |
| Tolak | `-` | `a-b` |
| Darab | `*` | `a*b` |
| Bahagi | `/` | `a/b` |
| Kuasa | `**` | `x**2` |
| Kurungan | `( )` | `(a+b)**2` |

Gunakan simbol darab `*` secara jelas.

Contoh:

- Notasi matematik: \(2\sin x\)
- Input aplikasi: `2*sin(x)`

Jangan bergantung pada pendaraban tersirat seperti `2x` atau `p sin(x)`.

### 3.2 Enam fungsi trigonometri

| Notasi matematik | Sintaks input |
|---|---|
| \(\sin x\) | `sin(x)` |
| \(\cos x\) | `cos(x)` |
| \(\tan x\) | `tan(x)` |
| \(\cot x\) | `cot(x)` |
| \(\sec x\) | `sec(x)` |
| \(\csc x\) | `csc(x)` |

Setiap fungsi mesti diikuti tanda kurung yang mengandungi argumennya.

Contoh:

```python
sin(x)
cos(2*x)
tan(x+y)
cot(x/2)
sec(x)**2
csc(3*x)
```

### 3.3 Menulis kuasa

Simbol `**` digunakan untuk menunjukkan kuasa.

| Notasi matematik | Sintaks input |
|---|---|
| \(\sin^2 x\) | `sin(x)**2` |
| \(\cos^2 x\) | `cos(x)**2` |
| \(\tan^2 x\) | `tan(x)**2` |
| \(\sec^2 x\) | `sec(x)**2` |
| \(\sin^3 x\) | `sin(x)**3` |
| \(\cos^4 x\) | `cos(x)**4` |

**Jangan keliru antara dua bentuk berikut:**

- `sin(x)**2` bermaksud \((\sin x)^2\).
- `sin(x**2)` bermaksud \(\sin(x^2)\).

Gunakan `sin(x)**2` untuk menulis sinus kuasa dua.

### 3.4 Pemalar pi (π) dan unit sudut

Aplikasi menerima `pi` dan simbol `π`.

| Sudut darjah | Radian | Input |
|---|---|---|
| 30° | \(\pi/6\) | `pi/6` |
| 45° | \(\pi/4\) | `pi/4` |
| 60° | \(\pi/3\) | `pi/3` |
| 90° | \(\pi/2\) | `pi/2` |
| 180° | \(\pi\) | `pi` |
| 360° | \(2\pi\) | `2*pi` |

**Aplikasi menggunakan radian.** Oleh itu, `sin(pi/6)` mewakili \(\sin 30^\circ\). Jangan masukkan `sin(30)` jika yang dimaksudkan ialah 30 darjah kerana aplikasi akan mentafsirkan 30 sebagai radian.

### 3.5 Punca kuasa dua

Gunakan `sqrt()` untuk menulis punca kuasa dua.

| Notasi matematik | Input |
|---|---|
| \(\sqrt 2\) | `sqrt(2)` |
| \(\sqrt 3\) | `sqrt(3)` |
| \(\sqrt x\) | `sqrt(x)` |
| \(\frac{\sqrt 3}{2}\) | `sqrt(3)/2` |

Punca kuasa dua nyata memerlukan ungkapan di bawah tanda punca kuasa dua bernilai bukan negatif.

### 3.6 Menggunakan pemboleh ubah

Aplikasi menerima pemboleh ubah nyata seperti `x`, `y`, `t`, `p`, `q`, `a` dan `b`.

Contoh:

```python
p*cos(x)
p*sin(x)+q*cos(x)
(p*cos(x)+q*sin(x))**2
```

### 3.7 Contoh input lengkap

| Ungkapan matematik | Sintaks aplikasi |
|---|---|
| \(\sin^2x+\cos^2x\) | `sin(x)**2+cos(x)**2` |
| \(1+\tan^2x\) | `1+tan(x)**2` |
| \(\sec^2x-\tan^2x\) | `sec(x)**2-tan(x)**2` |
| \(2\sin x\cos x\) | `2*sin(x)*cos(x)` |
| \(\sin(x+y)\) | `sin(x+y)` |
| \((a+b)^2\) | `(a+b)**2` |
| \(\frac{1-\cos^2x}{\sin x}\) | `(1-cos(x)**2)/sin(x)` |

## 4. Langkah membuktikan identiti

Sebagai contoh, buktikan:

\[
\sin^2x+\cos^2x=1.
\]

1. Buka tab **Ruang Pembuktian**.
2. Masukkan LHS:

   ```python
   sin(x)**2+cos(x)**2
   ```

3. Masukkan RHS:

   ```python
   1
   ```

4. Pilih strategi **Katalog identiti penuh**. Strategi ini disyorkan sebagai pilihan permulaan.
5. Klik **BUKTIKAN IDENTITI**.
6. Baca laporan pembuktian yang dijana.
7. Semak status, laluan pembuktian, langkah matematik, identiti yang digunakan dan syarat domain.
8. Jika perlu, eksport laporan Markdown atau sijil JSON.

Pintasan papan kekunci `Ctrl + Enter` juga boleh digunakan untuk menjalankan pembuktian.

## 5. Memahami strategi pembuktian

| Strategi yang dipaparkan | Tujuan |
|---|---|
| Katalog identiti penuh | Pilihan lalai yang disyorkan. Mencari identiti katalog yang dibenarkan serta premis yang dibekalkan. |
| Automatik | Membenarkan enjin memilih laluan pembuktian umum. |
| LHS ke RHS | Cuba mentransformasikan sebelah kiri kepada sebelah kanan. |
| RHS ke LHS | Cuba mentransformasikan sebelah kanan kepada sebelah kiri. |
| Kedua-dua belah kepada bentuk sepunya | Cuba menukarkan kedua-dua belah kepada ungkapan perantaraan yang sama. |
| Kaedah beza | Pilihan strategi yang disenaraikan; bukan rutin pembuktian beza khusus yang berasingan dalam keluaran ini. |
| Gunakan identiti yang dibekalkan | Menggunakan identiti tambahan dan teorem tersimpan tanpa katalog identiti terbina dalam. |
| Pengembangan sudut didahulukan | Pilihan susunan carian; bukan saluran pembuktian sudut khusus yang berasingan. |
| Transformasi Fu didahulukan | Pilihan susunan carian; bukan jaminan bahawa algoritma Fu akan dilaksanakan sebagai laluan berasingan. |
| Pengurangan algebra didahulukan | Pilihan susunan carian; bukan saluran pembuktian algebra khusus yang berasingan. |

Untuk penggunaan biasa, mulakan dengan **Katalog identiti penuh**. Pilihan yang disenaraikan sebagai susunan carian tidak menjamin bahawa kaedah khusus tersebut akan dilaksanakan.

## 6. Cara membaca laporan pembuktian

### 6.1 Pernyataan

Bahagian ini memaparkan identiti yang dimasukkan oleh pengguna, iaitu LHS = RHS.

### 6.2 Status

| Status pada skrin | Kod dalaman | Maksud |
|---|---|---|
| TERBUKTI | `PROVED` | Enjin telah membina laluan pembuktian yang sah berdasarkan peraturan yang dibenarkan. |
| DISANGKAL | `DISPROVED` | Enjin menemukan contoh balas berangka yang sah. |
| BELUM DAPAT DIPASTIKAN | `INCONCLUSIVE` | Enjin tidak berjaya membuktikan atau menyangkal pernyataan tersebut. |
| RALAT | `ERROR` | Input atau proses aplikasi mengalami ralat. |

Status `BELUM DAPAT DIPASTIKAN` tidak bermaksud pernyataan itu palsu. Carian katalog penuh dihadkan kepada maksimum tujuh penggunaan identiti dan 260 keadaan ungkapan yang dilawati. Pembuktian yang lebih panjang mungkin melebihi had ini.

### 6.3 Laluan pembuktian terpilih

Bahagian ini menunjukkan kaedah yang digunakan oleh enjin. Contohnya:

`GEOMETRI: G01 → G03 → G04`

menunjukkan bahawa identiti dibuktikan melalui laluan geometri bebas.

Laluan seperti `LHS menggunakan katalog identiti` menunjukkan bahawa enjin mentransformasikan sebelah kiri menggunakan identiti yang telah disahkan.

### 6.4 Syarat domain sepunya asal

Bahagian ini menyenaraikan syarat yang diperlukan supaya ungkapan asal ditakrifkan.

Contohnya:

\[
\tan x=\frac{\sin x}{\cos x}
\]

memerlukan:

\[
\cos x\ne0.
\]

| Fungsi | Syarat domain |
|---|---|
| `tan(x)` | `cos(x) ≠ 0` |
| `sec(x)` | `cos(x) ≠ 0` |
| `cot(x)` | `sin(x) ≠ 0` |
| `csc(x)` | `sin(x) ≠ 0` |

Syarat domain asal mesti dikekalkan walaupun ungkapan dipermudahkan. Sebagai contoh, `sin(x)/sin(x)` bersamaan dengan 1 hanya pada titik yang memenuhi `sin(x) ≠ 0` bagi ungkapan asal tersebut.

### 6.5 Rantaian pembuktian

Bahagian ini menunjukkan urutan ID identiti yang digunakan, contohnya:

`F03 → F01`

Baca bersama-sama bahagian langkah pembuktian untuk melihat cara setiap identiti digunakan.

### 6.6 Langkah pembuktian / analisis

Bahagian ini menunjukkan transformasi satu demi satu.

- **Sebelum:** ungkapan sebelum transformasi.
- **Selepas:** ungkapan selepas transformasi.
- **Justifikasi:** sebab langkah matematik dibenarkan.
- **ID identiti:** rujukan identiti yang digunakan.
- **Penggantian pemboleh ubah:** padanan pemboleh ubah dalam identiti dengan ungkapan sasaran.
- **Semakan:** pengesahan kesetaraan simbolik.

Murid digalakkan menulis semula setiap langkah dalam notasi matematik biasa dan menerangkan sebabnya.

### 6.7 Rujukan pustaka identiti dan teorem yang digunakan

Bahagian ini menyenaraikan ID identiti atau teorem yang menjadi asas pembuktian. Rujuk tab **Pustaka Identiti** untuk melihat rumus berkaitan.

### 6.8 Laluan pembuktian alternatif

Jika lebih daripada satu laluan pembuktian ditemukan, laluan alternatif dipaparkan untuk dibandingkan.

### 6.9 Contoh balas

Jika status ialah `DISANGKAL`, aplikasi memaparkan nilai pemboleh ubah yang menghasilkan nilai LHS dan RHS yang berbeza. Satu contoh balas yang sah sudah memadai untuk menyangkal identiti umum.

## 7. Memahami pembuktian geometri F08

Salah satu ciri penting aplikasi ialah pembuktian bebas bagi:

\[
\boxed{\sin^2x+\cos^2x=1}
\]

Pembuktian ini tidak mengandaikan F08 sebagai premis. Sebaliknya, enjin menggunakan tiga komponen geometri.

### G01 — Teorem Pythagoras melalui pembahagian geometri

Empat segi tiga bersudut tegak yang kongruen disusun di dalam segi empat sama yang bersisi `a+b`. Segi empat sama di bahagian tengah mempunyai sisi `c`.

Kesamaan luas memberikan:

\[
(a+b)^2=4\left(\frac{ab}{2}\right)+c^2.
\]

Kembangkan:

\[
a^2+2ab+b^2=2ab+c^2.
\]

Tolak `2ab` daripada kedua-dua belah:

\[
\boxed{a^2+b^2=c^2}.
\]

### G03 — Hubungan kuasa dua jarak pada satah Cartes

Ambil titik Cartes:

\[
P=(u,v).
\]

Unjuran serenjang pada paksi koordinat menghasilkan segi tiga bersudut tegak. Teorem Pythagoras memberikan:

\[
OP^2=u^2+v^2.
\]

### G04 — Penggantian menggunakan bulatan unit

Pilih titik pada bulatan unit:

\[
P=(\cos x,\sin x).
\]

Jejari bulatan unit ialah:

\[
OP=1.
\]

Gantikan koordinat titik ke dalam hubungan G03:

\[
1^2=\cos^2x+\sin^2x.
\]

Oleh itu:

\[
\boxed{\sin^2x+\cos^2x=1}.
\]

Laporan geometri turut memaparkan skema sijil, versi pemeriksa, ringkasan SHA-256, status pengesahan semula dan asas matematik yang dipercayai: `AX.REAL`, `AX.EUCLID`, `AX.AREA` dan `D.UNIT`.

Sijil ini mengesahkan skema pembuktian tetap dan kewajipan algebra yang ditetapkan berdasarkan asas tersebut. Sijil ini bukan pemformalan lengkap seluruh geometri Euclid daripada teori set.

## 8. Identiti asas yang perlu diketahui

| ID | Identiti | Syarat domain |
|---|---|---|
| F01 | \(\tan x=\frac{\sin x}{\cos x}\) | `cos(x) ≠ 0` |
| F02 | \(\cot x=\frac{\cos x}{\sin x}\) | `sin(x) ≠ 0` |
| F03 | \(\sec x=\frac{1}{\cos x}\) | `cos(x) ≠ 0` |
| F04 | \(\csc x=\frac{1}{\sin x}\) | `sin(x) ≠ 0` |
| F05 | \(\tan x\cot x=1\) | `sin(x) ≠ 0`, `cos(x) ≠ 0` |
| F06 | \(\sin x\csc x=1\) | `sin(x) ≠ 0` |
| F07 | \(\cos x\sec x=1\) | `cos(x) ≠ 0` |
| F08 | \(\sin^2x+\cos^2x=1\) | Semua nilai nyata bagi `x` |
| F09 | \(1+\tan^2x=\sec^2x\) | `cos(x) ≠ 0` |
| F10 | \(1+\cot^2x=\csc^2x\) | `sin(x) ≠ 0` |
| F11 | \(\sec^2x-\tan^2x=1\) | `cos(x) ≠ 0` |
| F12 | \(\csc^2x-\cot^2x=1\) | `sin(x) ≠ 0` |

F08, F09 dan F10 boleh digunakan semula untuk membuktikan identiti lain apabila rantaian kebergantungannya sah. Walau bagaimanapun, sesuatu teorem tidak boleh digunakan sebagai premis untuk membuktikan dirinya sendiri atau bentuk setara langsungnya.

## 9. Identiti tambahan dan hasil terdahulu

Dalam ruang pembuktian, pengguna boleh memasukkan identiti tambahan. Masukkan satu identiti pada setiap baris dengan format:

```text
Nama: ungkapan kiri = ungkapan kanan
```

Premis pengguna disahkan sebelum diterima dalam carian pembuktian. Jangan masukkan identiti yang belum disemak sebagai fakta.

### 9.1 Menggunakan bank teorem

Pilihan **Sertakan bank teorem tersimpan** membolehkan hasil yang telah disimpan digunakan dalam pembuktian seterusnya. Pilihan ini diaktifkan secara lalai.

### 9.2 Menyimpan hasil yang terbukti

1. Jalankan pembuktian.
2. Pastikan status ialah `TERBUKTI`.
3. Klik **Simpan hasil yang terbukti**.
4. Berikan nama kepada identiti tersebut.
5. Hasil akan disimpan dalam bank teorem setempat.

Hanya hasil berstatus `PROVED` boleh disimpan melalui fungsi ini.

### 9.3 Import dan eksport bank teorem

Tab **Bank Teorem** menyediakan fungsi tambah, buang, import JSON dan eksport JSON. Bank teorem disimpan pada komputer pengguna dan boleh digunakan tanpa talian.

Lokasi lazim pada Windows:

```text
%APPDATA%\TrigonometricProofEngine\theorem_bank.json
```

Edisi Bahasa Melayu dan Inggeris menggunakan lokasi bank yang sama supaya rekod teorem boleh dikongsi.

## 10. Menggunakan Pustaka Identiti

1. Buka tab **Pustaka Identiti**.
2. Masukkan ID seperti `F08`, rumus atau kata kunci seperti `Pythagoras`.
3. Klik **Cari**.
4. Baca baris yang sepadan.
5. Klik **Paparkan semua** untuk kembali kepada keseluruhan pustaka.

Pustaka yang dipaparkan kepada pengguna tersedia dalam Bahasa Melayu. Formula dan ID identiti dikekalkan dalam notasi asal.

## 11. Panduan untuk murid Tingkatan 5

Aliran pembelajaran yang disyorkan:

1. Cuba jawab soalan secara kendiri sebelum menggunakan aplikasi.
2. Kenal pasti LHS, RHS dan identiti yang mungkin digunakan.
3. Masukkan ungkapan dengan sintaks yang betul.
4. Jalankan pembuktian.
5. Bandingkan langkah aplikasi dengan jalan kerja sendiri.
6. Tulis semula pembuktian dalam notasi matematik biasa.
7. Pastikan setiap langkah mempunyai justifikasi dan syarat domain yang betul.

Matlamat utama ialah memahami sebab sesuatu transformasi dibenarkan, bukan sekadar mendapatkan status `TERBUKTI`.

## 12. Panduan untuk guru Matematik

Aplikasi boleh digunakan sebagai bahan sokongan demonstrasi, latihan berpandu dan pembelajaran kendiri.

### Aktiviti A — Lengkapkan langkah yang hilang

Paparkan laporan pembuktian yang satu langkahnya digugurkan. Minta murid mengenal pasti identiti atau hukum algebra yang diperlukan.

### Aktiviti B — Kenal pasti pernyataan palsu

Berikan identiti yang salah dan minta murid meneliti contoh balas dalam laporan `DISANGKAL`.

### Aktiviti C — Bandingkan laluan pembuktian

Minta murid membuktikan identiti yang sama menggunakan arah LHS ke RHS, RHS ke LHS atau bentuk sepunya apabila tersedia.

### Aktiviti D — Bina bank teorem

Murid membuktikan beberapa identiti, menyimpan hasil dan menggunakan teorem yang telah dibuktikan untuk menyelesaikan soalan lain.

### Aktiviti E — Teroka asas geometri

Gunakan laporan G01 → G03 → G04 untuk membincangkan hubungan antara geometri Euclid, koordinat Cartes dan identiti trigonometri.

## 13. Penyelesaian masalah lazim

| Masalah | Punca yang mungkin | Tindakan yang disyorkan |
|---|---|---|
| Ralat input | Sintaks tidak betul | Semak nama fungsi, kurungan dan operator. |
| Fungsi tidak diterima | Fungsi tidak disokong | Gunakan enam fungsi trigonometri dan `sqrt` sahaja. |
| Kuasa tidak betul | Kedudukan `**` atau kurungan salah | Gunakan `sin(x)**2` untuk \(\sin^2x\). |
| Nilai sudut tidak dijangka | Sudut darjah dimasukkan sebagai radian | Tukarkan darjah kepada radian. |
| BELUM DAPAT DIPASTIKAN | Carian tidak menemukan pembuktian | Cuba strategi lain atau periksa langkah yang belum dapat dibentuk. |
| DISANGKAL | Contoh balas ditemukan | Semak nilai contoh balas dan pernyataan asal. |
| Premis ditolak | Identiti tambahan tidak disahkan | Semak kesahan identiti dan format input. |
| Teorem tersimpan tiada | Bank tidak disertakan atau belum diimport | Aktifkan pilihan bank teorem atau import fail JSON. |

**Peringatan:** `BELUM DAPAT DIPASTIKAN` tidak sama dengan `DISANGKAL`. Identiti mungkin benar walaupun enjin belum dapat membuktikannya.

## 14. Had matematik aplikasi

### Disokong

- Enam fungsi trigonometri asas.
- Ungkapan sudut nyata.
- Operasi aritmetik dan kuasa.
- Pemalar `pi` dan punca kuasa dua.
- Beberapa pemboleh ubah nyata.
- Penggantian identiti katalog yang diaudit.
- Pengembangan dan pemfaktoran algebra dalam laluan yang disokong.
- Pembuktian geometri bebas bagi F08.
- Penggunaan semula teorem yang telah dibuktikan.
- Penjejakan syarat domain asal.

### Bukan fungsi umum aplikasi ini

- Penyelesaian semua persamaan trigonometri untuk semua penyelesaian.
- Penyelesaian semua ketaksamaan trigonometri.
- Pelukisan graf.
- Kalkulus umum.
- Trigonometri nombor kompleks.
- Pengaturcaraan Python umum.
- Pemformalan lengkap semua teorem matematik.

Ujian berangka hanya digunakan untuk mencari contoh balas. Ujian berangka tidak digunakan untuk mengesahkan identiti.

## 15. Eksport laporan dan sijil

- **Eksport Markdown:** menghasilkan laporan pembuktian yang boleh dibaca dan dikongsi.
- **Eksport sijil pembuktian:** menghasilkan rekod JSON berstruktur.

Nama medan JSON, kod status dan skema sijil dikekalkan dalam bahasa asal untuk memastikan keserasian mesin dan alat pengesah. Oleh itu, fail sijil JSON bukan dokumen terjemahan untuk bacaan biasa.

## 16. Nota istilah dan rujukan

Istilah **identiti** digunakan bagi makna matematik, manakala **pembuktian** merujuk proses membuktikan sesuatu pernyataan. Padanan ini disemak berpandukan PRPM DBP. Terjemahan dalam aplikasi menggunakan bahasa Melayu baku, tetapi bukan penerbitan rasmi DBP.

- [PRPM DBP — identity (makna matematik: identiti)](https://prpm.dbp.gov.my/Cari1?d=7120&keyword=identity)
- [PRPM DBP — pembuktian](https://prpm.dbp.gov.my/Cari1?d=371752&keyword=pembuktian)

## 17. Penutup

Enjin Pembuktian Trigonometri v0.6.1 edisi Bahasa Melayu dibangunkan untuk membantu murid dan guru memahami pembuktian identiti trigonometri secara lebih tersusun, telus dan interaktif.

Gunakan enjin untuk memahami penaakulan matematik, bukan sekadar mendapatkan jawapan.

**Enjin Pembuktian Trigonometri — Teroka. Ubah bentuk. Sahkan. Fahami.**
