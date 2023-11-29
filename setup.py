from setuptools import find_packages, setup

VERSION = '0.3.0'

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name='autoboot-web',
    version=VERSION,
    author='yizzuide',
    author_email='fu837014586@163.com',
    description='Web starter build with autoboot and FastAPI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yizzuide/autoboot_data',
    keywords=['autoboot', 'web', 'FastAPI'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'autoboot>=0.6.0',
        'fastapi>=0.70.1',
        'uvicorn>=0.16.0'
    ],
    extra_require={
        'all': ['starlette-csrf>=1.4.0']
    },
    tests_require=[
        'pytest>=6.2.0',
        'pytest-cov>=2.10.0'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License'
    ],
)