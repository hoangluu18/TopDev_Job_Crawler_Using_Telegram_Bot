import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup


def get_data_topdev(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm tất cả các thẻ div chứa thông tin công việc
        job_elements = soup.find_all('div', class_='flex-1')

        # Tạo bảng để lưu dữ liệu
        
        #jobs_data = PrettyTable()
        #jobs_data.field_names = ["Tiêu đề", "Tên công ty", "Địa điểm", "Trình độ"]
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
            
            #Xử lí dữ liệu
            if(title == "" or company == "" or location == "" or level == ""):
                
                continue   
            #jobs_data.add_row([title, company, location, level])  
            #text = jobs_data.get_string()
            #print(text)
            text += "----------------------------------\n"
            text += "Tiêu đề: " + title + "\n" + "Tên công ty: " + company + "\n" + "Địa điểm: " + location + "\n" + "Trình độ: " + level + "\n\n"
            text += "----------------------------------\n"
        return text
    else:
        return None