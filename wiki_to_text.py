from dewiki_functions import *

#wiki_xml_file = 'F:/simplewiki-20210401/simplewiki-20210401.xml'  # update this
wiki_xml_file = 'simplewiki-latest-pages-articles-multistream.xml'  # update this
json_save_dir = './wikiplaintext/'

if __name__ == '__main__':
    process_file_text(wiki_xml_file, json_save_dir)