pushd "%~dp0"
cd toppackage
python zzz_manual_install.py
cd ..
python create_doctree.py
make html