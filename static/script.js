async function analisis() {
    let frekuensi = parseFloat(document.getElementById("frekuensi").value);
    let rata_pengeluaran = parseFloat(document.getElementById("rata_pengeluaran").value);
    let jarak = parseFloat(document.getElementById("jarak").value);

    let hasil = document.getElementById("hasilTeks");

    if (isNaN(frekuensi) || isNaN(rata_pengeluaran) || isNaN(jarak)) {
        hasil.textContent = "Semua input harus diisi!";
        hasil.className = "hasil-box";
        return;
    }

 try {
        let response = await fetch("https://speskristalpremium.onrender.com/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                frekuensi: frekuensi,
                rata_pengeluaran: rata_pengeluaran,
                jarak: jarak
            })
        });

        let data = await response.json();
        let predict = data.hasil;

        if (predict === "Aktif") {
            hasil.textContent = "Pelanggan Aktif";
            hasil.className = "hasil-box status-aktif";
        }
        else if (predict === "Pasif") {
            hasil.textContent = "Pelanggan Pasif";
            hasil.className = "hasil-box status-pasif";
        }
        else {
            hasil.textContent = "Pelanggan Berhenti";
            hasil.className = "hasil-box status-berhenti";
        }
    }

    catch (err) {
        hasil.textContent = "Gagal terhubung ke server!";
        hasil.className = "hasil-box status-berhenti";
        console.error(err);
    }
}
