from googlesearch import search
import os

path = os.getcwd()

def main():
    domain = "co.id"  #represents the top-level domain (TLD) to be used for Google searches.
    link_blocked = ["id.linkedin.com", "linkedin.com", "youtube.com", "instagram.com", "facebook.com", "tokopedia.com",
                    "twitter.com", "reddit.com", "bukalapak.com", "shopee.com", "blibli.com"]
    # these above urls are excluded urls from the search results due to being blocked.

    input_text = input("Enter the text: ").strip() #enter some text, which is then stripped of leading and trailing whitespaces and stored in the variable 'input_text'....
    filename = "word.txt"  #store input texts in a file...
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(input_text)

####eplacing newline characters with spaces and splitting the raw texts...
    inputan_mentah = input_text
    inputan = inputan_mentah.replace("\n", " ").split(". ")

    hasil_plagiarism_final = []
    hasil_link_final = []

###Iterate the loop for each sentences in the input text, construct and perform Google search query for the sentences and append the plagiarized sentences and links.*****
    for i in range(len(inputan)):
        query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
        for j, link in enumerate(search(query, tld=domain, num=10, stop=10, pause=2)):
            if i != j:
                continue
            hasil_plagiarism_final.append(inputan[i])
            hasil_link_final.append(link)

### Filterring the links with the 'link_blocked' list and append the finals.....*****
    for i in range(len(hasil_plagiarism_final)):
        for j in range(len(hasil_link_final)):
            if i != j:
                continue
            while True:
                for k in range(len(link_blocked)):
                    if link_blocked[k] in hasil_link_final[j]:
                        break
                else:
                    break
                break

### Count the percentage of plagiarism with respect to the number of plagiarized sentences and the total number of sententences given.****
    count = len(inputan)
    count_hasil = len(hasil_link_final)
    hasil_persen = (count_hasil / count) * 100

####printing the outputs ===>
        # 1. Plagiarism Percentages,
        # 2. Plagiarized Texts,
        # 3. Source Plagiarism Links.
    print("Plagiarism percentage:", hasil_persen)
    print("Plagiarized text:")
    for text in hasil_plagiarism_final:
        print(text)
    print("Links:")
    for link in hasil_link_final:
        print(link)

if __name__ == "__main__":
    main()
