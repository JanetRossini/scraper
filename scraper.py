import os.path
import re

from picwriter import PicWriter
from plan import Plan


class Scraper:
    def __init__(self, article_name):
        """Set up for provided article name.
        Note that flags are initialized to do no web access and no file writing.
        """
        self.article_name = article_name
        base_path = '~/Documents/GitHub/janetrossini.github.io/_posts'
        self.read_path = os.path.expanduser(base_path)
        self.article_path = os.path.join(self.read_path, self.article_name)
        self.save_path = '~/Documents/GitHub/janetrossini.github.io/assets'
        self.do_read = False
        self.do_save = False

    def get_pic_names(self):
        """Read every line of the article looking for picture names to fetch.
        """
        pic_names = []
        with open(self.article_path, 'r') as fp:
            for line in fp.readlines():
                self.append_pic_name(line, pic_names)
        return pic_names

    def append_pic_name(self, line, pic_names):
        """For lines containing '[image]',
        pull out the image name and add it to the collection.
        The line will look like ![image](https://etc.png)
        The regex fetches everything inside the parens,
        which should be the url of the picture.
        """
        if '[image]' not in line:
            return
        url_regex = r'\((.*)\)'
        url_result = re.search(url_regex, line)
        url = url_result.group(1)
        if url:
            pic_names.append(url)

    def make_plan(self):
        """Convert list of picture names to an instance of Plan.
        A Plan is little more than a collection of PicWriter instances.
        The PicWriter does all the work, as we'll see."""
        plan = Plan()
        for name in self.get_pic_names():
            writer = PicWriter(name, self.save_path)
            plan.append(writer)
        return plan

    def execute_plan(self):
        """Execute the plan.
        Flags must be set True if you want anything done.
        Probably this method should accept the desired flags,
        at least as things stand now.
        """
        plan = self.make_plan()
        plan.execute(self.do_read, self.do_save)



