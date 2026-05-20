link = {}
dictionary = []
index = 0
sentences = []

while True:
    products = []
    best_product = [[], [], 0]
    actual_subject = ""

    sentence = str(input("Please Type Any Correct Sentence: ")).lower()
    words = sentence.split(" ")

    for word in words:
        if word not in link:
            link[word] = index
            dictionary.append([1, 1])
            index += 1

    for query in words:
        for key in words:
            if key == query:
                continue

            score = dictionary[link[query]][0] * dictionary[link[key]][1]

            products.append([[query], [key], score])

    for pair in products:
        if pair[2] > best_product[2]:
            best_product = pair
            print(best_product)

    print(best_product[0][0] + " is the Subject")

    actual_subject = str(input("What is the actual subject: ")).lower()

    if sentence not in sentences:
        dictionary[link[actual_subject]][0] = 10
        sentences.append(sentence)

    if input("Finish? (No / Yes): ") == "Yes":
        break