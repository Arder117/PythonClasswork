import requests
from bs4 import BeautifulSoup
import time


def fetch_baidu_search_results(keyword, num_pages=10):
    search_results = []
    base_url = "https://www.baidu.com/s"

    for page in range(num_pages):
        params = {
            'wd': keyword,
            'pn': page * 10  # 每页10个结果
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(base_url, params=params, headers=headers)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='result')

            for result in results:
                title = result.find('h3').text if result.find('h3') else "无标题"
                link = result.find('a')['href'] if result.find('a') else "无链接"
                snippet = result.find('div', class_='c-abstract').text if result.find('div',
                                                                                      class_='c-abstract') else "无摘要"

                search_results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })
        else:
            print(f"请求失败，状态码: {response.status_code}")

        time.sleep(1)

    return search_results


if __name__ == "__main__":
    keyword = str(input("请输入搜索关键词: "))
    results = fetch_baidu_search_results(keyword)

    for i, result in enumerate(results, start=1):
        print(f"结果 {i}:")
        print(f"标题: {result['title']}")
        print(f"链接: {result['link']}")
        print(f"摘要: {result['snippet']}\n")
