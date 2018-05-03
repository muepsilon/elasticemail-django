from setuptools import setup, find_packages

setup(name='elasticemail-django',
      version='0.1',
      description='Simple django backend for elasticemail',
      classifiers=[
        'Development Status :: Alpha',
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='email backend django elasticemail',
      url='https://github.com/muepsilon/elasticemail-django',
      author='Raj',
      author_email='rajpateld001@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'django'
      ],
      include_package_data=True,
      zip_safe=False)
