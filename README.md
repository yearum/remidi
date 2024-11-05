Fungsi ini menerima parameter n, yaitu jumlah bilangan yang ingin dihasilkan.
Menggunakan list comprehension untuk membuat daftar bilangan dari 1 sampai n dengan perulangan for i in range(1, n+1). Perulangan ini menghasilkan nilai i dimulai dari 1 hingga n.
Contoh: Jika n = 5, maka hitung_bilangan_urut(5) akan menghasilkan [1, 2, 3, 4, 5].
Fungsi ini menerima dua parameter: n (jumlah bilangan yang ingin dihasilkan) dan kenaikan (selisih antara bilangan berturut-turut).
Menggunakan list comprehension dengan perulangan for i in range(1, (n * kenaikan) + 1, kenaikan), yang akan menghasilkan bilangan mulai dari 1 hingga (n * kenaikan), dengan langkah (step) sebesar kenaikan.
Contoh: Jika n = 5 dan kenaikan = 3, maka hitung_bilangan_urut_naik(5, 3) akan menghasilkan [1, 4, 7, 10, 13].
Fungsi ini menerima dua parameter: n (jumlah bilangan acak yang ingin dihasilkan) dan batas_atas (batas maksimum untuk bilangan acak).
Menggunakan list comprehension untuk menghasilkan bilangan acak sebanyak n kali dengan random.randint(1, batas_atas), di mana setiap angka acak berada di antara 1 dan batas_atas.
Contoh: Jika n = 5 dan batas_atas = 10, maka hitung_bilangan_acak(5, 10) mungkin menghasilkan [3, 7, 1, 9, 5]. Hasilnya akan berbeda setiap kali program dijalankan karena bilangan ini acak.
