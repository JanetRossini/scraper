import os.path

import pytest
import requests
import re

from scraper import Scraper
from picwriter import PicWriter


class TestIdeas:
    def test_hookup(self):
        assert 2 + 2 == 4

    def test_grab(self):
        pic = 'https://janetrossini.github.io/assets/rgn4.png'
        response = requests.get(pic)
        assert response.status_code == 200

    @pytest.mark.skip("no point writing all the time")
    def test_write(self):
        pic = 'https://janetrossini.github.io/assets/rgn4.png'
        response = requests.get(pic)
        assert response.status_code == 200
        content = response.content
        # assert False
        desktop = '~/Desktop'
        true_desktop = os.path.expanduser(desktop)
        output_name = 'image_name.png'
        write_to = os.path.join(true_desktop, output_name)
        with open(write_to, 'wb') as handler:
            handler.write(content)

    def test_get_names(self):
        article_path = os.path.expanduser('~/Documents/GitHub/janetrossini.github.io/_posts/2024-06-28-bump.md')
        with open(article_path, 'r') as fp:
            for line in fp.readlines():
                process_line(line)
        assert True

    def test_scraper(self):
        article = '2024-06-28-bump.md'
        scraper = Scraper(article)
        assert scraper.article_name == article
        names = scraper.get_pic_names()
        # print(scraper.pic_names)
        g_name = 'https://i.gyazo.com/ee821384cd4a75bb8f3ecad4376afd76.jpg'
        a_name = '/assets/ee821384cd4a75bb8f3ecad4376afd76.jpg'
        assert g_name in names or a_name in names
        assert len(names) == 1
        # plan = scraper.make_plan()
        # assert len(plan) == len(names)
        # for w in plan:
        #     print(w)

    def test_pic_writer_write(self):
        pic_url = 'https://i.gyazo.com/b11997c6ccee94380b487332e7d25881.png'
        save_path = '~/Documents/GitHub/janetrossini.github.io/assets'
        writer = PicWriter(pic_url, save_path)
        assert writer.pic_url == pic_url
        assert writer.save_address == \
               '~/Documents/GitHub/janetrossini.github.io/assets/b11997c6ccee94380b487332e7d25881.png'
        writer.execute(False, False)

    @pytest.mark.skip("no point writing all the time")
    def test_do_whole_article(self):
        article = '2024-06-28-bump.md'
        scraper = Scraper(article)
        scraper.make_plan()
        scraper.do_read = True
        scraper.do_save = True
        scraper.execute_plan()

    # tested using the test just above
    # def test_live_fire(self):
    #     assert 'never tested read and save true' == ''


def process_line(line):
    write_path = os.path.expanduser('~/Documents/GitHub/janetrossini.github.io/assets')
    if '[image]' not in line:
        return
    # ![image](https://i.gyazo.com/b11997c6ccee94380b487332e7d25881.png)
    # print(f'\n{line=}')
    url_regex = r'\((.*)\)'
    url_result = re.search(url_regex, line)
    url = url_result.group(1)
    # print(f'{url=}')
    file_regex = r'i\.gyazo\.com/(.*)'
    result = re.search(file_regex, url)
    if result:
        save_file = result.group(1)
        # print(f'{save_file=}')
        to_write = os.path.join(write_path, save_file)
        # print(f'{to_write=}')
    else:
        print('no file?')

