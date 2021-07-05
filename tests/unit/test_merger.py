from __future__ import absolute_import, division, print_function

from operator import itemgetter

from mock import patch

from inspire_json_merger.api import merge

from utils import assert_ordered_conflicts, validate_subschema

from inspire_json_merger.config import (
    PublisherOnPublisherOperations,
    PublisherOnArxivOperations,
    ArxivOnArxivOperations,
    ArxivOnPublisherOperations,
)


@patch(
    "inspire_json_merger.api.get_configuration",
    return_value=PublisherOnPublisherOperations,
)
def test_merging_same_documents_publisher_on_publisher(fake_get_config):
    root = {
        "documents": [
            {
                "key": "pdf1.pdf",
                "description": "paper",
                "source": "arXiv",
                "fulltext": True,
                "url": "http://example.com/files/1234-1234-1234-1234/pdf1.pdf",
            },
            {
                "key": "pdf.tex",
                "description": "latex version",
                "source": "arXiv",
                "url": "http://example.com/files/1234-1234-1234-1234/pdf.tex",
            },
        ]
    }
    head = root
    update = root
    expected_merged = update
    expected_conflict = []
    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert_ordered_conflicts(conflict, expected_conflict)
    validate_subschema(merged)


@patch(
    "inspire_json_merger.api.get_configuration", return_value=PublisherOnArxivOperations
)
def test_merging_same_documents_publisher_on_arxiv(fake_get_config):
    root = {
        "documents": [
            {
                "key": "pdf1.pdf",
                "description": "paper",
                "source": "arXiv",
                "fulltext": True,
                "url": "http://example.com/files/1234-1234-1234-1234/pdf1.pdf",
            },
            {
                "key": "pdf.tex",
                "description": "latex version",
                "source": "arXiv",
                "url": "http://example.com/files/1234-1234-1234-1234/pdf.tex",
            },
        ]
    }
    head = root
    update = root
    expected_merged = update
    expected_conflict = []
    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert_ordered_conflicts(conflict, expected_conflict)
    validate_subschema(merged)


@patch("inspire_json_merger.api.get_configuration", return_value=ArxivOnArxivOperations)
def test_merging_same_documents_arxiv_on_arxiv(fake_get_config):
    root = {
        "documents": [
            {
                "key": "pdf1.pdf",
                "description": "paper",
                "source": "arXiv",
                "fulltext": True,
                "url": "http://example.com/files/1234-1234-1234-1234/pdf1.pdf",
            },
            {
                "key": "pdf.tex",
                "description": "latex version",
                "source": "arXiv",
                "url": "http://example.com/files/1234-1234-1234-1234/pdf.tex",
            },
        ]
    }
    head = root
    update = root
    expected_merged = head
    expected_conflict = []
    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert_ordered_conflicts(conflict, expected_conflict)
    validate_subschema(merged)


@patch(
    "inspire_json_merger.api.get_configuration", return_value=ArxivOnPublisherOperations
)
def test_merging_same_documents_arxiv_on_publisher(fake_get_config):
    root = {
        "documents": [
            {
                "key": "pdf1.pdf",
                "description": "paper",
                "source": "arXiv",
                "fulltext": True,
                "url": "http://example.com/files/1234-1234-1234-1234/pdf1.pdf",
            },
            {
                "key": "pdf.tex",
                "description": "latex version",
                "source": "arXiv",
                "url": "http://example.com/files/1234-1234-1234-1234/pdf.tex",
            },
        ]
    }
    head = root
    update = root
    expected_merged = update
    expected_conflict = []
    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert_ordered_conflicts(conflict, expected_conflict)
    validate_subschema(merged)


def test_real_record_merge_regression_1_authors_mismatch_on_update():
    root = {
        "$schema": "https://inspirehep.net/schemas/records/hep.json",
        "_collections": ["Literature"],
        "authors": [
            {"full_name": "Elliott"},
            {"full_name": "Chris"},
            {"full_name": "Gwilliam"},
            {"full_name": "Owen"},
        ],
        "titles": [
            {
                "source": "arXiv",
                "title": "Spontaneous symmetry breaking: a view from derived "
                "geometry",
            }
        ],
    }

    head = {
        "$schema": "https://inspirehep.net/schemas/records/hep.json",
        "_collections": ["Literature"],
        "authors": [
            {
                "affiliations": [
                    {
                        "record": {
                            "$ref": "https://inspirehep.net/api/institutions/945696"
                        },
                        "value": "UMass Amherst",
                    },
                    {
                        "record": {
                            "$ref": "https://inspirehep.net/api/institutions/1272963"
                        },
                        "value": "UMASS, Amherst, Dept. Math. Stat.",
                    },
                ],
                "emails": ["celliott@math.umass.edu"],
                "full_name": "Elliott",
                "ids": [{"schema": "INSPIRE BAI", "value": "Elliott.1"}],
                "signature_block": "ELAT",
                "uuid": "65aa01c7-99ec-4c35-ac6b-bbc667a4343e",
            },
            {
                "full_name": "Chris",
                "ids": [{"schema": "INSPIRE BAI", "value": "Chris.1"}],
                "signature_block": "CHR",
                "uuid": "36b3a255-f8f2-46a6-bfae-9e9d00335434",
            },
            {
                "affiliations": [
                    {
                        "record": {
                            "$ref": "https://inspirehep.net/api/institutions/945696"
                        },
                        "value": "UMass Amherst",
                    },
                    {
                        "record": {
                            "$ref": "https://inspirehep.net/api/institutions/1272963"
                        },
                        "value": "UMASS, Amherst, Dept. Math. Stat.",
                    },
                ],
                "emails": ["gwilliam@math.umass.edu"],
                "full_name": "Gwilliam",
                "ids": [{"schema": "INSPIRE BAI", "value": "Gwilliam.1"}],
                "signature_block": "GWALAN",
                "uuid": "66f5722f-e649-4438-a7f5-d01247371f22",
            },
            {
                "full_name": "Owen",
                "ids": [{"schema": "INSPIRE BAI", "value": "Owen.1"}],
                "signature_block": "OWAN",
                "uuid": "27de5ee5-d21a-47b2-b22c-fd44231128f9",
            },
        ],
        "titles": [
            {
                "source": "arXiv",
                "title": "Spontaneous symmetry breaking: a view from derived "
                "geometry",
            }
        ],
    }

    update = {
        "$schema": "https://inspirehep.net/schemas/records/hep.json",
        "_collections": ["Literature"],
        "authors": [{"full_name": "Elliott, Chris"}, {"full_name": "Gwilliam, Owen"}],
        "titles": [
            {
                "source": "arXiv",
                "title": "Spontaneous symmetry breaking: a view from derived "
                "geometry",
            }
        ],
    }
    expected_merged = dict(head)

    expected_conflicts = [
        {
            "path": "/authors/3",
            "op": "replace",
            "value": {"full_name": "Gwilliam, Owen"},
            "$type": "SET_FIELD",
        },
        {
            "path": "/authors/2",
            "op": "replace",
            "value": {"full_name": "Gwilliam, Owen"},
            "$type": "SET_FIELD",
        },
        {
            "path": "/authors/0",
            "op": "replace",
            "value": {"full_name": "Elliott, Chris"},
            "$type": "SET_FIELD",
        },
        {
            "path": "/authors/1",
            "op": "replace",
            "value": {"full_name": "Elliott, Chris"},
            "$type": "SET_FIELD",
        },
    ]

    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert sorted(conflict, key=itemgetter("path")) == sorted(
        expected_conflicts, key=itemgetter("path")
    )


@patch(
    "inspire_json_merger.api.get_configuration", return_value=PublisherOnArxivOperations
)
def test_merging_acquisition_source_publisher_on_arxiv(fake_get_config):
    root = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "arXiv",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    head = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "arXiv",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    update = {
        "acquisition_source": {
            "datetime": "2021-05-12T02:35:43.387350",
            "method": "beard",
            "source": "other source",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c1"
        }
    }
    expected_merged = update
    expected_conflict = []
    merged, conflict = merge(root, head, update)
    assert merged == expected_merged
    assert_ordered_conflicts(conflict, expected_conflict)
    validate_subschema(merged)


@patch(
    "inspire_json_merger.api.get_configuration", return_value=PublisherOnArxivOperations
)
def test_merging_cleans_acquisition_source_for_publisher_on_arxiv(fake_get_config):
    root = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "desy",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    head = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "arXiv",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    update = {
        "acquisition_source": {
            "datetime": "2021-05-12T02:35:43.387350",
            "method": "hepcrawl",
            "source": "desy",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c1"
        }
    }

    merged, conflict = merge(root, head, update)
    assert merged['acquisition_source']['source'] == 'desy'


@patch(
    "inspire_json_merger.api.get_configuration", return_value=PublisherOnPublisherOperations
)
def test_merging_cleans_acquisition_source_for_publisher_on_publisher(fake_get_config):
    root = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "desy",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    head = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "elsevier",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    update = {
        "acquisition_source": {
            "datetime": "2021-05-12T02:35:43.387350",
            "method": "hepcrawl",
            "source": "desy",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c1"
        }
    }

    merged, conflict = merge(root, head, update)
    assert merged['acquisition_source']['source'] == 'desy'


@patch(
    "inspire_json_merger.api.get_configuration", return_value=ArxivOnPublisherOperations
)
def test_merging_cleans_acquisition_source_for_arxiv_on_publisher(fake_get_config):
    root = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "arXiv",
            "source": "arXiv",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    head = {
        "acquisition_source": {
            "datetime": "2021-05-11T02:35:43.387350",
            "method": "hepcrawl",
            "source": "desy",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c0"
        }
    }
    update = {
        "acquisition_source": {
            "datetime": "2021-05-12T02:35:43.387350",
            "method": "hepcrawl",
            "source": "arXiv",
            "submission_number": "c8a0e3e0b20011eb8d930a580a6402c1"
        }
    }

    merged, conflict = merge(root, head, update)
    assert merged['acquisition_source']['source'] == 'arXiv'
