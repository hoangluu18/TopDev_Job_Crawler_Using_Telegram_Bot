#Author: github.com/hoangluu18

import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup


def get_data_topdev(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm tất cả các thẻ div chứa thông tin công việc
        job_elements = soup.find_all('div', class_='flex-1')

        #Khởi tạo chuỗi lưu trữ dữ liệu
        text = "" 

        # Duyệt qua từng phần tử công việc
        for job_element in job_elements:
            # Trích xuất thông tin từ từng phần tử
            title_element = job_element.find('h3', class_='line-clamp-1')
            title = title_element.a.text.strip() if title_element and title_element.a else ""  # Xử lý trường hợp không tìm thấy

            company_element = job_element.find('div', class_="mt-1 line-clamp-1")
            company = company_element.a.text.strip() if company_element else ""

            level_element = job_element.find('p', class_="text-gray-500")
            level = level_element.text.strip() if level_element else ""

            location_element = job_element.find('div', class_="text-gray-500")
            location = location_element.p.text.strip() if location_element else ""

            link_element = job_element.find('a', class_='text-lg font-bold transition-all text-primary')
            link = link_element['href'] if link_element else ""
            
            time_element = job_element.find('p',class_= 'whitespace-nowrap text-sm text-gray-400')
            time = time_element.text.strip() if time_element else ""
            
            #Xử lí link
            if(link.startswith('/en/')):
                link = "https://topdev.vn/" + link[4:]
            
            #Xử lí thời gian
            if(time.startswith('Posted')):
                time = time[7:]

            #Xử lí dữ liệu
            if(title == "" or company == "" or location == ""):
                
                continue   
            text += "----------------------------------\n"
            text += "Tiêu đề: " + title + "\n" + "Tên công ty: " + company + "\n" + "Địa điểm: " + location + "\n" + "Trình độ: " + level + "\n" + "Link: " + link + "\n" + "Thời gian đăng: " + time + "\n\n"
            text += "----------------------------------\n"
        
        return text
    else:
        return None