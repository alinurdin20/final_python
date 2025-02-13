import pandas as pd
data = {
    'Nama': ['Ali', 'Budi', 'Citra', 'Dian'],
    'Umur': [25, 30, 22, 28],
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan']
}
df = pd.DataFrame(data)
print(df)
