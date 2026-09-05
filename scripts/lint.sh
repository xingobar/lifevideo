#!/bin/bash
# 檢查並自動修復 unused imports、格式問題
ruff check --fix app/
ruff format app/
