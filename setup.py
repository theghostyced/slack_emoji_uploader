# TODO: Write the crawler class
# TODO: Implement a ratelimiter
# TODO: Write the colored logger file
# TODO: Implement the cli runner
# TODO: Finish up the cli by writing the setup

from setuptools import find_packages, setup

setup(
    name='slack_emoji_uploader',
    version='1.0',
    package=find_packages(),
    entry_points={
        'console_scripts': ['slack_uploader=slack_uploader.init:main']
    },
    author='Daniel Eze',
    author_email='dan4allu93@gmail.com',
    url='https://github.com/theghostced/slack_emoji_uploader',
    project_urls={
        'Source Code': 'https://github.com/theghostyced/slack_emoji_uploader',
    },
)