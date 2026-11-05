# Enjin Pembuktian Trigonometri v0.6.1 — Edisi Bahasa Melayu

Enjin Pembuktian Trigonometri ialah aplikasi desktop Windows yang beroperasi tanpa talian untuk membantu pembuktian identiti yang melibatkan enam fungsi trigonometri asas. Edisi ini menggunakan antara muka dan laporan dalam Bahasa Melayu, manakala sintaks input matematik, ID identiti, skema sijil dan struktur data mesin dikekalkan bagi memastikan keserasian dengan keluaran v0.6.1.

## 1. Kandungan keluaran

- `app.py` — antara muka desktop Bahasa Melayu.
- `engine.py` — enjin pembuktian simbolik v0.6.1; logik pembuktian dikekalkan.
- `geometry.py` — pembina dan pemeriksa sijil pembuktian geometri G01 → G03 → G04.
- `knowledge/Panduan_Identiti_MS.md` — pustaka identiti enam fungsi dalam Bahasa Melayu, termasuk 136 entri berindeks.
- `knowledge/SKILL.md` — katalog kanonik yang digunakan secara dalaman oleh enjin untuk mengekalkan keserasian parser dan pengesahan peraturan.
- `question-bank.md` — bank soalan Bahasa Melayu; ID dan ungkapan matematik dikekalkan.
- `proof-solutions.md` — penyelesaian pembuktian Bahasa Melayu yang sepadan dengan bank soalan.
- `V0.6_Panduan_Pengetahuan.md` — panduan pengetahuan dan peraturan penggunaan teorem.
- `Panduan_Pengguna.md` — panduan penggunaan untuk murid dan guru.
- `CHANGELOG.md` dan `TEST_RESULTS.txt` — sejarah perubahan dan keputusan pengujian.
- `reference/English_original/` — salinan dokumen sumber Bahasa Inggeris bagi rujukan silang.

## 2. Menjalankan aplikasi

### Menggunakan fail sumber Python

1. Pasang Python 3.11 atau versi lebih baharu.
2. Buka folder projek ini.
3. Jalankan `run_windows.bat`.
4. Skrip akan memasang kebergantungan yang diperlukan dan membuka aplikasi.

### Membina fail boleh laksana Windows

Jalankan `build_windows.bat` pada komputer Windows yang mempunyai Python 3.11 atau versi lebih baharu. Fail boleh laksana akan dihasilkan di:

`dist/EnjinPembuktianTrigonometri.exe`

Fail `.exe` yang dibina boleh dijalankan tanpa sambungan Internet. Fail boleh laksana prabina tidak disertakan dalam arkib sumber ini; pengguna boleh membinanya menggunakan skrip tersebut.

## 3. Bahasa dan keserasian

- Semua label antara muka, mesej laporan, panduan pengguna dan pustaka identiti yang dipaparkan kepada pengguna menggunakan Bahasa Melayu.
- Sintaks matematik kekal menggunakan `sin`, `cos`, `tan`, `cot`, `sec`, `csc`, `sqrt`, `pi`, `+`, `-`, `*`, `/` dan `**`.
- Status dalaman `PROVED`, `DISPROVED`, `INCONCLUSIVE` dan `ERROR` dikekalkan dalam data mesin. Paparan antara muka menterjemahkannya sebagai `TERBUKTI`, `DISANGKAL`, `BELUM DAPAT DIPASTIKAN` dan `RALAT`.
- ID F01–F12, nod G01/G03/G04, skema sijil, nama medan JSON dan metadata kebergantungan tidak diterjemahkan.
- Bank teorem disimpan pada lokasi pengguna yang sama seperti edisi Inggeris, iaitu `%APPDATA%\\TrigonometricProofEngine\\theorem_bank.json`. Oleh itu, kedua-dua edisi boleh berkongsi bank teorem yang sama.
- Sijil JSON kekal menggunakan nama medan dan nilai status asal supaya boleh dibaca oleh alat pengesah v0.6.1.

## 4. Skop matematik

Enjin menyokong ungkapan sudut nyata yang menggunakan enam fungsi trigonometri, operasi aritmetik, kuasa, pemalar `pi`, punca kuasa dua nyata dan pemboleh ubah nyata. Ia menyediakan penggantian identiti yang diaudit, prapemprosesan algebra terhad, penjejakan syarat domain, penggunaan semula teorem yang disahkan dan pembuktian geometri bebas bagi F08.

Enjin ini bukan penyelesai umum bagi semua persamaan atau ketaksamaan trigonometri, bukan perisian graf, dan bukan sistem algebra simbolik serba guna.

## 5. Asas istilah Bahasa Melayu

Istilah seperti **identiti** dalam bidang matematik dan **pembuktian** disemak berpandukan PRPM Dewan Bahasa dan Pustaka. Terjemahan ini menggunakan istilah Bahasa Melayu baku yang selaras dengan rujukan tersebut; dokumen ini bukan penerbitan atau pengesahan rasmi DBP.

- PRPM DBP — [identity (makna matematik: identiti)](https://prpm.dbp.gov.my/Cari1?d=7120&keyword=identity)
- PRPM DBP — [pembuktian](https://prpm.dbp.gov.my/Cari1?d=371752&keyword=pembuktian)

## 6. Menjalankan ujian

Daripada folder projek, jalankan:

```bash
python -m unittest discover -s tests -v
```

Ujian merangkumi parser, peraturan kebergantungan teorem, pembuktian F08 secara geometri, penggunaan semula F08–F10, laporan Bahasa Melayu, keserasian sijil, bank soalan dan penyelesaian.

## 7. Had kepercayaan

Sijil geometri F08 disemak berdasarkan asas yang diisytiharkan, iaitu `AX.REAL`, `AX.EUCLID`, `AX.AREA` dan `D.UNIT`. Pembuktian katalog yang lain ialah rekod transformasi simbolik dengan kebergantungan yang diaudit dan pengekalan domain asal. Enjin ini bukan pembukti teorem formal umum yang memformalkan semua asas matematik daripada teori set.

**Teroka. Ubah bentuk. Sahkan. Fahami.**
