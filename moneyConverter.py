import requests
def idr_uas():
    namaBank = (input('Silahkan ketik bank pilihan Anda : ')).lower()
    url = 'https://kurs.web.id/api/v1/' + namaBank
    data = requests.get(url)
    beli = int(data.json()['beli'])
    jual = int(data.json()['jual'])
    uang = float(input('Masukkan rupiah yang akan ditukarkan : '))
    hasil = str(round(uang / jual,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' USD'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def uas_idr():
    namaBank = (input('Silahkan ketik bank pilihan Anda : ')).lower()
    url = 'https://kurs.web.id/api/v1/' + namaBank
    data = requests.get(url)
    beli = int(data.json()['beli'])
    jual = int(data.json()['jual'])
    uang = float(input('Masukkan USD yang akan ditukarkan : '))
    hasil = str(round(uang * beli,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' Rupiah'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def idr_bitcoin():
    url = 'https://blockchain.info/ticker'
    data = requests.get(url)
    beli = int(data.json()['INR']['sell'])
    jual = int(data.json()['INR']['buy'])
    uang = int(input('Masukkan Rupiah yang akan ditukarkan : '))
    hasil = str(round(uang / beli,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' Coin'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def bitcoin_idr():
    url = 'https://blockchain.info/ticker'
    data = requests.get(url)
    beli = int(data.json()['INR']['sell'])
    jual = int(data.json()['INR']['buy'])
    uang = int(input('Masukkan Bitcoin yang akan ditukarkan : '))
    hasil = str(round(uang * jual,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' Rupiah'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def USD_bitcoin():
    url = 'https://blockchain.info/ticker'
    data = requests.get(url)
    beli = int(data.json()['USD']['sell'])
    jual = int(data.json()['USD']['buy'])
    uang = int(input('Masukkan USD yang akan ditukarkan : '))
    hasil = str(round(uang / beli,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' Coin'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def bitcoin_USD():
    url = 'https://blockchain.info/ticker'
    data = requests.get(url)
    beli = int(data.json()['USD']['sell'])
    jual = int(data.json()['USD']['buy'])
    uang = int(input('Masukkan Bitcoin yang akan ditukarkan : '))
    hasil = str(round(uang * jual,2))
    return print('Hasil penukaran Anda sebesar ' + hasil + ' USD'+'\nDengan kurs beli = ' + str(beli) + ' dan kurs jual = ' + str(jual))

def menu():
    Menu = int(input('Selamat Datang !\nSilahkan pilih konversi yang akan Anda lakukan :\n(1) IDR Indonesia => USD United States\n(2) USD United States => IDR Indonesia\n(3) Bitcoin Converter\n(4) Keluar\nPilihan Anda ( 1 / 2 / 3 ) : '))
    return Menu

def main_menu():
    while(True):
        menu_utama = menu()
        if menu_utama == 4:
            print('Terima Kasih !')
            break
        elif menu_utama == 1:
            x = idr_uas()
            break
        elif menu_utama == 2:
            y = uas_idr()
            break
        elif menu_utama == 3:
            bitcoin = int(input('Masukkan mata uang diinginkan\n(1) Rupiah\n(2) USD\nPilihan ( 1 / 2 ) : '))
            if bitcoin == 1:
                rpconverter = int(input('(1) Rupiah ke Bitcoin\n(2) Bitcoin ke Rupiah\nMasukkan pilihan ( 1 / 2 ) : '))
                if rpconverter == 1:
                    idr_bitcoin()
                    break
                if rpconverter == 2:
                    bitcoin_idr()
                    break
                else:
                    print('Maaf, input yang Anda masukkan salah')
            if bitcoin == 2:
                usdconverter = int(input('(1) USD ke Bitcoin\n(2) Bitcoin ke USD\nMasukkan pilihan ( 1 / 2 ) : '))
                if usdconverter == 1:
                    USD_bitcoin() 
                    break
                elif usdconverter == 2:
                    bitcoin_USD()
                    break
                else:
                     print('Maaf, input yang Anda masukkan salah')

        else:
            'Input yang Anda masukkan salah, coba lagi !'
                    
main_menu()