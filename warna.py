def pilih_warna_biru():
    warna_biru = (0, 0, 255)  
    return warna_biru

def gabungkan_warna(warna1, warna2):
    gabungan = (
        (warna1[0] + warna2[0]) // 2,
        (warna1[1] + warna2[1]) // 2,
        (warna1[2] + warna2[2]) // 2
    )
    return gabungan

def cmy_to_rgb(cmy):
    r = int((1 - cmy[0]) * 255)
    g = int((1 - cmy[1]) * 255)
    b = int((1 - cmy[2]) * 255)
    return (r, g, b)

def campur_warna_cmy(warna1_cmy, warna2_cmy):
    warna1_rgb = cmy_to_rgb(warna1_cmy)
    warna2_rgb = cmy_to_rgb(warna2_cmy)
    
    warna_campuran_rgb = gabungkan_warna(warna1_rgb, warna2_rgb)
    return warna_campuran_rgb

warna_biru = pilih_warna_biru()
print("Warna biru:", warna_biru)

warna1_rgb = (100, 150, 200)  
warna2_rgb = (50, 100, 150)   
warna_gabungan = gabungkan_warna(warna1_rgb, warna2_rgb)
print("Gabungan warna RGB:", warna_gabungan)

warna1_cmy = (0.2, 0.4, 0.6)  
warna2_cmy = (0.5, 0.3, 0.1)  
warna_campuran = campur_warna_cmy(warna1_cmy, warna2_cmy)
print("Campuran warna CMY (hasil dalam RGB):", warna_campuran)
