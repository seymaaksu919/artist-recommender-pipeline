# artist-recommender-pipeline

Bu kodda, sanatçılara ait bir veri kümesinden anlamlı özellikler çıkarmak için boyut indirgeme ve veri ön işleme tekniklerinin nasıl bir araya getirileceğini gösterir. Kodda MaxAbsScaler, NMF (Negatif Olmayan Matris Faktörizasyonu) ve Normalizer adımları bir pipeline içinde birleştirilmiştir.

## 🔍 Kodun Amacı

- Verileri -1 ile 1 arasına ölçeklemek (`MaxAbsScaler`)
- Boyutları düşürmek için NMF uygulamak
- Ortaya çıkan özellik vektörlerini normalize etmek (`Normalizer`)

Elde edilen özellikler, öneri sistemleri, kümeleme ve benzerlik analizi gibi işlemlerde kullanılabilir.

## ⚙️ Kullanılan Teknolojiler

- Python 3
- scikit-learn
- NumPy
- pandas

## 📊 Örnek Veri

Kod, örnek olarak şu şekilde rastgele oluşturulmuş 10x1000 boyutunda bir veri ile çalışır:
python
artists = np.abs(np.random.rand(10, 1000))
