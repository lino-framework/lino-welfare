# -*- coding: UTF-8 -*-
logger.info("Loading 47 objects to table ledger_account...")
# fields: id, ref, seqno, name, common_account, needs_partner, clearable, default_amount, sales_allowed, purchases_allowed, wages_allowed, taxes_allowed, clearings_allowed, bank_po_allowed
loader.save(create_ledger_account(1,u'1000',1,['Net income (loss)', 'Net income (loss)', 'Net income (loss)'],'1000',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(23,u'4',23,['Commercial assets & liabilities', 'Commercial assets & liabilities', 'Commercial assets & liabilities'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(2,u'4000',2,['Kunden', 'Clients', 'Customers'],'4000',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(3,u'4300',3,['Offene Zahlungsauftr\xe4ge', 'Ordres de paiement ouverts', 'Pending Payment Orders'],'4300',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(4,u'4400',4,['Lieferanten', 'Fournisseurs', 'Suppliers'],'4400',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(21,u'4450',21,['Auszuf\xfchrende Ausgabeanweisungen', 'Mandats \xe0 ex\xe9cuter', 'Disbursement orders to execute'],u'4450',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(5,u'4500',5,['Angestellte', 'Employ\xe9s', 'Employees'],'4500',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(7,u'4510',7,['Geschuldete Mehrwertsteuer', 'TVA d\xfbe', 'VAT due'],'4510',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(8,u'4511',8,['R\xfcckzahlbare Mehrwertsteuer', 'TVA \xe0 retourner', 'VAT returnable'],'4511',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(9,u'4512',9,['Abziehbare Mehrwertsteuer', 'TVA d\xe9ductible', 'VAT deductible'],'4512',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(10,u'4513',10,['Deklarierte Mehrwertsteuer', 'TVA d\xe9clar\xe9e', 'VAT declared'],'4513',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(6,u'4600',6,['Steuer\xe4mter', 'Steuer\xe4mter', 'Tax Offices'],'4600',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(22,u'4800',22,['Granted aids', 'Granted aids', 'Granted aids'],u'4800',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(11,u'4900',11,['Wartekonto', 'Wartekonto', 'Waiting account'],'4900',True,True,None,False,False,False,False,False,False))
loader.save(create_ledger_account(24,u'5',24,['Financial assets & liabilities', 'Financial assets & liabilities', 'Financial assets & liabilities'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(12,u'5500',12,['BestBank', 'BestBank', 'BestBank'],'5500',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(13,u'5700',13,['Kasse', 'Caisse', 'Cash'],'5700',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(25,u'6',25,['Ausgaben', 'D\xe9penses', 'Expenses'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(26,u'60',26,['Diplome', 'Diplome', 'Operation costs'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(15,u'6010',15,['Eink\xe4ufe von Dienstleistungen', 'Achats de services', 'Purchase of services'],'6010',False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(16,u'6020',16,['Investierungsk\xe4ufe', "Achats d'investissement", 'Purchase of investments'],'6020',False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(14,u'6040',14,['Wareneink\xe4ufe', 'Achats de marchandises', 'Purchase of goods'],'6040',False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(27,u'61',27,['L\xf6hne und Geh\xe4lter', 'Salaires', 'Wages'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(17,u'6300',17,['L\xf6hne und Geh\xe4lter', 'Salaires', 'Wages'],'6300',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(18,u'6900',18,['Net income', 'Net income', 'Net income'],'6900',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(28,u'7',28,['Revenues', 'Revenues', 'Revenues'],None,False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(19,u'7000',19,['Verkauf', 'Ventes', 'Sales'],'7000',False,False,None,True,False,False,False,False,False))
loader.save(create_ledger_account(20,u'7900',20,['Net loss', 'Net loss', 'Net loss'],'7900',False,False,None,False,False,False,False,False,False))
loader.save(create_ledger_account(37,u'820/333/01',37,['Vorschuss auf Verg\xfctungen o.\xe4.', 'Vorschuss auf Verg\xfctungen o.\xe4.', 'Vorschuss auf Verg\xfctungen o.\xe4.'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(38,u'821/333/01',38,['Vorschuss auf Pensionen', 'Vorschuss auf Pensionen', 'Vorschuss auf Pensionen'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(39,u'822/333/01',39,['Vorsch. Entsch. Arbeitsunf\xe4lle', 'Vorsch. Entsch. Arbeitsunf\xe4lle', 'Vorsch. Entsch. Arbeitsunf\xe4lle'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(40,u'823/333/01',40,['Vor. Kranken- u. Invalidengeld', 'Vor. Kranken- u. Invalidengeld', 'Vor. Kranken- u. Invalidengeld'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(41,u'825/333/01',41,['Vorschuss auf Familienzulage', 'Vorschuss auf Familienzulage', 'Vorschuss auf Familienzulage'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(42,u'826/333/01',42,['Vorschuss auf Arbeitslosengeld', 'Vorschuss auf Arbeitslosengeld', 'Vorschuss auf Arbeitslosengeld'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(43,u'827/333/01',43,['Vorschuss auf Behindertenzulag', 'Vorschuss auf Behindertenzulag', 'Vorschuss auf Behindertenzulag'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(30,u'832/330/01',30,['Allgemeine Beihilfen', 'Aides g\xe9n\xe9rales', 'Allgemeine Beihilfen'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(47,u'832/330/02',47,['Gesundheitsbeihilfe', 'Gesundheitsbeihilfe', 'Gesundheitsbeihilfe'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(32,u'832/330/03',32,['Heizkosten- u. Energiebeihilfe', 'Heizkosten- u. Energiebeihilfe', 'Heizkosten- u. Energiebeihilfe'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(31,u'832/330/03F',31,['Fonds Gas und Elektrizit\xe4t', 'Fonds Gas und Elektrizit\xe4t', 'Fonds Gas und Elektrizit\xe4t'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(36,u'832/330/04',36,['Mietkaution', 'Mietkaution', 'Mietkaution'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(35,u'832/333/22',35,['Mietbeihilfe', 'Mietbeihilfe', 'Mietbeihilfe'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(29,u'832/3331/01',29,['Eingliederungseinkommen', "Revenu d'insertion", 'Eingliederungseinkommen'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(34,u'832/334/27',34,['Sozialhilfe', 'Aide sociale', 'Sozialhilfe'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(33,u'832/3343/21',33,['Beihilfe f\xfcr Ausl\xe4nder', 'Beihilfe f\xfcr Ausl\xe4nder', 'Beihilfe f\xfcr Ausl\xe4nder'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(45,u'P82/000/00',45,['Einn. Dritter: Weiterleitung', 'Einn. Dritter: Weiterleitung', 'Einn. Dritter: Weiterleitung'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(46,u'P83/000/00',46,['Unber. erh. Betr\xe4ge + Erstatt.', 'Unber. erh. Betr\xe4ge + Erstatt.', 'Unber. erh. Betr\xe4ge + Erstatt.'],None,False,False,None,False,True,False,False,False,False))
loader.save(create_ledger_account(44,u'P87/000/00',44,['Abhebung von pers. Guthaben', 'Abhebung von pers. Guthaben', 'Abhebung von pers. Guthaben'],None,False,False,None,False,True,False,False,False,False))

loader.flush_deferred_objects()
