import pdfplumber

with pdfplumber.open(r'C:\Nice_Doc_repository\Akshay_DocumentRepo\SQL Always On - Engage 7.6.pdf') as pdf:
    print(f'Total pages: {len(pdf.pages)}')
    for i, page in enumerate(pdf.pages[:10]):
        text = page.extract_text()
        if text:
            print(f'--- Page {i+1} ---')
            print(text[:2000])
