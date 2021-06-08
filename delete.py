
name = [
    "Hsu, Gee-Sern Jison (editor)",
    "Timofte, Radu (editor)"
]

book = "Deep Learning for Facial Informatics"
place = "Basel"
publiher = "MDPI - Multidisciplinary Digital Publishing Institute"
year = "2020"
pages = "102"
url = "https://mdpi.com/books/pdfview/book/2884"


a, b = name[0].split(', ')
b = b[0]

fn = f"{a}, {b}"

lns = []
for n in name:
    a, b = n.split(', ')
    b = b[0]
    ln = f"{b}. {a}"
    lns.append(ln)
lns = ", ".join(lns)

print(
    f"{fn}. {book} / {lns}. - {place}: {publiher}, {year}. - {pages} c. // Directory of open access books (DOAB). –URL: {url} (дата обращения:  02.04.2021). – Режим доступа: для всех пользователей"
)