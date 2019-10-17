from flask import Flask, request, jsonify
from datetime import date
import pymysql.cursors

app = Flask(__name__)
connection = pymysql.connect(host='db4free.net',
                             user='andikaputra',
                             password='12345qwe',
                             db='db_pariwisata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=['POST'])
def root():
    data = request.get_json()
    intent = data['queryResult']['intent']['displayName']
    print(data)

    if intent == "Nama":
        return daftar_nama(data)
    elif intent == "umur":
        return daftar_umur(data)
    elif intent == "jenis kelamin":
        return daftar_jenis_kelamin(data)
    elif intent == "alamat":
        return daftar_alamat(data)
    elif intent == "no telepon":
        return daftar_no_telepon(data)
    elif intent == "destinasi":
        return daftar_destinasi(data)

    return jsonify({"fulfillmentText": "Mohon ulangi lagi"})


def daftar_nama(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""

    try:
        respon = "Masukkan umur Anda"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


def daftar_umur(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""

    try:
        respon = "Masukkan jenis kelamin Anda (ketik 1 atau 2). \n1. Laki-laki\n2. Perempuan"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


def daftar_jenis_kelamin(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""

    try:
        respon = "Masukkan alamat tempat tinggal Anda"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


def daftar_alamat(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""

    try:
        respon = "Masukkan nomor telepon Anda"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


def daftar_no_telepon(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""

    try:
        respon = "Masukkan destinasi pariwisata Anda. " \
                 "Pilih destinasi pariwisata Anda dengan mengetikkan nama destinasi pariwisata\n" \
                 "Berikut merupakan daftar destinasi pariwisata yang dapat Anda pilih:\n" \
                 "1. Teluk Gilimanuk\n" \
                 "2. Pantai Baluk Rening\n" \
                 "3. Wisata Alam Green Cliff\n" \
                 "4. Glagah Linggah\n" \
                 "5. Desa Pinggan\n" \
                 "6. Danau Batur\n" \
                 "7. White Sandy Beach\n" \
                 "8. Bukit Kursi\n" \
                 "9. Air Terjun Gitgit\n" \
                 "10. Taman Kupu-Kupu\n" \
                 "11. Kincir Waterfall\n" \
                 "12. Pantai Pasut"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


def daftar_destinasi(data):
    id_user = data['originalDetectIntentRequest']['payload']['data']['source']['userId']
    id_chat = data['originalDetectIntentRequest']['payload']['data']['message']['id']
    pesan = data['queryResult']['queryText']
    id_inbox = ""
    parameters = data['queryResult']['outputContexts'][0]['parameters']
    nama = parameters['nama']
    umur = parameters['umur']
    jenis_kelamin = parameters['jeniskelamin']
    alamat = parameters['alamat']
    no_telepon = parameters['notelepon']
    destinasi = parameters['destinasi']

    try:
        respon = "Data Tersimpan.\nTunggu Tour Guide Menghubungi Anda.\n\n" \
                 "Ketik \"Wisata\" untuk Melihat Tempat Wisata Lainnya"
        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_inbox (id_user, id_chat, pesan, tanggal) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_user, id_chat, pesan, date.today().strftime("%Y-%m-%d")))
            id_inbox = cursor.lastrowid
            sql = "INSERT INTO tb_kunjungan (nama, umur, jenis_kelamin, alamat, no_telepon, destinasi) VALUES " \
                  "(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nama, umur, jenis_kelamin, alamat, no_telepon, destinasi))

        connection.commit()

        with connection.cursor() as cursor:
            sql = "INSERT INTO tb_outbox (id_inbox, respon) VALUES (%s, %s)"
            cursor.execute(sql, (id_inbox, respon))
            sql = "UPDATE tb_inbox SET tb_inbox.`status` = '1' WHERE tb_inbox.`id` = %s"
            cursor.execute(sql, (id_inbox))

        connection.commit()

    except Exception as error:
        print(error)
        respon = "Terjadi kesalahan, silahkan coba lagi"

    response = {
        "fulfillmentText": respon
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run()
