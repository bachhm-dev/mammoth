import mammoth

resultFile = open("result.html","a")

with open("document.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
    resultFile.write(html)

