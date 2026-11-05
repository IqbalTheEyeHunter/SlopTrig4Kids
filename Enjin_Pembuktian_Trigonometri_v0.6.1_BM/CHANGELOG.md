# Sejarah Perubahan — Enjin Pembuktian Trigonometri (Bahasa Melayu)

## v0.6.1 — Edisi Bahasa Melayu

- Menterjemahkan semua tab, label, butang, arahan, mesej ralat dan bar status kepada Bahasa Melayu baku.
- Menyediakan label Bahasa Melayu bagi strategi pembuktian sambil mengekalkan nama strategi dalaman yang diperlukan oleh enjin.
- Menterjemahkan laporan pembuktian pada skrin dan eksport Markdown, termasuk laporan pembuktian geometri G01 → G03 → G04.
- Mengekalkan status dalaman `PROVED`, `DISPROVED`, `INCONCLUSIVE` dan `ERROR` untuk keserasian; paparan pengguna menggunakan padanan Bahasa Melayu.
- Menyediakan `Panduan_Identiti_MS.md` dengan kesemua 136 entri identiti berindeks. Formula dan ID dikekalkan.
- Menterjemahkan bank soalan, penyelesaian pembuktian dan panduan pengetahuan v0.6 kepada Bahasa Melayu.
- Menyediakan panduan pengguna untuk murid dan guru Matematik Tambahan Tingkatan 5.
- Mengekalkan enjin matematik v0.6.1, skema sijil, peraturan kebergantungan dan tingkah laku pembuktian tanpa perubahan.
- Mengekalkan perkongsian bank teorem antara edisi Bahasa Melayu dan Inggeris melalui lokasi data pengguna yang sama.

## v0.6.1 — Penambahbaikan laporan geometri yang diwarisi

- Memaparkan langkah sebenar G01, G03, G04 dan padanan sasaran dalam laporan pembuktian.
- Memaparkan skema sijil, versi pemeriksa, ringkasan SHA-256, status pengesahan semula dan asas matematik yang dipercayai.
- Mengelakkan label yang mengelirukan seperti bilangan penggunaan identiti sifar atau rujukan katalog bagi nod geometri.
- Mengekalkan keserasian sijil geometri v0.6.0.

## v0.6.0 — Penggunaan semula teorem dan bank latihan

- Membolehkan F08, F09 dan F10 digunakan semula untuk membuktikan sasaran lain tanpa membenarkan pembuktian berputar.
- Mengekalkan laluan geometri bebas G01 → G03 → G04 bagi F08.
- Menambah prapemprosesan algebra terhad untuk mengembangkan kuasa dua ungkapan tambah dan memfaktorkan parameter sepunya.
- Membuktikan identiti gabungan linear berparameter menggunakan F08.
- Menolak bentuk salah yang menggunakan `p*cos(x)` pada sebutan kedua sebagai `DISPROVED`.
- Memisahkan bank soalan daripada penyelesaian pembuktian.
