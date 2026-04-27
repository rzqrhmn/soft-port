# Roadmap

Plan saya selama 6 bulan ke depan. Akan banyak yang berubah, tapi setidaknya ada arah.

## Latar belakang singkat

Saya 10 tahun kerja di blower plant Krakatau Posco, banyak ngurus motor sinkron besar dan sistem pendukungnya. Sekarang lagi nyelesain MSc Electrical Engineering di Hochschule Kempten. Goal saya pindah ke role testing / commissioning / lab engineering di Jerman. Repo ini buat naikin sisi software/embedded saya, biar gak cuma "operator yang ngerti listrik".

15-30 menit per hari. Boleh skip, jangan berhenti.

## Level 1 - Python dasar pakai data sensor (Bulan 1)

Belum perlu hardware apapun. Tujuannya nyaman pakai Git, Python, dan baca data dari CSV.

Minggu 1: baca file CSV motor temperature, hitung mean/max/min, plot pakai matplotlib, bikin CLI tool sederhana.

Minggu 2: generate fake sensor data, deteksi anomaly pakai rolling mean + 2 sigma, bikin sensor reader berbasis class.

Minggu 3-4: polish dengan Rich library, logging, config file, error handling, type hints. Tambah tests pakai pytest. Setup GitHub Actions buat CI. Beresin README.

Output: 1 repo Python yang lumayan rapi, ada test, ada CI hijau. Bahan ngobrol pas interview kalau ditanya "pernah pakai Python untuk apa?".

## Level 2 - Protokol industrial (Bulan 2)

Masih tanpa hardware. Implementasi protokol komunikasi pabrik di Python murni.

- Parser frame Modbus RTU, termasuk CRC check
- Modbus TCP server simulator (pura-pura jadi sensor)
- CAN bus message decoder pakai DBC file
- MQTT pub/sub pakai broker Mosquitto lokal

Ini bagian yang paling jarang dipunya orang fresh dari Python. Kalau interview testing/commissioning, biasanya orang nanya soal Modbus, jadi punya kode yang bisa dipamerkan = nilai plus.

## Level 3 - Firmware simulasi (Bulan 3)

Mulai nulis C/C++ untuk Arduino/ESP32, tapi lewat Wokwi.com (gratis, jalan di browser, gak perlu beli apa-apa).

Minggu pertama: blink LED, serial print, baca sensor DHT22.
Minggu kedua: PWM untuk fade LED, state machine traffic light.
Minggu ketiga: PID controller di C, di-compile dan dites di laptop.
Minggu keempat: Modbus slave di Arduino virtual.

## Level 4 - Hardware beneran (Bulan 4-5, opsional)

Beli ESP32 dev board (~10 EUR di Reichelt), DHT22 sensor (~3 EUR), breadboard kit. Total sekitar 25-30 EUR.

Bikin temperature monitor: ESP32 baca sensor, kirim ke MQTT broker, dashboard web kecil pakai Flask, log ke SQLite, alert email kalau lewat threshold.

Bagian penting: foto dokumentasi rangkaiannya, masukin ke README. Recruiter Jerman seneng lihat orang yang beneran solder dan rapikan kabel.

## Level 5 - Capstone: condition monitoring motor (Bulan 6)

Ini yang paling nyambung sama pengalaman saya. ESP32 + accelerometer MPU6050 (~5 EUR) ditempel ke kipas atau motor kecil. Baca data getaran, latih model klasifikasi sederhana di laptop (normal vs unbalanced vs bearing aus), deploy modelnya ke ESP32 pakai TF Lite Micro. Alert via MQTT.

Kalau jadi, ini cerita interview yang bagus: "Pengalaman 10 tahun saya di motor industrial saya gabungkan dengan ML edge device. Begini implementasinya."

## Yang saya harapin di akhir 6 bulan

- 5 repo public di GitHub yang isinya kode beneran, ada test, ada README
- Sekitar 100-150 hari commit (skip OK, gak fanatik 365 days)
- Satu artikel LinkedIn yang nyeritain capstone project
- Sebuah portfolio yang bisa saya tunjukin ke HR Jerman tanpa malu

Itu udah cukup buat tembus screening Werkstudent / Praktikum / junior testing role. Sisanya tergantung interview.

## Catatan

Roadmap ini bukan kontrak. Kalau di tengah jalan saya nemu hal yang lebih menarik atau lebih relevan ke job posting yang saya incar, saya geser. Yang penting: ada output public tiap minggu.
