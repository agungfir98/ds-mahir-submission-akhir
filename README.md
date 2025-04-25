# Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institute

> ⚠️ Peringatan 
> 
> Skenario dalam proyek ini hanyalah fiktif belaka. Apabila terdapat kesamaan nama tokoh, perusahaan, ataupun produk, itu adalah kebetulan semata dan tidak ada unsur kesengajaan.
## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
Proyek ini berupaya mengidentifikasi faktor apa saja yang dapat membuat siswa pada Jaya Jaya Institute melakukan drop out dengan melihat hubungan data yang dianggap relevan seperti hubungan antara dropout berdasarkan siswa dengan scholarship(beasiswa), siswa yang memliki hutang, siswa yang telah membayar kuliah, nilai semester lalu dan nilai admisi. Lalu proyek ini juga membuat model machine learning guna memprediksi siswa yang mungkin akan melakukan drop out.

### Persiapan

Sumber data: [Dataset Jaya Jaya Maju Institute](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

**Clone repo**
```bash
# clone this repo 
git clone https://github.com/agungfir98/ds-mahir-submission-akhir.git
cd ds-mahir-submission-akhir
```
**Setup virtual Environtment (opsional)**
```bash
python -m venv ./venv
source ./venv/Script/activate
```
### setup
```bash
pip install -r requirements.txt
```
## Business Dashboard
Link: [Tableau Public](https://public.tableau.com/views/student-performance_17449614272170/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Dashboard mencakup faktor yang mungkin dapat menyebabkan siswa untuk drop out seperti apakah siswa adalah penerima beasiswa, apakah siswa berhutang, apakah siswa telah membayar biaya kuliah, dan nilai siswa semester lalu

## Menjalankan Sistem Machine Learning
Link: [Streamlit cloud](https://agungfir98-ds-mahir-submission-akhir-prediction-app.streamlit.app/)

run on local:
```shell
streamlit run predict_app.py
```

## Conclusion

Beberapa hal mempengaruhi kerentanan siswa untuk melakukan drop out, mulai dari kondisi finansial siswa. siswa yang tidak memiliki beasiswa cenderung untuk dropout, begitu juga  dan juga nilai siswa pada semester lalu.

### Rekomendasi Action Items (Optional)

- Memberi konsultasi terhadap siswa yang memiliki masalah biaya.
- Mengevaluasi biaya perkuliahan
- mengevaluasi tentang banyaknya siswa yang memiliki nilai rendah dan tidak lolos kelas pada semester 1
- memberi beasiswa terhadap siswa yang layak seperti yang terkendala biaya dan berprestasi