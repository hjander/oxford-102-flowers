import json


class AugmentedManifest(object):

    def __init__(self, dest_file_path):
        try:
            self.augmented_manifest_file = open(dest_file_path, 'w')
        except OSError as e:
            print(e)

    def add_entry(self, entry):
        self.augmented_manifest_file.write("{}\n".format(json.dumps(entry)))

    def finished_writing(self):
        self.augmented_manifest_file.close()