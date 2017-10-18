import os


class FieldNames(object):
    PAPER_ID = "id"
    TITLE = "title"
    ABSTRACT = "abstract"
    AUTHORS = "authors"

    VENUE = "venue"
    YEAR = "year"

    IN_CITATIONS = "in_citations"
    OUT_CITATIONS = "out_citations"
    KEY_PHRASES = "key_phrases"

    URLS = "pdf_urls"
    S2_URL = "s2_url"

    OUT_CITATIONS_COUNT = 'out_citation_count'
    IN_CITATIONS_COUNT = 'in_citation_count'

    DATE = 'date'


class FilePaths(object):
    BASE_DIR = '/net/nfs.corp/s2-research/citeomatic/naacl2017/'

    DBLP_GOLD_DIR = os.path.join(BASE_DIR, 'comparison/dblp/gold')
    DBLP_CORPUS_JSON = os.path.join(BASE_DIR, 'comparison/dblp/corpus.json')
    DBLP_DB_FILE = os.path.join(BASE_DIR, 'db/dblp.sqlite.db')

    PUBMED_GOLD_DIR = os.path.join(BASE_DIR, 'comparison/pubmed/gold')
    PUBMED_CORPUS_JSON = os.path.join(BASE_DIR, 'comparison/pubmed/corpus.json')
    PUBMED_DB_FILE = os.path.join(BASE_DIR, 'db/pubmed.sqlite.db')

    OC_FILE = os.path.join(BASE_DIR, 'open_corpus/papers-2017-02-21.json.gz')
    OC_CORPUS_JSON = os.path.join(BASE_DIR, 'open_corpus/corpus.json')
    OC_DB_FILE = os.path.join(BASE_DIR, 'db/oc.sqlite.db')

    def get_json_path(self, corpus_name):
        if corpus_name.lower() == 'dblp':
            return self.DBLP_CORPUS_JSON
        elif corpus_name.lower() == 'pubmed':
            return self.PUBMED_CORPUS_JSON
        elif (corpus_name.lower() == 'oc'
              or corpus_name.lower() == 'open_corpus'
              or corpus_name.lower() == 'opencorpus'):
            return self.OC_CORPUS_JSON
        else:
            return None

    def get_db_path(self, corpus_name):
        if corpus_name.lower() == 'dblp':
            return self.DBLP_DB_FILE
        elif corpus_name.lower() == 'pubmed':
            return self.PUBMED_DB_FILE
        elif (corpus_name.lower() == 'oc'
              or corpus_name.lower() == 'open_corpus'
              or corpus_name.lower() == 'opencorpus'):
            return self.OC_DB_FILE
        else:
            return None


class Document(object):
    _fields = [
        FieldNames.TITLE,
        FieldNames.ABSTRACT,
        FieldNames.AUTHORS,
        FieldNames.OUT_CITATIONS,
        FieldNames.YEAR,
        FieldNames.PAPER_ID,
        FieldNames.VENUE,
        FieldNames.IN_CITATIONS_COUNT,
        FieldNames.OUT_CITATIONS_COUNT,
        FieldNames.KEY_PHRASES,
        FieldNames.DATE
    ]

    def __init__(
            self,
            title,
            abstract,
            authors,
            out_citations,
            year,
            id: str,
            venue,
            in_citation_count,
            out_citation_count,
            key_phrases,
            date=None
    ):
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.out_citations = out_citations
        self.year = year
        self.id = id
        self.venue = venue
        self.in_citation_count = in_citation_count
        self.out_citation_count = out_citation_count
        self.key_phrases = key_phrases
        self.date = date

    def __iter__(self):
        for k in self._fields:
            yield getattr(self, k)

    def _asdict(self):
        return dict(**self.__dict__)