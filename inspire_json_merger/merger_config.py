# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2017 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from __future__ import absolute_import, division, print_function

from json_merger.config import DictMergerOps, UnifierOps

from .comparators import COMPARATORS
"""
This module provides different sets of rules that `inspire_json_merge`
"""


class MergerConfigurationOperations(object):
    default_dict_merge_op = DictMergerOps.FALLBACK_KEEP_UPDATE
    default_list_merge_op = UnifierOps.KEEP_ONLY_UPDATE_ENTITIES
    filter_out = None
    list_dict_ops = None
    list_merge_ops = None
    comparators = None


class ArxivOnArxivOperations(MergerConfigurationOperations):
    # We an always default to KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST so
    # this is less verbose.
    comparators = COMPARATORS
    filter_out = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'deleted',
        'deleted_records',
        'documents',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'figures',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'record_affiliations',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'related_records',
        'report_numbers',
        'self',
        'special_collections',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
    ]

    list_merge_ops = {
        '_collections': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        '_desy_bookkeeping': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        '_files': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        '_private_notes': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'abstracts': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'arxiv_eprints': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.alternative_names': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.credit_roles':
            UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.emails': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.full_name': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.ids': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.inspire_roles': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.raw_affiliations': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'book_series': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'collaborations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'copyright': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'corporate_author': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'deleted_records': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'documents': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'document_type': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'dois': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'editions':  UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'external_system_identifiers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'figures': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'funding_info': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'inspire_categories': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'isbns': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'license': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'public_notes': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'publication_info': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'record_affiliations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records':     UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'texkeys': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'titles': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'urls': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST
    }

    list_dict_ops = {
        '$schema': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_export_to': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_private_notes': DictMergerOps.FALLBACK_KEEP_HEAD,
        'accelerator_experiments': DictMergerOps.FALLBACK_KEEP_HEAD,
        'acquisition_source': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.affiliations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.curated_relation': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.full_name': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.ids': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.record': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.signature_block': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.uuid': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'book_series': DictMergerOps.FALLBACK_KEEP_HEAD,
        'control_number': DictMergerOps.FALLBACK_KEEP_HEAD,
        'curated': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted_records': DictMergerOps.FALLBACK_KEEP_HEAD,
        'funding_info': DictMergerOps.FALLBACK_KEEP_HEAD,
        'legacy_creation_date': DictMergerOps.FALLBACK_KEEP_HEAD,
        'new_record': DictMergerOps.FALLBACK_KEEP_HEAD,
        'persistent_identifiers': DictMergerOps.FALLBACK_KEEP_HEAD,
        'preprint_date': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.label': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.title': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'self': DictMergerOps.FALLBACK_KEEP_HEAD,
        'succeeding_entry': DictMergerOps.FALLBACK_KEEP_HEAD,
        'texkeys': DictMergerOps.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': DictMergerOps.FALLBACK_KEEP_HEAD,
        'title_translations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'urls': DictMergerOps.FALLBACK_KEEP_HEAD,
    }


class PublisherOnArxivOperations(MergerConfigurationOperations):
    comparators = COMPARATORS
    filter_out = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'deleted',
        'deleted_records',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'references.report_numbers',
        'references.self',
        'references.special_collections',
        'references.succeeding_entry',
        'references.texkeys',
        'references.thesis_info',
        'references.thesis_info.institutions',
        'references.title_translations',
        'references.titles',
        'references.urls',
        'withdrawn',
        'related_records',
        'record_affiliations',
    ]

    list_merge_ops = {
        '_desy_bookkeeping': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        '_files': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        '_private_notes': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'abstracts': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'arxiv_eprints': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.alternative_names': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.credit_roles': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.emails': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'authors.ids': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'authors.raw_affiliations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'book_series': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'collaborations': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'copyright': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'corporate_author': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'deleted_records': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'documents': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'document_type': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'dois': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'editions': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'external_system_identifiers': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'figures': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'funding_info': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'imprints': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'inspire_categories': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'isbns': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'license': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'public_notes': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'publication_info': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'record_affiliations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records':     UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'references.reference.authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'texkeys': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'titles': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'urls': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST
    }

    list_dict_ops = {
        '$schema': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_export_to': DictMergerOps.FALLBACK_KEEP_HEAD,
        'abstracts': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'accelerator_experiments': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'acquisition_source': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'arxiv_eprints': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.affiliations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.alternative_names': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.credit_roles': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.curated_relation': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.full_name': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.ids': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.record': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.signature_block': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.uuid': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'book_series': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'citeable': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'collaborations': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'control_number': DictMergerOps.FALLBACK_KEEP_HEAD,
        'copyright': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'core': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'corporate_author': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'curated': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted_records': DictMergerOps.FALLBACK_KEEP_HEAD,
        'editions': DictMergerOps.FALLBACK_KEEP_HEAD,
        'funding_info': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'inspire_categories': DictMergerOps.FALLBACK_KEEP_HEAD,
        'isbns': DictMergerOps.FALLBACK_KEEP_HEAD,
        'preprint_date': DictMergerOps.FALLBACK_KEEP_HEAD,
        'publication_info': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'refereed': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.label': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.publication_info': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references.reference.title': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'report_numbers': DictMergerOps.FALLBACK_KEEP_HEAD,
        'self': DictMergerOps.FALLBACK_KEEP_HEAD,
        'succeeding_entry': DictMergerOps.FALLBACK_KEEP_HEAD,
        'texkeys': DictMergerOps.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'title_translations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'urls': DictMergerOps.FALLBACK_KEEP_HEAD
    }


class PublisherOnPublisherOperations(MergerConfigurationOperations):
    # We an always default to KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST so
    # this is less verbose.
    comparators = COMPARATORS
    filter_out = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'deleted',
        'deleted_records',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'report_numbers',
        'self',
        'special_collections',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
        'related_records',
        'record_affiliations',
    ]

    list_merge_ops = {
        '_collections': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        '_desy_bookkeeping': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        '_files': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        '_private_notes': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'abstracts': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'arxiv_eprints': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.alternative_names': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.credit_roles': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.emails': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.full_name': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.ids': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.inspire_roles': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'authors.raw_affiliations': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'book_series': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'collaborations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'copyright': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'corporate_author': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'deleted_records': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'document_type': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'documents': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'dois': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'editions':  UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'external_system_identifiers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'figures': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'funding_info': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'inspire_categories': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'isbns': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'license': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'public_notes': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'publication_info': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'record_affiliations': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.authors': UnifierOps.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'texkeys': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': UnifierOps.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': UnifierOps.KEEP_ONLY_HEAD_ENTITIES,
        'titles': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'urls': UnifierOps.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST
    }
    list_dict_ops = {
        '$schema': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_export_to': DictMergerOps.FALLBACK_KEEP_HEAD,
        '_private_notes': DictMergerOps.FALLBACK_KEEP_HEAD,
        'accelerator_experiments': DictMergerOps.FALLBACK_KEEP_HEAD,
        'acquisition_source': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.affiliations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.curated_relation': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.full_name': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.ids': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.record': DictMergerOps.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.signature_block': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'authors.uuid': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'book_series': DictMergerOps.FALLBACK_KEEP_HEAD,
        'control_number': DictMergerOps.FALLBACK_KEEP_HEAD,
        'curated': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted': DictMergerOps.FALLBACK_KEEP_HEAD,
        'deleted_records': DictMergerOps.FALLBACK_KEEP_HEAD,
        'funding_info': DictMergerOps.FALLBACK_KEEP_HEAD,
        'legacy_creation_date': DictMergerOps.FALLBACK_KEEP_HEAD,
        'new_record': DictMergerOps.FALLBACK_KEEP_HEAD,
        'persistent_identifiers': DictMergerOps.FALLBACK_KEEP_HEAD,
        'preprint_date': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference': DictMergerOps.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.label': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.title': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': DictMergerOps.FALLBACK_KEEP_UPDATE,
        'self': DictMergerOps.FALLBACK_KEEP_HEAD,
        'succeeding_entry': DictMergerOps.FALLBACK_KEEP_HEAD,
        'texkeys': DictMergerOps.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': DictMergerOps.FALLBACK_KEEP_HEAD,
        'title_translations': DictMergerOps.FALLBACK_KEEP_HEAD,
        'urls': DictMergerOps.FALLBACK_KEEP_HEAD,
    }
