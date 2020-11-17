import PyPDF2


def get_vat_from_pdf(pdf_path, begin_search_string, end_search_string, no_occurrences):
    # creating a pdf file object
    pdf_file_obj = open(pdf_path, 'rb')

    # creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # number of pages in pdf file
    # no_of_pages = pdf_reader.numPages

    # creating a page object
    page_obj = pdf_reader.getPage(0)

    # extracting text from page
    page_text = page_obj.extractText()

    begin_slice = 0

    if no_occurrences == 1:
        begin_slice = page_text.find(begin_search_string) + len(begin_search_string)
    elif no_occurrences == 2:
        begin_slice = page_text.find(begin_search_string,
                                     page_text.find(begin_search_string) + len(begin_search_string)) + \
                      len(begin_search_string)
    else:
        print('GET_VAT_FROM_PDF: Number of occurrences is not in range pick 1 or 2')

    end_slice = page_text.find(end_search_string, begin_slice)
    return page_text[begin_slice: end_slice].strip()


print(get_vat_from_pdf(r'pdfs/Factura CS16505 - Betarom.pdf', 'C.I.F.: RO', 'Banca:', 2))
