
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis_dilmanpreet_101903506",
    version="1.0",
    author="Dilmanpreet Singh",
    author_email="singh.dp.287@gmail.com",
    description="It's a package that calcuates Topsis score and ranks accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/dpsingh287/topsis-test-101",
    download_url="https://github.com/dpsingh287/topsis-test-101/archive/refs/tags/v_01.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["topsis_test_101"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Dilmanpreet_101903506.101903506:main",
        ]
    },
)
