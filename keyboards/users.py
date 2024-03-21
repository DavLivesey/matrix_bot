class USERCARD:
    def __init__(self, fullname, apteka, zkgu, bgu1, bgu2, dieta, mis, tis, sed) -> None:
        self.fullname = fullname
        self.apteka = False
        self.zkgu = False
        self.bgu1 = False
        self.bgu2 = False
        self.dieta = False
        self.mis = False
        self.tis = False
        self.sed = False

    def show_user(self):
        return (f'{self.fullname} имеет следующие доступы:\n 1С-Аптека - {self.apteka}\n ' \
                f'1С_ЗКГУ - {self.zkgu}, 1С_БГУ 1.0 - {self.bgu1}, 1С_БГУ 2.0 {self.bgu2}, ' \
                    f'1С_Диетпитание - {self.dieta}, МИС - {self.mis}, ТИС - {self.tis}, СЭД - {self.sed}')

    def edit_user(fullname):
        pass

