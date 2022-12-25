import os
import telegram
from doodstream import DoodstreamClient

# Masukkan token API bot yang didapat dari Bot Father ke dalam variabel TOKEN
TOKEN = "5635344869:AAF3jPheTnvDKAF2Qils437SYjEy9UsyLQw"

# Masukkan kredensial API Doodstream ke dalam variabel DOODSTREAM_API_KEY dan DOODSTREAM_API_SECRET
DOODSTREAM_API_KEY = "178004q1tpxmjk3f0p4ze3"
DOODSTREAM_API_SECRET = "178004q1tpxmjk3f0p4ze3"

# Buat client Doodstream
client = DoodstreamClient(api_key=DOODSTREAM_API_KEY, api_secret=DOODSTREAM_API_SECRET)

# Buat objek updater dari telegram
updater = telegram.ext.Updater(token=TOKEN, use_context=True)

# Buat handler untuk perintah "/upload"
def upload_handler(update, context):
  # Cek apakah pengguna telah mengirimkan file video
  if update.message.video:
    video_file = update.message.video.get_file()
    # Unggah video ke Doodstream
    response = client.videos.create(video=video_file)
    video_url = response["url"]
    # Kirim pesan ke pengguna yang berisi URL video di Doodstream
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Video Anda telah diunggah ke Doodstream: {video_url}")
  else:
    # Kirim pesan ke pengguna jika tidak ada file video yang dikirimkan
    context.bot.send_message(chat_id=update.effective_chat.id, text="Silakan kirim file video dengan menggunakan perintah /upload")

# Tambahkan handler untuk perintah "/upload"
updater.dispatcher.add_handler(telegram.ext.CommandHandler("upload", upload_handler))

# Jalankan updater
updater.start_polling()
