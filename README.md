#Setup guide
*This setup guide assumes that you already have the following softwares installed in your machine*

- Git and a Github Account
- Python 2.7 or above
- virtualenv for Python 2.7 or above
- Postgresql

1. Clone repository
```
git clone <repository_url>
```
2. Create virtual environment
```
python -m virtualenv env
```
3. Activate Virtual environment
```
source ./env/Scripts/activate
```
4. Install libraries for source code
```
pip install -r requirements.txt -t lib
```
5. Right click on the lib folder and mark directory as Sources Root.
6. Run your backend application
```
./run_local.sh
```