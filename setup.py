from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='Flask-Hedwig',
    version='0.1',
    url='https://github.com/kimjayd/flask-hedwig',
    license='MIT',
    author='Hyunjun Kim',
    author_email='kim@hyunjun.kr',
    description='Flask-Hedwig extension',
    long_description=long_description,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    install_requires=['Flask', 'Jinja2', 'Hedwig'],
    platforms='any',
)
