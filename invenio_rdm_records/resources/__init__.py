# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio RDM module to create REST APIs."""

from .resources import BibliographicDraftActionResource, \
    BibliographicDraftActionResourceConfig, BibliographicDraftResource, \
    BibliographicDraftResourceConfig, BibliographicRecordResource, \
    BibliographicRecordResourceConfig, BibliographicUserRecordsResource, \
    BibliographicUserRecordsResourceConfig

__all__ = (
    "BibliographicDraftActionResource",
    "BibliographicDraftActionResourceConfig",
    "BibliographicDraftResource",
    "BibliographicDraftResourceConfig",
    "BibliographicRecordResource",
    "BibliographicRecordResourceConfig",
    "BibliographicUserRecordsResource",
    "BibliographicUserRecordsResourceConfig",
)
