from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
from urllib.parse import quote
from axtar import Kitab


global_axtarilan_soz = ""

kitab = Kitab()
string = "İ"
print(quote(string.lower()).replace("i%CC%87", "i"))
print(quote("i"))
class Interface(GridLayout):
    def axtar(self):
        global global_axtarilan_soz
        global_axtarilan_soz = self.ids.kitab_adi.text.lower()
        quoted_axtarilan_soz = quote(global_axtarilan_soz).replace("i%CC%87", "i")
        libraff_url = f"https://www.libraff.az/index.php?dispatch=products.get_products_list&page=1&is_ajax=1&q={quoted_axtarilan_soz}"
        UrlRequest(libraff_url, on_success=self.libraff_netice, on_failure=self.libraff_netice)

    def libraff_netice(self, req_body, result):
        global global_axtarilan_soz
        libraff_kitab  =   result['products']

        libraff_price = kitab.libraff_price(libraff_kitab[0]['price'])

        if  libraff_kitab:
            libraf_yoxla = kitab.libraff(global_axtarilan_soz, libraff_kitab[0]['product'].lower())
            if libraf_yoxla:
                self.ids.libraff.text = f"Libraff: {libraff_price} AZN"
            else:
                self.ids.libraff.text = "Libraff-da tapılmadı"
        else:
            self.ids.libraff.text = "Libraff-da tapılmadı"


class LayoutsApp(App):
    pass


LayoutsApp().run()