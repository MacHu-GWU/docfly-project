#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Config:
    GITHUB_ACCOUNT = "MacHu-GWU"
    GITHUB_REPO_NAME = "docfly-project"
    PACKAGE_NAME = "docfly"
    DEV_PY_VER_MAJOR = "3"
    DEV_PY_VER_MINOR = "8"
    DEV_PY_VER_MICRO = "11"
    TOX_TEST_VERSIONS = [
        "2.7.18",
        "3.7.12",
        "3.8.11",
        "3.9.6",
    ]

    # --- Documentation Build
    DOC_HOST_RTD_PROJECT_NAME = "docfly"
    DOC_HOST_AWS_PROFILE = None
    DOC_HOST_S3_BUCKET = None

    # --- AWS Lambda Related
    AWS_LAMBDA_DEPLOY_AWS_PROFILE = None
    AWS_LAMBDA_DEPLOY_S3_BUCKET = None
    AWS_LAMBDA_BUILD_DOCKER_IMAGE = None
    AWS_LAMBDA_BUILD_DOCKER_IMAGE_WORKSPACE_DIR = None
    AWS_LAMBDA_TEST_DOCKER_IMAGE = None
