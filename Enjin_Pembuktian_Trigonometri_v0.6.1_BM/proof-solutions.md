# Enjin Pembuktian Trigonometri v0.6.0 — Penyelesaian Pembuktian

**Bank soalan pendamping:** `question-bank.md`  
**Tujuan:** terbitan pembuktian yang telah disemak bagi semua entri dalam bank soalan v0.6.0.

## 1. Dasar pembuktian

- Setiap penyelesaian yang disenaraikan sepadan dengan soalan yang memperoleh status enjin `PROVED`.
- Setiap pengembangan algebra, pemfaktoran dan penggunaan teorem dipaparkan sebagai langkah yang berasingan.
- F08/F09/F10 hanya boleh digunakan semula sebagai premis apabila sasaran yang diminta bukan teorem yang sama atau bentuk teorem tersebut yang didarab dengan pemalar atau disusun semula.
- F08 mempunyai sijil geometri bebas; F09 dan F10 mewarisi asas yang telah diaudit itu masing-masing melalui F01/F03 dan F02/F04.
- Syarat domain daripada ungkapan asal kekal terpakai sepanjang pembuktian.

## 2. Penyelesaian bagi bank templat operasi terhingga


---

## a + b = c

Tiada entri yang berjaya dibuktikan dijana bagi templat operasi ini dalam ruang carian terhingga yang dinyatakan.

---

## a - b = c

Tiada entri yang berjaya dibuktikan dijana bagi templat operasi ini dalam ruang carian terhingga yang dinyatakan.

---

## ab = c

### QB-03-001 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-002 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-003 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-004 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-005 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-006 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-007 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-008 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-009 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-010 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-011 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-012 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-013 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-014 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-015 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-016 — `1 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## a/b = c

### QB-04-001 — `1 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-002 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-003 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-004 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-005 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-006 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-007 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-008 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-009 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-010 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-011 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-012 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-013 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-014 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-015 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-016 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-017 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-018 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-019 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-020 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-021 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + c = d

### QB-05-001 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-05-002 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F08`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula


---

## ab - c = d

### QB-06-001 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F01, F08, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-tan(x) + csc(x)*sec(x)` → `-tan(x) + csc(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `-tan(x) + csc(x)/cos(x)` → `-(cos(x)*tan(x) - csc(x))/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x)*tan(x) - csc(x))/cos(x)` → `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` → `-tan(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-tan(x) + 1/(sin(x)*cos(x))` → `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))` → `-(sin(x)**2 - 1)/(sin(x)*cos(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
7. `-(sin(x)**2 - 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
8. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
9. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
10. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-06-002 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04, F08, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` → `csc(x)/cos(x) - cos(x)/sin(x)`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `csc(x)/cos(x) - cos(x)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
7. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
8. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula


---

## abc = d

### QB-07-001 — `sin(x)**2*csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-002 — `sin(x)*cos(x)*sec(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cos(x)*sec(x)` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-003 — `sin(x)*cos(x)*csc(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-004 — `sin(x)*tan(x)*cot(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*tan(x)*cot(x)` → `sin(x)**2*cot(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)**2*cot(x)/cos(x)` → `sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-005 — `sin(x)*tan(x)*csc(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-006 — `sin(x)*cot(x)*sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)*sec(x)` → `cos(x)*sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-007 — `sin(x)*cot(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)*csc(x)` → `cot(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-008 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-009 — `sin(x)*csc(x)*sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-010 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-011 — `sin(x)*csc(x)**2 = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-012 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-013 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-014 — `cos(x)**2*sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)**2*sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-015 — `cos(x)*tan(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)*cot(x)` → `sin(x)*cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-016 — `cos(x)*tan(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)*sec(x)` → `tan(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-017 — `cos(x)*tan(x)*csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)*csc(x)` → `sin(x)*csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-018 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-019 — `cos(x)*cot(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*cot(x)*sec(x)` → `cot(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-020 — `cos(x)*sec(x)**2 = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)**2` → `1/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-021 — `cos(x)*csc(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-022 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-023 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-024 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-025 — `tan(x)**2*cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)**2*cot(x)` → `sin(x)**2*cot(x)/cos(x)**2` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)**2*cot(x)/cos(x)**2` → `sin(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-026 — `tan(x)*cot(x)**2 = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)**2` → `sin(x)*cot(x)**2/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)**2/cos(x)` → `cos(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-027 — `tan(x)*cot(x)*sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-028 — `tan(x)*cot(x)*csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-029 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-030 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-031 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-032 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-033 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-034 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-035 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-036 — `1 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab/c = d

### QB-08-001 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-002 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-003 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-004 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-005 — `sin(x)*cot(x)/cos(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-006 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-007 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-008 — `sin(x)*sec(x)/tan(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-009 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-010 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-011 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-012 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-013 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-014 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-015 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-016 — `1 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-017 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-018 — `cos(x)*tan(x)/sin(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-019 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-020 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-021 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-022 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-023 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-024 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-025 — `cos(x)*csc(x)/cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-026 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-027 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-028 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-029 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-030 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-031 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-032 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-033 — `tan(x)*csc(x)/sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-034 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-035 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-036 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-037 — `cot(x)*sec(x)/csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-038 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-039 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-040 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-041 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-042 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-043 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-044 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-045 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-046 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-047 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-048 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + cd = e

### QB-09-001 — `sin(x)**2 + cos(x)**2 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `GEO: G01 → G03 → G04`  
**ID identiti/pembuktian:** `G01, G03, G04`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

1. **G01 — Teorem Pythagoras Euclid.** Pembuktian melalui pembahagian sebuah segi empat sama menghasilkan hubungan bukan trigonometri `u**2 + v**2 = r**2` bagi segi tiga bersudut tegak.
2. **G03 — Rumus kuasa dua jarak pada satah Cartes.** Unjuran serenjang bagi titik `(u,v)` menghasilkan `OP**2 = u**2 + v**2`, termasuk koordinat bertanda dan kes pada paksi.
3. **G04 — Penggantian menggunakan bulatan unit.** Titik `(cos(x), sin(x))` mempunyai jejari `1`; oleh itu, `cos(x)**2 + sin(x)**2 = 1` bagi setiap nilai nyata `x`.
4. **Kesimpulan.** Bentuk F08 yang diminta terhasil daripada sijil geometri yang telah disemak. F08 tidak digunakan sebagai premis dalam pembuktiannya sendiri.

**Sijil:** `trigonometric-geometric-proof-certificate-v1` — `PROVED`.

### QB-09-002 — `sin(x)*tan(x) + sin(x)*cot(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F01, F03, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*tan(x) + sin(x)*cot(x)` → `sin(x)*tan(x) + cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
5. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-09-003 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-09-004 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F08`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-09-005 — `cos(x)*tan(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F04, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x) + cos(x)*cot(x)` → `sin(x) + cos(x)*cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
5. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula


---

## ab - cd = e

### QB-10-001 — `-sin(x)*tan(x) + tan(x)*csc(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F01, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-sin(x)*tan(x) + tan(x)*csc(x)` → `-sin(x)*tan(x) + tan(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `-sin(x)*tan(x) + tan(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)*tan(x)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(sin(x) - 1)*(sin(x) + 1)*tan(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `-(sin(x) - 1)*(sin(x) + 1)/cos(x)` → `-sin(x)**2/cos(x) + 1/cos(x)`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`
5. `-sin(x)**2/cos(x) + 1/cos(x)` → `(1 - sin(x)**2)/cos(x)`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`
6. `(1 - sin(x)**2)/cos(x)` → `cos(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-002 — `-cos(x)*cot(x) + cot(x)*sec(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F02, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-cos(x)*cot(x) + cot(x)*sec(x)` → `-cos(x)*cot(x) + cot(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `-cos(x)*cot(x) + cot(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)*cot(x)/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x) - 1)*(cos(x) + 1)*cot(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `-(cos(x) - 1)*(cos(x) + 1)/sin(x)` → `-cos(x)**2/sin(x) + 1/sin(x)`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
5. `-cos(x)**2/sin(x) + 1/sin(x)` → `(1 - cos(x)**2)/sin(x)`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/sin(x)` → `sin(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-003 — `-sin(x)*sec(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F03, F08, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-sin(x)*sec(x) + csc(x)*sec(x)` → `-sin(x)*sec(x) + sec(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `-sin(x)*sec(x) + sec(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)*sec(x)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(sin(x) - 1)*(sin(x) + 1)*sec(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)/(sin(x)*cos(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `-(sin(x) - 1)*(sin(x) + 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
7. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-004 — `-cos(x)*csc(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F08, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-cos(x)*csc(x) + csc(x)*sec(x)` → `-cos(x)*csc(x) + csc(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `-cos(x)*csc(x) + csc(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)*csc(x)/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x) - 1)*(cos(x) + 1)*csc(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)/(sin(x)*cos(x))` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `-(cos(x) - 1)*(cos(x) + 1)/(sin(x)*cos(x))` → `-cos(x)/sin(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-cos(x)/sin(x) + 1/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
7. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-005 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F01, F08, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-tan(x) + csc(x)*sec(x)` → `-tan(x) + csc(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `-tan(x) + csc(x)/cos(x)` → `-(cos(x)*tan(x) - csc(x))/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x)*tan(x) - csc(x))/cos(x)` → `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` → `-tan(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-tan(x) + 1/(sin(x)*cos(x))` → `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))` → `-(sin(x)**2 - 1)/(sin(x)*cos(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
7. `-(sin(x)**2 - 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
8. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
9. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
10. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-006 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04, F08, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` → `csc(x)/cos(x) - cos(x)/sin(x)`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `csc(x)/cos(x) - cos(x)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
7. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
8. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-007 — `-sin(x)*tan(x) + sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F08`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `-sin(x)*tan(x) + sec(x)` → `-sin(x)**2/cos(x) + sec(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `-sin(x)**2/cos(x) + sec(x)` → `(-sin(x)**2 + cos(x)*sec(x))/cos(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `cos(x) ≠ 0`
3. `(-sin(x)**2 + cos(x)*sec(x))/cos(x)` → `(1 - sin(x)**2)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `(1 - sin(x)**2)/cos(x)` → `cos(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

### QB-10-008 — `-cos(x)*cot(x) + csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F08`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `-cos(x)*cot(x) + csc(x)` → `csc(x) - cos(x)**2/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `csc(x) - cos(x)**2/sin(x)` → `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)`
   - Justifikasi: Faktorkan hasil tambah sebutan pecahan untuk menzahirkan struktur algebra sepunya; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)` → `-(cos(x)**2 - 1)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `-(cos(x)**2 - 1)/sin(x)` → `-cos(x)**2/sin(x) + 1/sin(x)`
   - Justifikasi: Agihkan faktor -1 kepada ungkapan berbentuk hasil tambah; tiada identiti trigonometri digunakan.
   - Syarat: `sin(x) ≠ 0`
5. `-cos(x)**2/sin(x) + 1/sin(x)` → `(1 - cos(x)**2)/sin(x)`
   - Justifikasi: Gabungkan sebutan pecahan menggunakan penyebut sepunya tanpa menggunakan identiti trigonometri yang lain.
   - Syarat: `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/sin(x)` → `sin(x)` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula


---

## ab/cd = e

### QB-11-001 — `1 = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-002 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-003 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-004 — `sin(x)**2/(cos(x)*tan(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)**2/(cos(x)*tan(x))` → `sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-005 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-006 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-007 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-008 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-009 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-010 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-011 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-012 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-013 — `sin(x)*cot(x)/cos(x)**2 = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/cos(x)**2` → `1/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-014 — `sin(x)*cot(x)/(cos(x)*tan(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/(cos(x)*tan(x))` → `cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-015 — `sin(x)*cot(x)/(cos(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-016 — `sin(x)*cot(x)/(cos(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-017 — `sin(x)*cot(x)/cos(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-018 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-019 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-020 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-021 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-022 — `sin(x)*sec(x)/(cos(x)*tan(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/(cos(x)*tan(x))` → `sec(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-023 — `sin(x)*sec(x)/tan(x)**2 = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/tan(x)**2` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-024 — `sin(x)*sec(x)/(tan(x)*cot(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-025 — `sin(x)*sec(x)/(tan(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-026 — `sin(x)*sec(x)/tan(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-027 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-028 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-029 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-030 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `Algebra sahaja`  
**ID identiti/pembuktian:** `Algebra sahaja`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

Pernyataan ini dibuktikan melalui kesamaan algebra yang tepat; sijil merekodkan transformasi yang telah disemak.

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-031 — `sin(x)*csc(x)/(cos(x)*tan(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/(cos(x)*tan(x))` → `csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-032 — `sin(x)*csc(x)/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-033 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-034 — `sin(x)*csc(x)/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-035 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-036 — `sin(x)*csc(x)/(cot(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)**2*csc(x)/(cos(x)*sec(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/(cos(x)*sec(x))` → `sin(x)**2*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-037 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-038 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-039 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-040 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-041 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-042 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-043 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-044 — `sin(x)/(cos(x)*tan(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)/(cos(x)*tan(x))` → `1` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-045 — `sin(x)/(cos(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-046 — `sin(x)/(tan(x)*cot(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sin(x)/(tan(x)*cot(x))` → `cos(x)/cot(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-047 — `cos(x)**2/(sin(x)*cot(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-048 — `cos(x)*tan(x)/sin(x)**2 = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/sin(x)**2` → `1/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-049 — `cos(x)*tan(x)/(sin(x)*cot(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/(sin(x)*cot(x))` → `tan(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-050 — `cos(x)*tan(x)/(sin(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/(sin(x)*sec(x))` → `1/sec(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-051 — `cos(x)*tan(x)/(sin(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/(sin(x)*csc(x))` → `1/csc(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-052 — `cos(x)*tan(x)/sin(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-053 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-054 — `cos(x)*sec(x)/(sin(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-055 — `cos(x)*sec(x)/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-056 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-057 — `cos(x)*sec(x)/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)**2*sec(x)/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/(sin(x)*cot(x))` → `cos(x)*sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-058 — `cos(x)*sec(x)/(tan(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)**2*sec(x)/(sin(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/(sin(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-059 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-060 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-061 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-062 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-063 — `cos(x)*csc(x)/(sin(x)*cot(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-064 — `cos(x)*csc(x)/(tan(x)*cot(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)**2*csc(x)/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2*csc(x)/(sin(x)*cot(x))` → `cos(x)*csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-065 — `cos(x)*csc(x)/cot(x)**2 = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04, F01`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/cot(x)**2` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-066 — `cos(x)*csc(x)/(cot(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-067 — `cos(x)*csc(x)/cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-068 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F02`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-069 — `cos(x)/(sin(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-070 — `cos(x)/(sin(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-071 — `cos(x)/(tan(x)*cot(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cos(x)/(tan(x)*cot(x))` → `cos(x)**2/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-072 — `tan(x)**2/(sin(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `tan(x)**2/(sin(x)*sec(x))` → `sin(x)/(cos(x)**2*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)**2*sec(x))` → `sin(x)/cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-073 — `tan(x)*cot(x)/(sin(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/(sin(x)*sec(x))` → `cot(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-074 — `tan(x)*cot(x)/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F05`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/(sin(x)*csc(x))` → `tan(x)*cot(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `tan(x)*cot(x)` → `1` — **F05**
   - Teorem yang digunakan: F05 — tan x · cot x = 1
   - Justifikasi: Gunakan identiti F05 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F05 bergantung pada F01
- F05 bergantung pada F02

### QB-11-075 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-076 — `tan(x)*cot(x)/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F05`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/(cos(x)*sec(x))` → `tan(x)*cot(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `tan(x)*cot(x)` → `1` — **F05**
   - Teorem yang digunakan: F05 — tan x · cot x = 1
   - Justifikasi: Gunakan identiti F05 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F05 bergantung pada F01
- F05 bergantung pada F02

### QB-11-077 — `tan(x)*cot(x)/(cos(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/(cos(x)*csc(x))` → `tan(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-078 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-079 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/sec(x)` → `cos(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-080 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-081 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-082 — `tan(x)*csc(x)/(sin(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/(sin(x)*sec(x))` → `csc(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-083 — `tan(x)*csc(x)/(cos(x)*sec(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F01, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/(cos(x)*sec(x))` → `tan(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-084 — `tan(x)*csc(x)/(cot(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*tan(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-085 — `tan(x)*csc(x)/sec(x)**2 = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/sec(x)**2` → `sin(x)*csc(x)/(cos(x)*sec(x)**2)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x)**2)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-086 — `tan(x)*csc(x)/sec(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-087 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-088 — `tan(x)/(sin(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `tan(x)/(sin(x)*sec(x))` → `1/(cos(x)*sec(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/(cos(x)*sec(x))` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-089 — `tan(x)/(sin(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-090 — `tan(x)/(cos(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `tan(x)/(cos(x)*sec(x))` → `tan(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-091 — `cot(x)**2/(cos(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)**2/(cos(x)*csc(x))` → `cos(x)/(sin(x)**2*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)**2*csc(x))` → `cos(x)/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-092 — `cot(x)*sec(x)/(sin(x)*csc(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)*sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
3. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-093 — `cot(x)*sec(x)/(cos(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/(cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-094 — `cot(x)*sec(x)/(tan(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-095 — `cot(x)*sec(x)/csc(x)**2 = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/csc(x)**2` → `cos(x)*sec(x)/(sin(x)*csc(x)**2)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x)**2)` → `1/(sin(x)*csc(x)**2)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x)**2)` → `sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-096 — `cot(x)*sec(x)/csc(x) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-097 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-098 — `cot(x)/(sin(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-099 — `cot(x)/(cos(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-100 — `cot(x)/(cos(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F04`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `cot(x)/(cos(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-101 — `sec(x)**2/(tan(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)**2/(tan(x)*csc(x))` → `cos(x)*sec(x)**2/(sin(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)**2/(sin(x)*csc(x))` → `1/(sin(x)*cos(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/(sin(x)*cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
4. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-102 — `sec(x)/(sin(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-103 — `sec(x)/(tan(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-104 — `sec(x)/(tan(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F03, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-105 — `csc(x)**2/(cot(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)**2/(cot(x)*sec(x))` → `sin(x)*csc(x)**2/(cos(x)*sec(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)**2/(cos(x)*sec(x))` → `sin(x)*csc(x)**2` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
4. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-106 — `csc(x)/(cos(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-107 — `csc(x)/(tan(x)*cot(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-108 — `csc(x)/(cot(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03, F04`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-109 — `1/(sin(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/(sin(x)*cot(x))` → `1/cos(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-110 — `1/(sin(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/(sin(x)*sec(x))` → `cos(x)/sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-111 — `1/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04`  
**Domain sepunya asal:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-112 — `1/(cos(x)*tan(x)) = csc(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/(cos(x)*tan(x))` → `1/sin(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-113 — `1/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F03`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Pembuktian**

1. `1/(cos(x)*sec(x))` → `1` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-114 — `1/(cos(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F04, F01`  
**Domain sepunya asal:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah songsang pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-115 — `1/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F02`  
**Domain sepunya asal:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/(tan(x)*cot(x))` → `cos(x)/(sin(x)*cot(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-116 — `1/(tan(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F01, F04`  
**Domain sepunya asal:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Pembuktian**

1. `1/(tan(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F01**
   - Teorem yang digunakan: F01 — tan x = sin x / cos x
   - Justifikasi: Gunakan identiti F01 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Teorem yang digunakan: F04 — csc x = 1/sin x
   - Justifikasi: Gunakan identiti F04 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-117 — `1/(cot(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Laluan pembuktian terpilih:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F02, F03`  
**Domain sepunya asal:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Pembuktian**

1. `1/(cot(x)*sec(x))` → `sin(x)/(cos(x)*sec(x))` — **F02**
   - Teorem yang digunakan: F02 — cot x = cos x / sin x
   - Justifikasi: Gunakan identiti F02 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Teorem yang digunakan: F03 — sec x = 1/cos x
   - Justifikasi: Gunakan identiti F03 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.


## 3. Penyelesaian tambahan yang menunjukkan penggunaan semula teorem

### SUP-001 — Identiti gabungan linear ortogon

**Pernyataan:** `(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2 = p**2+q**2`

**Status:** `PROVED`  
**Laluan pembuktian:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F08`  
**Domain sepunya asal:** Semua nilai nyata bagi pemboleh ubah dalam pernyataan tersebut.

**Pembuktian**

1. `(p*sin(x) - q*cos(x))**2 + (p*cos(x) + q*sin(x))**2` → `p**2*sin(x)**2 + p**2*cos(x)**2 + q**2*sin(x)**2 + q**2*cos(x)**2`
   - Justifikasi: Gunakan hukum pengagihan untuk mengembangkan kuasa dua gabungan linear; fungsi trigonometri dianggap sebagai faktor algebra.
2. `p**2*sin(x)**2 + p**2*cos(x)**2 + q**2*sin(x)**2 + q**2*cos(x)**2` → `(p**2 + q**2)*(sin(x)**2 + cos(x)**2)`
   - Justifikasi: Kumpulkan faktor parameter sepunya untuk menzahirkan hasil tambah sin(x)**2 + cos(x)**2 supaya identiti yang telah dibuktikan dapat digunakan.
3. `(p**2 + q**2)*(sin(x)**2 + cos(x)**2)` → `p**2 + q**2` — **F08**
   - Teorem yang digunakan: F08 — sin²x + cos²x = 1
   - Justifikasi: Gunakan identiti F08 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula

---

### SUP-002 — Penggunaan F09 dalam identiti yang berlainan

**Pernyataan:** `(1+tan(x)**2)*cos(x)**2 = sec(x)**2*cos(x)**2`

**Status:** `PROVED`  
**Laluan pembuktian:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F09`  
**Domain sepunya asal:** `cos(x) ≠ 0`

**Pembuktian**

1. `(tan(x)**2 + 1)*cos(x)**2` → `cos(x)**2*sec(x)**2` — **F09**
   - Teorem yang digunakan: F09 — 1 + tan²x = sec²x
   - Justifikasi: Gunakan identiti F09 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `cos(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F09 bergantung pada F08
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula
- F09 bergantung pada F01
- F09 bergantung pada F03

---

### SUP-003 — Penggunaan F10 dalam identiti yang berlainan

**Pernyataan:** `(1+cot(x)**2)*sin(x)**2 = csc(x)**2*sin(x)**2`

**Status:** `PROVED`  
**Laluan pembuktian:** `LHS menggunakan katalog identiti`  
**ID identiti/pembuktian:** `F10`  
**Domain sepunya asal:** `sin(x) ≠ 0`

**Pembuktian**

1. `(cot(x)**2 + 1)*sin(x)**2` → `sin(x)**2*csc(x)**2` — **F10**
   - Teorem yang digunakan: F10 — 1 + cot²x = csc²x
   - Justifikasi: Gunakan identiti F10 yang telah dibuktikan dalam arah hadapan pada subungkapan yang sepadan. Identiti yang telah disubstitusikan disemak terhadap langkah yang direkodkan.
   - Penggantian pemboleh ubah: `x → x`
   - Syarat: `sin(x) ≠ 0`

**Sijil:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Asal usul kebergantungan teorem**
- F10 bergantung pada F08
- F08 bergantung pada GEO.F08
- GEO.F08 hanya diterima selepas G01 -> G03 -> G04 disemak semula
- F10 bergantung pada F02
- F10 bergantung pada F04

## 4. Pernyataan hampir serupa yang ditolak — bukan soalan yang berjaya dibuktikan

**Pernyataan seperti yang mula-mula ditaip:** `(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2 = p**2+q**2`

**Status:** `DISPROVED`

Tanda kurung kedua mengandungi `p*cos(x)` dan bukannya `q*cos(x)`. Satu contoh balas yang tepat sudah memadai:

Ambil `p = 1`, `q = 0`, `x = 0`.

- LHS = `(1*1 + 0*0)**2 + (1*0 - 1*1)**2 = 1 + 1 = 2`.
- RHS = `1**2 + 0**2 = 1`.
- Oleh itu, pernyataan seperti yang ditulis adalah palsu dan tidak boleh diberikan status `PROVED`.

Identiti yang telah dibetulkan dalam `SUP-001` berjaya dibuktikan menggunakan F08.
