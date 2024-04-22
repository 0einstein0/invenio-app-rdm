# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2022 data-futures.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Mirador preview."""

from flask import current_app, render_template


def can_preview(file):
    """Check if file can be previewed by this previewer.

    :param file: The file to be previewed.
    :returns: Boolean
    """
    # supported_extensions list needs . prefixed -
    preview_extensions = current_app.config["MIRADOR_PREVIEW_EXTENSIONS"]
    supported_extensions = ["." + ext for ext in preview_extensions]
    return file.has_extensions(*supported_extensions)


def preview(file):
    """Render template."""

    return render_template(
        "invenio_app_rdm/records/mirador_preview.html",
        file=file,
        manifest_url=file.record.links['self_iiif_manifest'],
        ui_config=current_app.config["MIRADOR_PREVIEW_CONFIG"],
    )
