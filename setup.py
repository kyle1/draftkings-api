from setuptools import setup


with open(file='README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='draftkings-api',
    version='0.0.1',
    description='DraftKings API wrapper',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kyle1/draftkings-api',
    author='Kyle Overstreet',
    author_email='kyoverstreet@gmail.com',  
    classifiers=[
        'Development Status :: 4 - Beta',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    license='MIT',
    packages=['draftkings-api'],
    package_dir={'draftkings-api': 'draftkings-api'},
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.28,<2.29'
    ],
    project_urls={
        'Documentation': 'https://github.com/kyle1/draftkings-api',
        'Source': 'https://github.com/kyle1/draftkings-api',
    },
    keywords=['python', 'draftkings', 'draftkings-client']
)
