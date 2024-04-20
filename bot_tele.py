from telegram import Bot
from telegram.ext import Updater, CommandHandler
import crawl_topdev

# Token của bot Telegram 

TELEGRAM_TOKEN = 'PATH_TO_YOUR_TOKEN'

# Đường dẫn của trang web cần crawl dữ liệu
urlHome = 'https://topdev.vn/it-jobs'
urlDanang = 'https://topdev.vn/it-jobs/da-nang-kl48'
urlHochiminh = 'https://topdev.vn/it-jobs/ho-chi-minh-kl79'
urlHanoi = 'https://topdev.vn/it-jobs/ha-noi-kl01'

# Function xử lý lệnh /start của bot
def start(update, context):
    text = "Bot thu thập thông tin việc làm từ TopDev.\n Các lệnh:\n - /start: Bắt đầu bot\n - /get: Lấy danh sách việc làm mới nhất từ TopDev\n - /help: Hiển thị trợ giúp\n - /getdanang: Lấy danh sách việc làm ở Đà Nẵng\n - /gethochiminh: Lấy danh sách việc làm ở Hồ Chí Minh\n - /gethanoi: Lấy danh sách việc làm ở Hà Nội\n" 
    update.message.reply_text(text)

# Function xử lý lệnh /get của bot
def get_jobs(update, context):
    
    city_urls = {
        'getdanang': urlDanang,
        'gethochiminh': urlHochiminh,
        'gethanoi': urlHanoi,
        'get': urlHome
    }

    # Lấy lệnh từ tin nhắn
    command = update.message.text.split()[0][1:]

    # Lấy URL tương ứng với lệnh
    url = city_urls.get(command, urlHome)

    # Lấy dữ liệu từ TopDev
    jobs_data = crawl_topdev.get_data_topdev(url)
    
    if jobs_data is None:
        update.message.reply_text("Có lỗi xảy ra khi lấy dữ liệu từ TopDev")
    else:
        
        update.message.reply_text(jobs_data)
        

# Function chính để thiết lập bot
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Thêm các lệnh xử lý
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('get', get_jobs))
    dp.add_handler(CommandHandler('help', start))
    dp.add_handler(CommandHandler('getdanang', get_jobs))
    dp.add_handler(CommandHandler('gethochiminh', get_jobs))
    dp.add_handler(CommandHandler('gethanoi', get_jobs))
    
    # Bắt đầu bot và chạy nó cho đến khi bạn nhấn Ctrl-C hoặc quá trình bị gián đoạn
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
