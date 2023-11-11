import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_discription = fh.read()
    


__version__ ='0.0.0'

REPO_NAME = 'End-to-end-text-summarization'
AUTHOR_NAME = 'Ravi352'
SRC_REPO = 'textSummarization'
AUTHOR_EMAIL = 'kravi2746@gamil.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for NLP app",
    long_description=long_discription,
    long_discription_content='/text/markdown',
    url = f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)