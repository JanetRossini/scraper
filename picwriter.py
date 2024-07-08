import os
import re
import requests


class PicWriter:
    """Given one picture url,
    read that url's contents,
    and write the contents to the provided path,
    with the same name as found in the url.
    e.g. 'https://i.gyazo.com/deadbeef.png'
    """
    def __init__(self, pic_url, path):
        """Initialize with file name and path to save file to.
        regex selects everything after `.com/` as image file name.
        """
        self.pic_url = pic_url
        file_regex = r'i\.gyazo\.com/(.*)'
        result = re.search(file_regex, pic_url)
        if not result:
            raise ValueError('cannot find image file name')
        else:
            save_name = result.group(1)
            self.save_address = os.path.join(path, save_name)

    def __repr__(self):
        """debug print for convenience"""
        return f'PicWriter({self.pic_url=} {self.save_address=}'

    def execute(self, do_read, do_save):
        """depending on flags:
        do_read: read the saved url (requests.get) and
        do_save: save the contents
        """
        if do_read:
            response = requests.get(self.pic_url)
            if response.status_code != 200:
                raise FileNotFoundError
        else:
            response = None
        self.save_content(response, do_save)

    def save_content(self, response, do_save):
        """Save the file if flag is True,
        and if we receive a non-None response.
        We call this method even if we got no good response,
        because it prints the trace information.
        """
        expanded = os.path.expanduser(self.save_address)
        print(f'save file: {expanded=}')
        if not do_save:
            print(f"not written {do_save=}")
        elif response is None:
            print(f'not written, response is None')
        else:
            content = response.content  # this is the actual .png / .jpg data
            with open(expanded, "wb") as handler:
                handler.write(content)
                print("written")
