import re
class Kitab:

    def libraff(self, axtarilan_soz, saytdaki_soz):
        print(f"Libraff funksiyasinin icherisindeyem {axtarilan_soz} - {saytdaki_soz}")
        if axtarilan_soz == saytdaki_soz:
            return True
        else:
            similarity_percentage = self.similarity(axtarilan_soz, saytdaki_soz)
            if similarity_percentage > 80:
                return True
            else:
                result_list = saytdaki_soz.split(" ")
                if axtarilan_soz in result_list:
                    return True
                else:
                    return False

    def libraff_price(self, price_text):
        # Define a regular expression pattern to match the number
        pattern = r'<span class="ty-price-num ty-nowrap">([\d.]+)</span>'

        # Use re.findall to find all matches of the pattern in the string
        matches = re.findall(pattern, price_text)
        return matches[0]

    def similarity(self, sentence1, sentence2):
        print("calculate_cosine_similarity funksiyasinin ichindeyem")
        set_a = set(sentence1)
        set_b = set(sentence2)

        similarity = len(set_a.intersection(set_b)) / len(set_a.union(set_b)) * 100
        return similarity
