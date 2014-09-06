
class FlexibleForm:
    help_texts = {}

    def replace_help_texts(self, help_texts=None):
        if not help_texts:
            help_texts = self.help_texts

        for field, help_text in help_texts.iteritems():
            try:
                self.fields[field].help_text = help_text
            except KeyError:
                pass
