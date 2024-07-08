
class Plan:
    def __init__(self):
        """Just a simple collection of PicWriter instances.
        Might become more clever in a later version.
        Build this way because we want to have a place for `execute`.
        """
        self.pic_writers = []

    def append(self, pic_writer):
        """Add a PicWriter to our list"""
        self.pic_writers.append(pic_writer)

    def execute(self, do_read, do_save):
        """Execute all the PicWriters in the Plan.
        This is what causes the file to be scanned
        and the pictures retrieved.
        """
        for writer in self.pic_writers:
            writer.execute(do_read, do_save)
