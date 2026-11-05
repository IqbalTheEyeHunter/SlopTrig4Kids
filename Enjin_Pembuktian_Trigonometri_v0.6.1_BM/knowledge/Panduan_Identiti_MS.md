# Pustaka Rujukan Identiti Trigonometri — Bahasa Melayu

**Enjin:** Enjin Pembuktian Trigonometri v0.6.1  
**Bahasa:** Bahasa Melayu baku  
**Skop:** Enam fungsi trigonometri asas

## Pengenalan

Pustaka ini menghimpunkan identiti dan hubungan matematik yang melibatkan fungsi sinus, kosinus, tangen, kotangen, sekan dan kosekan. Identiti digunakan sebagai rujukan untuk pembelajaran serta pembuktian ungkapan trigonometri.

Notasi matematik, ID identiti dan ungkapan simbolik dikekalkan supaya sepadan dengan pangkalan data yang digunakan oleh enjin. Huraian dan syarat domain diberikan dalam bahasa Melayu.

**Ringkasan katalog:** 136 entri berindeks; 125 peraturan kesamaan boleh laksana; 17 entri bersyarat; 10 ketaksamaan. Entri berindeks tidak semestinya boleh digunakan secara automatik dalam carian pembuktian.

## 1. Enam fungsi trigonometri dan domainnya

| Fungsi | Takrif melalui sinus dan kosinus | Tidak ditakrifkan apabila | Punca (jika ditakrifkan) |
|---|---|---|---|
| `sin x` | Koordinat menegak pada bulatan unit | Tiada | `x=kπ` |
| `cos x` | Koordinat mengufuk pada bulatan unit | Tiada | `x=π/2+kπ` |
| `tan x` | `sin x/cos x` | `cos x=0` | `x=kπ` |
| `cot x` | `cos x/sin x` | `sin x=0` | `x=π/2+kπ` |
| `sec x` | `1/cos x` | `cos x=0` | Tiada |
| `csc x` | `1/sin x` | `sin x=0` | Tiada |

### 1.1 Senarai syarat domain

| Ungkapan | Syarat yang diperlukan |
|---|---|
| `1/sin x`, `cot x`, `csc x` | `sin x ≠ 0` |
| `1/cos x`, `tan x`, `sec x` | `cos x ≠ 0` |
| `1/tan x`, `1/cot x` | `sin x ≠ 0` dan `cos x ≠ 0` |
| `1/(1−cos x)` | `cos x ≠ 1` |
| `1/(1+cos x)` | `cos x ≠ −1` |
| `1/(1−sin x)` | `sin x ≠ 1` |
| `1/(1+sin x)` | `sin x ≠ −1` |
| `sqrt((1−cos x)/2)` | Sentiasa bernilai nyata; ungkapan punca kuasa dua sahaja bersamaan `|sin(x/2)|` |
| `sqrt((1+cos x)/2)` | Sentiasa bernilai nyata; ungkapan punca kuasa dua sahaja bersamaan `|cos(x/2)|` |

**Perhatian tentang domain:** `tan x · cot x = 1` hanya apabila kedua-dua fungsi ditakrifkan, iaitu `sin x ≠ 0` dan `cos x ≠ 0`. Sebaliknya, `sin x · csc x = 1` hanya memerlukan `sin x ≠ 0`.

## 2. Indeks induk identiti trigonometri

Identiti di bawah disusun mengikut kumpulan. Formula dan ID dikekalkan seperti dalam katalog asal supaya padanan dengan enjin pembuktian tidak berubah.

| ID | Identiti | Syarat domain / catatan |
|---|---|---|

### F — Asas: hasil bahagi, fungsi salingan dan identiti Pythagoras

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| F01 | `tan x = sin x / cos x` | cos x ≠ 0 |
| F02 | `cot x = cos x / sin x` | sin x ≠ 0 |
| F03 | `sec x = 1/cos x` | cos x ≠ 0 |
| F04 | `csc x = 1/sin x` | sin x ≠ 0 |
| F05 | `tan x · cot x = 1` | `sin x ≠ 0` dan `cos x ≠ 0` |
| F06 | `sin x · csc x = 1` | sin x ≠ 0 |
| F07 | `cos x · sec x = 1` | cos x ≠ 0 |
| F08 | `sin²x + cos²x = 1` | Semua nilai nyata bagi `x` |
| F09 | `1 + tan²x = sec²x` | cos x ≠ 0 |
| F10 | `1 + cot²x = csc²x` | sin x ≠ 0 |
| F11 | `sec²x − tan²x = 1` | cos x ≠ 0 |
| F12 | `csc²x − cot²x = 1` | sin x ≠ 0 |
| F13 | `sec²x + csc²x = sec²x csc²x` | `sin x ≠ 0` dan `cos x ≠ 0` |
| F14 | `tan²x + cot²x + 2 = sec²x csc²x` | `sin x ≠ 0` dan `cos x ≠ 0` |
| F15 | `tan x + cot x = sec x csc x` | `sin x ≠ 0` dan `cos x ≠ 0` |
| F16 | `(sec x−tan x)(sec x+tan x)=1` | cos x ≠ 0 |
| F17 | `(csc x−cot x)(csc x+cot x)=1` | sin x ≠ 0 |
| F18 | `sin²x = 1−cos²x` | Semua nilai nyata bagi `x` |
| F19 | `cos²x = 1−sin²x` | Semua nilai nyata bagi `x` |
| F20 | `tan²x = sec²x−1`, `cot²x = csc²x−1` | Domain fungsi yang berkenaan |

### S — Kesimetrian, anjakan dan keberkalaan

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| S01 | `sin(−x)=−sin x`, `cos(−x)=cos x` | Semua nilai nyata bagi `x` |
| S02 | `tan(−x)=−tan x`, `cot(−x)=−cot x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S03 | `sec(−x)=sec x`, `csc(−x)=−csc x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S04 | `sin(x+2kπ)=sin x`, `cos(x+2kπ)=cos x` | Semua nilai nyata bagi `x` |
| S05 | `tan(x+kπ)=tan x`, `cot(x+kπ)=cot x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S06 | `sec(x+2kπ)=sec x`, `csc(x+2kπ)=csc x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S07 | `sin(x+π)=−sin x`, `cos(x+π)=−cos x` | Semua nilai nyata bagi `x` |
| S08 | `tan(x+π)=tan x`, `cot(x+π)=cot x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S09 | `sec(x+π)=−sec x`, `csc(x+π)=−csc x` | Pada titik yang fungsi berkenaan ditakrifkan |
| S10 | `sin(π−x)=sin x`, `cos(π−x)=−cos x` | Semua nilai nyata bagi `x` |
| S11 | `sin(π/2−x)=cos x`, `cos(π/2−x)=sin x` | Semua nilai nyata bagi `x` |
| S12 | `tan(π/2−x)=cot x`, `cot(π/2−x)=tan x` | Kedua-dua belah ditakrifkan |
| S13 | `sec(π/2−x)=csc x`, `csc(π/2−x)=sec x` | Kedua-dua belah ditakrifkan |
| S14 | `sin(π/2+x)=cos x`, `cos(π/2+x)=−sin x` | Semua nilai nyata bagi `x` |
| S15 | `tan(π/2+x)=−cot x`, `cot(π/2+x)=−tan x` | Kedua-dua belah ditakrifkan |
| S16 | `sec(π/2+x)=−csc x`, `csc(π/2+x)=sec x` | Kedua-dua belah ditakrifkan |
| S17 | `sin(2π−x)=−sin x`, `cos(2π−x)=cos x` | Semua nilai nyata bagi `x` |
| S18 | `sin(π+x)=−sin x`, `cos(π+x)=−cos x` | Semua nilai nyata bagi `x` |

### A — Identiti penambahan dan penolakan sudut

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| A01 | `sin(x+y)=sin x cos y+cos x sin y` | Semua nilai nyata |
| A02 | `sin(x−y)=sin x cos y−cos x sin y` | Semua nilai nyata |
| A03 | `cos(x+y)=cos x cos y−sin x sin y` | Semua nilai nyata |
| A04 | `cos(x−y)=cos x cos y+sin x sin y` | Semua nilai nyata |
| A05 | `tan(x+y)=(tan x+tan y)/(1−tan x tan y)` | `cos x ≠ 0`, `cos y ≠ 0` dan `cos(x+y) ≠ 0` |
| A06 | `tan(x−y)=(tan x−tan y)/(1+tan x tan y)` | `cos x ≠ 0`, `cos y ≠ 0` dan `cos(x−y) ≠ 0` |
| A07 | `cot(x+y)=(cot x cot y−1)/(cot x+cot y)` | `sin x ≠ 0`, `sin y ≠ 0` dan `sin(x+y) ≠ 0` |
| A08 | `cot(x−y)=(cot x cot y+1)/(cot y−cot x)` | `sin x ≠ 0`, `sin y ≠ 0` dan `sin(x−y) ≠ 0` |
| A09 | `sin(x+y)+sin(x−y)=2sin x cos y` | Semua nilai nyata |
| A10 | `sin(x+y)−sin(x−y)=2cos x sin y` | Semua nilai nyata |
| A11 | `cos(x+y)+cos(x−y)=2cos x cos y` | Semua nilai nyata |
| A12 | `cos(x−y)−cos(x+y)=2sin x sin y` | Semua nilai nyata |
| A13 | `sin(x+y)sin(x−y)=sin²x−sin²y` | Semua nilai nyata |
| A14 | `cos(x+y)cos(x−y)=cos²x−sin²y` | Semua nilai nyata |
| A15 | `cos(x+y)cos(x−y)=cos²x+cos²y−1` | Semua nilai nyata |
| A16 | `sin(x+y)cos(x−y)=sin x cos x+sin y cos y` | Semua nilai nyata |
| A17 | `cos(x+y)sin(x−y)=sin x cos x−sin y cos y` | Semua nilai nyata |
| A18 | `sec(x+y)=sec x sec y/(1−tan x tan y)` | `cos x ≠ 0`, `cos y ≠ 0` dan `cos(x+y) ≠ 0` |
| A19 | `sec(x−y)=sec x sec y/(1+tan x tan y)` | `cos x ≠ 0`, `cos y ≠ 0` dan `cos(x−y) ≠ 0` |
| A20 | `csc(x+y)=csc x csc y/(cot x+cot y)` | `sin x ≠ 0`, `sin y ≠ 0` dan `sin(x+y) ≠ 0` |
| A21 | `csc(x−y)=csc x csc y/(cot y−cot x)` | `sin x ≠ 0`, `sin y ≠ 0` dan `sin(x−y) ≠ 0` |

### D — Sudut berganda, sudut tiga kali ganda dan gandaan umum

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| D01 | `sin 2x=2sin x cos x` | Semua nilai nyata |
| D02 | `cos 2x=cos²x−sin²x` | Semua nilai nyata |
| D03 | `cos 2x=1−2sin²x` | Semua nilai nyata |
| D04 | `cos 2x=2cos²x−1` | Semua nilai nyata |
| D05 | `tan 2x=2tan x/(1−tan²x)` | `cos x ≠ 0` dan `cos 2x ≠ 0` |
| D06 | `cot 2x=(cot²x−1)/(2cot x)` | `sin x ≠ 0` dan `cos x ≠ 0` |
| D07 | `sin 3x=3sin x−4sin³x` | Semua nilai nyata |
| D08 | `cos 3x=4cos³x−3cos x` | Semua nilai nyata |
| D09 | `tan 3x=(3tan x−tan³x)/(1−3tan²x)` | `cos x ≠ 0` dan `cos 3x ≠ 0` |
| D10 | `cot 3x=(cot³x−3cot x)/(3cot²x−1)` | `sin x ≠ 0` dan `sin 3x ≠ 0`; penyebut tidak sifar secara automatik |
| D11 | `sin 4x=4sin x cos x(cos²x−sin²x)` | Semua nilai nyata |
| D12 | `cos 4x=1−8sin²x cos²x` | Semua nilai nyata |
| D13 | `sin((n+1)x)=2cos x sin(nx)−sin((n−1)x)` | `n` ialah nombor bulat dengan `n ≥ 1`; semua nilai nyata |
| D14 | `cos((n+1)x)=2cos x cos(nx)−cos((n−1)x)` | `n` ialah nombor bulat dengan `n ≥ 1`; semua nilai nyata |
| D15 | `sin(nx)=sin x · U_(n−1)(cos x)` | `n` ialah nombor bulat dengan `n ≥ 1`; `U_0(t)=1`, `U_1(t)=2t`, `U_(m+1)=2tU_m−U_(m−1)` |
| D16 | `cos(nx)=T_n(cos x)` | `n` ialah nombor bulat dengan `n ≥ 0`; `T_0(t)=1`, `T_1(t)=t`, `T_(m+1)=2tT_m−T_(m−1)` |

### H — Sudut separuh, pengurangan kuasa dan penggantian tangen separuh sudut

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| H01 | `sin²(x/2)=(1−cos x)/2` | Semua nilai nyata |
| H02 | `cos²(x/2)=(1+cos x)/2` | Semua nilai nyata |
| H03 | `sin(x/2)=±√((1−cos x)/2)` | Pilih tanda berdasarkan kuadran sebenar bagi `x/2` |
| H04 | `cos(x/2)=±√((1+cos x)/2)` | Pilih tanda berdasarkan kuadran sebenar bagi `x/2` |
| H05 | `tan(x/2)=sin x/(1+cos x)` | `cos(x/2) ≠ 0` (oleh itu `1+cos x ≠ 0`) |
| H06 | `tan(x/2)=(1−cos x)/sin x` | `sin x ≠ 0`; syarat ini mengecualikan beberapa titik yang membolehkan `tan(x/2)` ditakrifkan |
| H07 | `tan(x/2)=tan x/(sec x+1)` | `cos x ≠ 0` dan `cos(x/2) ≠ 0`; selain itu, `sec x+1 ≠ 0` |
| H08 | `cot(x/2)=(1+cos x)/sin x` | sin x ≠ 0 |
| H09 | `cot(x/2)=sin x/(1−cos x)` | `sin(x/2) ≠ 0` |
| H10 | `sin²x=(1−cos 2x)/2` | Semua nilai nyata |
| H11 | `cos²x=(1+cos 2x)/2` | Semua nilai nyata |
| H12 | `sin x cos x=(sin 2x)/2` | Semua nilai nyata |
| H13 | `sin⁴x=(3−4cos 2x+cos 4x)/8` | Semua nilai nyata |
| H14 | `cos⁴x=(3+4cos 2x+cos 4x)/8` | Semua nilai nyata |
| H15 | `sin²x cos²x=(1−cos 4x)/8` | Semua nilai nyata |
| H16 | If `t=tan(x/2)`, `sin x=2t/(1+t²)` | cos(x/2) ≠ 0 |
| H17 | If `t=tan(x/2)`, `cos x=(1−t²)/(1+t²)` | cos(x/2) ≠ 0 |
| H18 | If `t=tan(x/2)`, `tan x=2t/(1−t²)` | `cos(x/2) ≠ 0` dan `cos x ≠ 0` |
| H19 | If `t=tan(x/2)`, `cot x=(1−t²)/(2t)` | `cos(x/2) ≠ 0` dan `sin x ≠ 0` |
| H20 | If `t=tan(x/2)`, `sec x=(1+t²)/(1−t²)` | `cos(x/2) ≠ 0` dan `cos x ≠ 0` |
| H21 | If `t=tan(x/2)`, `csc x=(1+t²)/(2t)` | `cos(x/2) ≠ 0` dan `sin x ≠ 0` |

### P — Hasil darab kepada hasil tambah dan hasil tambah kepada hasil darab

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| P01 | `2sin x cos y=sin(x+y)+sin(x−y)` | Semua nilai nyata |
| P02 | `2cos x sin y=sin(x+y)−sin(x−y)` | Semua nilai nyata |
| P03 | `2cos x cos y=cos(x+y)+cos(x−y)` | Semua nilai nyata |
| P04 | `2sin x sin y=cos(x−y)−cos(x+y)` | Semua nilai nyata |
| P05 | `sin x+sin y=2sin((x+y)/2)cos((x−y)/2)` | Semua nilai nyata |
| P06 | `sin x−sin y=2cos((x+y)/2)sin((x−y)/2)` | Semua nilai nyata |
| P07 | `cos x+cos y=2cos((x+y)/2)cos((x−y)/2)` | Semua nilai nyata |
| P08 | `cos x−cos y=−2sin((x+y)/2)sin((x−y)/2)` | Semua nilai nyata |
| P09 | `sin x+cos x=√2 sin(x+π/4)` | Semua nilai nyata |
| P10 | `cos x−sin x=√2 cos(x+π/4)` | Semua nilai nyata |
| P11 | `a sin x+b cos x=R sin(x+φ)` | `R=√(a²+b²)>0`; pilih `cos φ=a/R`, `sin φ=b/R` |
| P12 | `a cos x+b sin x=R cos(x−φ)` | `R=√(a²+b²)>0`; pilih `cos φ=a/R`, `sin φ=b/R` |

### R — Pemfaktoran semula dan ungkapan berpasangan

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| R01 | `(1−cos x)/sin x=sin x/(1+cos x)` | sin x ≠ 0 |
| R02 | `(1+cos x)/sin x=sin x/(1−cos x)` | sin x ≠ 0 |
| R03 | `(1−sin x)/cos x=cos x/(1+sin x)` | cos x ≠ 0 |
| R04 | `(1+sin x)/cos x=cos x/(1−sin x)` | cos x ≠ 0 |
| R05 | `1/(sec x+tan x)=sec x−tan x` | cos x ≠ 0 |
| R06 | `1/(csc x+cot x)=csc x−cot x` | sin x ≠ 0 |
| R07 | `(sec x+tan x)²=(1+sin x)/(1−sin x)` | cos x ≠ 0 |
| R08 | `(csc x+cot x)²=(1+cos x)/(1−cos x)` | sin x ≠ 0 |
| R09 | `(sec x−tan x)²=(1−sin x)/(1+sin x)` | cos x ≠ 0 |
| R10 | `(csc x−cot x)²=(1−cos x)/(1+cos x)` | sin x ≠ 0 |
| R11 | `tan x/(sec x+1)=sin x/(1+cos x)` | `cos x ≠ 0` dan `1+cos x ≠ 0` |
| R12 | `cot x/(csc x+1)=cos x/(1+sin x)` | `sin x ≠ 0` dan `1+sin x ≠ 0` |
| R13 | `1/(1−sin x)+1/(1+sin x)=2sec²x` | cos x ≠ 0 |
| R14 | `1/(1−cos x)+1/(1+cos x)=2csc²x` | sin x ≠ 0 |
| R15 | `1/(1−sin x)−1/(1+sin x)=2tan x sec x` | cos x ≠ 0 |
| R16 | `1/(1−cos x)−1/(1+cos x)=2cot x csc x` | sin x ≠ 0 |
| R17 | `(tan x+sec x)/(tan x−sec x)=−(sec x+tan x)²` | cos x ≠ 0 |
| R18 | `(cot x+csc x)/(cot x−csc x)=−(csc x+cot x)²` | sin x ≠ 0 |

### I — Ketaksamaan

| ID | Identiti | Syarat domain / catatan |
|---|---|---|
| I01 | `−1≤sin x≤1`, `−1≤cos x≤1` | Bulatan unit |
| I02 | `0≤sin²x≤1`, `0≤cos²x≤1` | Sifat kuasa dua dan F08 |
| I03 | ` | sin x cos x |
| I04 | ` | sin x+cos x |
| I05 | ` | a sin x+b cos x |
| I06 | `sec²x≥1` | F09 dengan syarat `cos x ≠ 0` |
| I07 | `csc²x≥1` | F10 dengan syarat `sin x ≠ 0` |
| I08 | `tan²x+cot²x≥2` | Bagi `sin x cos x ≠ 0`, `(tan x−cot x)² ≥ 0` dan `tan x cot x = 1` |
| I09 | ` | sin x |
| I10 | `1≤ | sin x |

## 3. Panduan penggunaan identiti

1. Kenal pasti bentuk fungsi trigonometri yang muncul dalam ungkapan.
2. Semak sama ada fungsi yang digunakan ditakrifkan pada sudut berkenaan.
3. Pilih identiti yang sepadan dengan struktur ungkapan.
4. Lakukan penggantian identiti satu demi satu dan catatkan setiap langkah algebra.
5. Kekalkan semua syarat domain daripada ungkapan asal.
6. Jangan gunakan identiti yang sedang dibuktikan sebagai premis untuk membuktikan identiti itu sendiri.

## 4. Identiti asas F01–F12

Identiti asas berikut merupakan rujukan utama bagi enam fungsi trigonometri. Semua rumus ini turut disenaraikan dalam indeks induk di atas.

- **F01:** `tan x = sin x/cos x`, dengan syarat `cos x ≠ 0`.
- **F02:** `cot x = cos x/sin x`, dengan syarat `sin x ≠ 0`.
- **F03:** `sec x = 1/cos x`, dengan syarat `cos x ≠ 0`.
- **F04:** `csc x = 1/sin x`, dengan syarat `sin x ≠ 0`.
- **F05:** `tan x · cot x = 1`, dengan syarat `sin x ≠ 0` dan `cos x ≠ 0`.
- **F06:** `sin x · csc x = 1`, dengan syarat `sin x ≠ 0`.
- **F07:** `cos x · sec x = 1`, dengan syarat `cos x ≠ 0`.
- **F08:** `sin²x + cos²x = 1`, bagi semua nilai nyata `x`.
- **F09:** `1 + tan²x = sec²x`, dengan syarat `cos x ≠ 0`.
- **F10:** `1 + cot²x = csc²x`, dengan syarat `sin x ≠ 0`.
- **F11:** `sec²x − tan²x = 1`, dengan syarat `cos x ≠ 0`.
- **F12:** `csc²x − cot²x = 1`, dengan syarat `sin x ≠ 0`.

### 4.1 Asas pembuktian dan penggunaan semula teorem

- F08 dibuktikan secara bebas melalui laluan geometri `G01 → G03 → G04`.
- F09 diterbitkan daripada F08, F01 dan F03.
- F10 diterbitkan daripada F08, F02 dan F04.
- F08, F09 dan F10 boleh digunakan semula untuk membuktikan pernyataan lain jika rantaian kebergantungannya sah.
- Sesuatu teorem tidak boleh digunakan sebagai premis untuk membuktikan dirinya sendiri atau bentuk yang setara secara langsung dengannya.

## 5. Istilah matematik yang digunakan

| Istilah | Maksud dalam aplikasi |
|---|---|
| Identiti trigonometri | Kesamaan yang benar bagi semua nilai sudut dalam domain sepunya yang ditetapkan |
| Pembuktian | Proses menunjukkan bahawa sesuatu pernyataan matematik benar melalui hujah yang sah |
| Ungkapan | Gabungan nombor, pemboleh ubah, operasi dan fungsi |
| Domain | Set nilai yang membolehkan sesuatu ungkapan ditakrifkan |
| Domain sepunya | Set nilai yang membolehkan kedua-dua belah pernyataan ditakrifkan |
| Premis | Pernyataan yang diterima sebagai asas dalam sesuatu pembuktian |
| Teorem | Pernyataan matematik yang telah dibuktikan |
| Pengembangan | Proses menggunakan hukum pengagihan untuk membuka kurungan |
| Pemfaktoran | Proses menulis ungkapan sebagai hasil darab faktor |
| Penggantian | Proses menggantikan subungkapan dengan ungkapan yang setara |
| Contoh balas | Satu contoh yang menunjukkan bahawa pernyataan umum adalah palsu |
| Bulatan unit | Bulatan berpusat di asalan dengan jejari satu |
| Unjuran serenjang | Unjuran yang membentuk sudut tegak dengan garis atau paksi sasaran |

## 6. Nota skop dan kebolehgunaan

- Pustaka ini mengandungi 136 entri berindeks daripada rujukan enam fungsi.
- Sebanyak 125 peraturan kesamaan boleh digunakan oleh enjin selepas pengesahan simbolik dan semakan syarat kebergantungan.
- Entri bersyarat, ketaksamaan atau rumus yang memerlukan andaian tambahan tidak semestinya boleh digunakan secara automatik.
- Formula dan ID dikekalkan dalam notasi asal untuk menjamin keserasian dengan enjin pembuktian.
- Pustaka ini ialah rujukan pembelajaran; ia bukan jaminan bahawa setiap identiti boleh dibuktikan oleh strategi carian semasa.

## 7. Rujukan istilah

Padanan istilah seperti **identiti** dalam bidang matematik dan **pembuktian** disemak berpandukan entri PRPM Dewan Bahasa dan Pustaka. Dokumen ini bukan penerbitan rasmi atau pengesahan rasmi DBP.

- PRPM DBP, entri “identity” (makna matematik: identiti): https://prpm.dbp.gov.my/Cari1?d=7120&keyword=identity
- PRPM DBP, entri “pembuktian”: https://prpm.dbp.gov.my/Cari1?d=371752&keyword=pembuktian
