import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

project_urls = {
    "Homepage": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    "Issue tracker": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues",
    "Code": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    "Documentation": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/wiki",
}

setuptools.setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.github_username}}',
    author_email='{{cookiecutter.email}}',
    license='{{cookiecutter.open_source_license}}',
    description='{{cookiecutter.project_short_description}}',
    long_description_content_type="text/markdown",
    long_description=open("README.md").read()
    + "\n\n"
    + open("CHANGELOG.md").read(),
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    project_urls=project_urls,
    install_requires=[],
    python_requires=">=3.6",
)
